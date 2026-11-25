"""Participant awareness.

Source: RoB 2, 22 August 2019, Box 6, pp. 28-29; effect of assignment to intervention.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class ParticipantAwareness(RoB2Rubric):
    """Assess signaling question 2.1 for the specified trial result."""

    rubric_id: str = "2.1"
    rob2_domain_id: str = "D2"
    name: str = "Participant awareness"
    question: str = (
        "Were participants aware of their assigned intervention during the trial?"
    )
    guidance: str = (
        "If participants are aware of their assigned intervention it is more "
        "likely that health-related behaviours will differ between the "
        "intervention groups. Blinding participants, most commonly through use of"
        " a placebo or sham intervention, may prevent such differences. If "
        "participants experienced side effects or toxicities that they knew to be"
        " specific to one of the interventions, answer this question ‘Yes’ or "
        "‘Probably yes’."
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
