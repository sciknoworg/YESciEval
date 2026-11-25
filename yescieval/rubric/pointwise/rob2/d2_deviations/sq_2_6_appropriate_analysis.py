"""Analysis of assignment to intervention.

Source: RoB 2, 22 August 2019, Box 6, pp. 28-29; effect of assignment to intervention.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class AppropriateAnalysis(RoB2Rubric):
    """Assess signaling question 2.6 for the specified trial result."""

    rubric_id: str = "2.6"
    rob2_domain_id: str = "D2"
    name: str = "Analysis of assignment to intervention"
    question: str = "Was an appropriate analysis used to estimate the effect of assignment to intervention?"
    guidance: str = (
        "Both intention-to-treat (ITT) analyses and modified intention-to-treat "
        "(mITT) analyses excluding participants with missing outcome data should "
        "be considered appropriate. Both naïve ‘per-protocol’ analyses (excluding"
        " trial participants who did not receive their assigned intervention) and"
        " ‘as treated’ analyses (in which trial participants are grouped "
        "according to the intervention that they received, rather than according "
        "to their assigned intervention) should be considered inappropriate. "
        "Analyses excluding eligible trial participants post-randomization should"
        " also be considered inappropriate, but post-randomization exclusions of "
        "ineligible participants (when eligibility was not confirmed until after "
        "randomization, and could not have been influenced by intervention group "
        "assignment) can be considered appropriate."
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
