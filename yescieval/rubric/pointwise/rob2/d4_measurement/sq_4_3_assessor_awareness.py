"""Outcome assessor awareness.

Source: RoB 2, 22 August 2019, Box 10, pp. 54-55.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class AssessorAwareness(RoB2Rubric):
    """Assess signaling question 4.3 for the specified trial result."""

    rubric_id: str = "4.3"
    rob2_domain_id: str = "D4"
    name: str = "Outcome assessor awareness"
    question: str = "Were outcome assessors aware of the intervention received by study participants?"
    guidance: str = (
        "Answer ‘No’ if outcome assessors were blinded to intervention status. "
        "For participant-reported outcomes, the outcome assessor is the study "
        "participant."
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
