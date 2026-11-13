"""
Ordered RoB 2 signalling workflows with explicit, deterministic skip rules.

Routing follows the 22 August 2019 parallel-group tool, including the Domain 2
assignment-to-intervention path. Whether a question is asked is decided here,
not by a judge; skipped questions get an NA result written by the workflow.
"""

from typing import Dict, List, Literal, Mapping, Optional, Set, Tuple, Type

from pydantic import BaseModel, ConfigDict, Field, model_validator

from ....base import (
    Judge,
    Parser,
    RoB2EvaluationInput,
    RoB2Rubric,
    RoB2SignalingResponse,
    RoB2SignalingResult,
)
from .d1_randomization import AllocationConcealment, BaselineDifferences, RandomSequence
from .d2_deviations import (
    AnalysisFailureImpact,
    AppropriateAnalysis,
    CareProviderAwareness,
    DeviationBalance,
    DeviationOutcomeImpact,
    ParticipantAwareness,
    TrialContextDeviations,
)
from .d3_missing_data import (
    EvidenceNoMissingDataBias,
    MissingnessCouldDepend,
    MissingnessLikelyDepended,
    OutcomeDataAvailability,
)
from .d4_measurement import (
    AssessmentCouldBeInfluenced,
    AssessmentLikelyInfluenced,
    AssessorAwareness,
    MeasurementDifference,
    MeasurementMethod,
)
from .d5_reported_result import (
    MultipleEligibleAnalyses,
    MultipleOutcomeMeasurements,
    PrespecifiedAnalysis,
)


class UnsupportedRoB2PathError(ValueError):
    """The requested RoB 2 path has not been implemented."""


class AnswerCondition(BaseModel):
    """An earlier signalling answer belongs to an explicitly listed set."""

    model_config = ConfigDict(extra="forbid")

    rubric_id: str = Field(min_length=1)
    responses: Set[RoB2SignalingResponse] = Field(min_length=1)


class ApplicabilityRule(BaseModel):
    """Combine earlier answers with an explicit any/all condition."""

    model_config = ConfigDict(extra="forbid")

    mode: Literal["any", "all"]
    conditions: List[AnswerCondition] = Field(min_length=1)

    def applies(self, prior_results: Mapping[str, RoB2SignalingResult]) -> bool:
        """Return True if the question must be asked, given the earlier answers in its domain."""
        matches = []
        for condition in self.conditions:
            if condition.rubric_id not in prior_results:
                raise ValueError(f"Missing prerequisite answer: {condition.rubric_id}")
            matches.append(prior_results[condition.rubric_id].response in condition.responses)
        return any(matches) if self.mode == "any" else all(matches)


def _rubric_id(criterion: Type[RoB2Rubric]) -> str:
    return criterion.model_fields["rubric_id"].default


class RoB2DomainWorkflow(BaseModel):
    """A domain's ordered questions and their dependencies on earlier answers."""

    model_config = ConfigDict(extra="forbid")

    domain_id: Literal["D1", "D2", "D3", "D4", "D5"]
    ordered_rubrics: Tuple[Type[RoB2Rubric], ...] = Field(min_length=1)
    applicability: Dict[str, ApplicabilityRule] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_dependencies(self) -> "RoB2DomainWorkflow":
        """Check the workflow definition: unique IDs, one domain, rules only on earlier questions."""
        seen = set()
        for criterion in self.ordered_rubrics:
            rubric_id = _rubric_id(criterion)
            if not isinstance(rubric_id, str) or not rubric_id.strip():
                raise ValueError("Workflow rubrics must declare a nonblank rubric ID")
            if rubric_id in seen:
                raise ValueError(f"Duplicate workflow rubric ID: {rubric_id}")
            if criterion.model_fields["rob2_domain_id"].default != self.domain_id:
                raise ValueError(f"Rubric {rubric_id} belongs to a different domain")
            rule = self.applicability.get(rubric_id)
            if rule is not None and not {c.rubric_id for c in rule.conditions} <= seen:
                raise ValueError(f"Applicability for {rubric_id} references missing or future prerequisites")
            seen.add(rubric_id)
        if set(self.applicability) - seen:
            raise ValueError("Applicability contains unknown rubric IDs")
        return self


def _when(*rubric_ids: str, responses: Set[str], mode: Literal["any", "all"] = "any") -> ApplicabilityRule:
    return ApplicabilityRule(
        mode=mode,
        conditions=[AnswerCondition(rubric_id=rubric_id, responses=responses) for rubric_id in rubric_ids],
    )


DEFAULT_WORKFLOWS: Dict[str, RoB2DomainWorkflow] = {
    "D1": RoB2DomainWorkflow(
        domain_id="D1",
        ordered_rubrics=(RandomSequence, AllocationConcealment, BaselineDifferences),
    ),
    "D2": RoB2DomainWorkflow(
        domain_id="D2",
        ordered_rubrics=(
            ParticipantAwareness,
            CareProviderAwareness,
            TrialContextDeviations,
            DeviationOutcomeImpact,
            DeviationBalance,
            AppropriateAnalysis,
            AnalysisFailureImpact,
        ),
        applicability={
            "2.3": _when("2.1", "2.2", responses={"Y", "PY", "NI"}),
            "2.4": _when("2.3", responses={"Y", "PY"}),
            "2.5": _when("2.4", responses={"Y", "PY", "NI"}),
            "2.7": _when("2.6", responses={"N", "PN", "NI"}),
        },
    ),
    "D3": RoB2DomainWorkflow(
        domain_id="D3",
        ordered_rubrics=(
            OutcomeDataAvailability,
            EvidenceNoMissingDataBias,
            MissingnessCouldDepend,
            MissingnessLikelyDepended,
        ),
        applicability={
            "3.2": _when("3.1", responses={"N", "PN", "NI"}),
            "3.3": _when("3.2", responses={"N", "PN"}),
            "3.4": _when("3.3", responses={"Y", "PY", "NI"}),
        },
    ),
    "D4": RoB2DomainWorkflow(
        domain_id="D4",
        ordered_rubrics=(
            MeasurementMethod,
            MeasurementDifference,
            AssessorAwareness,
            AssessmentCouldBeInfluenced,
            AssessmentLikelyInfluenced,
        ),
        applicability={
            "4.3": _when("4.1", "4.2", responses={"N", "PN", "NI"}, mode="all"),
            "4.4": _when("4.3", responses={"Y", "PY", "NI"}),
            "4.5": _when("4.4", responses={"Y", "PY", "NI"}),
        },
    ),
    "D5": RoB2DomainWorkflow(
        domain_id="D5",
        ordered_rubrics=(
            PrespecifiedAnalysis,
            MultipleOutcomeMeasurements,
            MultipleEligibleAnalyses,
        ),
    ),
}


def check_effect_of_interest(evaluation_input: RoB2EvaluationInput) -> None:
    """
    Require the effect of interest that Domain 2 needs.

    Raises `ValueError` if it is missing and `UnsupportedRoB2PathError` for "adherence".
    """
    if evaluation_input.effect_of_interest is None:
        raise ValueError("Domain 2 requires effect_of_interest='assignment'")
    if evaluation_input.effect_of_interest == "adherence":
        # TODO(rob2): Domain 2 adherence-to-intervention path (different questions and rules)
        raise UnsupportedRoB2PathError("Domain 2 adherence-to-intervention is not implemented")


class RoB2DomainRunner:
    """Ask the applicable questions of one domain and keep explicit NA records for skipped ones."""

    def __init__(self, parser: Optional[Parser] = None, max_new_tokens: int = 1024):
        if not isinstance(max_new_tokens, int) or isinstance(max_new_tokens, bool) or max_new_tokens < 1:
            raise ValueError("max_new_tokens must be a positive integer")
        self.parser = parser
        self.max_new_tokens = max_new_tokens

    def run(self,
            workflow: RoB2DomainWorkflow,
            evaluation_input: RoB2EvaluationInput,
            judge: Judge) -> Dict[str, RoB2SignalingResult]:
        """
        Ask the domain's questions in order and return one result per question.

        A question whose applicability rule does not hold is not asked; it gets an NA result.
        Each asked question receives the earlier results of its domain as `prior_results`.
        The judge must return a validated `RoB2SignalingResult` (see `RoB2Rubric.response_model`);
        it is used as returned.
        """
        if workflow.domain_id == "D2":
            check_effect_of_interest(evaluation_input)
        results: Dict[str, RoB2SignalingResult] = {}
        for criterion in workflow.ordered_rubrics:
            rubric_id = _rubric_id(criterion)
            rule = workflow.applicability.get(rubric_id)
            if rule is not None and not rule.applies(results):
                results[rubric_id] = RoB2SignalingResult(
                    rubric_id=rubric_id,
                    response=RoB2SignalingResponse.NA,
                    rationale="Not applicable: the prerequisite signaling answers do not activate this question.",
                    evidence=[],
                )
                continue
            rubric = criterion(evaluation_input=evaluation_input, prior_results=dict(results))
            # TODO(rob2): HF judges return raw text; parse it with self.parser into rubric.response_model
            #  once GPTParser supports rubric response models (#56)
            results[rubric_id] = judge.judge(rubric, max_new_tokens=self.max_new_tokens)
        return results
