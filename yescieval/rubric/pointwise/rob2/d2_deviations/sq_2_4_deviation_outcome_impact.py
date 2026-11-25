"""Outcome impact of deviations.

Source: RoB 2, 22 August 2019, Box 6, pp. 28-29; effect of assignment to intervention.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class DeviationOutcomeImpact(RoB2Rubric):
    """Assess signaling question 2.4 for the specified trial result."""

    rubric_id: str = "2.4"
    rob2_domain_id: str = "D2"
    name: str = "Outcome impact of deviations"
    question: str = "Were these deviations likely to have affected the outcome?"
    guidance: str = (
        "Changes from assigned intervention that are inconsistent with the trial "
        "protocol and arose because of the trial context will impact on the "
        "intervention effect estimate if they affect the outcome, but not "
        "otherwise."
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
