import json
import unittest
from types import SimpleNamespace
from typing import ClassVar, Literal
from unittest.mock import MagicMock, patch
from pydantic import BaseModel, ValidationError
from yescieval import GPTCustomAutoJudge, Rubric
from yescieval.base import RubricLikertScale
from yescieval.rubric.pointwise.breadth import (ContextCoverage, DimensionCoverage, MethodCoverage,
                                                ScaleCoverage, ScopeCoverage)
from yescieval.rubric.pointwise.depth import CausalReasoning, MechanisticUnderstanding, TemporalPrecision
from yescieval.rubric.pointwise.fidelity import Completeness, Correctness, Informativeness
from yescieval.rubric.pointwise.gap import GapIdentification
from yescieval.rubric.pointwise.innovation import StateOfTheArtAndNovelty
from yescieval.rubric.pointwise.rigor import (EpistemicCalibration, ExplicitUncertainty,
                                              QuantitativeEvidenceAndUncertainty)
from yescieval.rubric.pointwise.structural import Coherence, Integration, Relevancy
from yescieval.rubric.pointwise.stylistic import Cohesion, Conciseness, Readability

EXISTING_POINTWISE_RUBRICS = (
    ContextCoverage, DimensionCoverage, MethodCoverage, ScaleCoverage, ScopeCoverage,
    CausalReasoning, MechanisticUnderstanding, TemporalPrecision,
    Completeness, Correctness, Informativeness,
    GapIdentification, StateOfTheArtAndNovelty,
    EpistemicCalibration, ExplicitUncertainty, QuantitativeEvidenceAndUncertainty,
    Coherence, Integration, Relevancy,
    Cohesion, Conciseness, Readability,
)


class LabelResult(BaseModel):
    """Test result model with a categorical field, unrelated to any shipped rubric."""

    label: Literal["yes", "no", "unclear"]
    rationale: str


class LabelRubric(Rubric):
    """Test rubric that declares its own response model and rejects the label "unclear"."""

    response_model: ClassVar[type] = LabelResult

    name: str = "Label"
    system_prompt_template: str = "You are a test judge."
    user_prompt_template: str = "Is the claim supported?"

    def verbalize_user_prompt(self) -> str:
        return self.user_prompt_template

    def validate_result(self, result: LabelResult) -> LabelResult:
        if result.label == "unclear":
            raise ValueError("label unclear is not allowed for this rubric")
        return result


def function_call_message(payload) -> SimpleNamespace:
    """Build a chat message whose function call carries `payload` as JSON arguments."""
    arguments = payload if isinstance(payload, str) else json.dumps(payload)
    return SimpleNamespace(content=None, function_call=SimpleNamespace(arguments=arguments))


def text_message(payload) -> SimpleNamespace:
    """Build a chat message whose content carries `payload` as JSON text."""
    content = payload if isinstance(payload, str) else json.dumps(payload)
    return SimpleNamespace(content=content, function_call=None)


def make_judge(model_name: str, *messages: SimpleNamespace, max_attempts: int = 3) -> GPTCustomAutoJudge:
    """Create a judge whose OpenAI client returns `messages` in order, without network access."""
    judge = GPTCustomAutoJudge(max_attempts=max_attempts, retry_delay=0)
    judge.model_name = model_name
    judge.client = MagicMock()
    judge.client.chat.completions.create.side_effect = [
        SimpleNamespace(choices=[SimpleNamespace(message=message)]) for message in messages
    ]
    return judge


class TestGPTCustomAutoJudge(unittest.TestCase):

    def setUp(self):
        self.papers = {"A Study on AI": "This paper discusses AI."}
        self.likert_rubric = Informativeness(papers=self.papers,
                                             question="this is a dummy question",
                                             answer="synthesis answer")
        self.label_rubric = LabelRubric()
        self.likert = {"rating": 4, "rationale": "Informative synthesis."}
        self.label = {"label": "yes", "rationale": "The claim is stated in the abstract."}

    def request(self, judge: GPTCustomAutoJudge, call: int = 0) -> dict:
        return judge.client.chat.completions.create.call_args_list[call].kwargs

    def test_existing_pointwise_rubrics_return_likert_scale(self):
        for rubric_class in EXISTING_POINTWISE_RUBRICS:
            with self.subTest(rubric=rubric_class.__name__):
                rubric = rubric_class(papers=self.papers, question="q", answer="a")
                judge = make_judge("gpt-4o", function_call_message(self.likert))
                result = judge.judge(rubric)
                self.assertEqual(result, RubricLikertScale(**self.likert))
                request = self.request(judge)
                self.assertEqual(request["messages"], rubric.instruct())
                self.assertEqual(request["functions"][0]["parameters"], RubricLikertScale.model_json_schema())

    def test_existing_rubric_text_response_keyed_by_rubric_name(self):
        for rubric_class in EXISTING_POINTWISE_RUBRICS:
            with self.subTest(rubric=rubric_class.__name__):
                rubric = rubric_class(papers=self.papers, question="q", answer="a")
                judge = make_judge("gpt-5.2", text_message({rubric.name: self.likert}))
                self.assertEqual(judge.judge(rubric), RubricLikertScale(**self.likert))
                self.assertNotIn("functions", self.request(judge))

    def test_function_call_request(self):
        judge = make_judge("gpt-4o", function_call_message(self.likert))
        judge.judge(self.likert_rubric)
        request = self.request(judge)
        self.assertEqual(request["model"], "gpt-4o")
        self.assertEqual(request["messages"], self.likert_rubric.instruct())
        self.assertEqual(request["function_call"], {"name": request["functions"][0]["name"]})

    def test_custom_response_model(self):
        judge = make_judge("gpt-4o", function_call_message(self.label))
        result = judge.judge(self.label_rubric)
        self.assertIsInstance(result, LabelResult)
        self.assertEqual(result, LabelResult(**self.label))
        self.assertEqual(self.request(judge)["functions"][0]["parameters"], LabelResult.model_json_schema())

    def test_unkeyed_text_response(self):
        judge = make_judge("gpt-5.2", text_message(self.label))
        self.assertEqual(judge.judge(self.label_rubric), LabelResult(**self.label))

    def test_rubric_rejection_is_retried(self):
        rejected = {**self.label, "label": "unclear"}
        judge = make_judge("gpt-4o", function_call_message(rejected), function_call_message(self.label))
        self.assertEqual(judge.judge(self.label_rubric).label, "yes")
        self.assertEqual(judge.client.chat.completions.create.call_count, 2)

    def test_rubric_rejection_fails_after_max_attempts(self):
        rejected = function_call_message({**self.label, "label": "unclear"})
        judge = make_judge("gpt-4o", rejected, rejected, max_attempts=2)
        with self.assertRaisesRegex(ValueError, "not allowed"):
            judge.judge(self.label_rubric)
        self.assertEqual(judge.client.chat.completions.create.call_count, 2)

    def test_malformed_json_is_retried(self):
        judge = make_judge("gpt-4o", function_call_message("{not json"), function_call_message(self.likert))
        self.assertEqual(judge.judge(self.likert_rubric), RubricLikertScale(**self.likert))

    def test_invalid_payload_raises_validation_error(self):
        invalid = function_call_message({"rating": 7, "rationale": "Out of range."})
        judge = make_judge("gpt-4o", invalid, invalid, invalid)
        with self.assertRaises(ValidationError):
            judge.judge(self.likert_rubric)
        self.assertEqual(judge.client.chat.completions.create.call_count, 3)

    def test_api_error_is_retried(self):
        judge = make_judge("gpt-4o")
        response = SimpleNamespace(choices=[SimpleNamespace(message=function_call_message(self.likert))])
        judge.client.chat.completions.create.side_effect = [ConnectionError("timeout"), response]
        self.assertEqual(judge.judge(self.likert_rubric), RubricLikertScale(**self.likert))

    def test_retry_delay_is_used_and_not_after_last_attempt(self):
        invalid = function_call_message("{not json")
        judge = make_judge("gpt-4o", invalid, invalid, invalid)
        judge.retry_delay = 1
        with patch("yescieval.utils.llms.time.sleep") as sleep:
            with self.assertRaises(ValueError):
                judge.judge(self.likert_rubric)
        self.assertEqual([c.args for c in sleep.call_args_list], [(1,), (1,)])

    def test_uninitialized_judge(self):
        with self.assertRaisesRegex(ValueError, "not initialized"):
            GPTCustomAutoJudge().judge(self.likert_rubric)

    def test_missing_token(self):
        with self.assertRaisesRegex(ValueError, "token"):
            GPTCustomAutoJudge().from_pretrained(model_id="gpt-4o")

    def test_default_construction_is_unchanged(self):
        judge = GPTCustomAutoJudge()
        with patch("yescieval.judge.custom.OpenAI") as client:
            judge.from_pretrained(model_id="gpt-4o", token="test-key")
        client.assert_called_once_with(api_key="test-key")
        self.assertEqual(judge.model_name, "gpt-4o")
        self.assertEqual((judge.max_attempts, judge.retry_delay), (3, 5))


if __name__ == "__main__":
    unittest.main()
