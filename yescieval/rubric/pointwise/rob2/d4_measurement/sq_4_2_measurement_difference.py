"""Differences in outcome measurement.

Source: RoB 2, 22 August 2019, Box 10, pp. 54-55.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class MeasurementDifference(RoB2Rubric):
    """Assess signaling question 4.2 for the specified trial result."""

    rubric_id: str = "4.2"
    rob2_domain_id: str = "D4"
    name: str = "Differences in outcome measurement"
    question: str = "Could measurement or ascertainment of the outcome have differed between intervention groups?"
    guidance: str = (
        "Comparable methods of outcome measurement (data collection) involve the "
        "same measurement methods and thresholds, used at comparable time points."
        " Differences between intervention groups may arise because of "
        "‘diagnostic detection bias’ in the context of passive collection of "
        "outcome data, or if an intervention involves additional visits to a "
        "healthcare provider, leading to additional opportunities for outcome "
        "events to be identified."
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
