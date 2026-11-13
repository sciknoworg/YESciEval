"""
RoB 2 (22 August 2019, individually randomized parallel-group trials).

The 22 signalling questions live in d1_randomization ... d5_reported_result;
the data models and the parent rubric `RoB2Rubric` live in `yescieval.base`.
Entry point: `RoB2AssessmentRunner().run(evaluation_input, judge)`.
"""

# TODO(rob2): tests for models, prompts, workflow, decision rules and runner
# TODO(rob2): docs (docs/source/rubrics.rst, README)

from .aggregation import RoB2OverallRule
from .decision_rules import (
    DECISION_RULES,
    D1DecisionRule,
    D2DecisionRule,
    D3DecisionRule,
    D4DecisionRule,
    D5DecisionRule,
)
from .runner import RoB2AssessmentRunner
from .workflow import (
    DEFAULT_WORKFLOWS,
    AnswerCondition,
    ApplicabilityRule,
    RoB2DomainWorkflow,
    UnsupportedRoB2PathError,
    check_effect_of_interest,
    RoB2DomainRunner,
)

__all__ = [
    "DECISION_RULES",
    "DEFAULT_WORKFLOWS",
    "AnswerCondition",
    "ApplicabilityRule",
    "D1DecisionRule",
    "D2DecisionRule",
    "D3DecisionRule",
    "D4DecisionRule",
    "D5DecisionRule",
    "RoB2AssessmentRunner",
    "RoB2DomainWorkflow",
    "RoB2OverallRule",
    "UnsupportedRoB2PathError",
    "check_effect_of_interest",
    "RoB2DomainRunner",
]
