"""Balance of deviations.

Source: RoB 2, 22 August 2019, Box 6, pp. 28-29; effect of assignment to intervention.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class DeviationBalance(RoB2Rubric):
    """Assess signaling question 2.5 for the specified trial result."""

    rubric_id: str = "2.5"
    rob2_domain_id: str = "D2"
    name: str = "Balance of deviations"
    question: str = (
        "Were these deviations from intended intervention balanced between groups?"
    )
    guidance: str = (
        "Changes from assigned intervention that are inconsistent with the trial "
        "protocol and arose because of the trial context are more likely to "
        "impact on intervention effect estimate if they are not balanced between "
        "the intervention groups."
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
