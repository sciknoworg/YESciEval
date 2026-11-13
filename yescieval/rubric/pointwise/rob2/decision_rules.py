"""
Deterministic *suggested* RoB 2 domain judgments.

Source: the official 22 August 2019 guidance for individually randomized,
parallel-group trials, Tables 3/4, 6, 10, 12 and 14 and Figures 1, 2, 4, 5, 7:
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view

These rules encode the published decision logic, not clinical interpretation of
trial evidence. Domain 2 evaluates the effect of assignment to intervention.
Human overrides belong in the assessment record, never in this rules engine.
"""

from typing import Mapping, Tuple

from ....base import RoB2Judgment, RoB2SignalingResponse, RoB2SignalingResult

_YES = frozenset((RoB2SignalingResponse.Y, RoB2SignalingResponse.PY))
_NO = frozenset((RoB2SignalingResponse.N, RoB2SignalingResponse.PN))
_NI = RoB2SignalingResponse.NI
_LOW = RoB2Judgment.LOW
_SOME = RoB2Judgment.SOME_CONCERNS
_HIGH = RoB2Judgment.HIGH
_SEVERITY = {_LOW: 0, _SOME: 1, _HIGH: 2}


def _responses(domain_id: str,
               count: int,
               results: Mapping[str, RoB2SignalingResult]) -> Tuple[RoB2SignalingResponse, ...]:
    """Responses to questions <n>.1 ... <n>.<count>, in order (NA for skipped questions)."""
    number = domain_id[1:]
    return tuple(results[f"{number}.{index}"].response for index in range(1, count + 1))


class D1DecisionRule:
    """Randomization: official Figure 1 and Tables 3/4 (pp. 19–20)."""

    domain_id = "D1"

    @staticmethod
    def evaluate(results: Mapping[str, RoB2SignalingResult]) -> RoB2Judgment:
        """Return the suggested D1 judgment."""
        sequence, concealment, imbalance = _responses("D1", 3, results)
        if concealment in _NO:
            return _HIGH
        if concealment == _NI:
            return _HIGH if imbalance in _YES else _SOME
        # Figure 1 explicitly resolves the nonrandom-sequence path, including
        # the combination omitted from the abbreviated mapping in Table 4.
        if sequence in _NO or imbalance in _YES:
            return _SOME
        return _LOW


class D2DecisionRule:
    """Deviations, effect of assignment: official Table 6 (p. 32)."""

    domain_id = "D2"

    @staticmethod
    def evaluate(results: Mapping[str, RoB2SignalingResult]) -> RoB2Judgment:
        """Return the suggested D2 judgment (worse of the deviations part and the analysis part)."""
        participants, personnel, deviations, outcome, balanced, analysis, impact = _responses("D2", 7, results)
        if participants in _NO and personnel in _NO or deviations in _NO:
            deviations_judgment = _LOW
        elif deviations == _NI or outcome in _NO or balanced in _YES:
            deviations_judgment = _SOME
        else:
            deviations_judgment = _HIGH

        if analysis in _YES:
            analysis_judgment = _LOW
        elif impact in _NO:
            analysis_judgment = _SOME
        else:
            analysis_judgment = _HIGH
        return max((deviations_judgment, analysis_judgment), key=_SEVERITY.__getitem__)


class D3DecisionRule:
    """Missing outcome data: official Table 10 (p. 47)."""

    domain_id = "D3"

    @staticmethod
    def evaluate(results: Mapping[str, RoB2SignalingResult]) -> RoB2Judgment:
        """Return the suggested D3 judgment."""
        complete, evidence, possible, likely = _responses("D3", 4, results)
        if complete in _YES or evidence in _YES or possible in _NO:
            return _LOW
        return _SOME if likely in _NO else _HIGH


class D4DecisionRule:
    """Outcome measurement: official Table 12 (p. 57)."""

    domain_id = "D4"

    @staticmethod
    def evaluate(results: Mapping[str, RoB2SignalingResult]) -> RoB2Judgment:
        """Return the suggested D4 judgment."""
        inappropriate, different, aware, possible, likely = _responses("D4", 5, results)
        if inappropriate in _YES or different in _YES:
            return _HIGH
        if aware in _NO or possible in _NO:
            return _SOME if different == _NI else _LOW
        return _SOME if likely in _NO else _HIGH


class D5DecisionRule:
    """Selection of reported result: official Table 14 (p. 67)."""

    domain_id = "D5"

    @staticmethod
    def evaluate(results: Mapping[str, RoB2SignalingResult]) -> RoB2Judgment:
        """Return the suggested D5 judgment."""
        planned, outcomes, analyses = _responses("D5", 3, results)
        if outcomes in _YES or analyses in _YES:
            return _HIGH
        if planned in _YES and outcomes in _NO and analyses in _NO:
            return _LOW
        return _SOME


DECISION_RULES = (D1DecisionRule, D2DecisionRule, D3DecisionRule, D4DecisionRule, D5DecisionRule)
