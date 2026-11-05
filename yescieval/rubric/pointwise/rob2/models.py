from enum import Enum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


def _require_text(value: str) -> str:
    """Reject empty or whitespace-only strings; return the value unchanged."""
    if not value.strip():
        raise ValueError("must not be empty or whitespace-only")
    return value


class EvidenceDocument(BaseModel):
    """
    One source document used as evidence in a RoB 2 assessment.

    `document_id` and `content` must contain non-whitespace text; values are kept unchanged.
    """
    model_config = ConfigDict(extra="forbid")

    document_id: str
    document_type: Literal[
        "primary_report",
        "supplement",
        "protocol",
        "registry",
        "sap",
        "other",
    ]
    content: str

    @field_validator("document_id", "content")
    @classmethod
    def _reject_blank(cls, value: str) -> str:
        return _require_text(value)


class RoB2EvaluationInput(BaseModel):
    """
    One RoB 2 evaluation instance: a single trial result and its evidence documents.

    Required text fields must contain non-whitespace text; values are kept unchanged.
    Document IDs must be unique within one instance so evidence references are unambiguous.
    `effect_of_interest` is optional here; Domain 2 execution enforces it when needed.
    """
    model_config = ConfigDict(extra="forbid")

    study_id: str
    target_outcome: str
    intervention: str
    comparator: str
    timepoint: str | None = None
    effect_of_interest: Literal["assignment", "adherence"] | None = None
    evidence_documents: list[EvidenceDocument] = Field(..., min_length=1)

    @field_validator("study_id", "target_outcome", "intervention", "comparator")
    @classmethod
    def _reject_blank(cls, value: str) -> str:
        return _require_text(value)

    @model_validator(mode="after")
    def _reject_duplicate_document_ids(self) -> "RoB2EvaluationInput":
        seen = set()
        duplicates = []
        for document in self.evidence_documents:
            if document.document_id in seen and document.document_id not in duplicates:
                duplicates.append(document.document_id)
            seen.add(document.document_id)
        if duplicates:
            raise ValueError(f"duplicate document_id values: {', '.join(duplicates)}")
        return self


class RoB2SignalingResponse(str, Enum):
    """RoB 2 response options for one signaling question."""

    Y = "Y"
    PY = "PY"
    PN = "PN"
    N = "N"
    NI = "NI"
    NA = "NA"


class EvidenceSpan(BaseModel):
    """
    A passage quoted from one evidence document to support a signaling-question response.

    `document_id` and `quoted_text` must contain non-whitespace text; values are kept unchanged.
    """
    model_config = ConfigDict(extra="forbid")

    document_id: str
    quoted_text: str

    @field_validator("document_id", "quoted_text")
    @classmethod
    def _reject_blank(cls, value: str) -> str:
        return _require_text(value)


class RoB2SignalingResult(BaseModel):
    """
    The result of evaluating one RoB 2 signaling question.

    `rubric_id` and `rationale` must contain non-whitespace text; values are kept unchanged.
    `evidence` may be empty, e.g. for `NI` responses or workflow-generated `NA` results.
    Rubric-specific checks, such as allowed responses, are applied by the rubric's `validate_result()`.
    """
    model_config = ConfigDict(extra="forbid")

    rubric_id: str
    response: RoB2SignalingResponse
    rationale: str
    evidence: list[EvidenceSpan]

    @field_validator("rubric_id", "rationale")
    @classmethod
    def _reject_blank(cls, value: str) -> str:
        return _require_text(value)
