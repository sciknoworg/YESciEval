"""Care provider awareness.

Source: RoB 2, 22 August 2019, Box 6, pp. 28-29; effect of assignment to intervention.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class CareProviderAwareness(RoB2Rubric):
    """Assess signaling question 2.2 for the specified trial result."""

    rubric_id: str = "2.2"
    rob2_domain_id: str = "D2"
    name: str = "Care provider awareness"
    question: str = "Were carers and people delivering the interventions aware of participants' assigned intervention during the trial?"
    guidance: str = (
        "If carers or people delivering the interventions are aware of the "
        "assigned intervention then its implementation, or administration of "
        "non-protocol interventions, may differ between the intervention groups. "
        "Blinding may prevent such differences. If participants experienced side "
        "effects or toxicities that carers or people delivering the interventions"
        " knew to be specific to one of the interventions, answer question ‘Yes’ "
        "or ‘Probably yes’. If randomized allocation was not concealed, then it "
        "is likely that carers and people delivering the interventions were aware"
        " of participants' assigned intervention during the trial."
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
