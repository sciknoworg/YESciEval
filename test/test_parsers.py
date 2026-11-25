import json
import unittest
from types import SimpleNamespace
from typing import ClassVar, Literal
from unittest.mock import MagicMock, patch
from pydantic import BaseModel, ValidationError
from yescieval import GPTParser, Parser, Rubric
from yescieval.base import RubricLikertScale
from yescieval.rubric.pointwise.fidelity import Informativeness


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


def completion(arguments) -> SimpleNamespace:
    """Build a chat completion whose function call carries `arguments` (JSON-encoded unless a string)."""
    arguments = arguments if isinstance(arguments, str) else json.dumps(arguments)
    message = SimpleNamespace(content=None, function_call=SimpleNamespace(arguments=arguments))
    return SimpleNamespace(choices=[SimpleNamespace(message=message)])


def make_parser(*responses, max_attempts: int = 3) -> GPTParser:
    """Create a parser whose OpenAI client returns `responses` in order, without network access."""
    with patch("yescieval.parser.parsers.OpenAI"):
        parser = GPTParser(openai_key="test-key", max_attempts=max_attempts, retry_delay=0)
    parser.client = MagicMock()
    parser.client.chat.completions.create.side_effect = list(responses)
    return parser


class TestParserBase(unittest.TestCase):

    def test_parser_is_abstract(self):
        with self.assertRaises(TypeError):
            Parser()

    def test_existing_subclass_with_old_signature_still_works(self):
        class OldStyleParser(Parser):
            def parse(self, raw_output: str) -> RubricLikertScale:
                return RubricLikertScale.model_validate_json(raw_output)

        result = OldStyleParser().parse('{"rating": 2, "rationale": "Weak."}')
        self.assertEqual(result, RubricLikertScale(rating=2, rationale="Weak."))


class TestGPTParser(unittest.TestCase):

    def setUp(self):
        self.raw_output = "Rating: 4. Rationale: the answer covers diagnostics and personalized medicine."
        self.likert = {"rating": 4, "rationale": "Covers diagnostics and personalized medicine."}
        self.label = {"label": "yes", "rationale": "The claim is stated in the abstract."}
        self.likert_rubric = Informativeness(papers={"A Study on AI": "This paper discusses AI."},
                                             question="this is a dummy question",
                                             answer="synthesis answer")

    def request(self, parser: GPTParser, call: int = 0) -> dict:
        return parser.client.chat.completions.create.call_args_list[call].kwargs

    def test_existing_call_parses_likert_scale(self):
        parser = make_parser(completion(self.likert))
        result = parser.parse(raw_output=self.raw_output)
        self.assertIsInstance(result, RubricLikertScale)
        self.assertEqual(result, RubricLikertScale(**self.likert))
        request = self.request(parser)
        self.assertEqual(request["model"], "gpt-4o-mini")
        self.assertEqual(request["messages"], [{"role": "user", "content": self.raw_output}])
        self.assertEqual(request["functions"][0]["parameters"], RubricLikertScale.model_json_schema())
        self.assertEqual(request["function_call"], {"name": request["functions"][0]["name"]})

    def test_existing_positional_call(self):
        parser = make_parser(completion(self.likert))
        self.assertEqual(parser.parse(self.raw_output), RubricLikertScale(**self.likert))

    def test_default_constructor_is_unchanged(self):
        with patch("yescieval.parser.parsers.OpenAI") as client:
            parser = GPTParser("test-key")
        client.assert_called_once_with(api_key="test-key")
        self.assertEqual((parser.parser_model, parser.max_attempts, parser.retry_delay), ("gpt-4o-mini", 3, 3))

    def test_custom_response_model(self):
        parser = make_parser(completion(self.label))
        result = parser.parse(self.raw_output, response_model=LabelResult)
        self.assertEqual(result, LabelResult(**self.label))
        self.assertEqual(self.request(parser)["functions"][0]["parameters"], LabelResult.model_json_schema())

    def test_response_model_without_rubric_skips_rubric_validation(self):
        parser = make_parser(completion({**self.label, "label": "unclear"}))
        self.assertEqual(parser.parse(self.raw_output, response_model=LabelResult).label, "unclear")

    def test_rubric_selects_model_and_validation(self):
        parser = make_parser(completion({**self.label, "label": "unclear"}), completion(self.label))
        result = parser.parse(self.raw_output, rubric=LabelRubric())
        self.assertEqual(result, LabelResult(**self.label))
        self.assertEqual(self.request(parser)["functions"][0]["parameters"], LabelResult.model_json_schema())
        self.assertEqual(parser.client.chat.completions.create.call_count, 2)

    def test_rubric_rejection_fails_after_max_attempts(self):
        rejected = completion({**self.label, "label": "unclear"})
        parser = make_parser(rejected, rejected, max_attempts=2)
        with self.assertRaisesRegex(ValueError, "not allowed"):
            parser.parse(self.raw_output, rubric=LabelRubric())
        self.assertEqual(parser.client.chat.completions.create.call_count, 2)

    def test_rubric_response_model_takes_precedence(self):
        parser = make_parser(completion(self.likert))
        result = parser.parse(self.raw_output, response_model=LabelResult, rubric=self.likert_rubric)
        self.assertEqual(result, RubricLikertScale(**self.likert))

    def test_existing_rubric_keyed_output(self):
        parser = make_parser(completion({"Informativeness": self.likert}))
        self.assertEqual(parser.parse(self.raw_output, rubric=self.likert_rubric), RubricLikertScale(**self.likert))

    def test_invalid_categorical_value_is_rejected(self):
        invalid = completion({**self.label, "label": "maybe"})
        parser = make_parser(invalid, invalid, invalid)
        with self.assertRaises(ValidationError):
            parser.parse(self.raw_output, response_model=LabelResult)
        self.assertEqual(parser.client.chat.completions.create.call_count, 3)

    def test_malformed_json_is_retried(self):
        parser = make_parser(completion("{not json"), completion(self.likert))
        self.assertEqual(parser.parse(self.raw_output), RubricLikertScale(**self.likert))

    def test_api_error_is_retried(self):
        parser = make_parser(ConnectionError("timeout"), completion(self.likert))
        self.assertEqual(parser.parse(self.raw_output), RubricLikertScale(**self.likert))


if __name__ == "__main__":
    unittest.main()
