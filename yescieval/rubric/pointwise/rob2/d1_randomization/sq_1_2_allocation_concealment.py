"""Allocation concealment.

Source: RoB 2, 22 August 2019, Box 4, pp. 17-18.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class AllocationConcealment(RoB2Rubric):
    """Assess signaling question 1.2 for the specified trial result."""

    rubric_id: str = "1.2"
    rob2_domain_id: str = "D1"
    name: str = "Allocation concealment"
    question: str = "Was the allocation sequence concealed until participants were enrolled and assigned to interventions?"
    guidance: str = (
        "Answer ‘Yes’ if the trial used any form of remote or centrally "
        "administered method to allocate interventions to participants, where the"
        " process of allocation is controlled by an external unit or "
        "organization, independent of the enrolment personnel (e.g. independent "
        "central pharmacy, telephone or internet-based randomization service "
        "providers).\n\n"
        "Answer ‘Yes’ if envelopes or drug containers were used appropriately. "
        "Envelopes should be opaque, sequentially numbered, sealed with a "
        "tamper-proof seal and opened only after the envelope has been "
        "irreversibly assigned to the participant. Drug containers should be "
        "sequentially numbered and of identical appearance, and dispensed or "
        "administered only after they have been irreversibly assigned to the "
        "participant. This level of detail is rarely provided in reports, and a "
        "judgement may be required to justify an answer of ‘Probably yes’ or "
        "‘Probably no’.\n\n"
        "Answer ‘No’ if there is reason to suspect that the enrolling "
        "investigator or the participant had knowledge of the forthcoming "
        "allocation."
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
