"""One complete RoB 2 assessment: five domains with one judge, then the overall judgment."""

from typing import Optional

from ....base import Judge, Parser, RoB2DomainResult, RoB2EvaluationInput, RoB2OverallResult
from .aggregation import RoB2OverallRule
from .decision_rules import DECISION_RULES
from .workflow import DEFAULT_WORKFLOWS, RoB2DomainRunner, check_effect_of_interest


class RoB2AssessmentRunner:
    """Assess one trial result using one judge and deterministic decision rules."""

    def __init__(self, *, parser: Optional[Parser] = None, max_new_tokens: int = 1024):
        self.domain_runner = RoB2DomainRunner(parser=parser, max_new_tokens=max_new_tokens)

    def run(self, evaluation_input: RoB2EvaluationInput, judge: Judge) -> RoB2OverallResult:
        """
        Run D1-D5 in order and return all signalling results, five domain judgments and the overall judgment.

        Domain 2 always runs, so `effect_of_interest` is checked once here, before any judge call.
        """
        check_effect_of_interest(evaluation_input)
        domains = {}
        for rule in DECISION_RULES:
            results = self.domain_runner.run(DEFAULT_WORKFLOWS[rule.domain_id], evaluation_input, judge)
            domains[rule.domain_id] = RoB2DomainResult(
                domain_id=rule.domain_id,
                signaling_results=results,
                suggested_judgment=rule.evaluate(results),
            )
        return RoB2OverallResult(domains=domains, suggested_judgment=RoB2OverallRule.evaluate(domains))
