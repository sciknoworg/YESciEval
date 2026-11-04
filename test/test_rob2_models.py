import unittest
from pydantic import ValidationError
from yescieval.rubric.pointwise.rob2 import EvidenceDocument, RoB2EvaluationInput


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


if __name__ == '__main__':
    unittest.main()
