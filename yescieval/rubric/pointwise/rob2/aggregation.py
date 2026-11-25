"""Deterministic overall RoB 2 judgment from the five domain results."""

from typing import Mapping

from ....base import RoB2DomainResult, RoB2Judgment


class RoB2OverallRule:
    """
    Use each domain's justified final judgment, or its suggested judgment.

    Multiple 'some concerns' domains do not automatically produce 'high'.
    Such a change must be an explicit, justified overall override.
    """

    @staticmethod
    def evaluate(domains: Mapping[str, RoB2DomainResult]) -> RoB2Judgment:
        """Return 'high' if any domain is high, 'low' if all are low, else 'some_concerns'."""
        judgments = [
            domain.final_judgment if domain.final_judgment is not None else domain.suggested_judgment
            for domain in domains.values()
        ]
        if RoB2Judgment.HIGH in judgments:
            return RoB2Judgment.HIGH
        if all(judgment == RoB2Judgment.LOW for judgment in judgments):
            return RoB2Judgment.LOW
        return RoB2Judgment.SOME_CONCERNS
