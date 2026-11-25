"""Potential influence on outcome assessment.

Source: RoB 2, 22 August 2019, Box 10, pp. 54-55.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class AssessmentCouldBeInfluenced(RoB2Rubric):
    """Assess signaling question 4.4 for the specified trial result."""

    rubric_id: str = "4.4"
    rob2_domain_id: str = "D4"
    name: str = "Potential influence on outcome assessment"
    question: str = "Could assessment of the outcome have been influenced by knowledge of intervention received?"
    guidance: str = (
        "Knowledge of the assigned intervention could influence "
        "participant-reported outcomes (such as level of pain), observer-reported"
        " outcomes involving some judgement, and intervention provider decision "
        "outcomes. They are unlikely to influence observer-reported outcomes that"
        " do not involve judgement, for example all-cause mortality."
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
