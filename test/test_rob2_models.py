import unittest
from typing import ClassVar
from pydantic import ValidationError
from yescieval import Rubric
from yescieval.base import RubricLikertScale
from yescieval.rubric.pointwise.rob2 import (
    EvidenceDocument,
    EvidenceSpan,
    RoB2EvaluationInput,
    RoB2SignalingResponse,
    RoB2SignalingResult,
)


class TestRoB2Models(unittest.TestCase):

    def setUp(self):
        self.base = {
            "study_id": "NCT00000001",
            "target_outcome": "All-cause mortality",
            "intervention": "Drug A",
            "comparator": "Placebo",
        }
        self.report = {"document_id": "doc-1", "document_type": "primary_report", "content": "Trial report text."}

    def test_valid_single_document_input(self):
        evaluation = RoB2EvaluationInput(**self.base, evidence_documents=[EvidenceDocument(**self.report)])
        self.assertEqual(len(evaluation.evidence_documents), 1)
        self.assertEqual(evaluation.evidence_documents[0].document_type, "primary_report")
        self.assertIsNone(evaluation.timepoint)
        self.assertIsNone(evaluation.effect_of_interest)

    def test_valid_multi_document_input(self):
        protocol = {"document_id": "doc-2", "document_type": "protocol", "content": "Protocol text."}
        evaluation = RoB2EvaluationInput(
            **self.base,
            timepoint="28 days",
            effect_of_interest="assignment",
            evidence_documents=[self.report, protocol],
        )
        self.assertEqual([d.document_id for d in evaluation.evidence_documents], ["doc-1", "doc-2"])

    def test_missing_evidence_documents(self):
        with self.assertRaises(ValidationError):
            RoB2EvaluationInput(**self.base)
        with self.assertRaises(ValidationError):
            RoB2EvaluationInput(**self.base, evidence_documents=[])

    def test_invalid_document_type(self):
        with self.assertRaises(ValidationError):
            EvidenceDocument(**{**self.report, "document_type": "press_release"})

    def test_empty_document_content(self):
        for content in ("", "   \n\t"):
            with self.assertRaises(ValidationError):
                EvidenceDocument(**{**self.report, "content": content})

    def test_empty_document_id(self):
        for document_id in ("", "   "):
            with self.assertRaises(ValidationError):
                EvidenceDocument(**{**self.report, "document_id": document_id})

    def test_evidence_text_is_not_modified(self):
        content = "  Leading and trailing whitespace is kept.\n"
        document = EvidenceDocument(**{**self.report, "content": content})
        self.assertEqual(document.content, content)

    def test_empty_required_assessment_fields(self):
        for field in ("study_id", "target_outcome", "intervention", "comparator"):
            for value in ("", "   \n\t"):
                with self.assertRaises(ValidationError):
                    RoB2EvaluationInput(**{**self.base, field: value}, evidence_documents=[self.report])

    def test_required_assessment_fields_are_not_modified(self):
        evaluation = RoB2EvaluationInput(**{**self.base, "study_id": " NCT00000001 "}, evidence_documents=[self.report])
        self.assertEqual(evaluation.study_id, " NCT00000001 ")

    def test_duplicate_document_ids(self):
        duplicate = {"document_id": "doc-1", "document_type": "protocol", "content": "Protocol text."}
        with self.assertRaisesRegex(ValidationError, "duplicate document_id values: doc-1"):
            RoB2EvaluationInput(**self.base, evidence_documents=[self.report, duplicate])

    def test_unexpected_fields(self):
        with self.assertRaises(ValidationError) as ctx:
            EvidenceDocument(**self.report, page_count=12)
        self.assertEqual(ctx.exception.errors()[0]["type"], "extra_forbidden")
        with self.assertRaises(ValidationError) as ctx:
            RoB2EvaluationInput(**self.base, evidence_documents=[self.report], question="unused")
        self.assertEqual(ctx.exception.errors()[0]["type"], "extra_forbidden")

    def test_invalid_effect_of_interest(self):
        with self.assertRaises(ValidationError):
            RoB2EvaluationInput(**self.base, effect_of_interest="per_protocol", evidence_documents=[self.report])

    def test_json_round_trip(self):
        protocol = {"document_id": "doc-2", "document_type": "protocol", "content": "  Protocol text.\n"}
        evaluation = RoB2EvaluationInput(
            **self.base,
            timepoint="28 days",
            effect_of_interest="adherence",
            evidence_documents=[self.report, protocol],
        )
        restored = RoB2EvaluationInput.model_validate_json(evaluation.model_dump_json())
        self.assertEqual(restored, evaluation)


class SignalingQuestionRubric(Rubric):
    """Test RoB 2 rubric: declares the RoB 2 result model and rejects responses it does not allow."""

    response_model: ClassVar[type] = RoB2SignalingResult
    allowed_responses: ClassVar[set[RoB2SignalingResponse]] = {
        RoB2SignalingResponse.Y,
        RoB2SignalingResponse.PY,
        RoB2SignalingResponse.PN,
        RoB2SignalingResponse.N,
        RoB2SignalingResponse.NI,
    }

    system_prompt_template: str = "You are a RoB 2 assessor."
    user_prompt_template: str = "Answer signaling question 1.1."

    def verbalize_user_prompt(self) -> str:
        return self.user_prompt_template

    def validate_result(self, result: RoB2SignalingResult) -> RoB2SignalingResult:
        if result.response not in self.allowed_responses:
            raise ValueError(f"response {result.response.value} is not allowed for this rubric")
        return result


class TestRoB2SignalingResult(unittest.TestCase):

    def setUp(self):
        self.span = {"document_id": "doc-1", "quoted_text": "Participants were randomised by computer."}
        self.result = {
            "rubric_id": "1.1",
            "response": "Y",
            "rationale": "A computer-generated sequence was used.",
            "evidence": [self.span],
        }

    def test_valid_result_for_every_response(self):
        self.assertEqual([r.value for r in RoB2SignalingResponse], ["Y", "PY", "PN", "N", "NI", "NA"])
        for response in RoB2SignalingResponse:
            result = RoB2SignalingResult(**{**self.result, "response": response.value})
            self.assertIs(result.response, response)

    def test_invalid_response_rejected(self):
        for response in ("Maybe", "yes", "", "Low"):
            with self.assertRaises(ValidationError) as ctx:
                RoB2SignalingResult(**{**self.result, "response": response})
            self.assertEqual(ctx.exception.errors()[0]["type"], "enum")

    def test_empty_evidence_allowed(self):
        result = RoB2SignalingResult(**{**self.result, "response": "NI", "evidence": []})
        self.assertEqual(result.evidence, [])

    def test_missing_fields_rejected(self):
        for field in ("rubric_id", "response", "rationale", "evidence"):
            payload = dict(self.result)
            del payload[field]
            with self.assertRaises(ValidationError):
                RoB2SignalingResult(**payload)

    def test_empty_text_fields_rejected(self):
        for field in ("rubric_id", "rationale"):
            for value in ("", "   \n\t"):
                with self.assertRaises(ValidationError):
                    RoB2SignalingResult(**{**self.result, field: value})
        for field in ("document_id", "quoted_text"):
            for value in ("", "   "):
                with self.assertRaises(ValidationError):
                    EvidenceSpan(**{**self.span, field: value})

    def test_unexpected_fields(self):
        with self.assertRaises(ValidationError) as ctx:
            EvidenceSpan(**self.span, page=3)
        self.assertEqual(ctx.exception.errors()[0]["type"], "extra_forbidden")
        with self.assertRaises(ValidationError) as ctx:
            RoB2SignalingResult(**self.result, rating=4)
        self.assertEqual(ctx.exception.errors()[0]["type"], "extra_forbidden")

    def test_evidence_spans_preserved(self):
        second = {"document_id": "doc-2", "quoted_text": "  Allocation was concealed.\n"}
        result = RoB2SignalingResult(**{**self.result, "evidence": [self.span, second]})
        self.assertEqual([e.model_dump() for e in result.evidence], [self.span, second])

    def test_json_round_trip(self):
        result = RoB2SignalingResult(**{**self.result, "response": "PY"})
        restored = RoB2SignalingResult.model_validate_json(result.model_dump_json())
        self.assertEqual(restored, result)
        self.assertIs(restored.response, RoB2SignalingResponse.PY)


class TestRoB2ResponseModelContract(unittest.TestCase):

    def setUp(self):
        self.rubric = SignalingQuestionRubric()
        self.result = {"rubric_id": "1.1", "rationale": "Reported in the methods.", "evidence": []}

    def test_rob2_rubric_resolves_to_signaling_result(self):
        self.assertIs(SignalingQuestionRubric.response_model, RoB2SignalingResult)
        self.assertIs(self.rubric.response_model, RoB2SignalingResult)
        self.assertIs(Rubric.response_model, RubricLikertScale)

    def test_allowed_response_accepted(self):
        result = RoB2SignalingResult(**self.result, response="PY")
        self.assertIs(self.rubric.validate_result(result), result)

    def test_disallowed_response_rejected_by_rubric(self):
        result = RoB2SignalingResult(**self.result, response="NA")
        with self.assertRaisesRegex(ValueError, "response NA is not allowed"):
            self.rubric.validate_result(result)


if __name__ == '__main__':
    unittest.main()
