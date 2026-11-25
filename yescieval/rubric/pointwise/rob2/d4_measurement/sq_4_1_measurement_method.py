"""Suitability of outcome measurement.

Source: RoB 2, 22 August 2019, Box 10, pp. 54-55.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class MeasurementMethod(RoB2Rubric):
    """Assess signaling question 4.1 for the specified trial result."""

    rubric_id: str = "4.1"
    rob2_domain_id: str = "D4"
    name: str = "Suitability of outcome measurement"
    question: str = "Was the method of measuring the outcome inappropriate?"
    guidance: str = (
        "This question aims to identify methods of outcome measurement (data "
        "collection) that are unsuitable for the outcome they are intended to "
        "evaluate. The question does not aim to assess whether the choice of "
        "outcome being evaluated was sensible (e.g. because it is a surrogate or "
        "proxy for the main outcome of interest). In most circumstances, for "
        "pre-specified outcomes, the answer to this question will be ‘No’ or "
        "‘Probably no’.\n\n"
        "Answer ‘Yes’ or ‘Probably yes’ if the method of measuring the outcome is"
        " inappropriate, for example because:\n"
        "(1) it is unlikely to be sensitive to plausible intervention effects "
        "(e.g. important ranges of outcome values fall outside levels that are "
        "detectable using the measurement method); or\n"
        "(2) the measurement instrument has been demonstrated to have poor "
        "validity."
    )
    allowed_responses: set[RoB2SignalingResponse] = Field(
        default_factory=lambda: {
            RoB2SignalingResponse("Y"),
            RoB2SignalingResponse("PY"),
            RoB2SignalingResponse("PN"),
            RoB2SignalingResponse("N"),
            RoB2SignalingResponse("NI"),
        }
    )
