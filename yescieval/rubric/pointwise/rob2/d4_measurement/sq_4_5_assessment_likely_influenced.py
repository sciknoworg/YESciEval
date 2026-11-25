"""Likely influence on outcome assessment.

Source: RoB 2, 22 August 2019, Box 10, pp. 54-55.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class AssessmentLikelyInfluenced(RoB2Rubric):
    """Assess signaling question 4.5 for the specified trial result."""

    rubric_id: str = "4.5"
    rob2_domain_id: str = "D4"
    name: str = "Likely influence on outcome assessment"
    question: str = "Is it likely that assessment of the outcome was influenced by knowledge of intervention received?"
    guidance: str = (
        "This question distinguishes between situations in which (i) knowledge of"
        " intervention status could have influenced outcome assessment but there "
        "is no reason to believe that it did (assessed as ‘Some concerns’) from "
        "those in which (ii) knowledge of intervention status was likely to "
        "influence outcome assessment (assessed as ‘High’). When there are strong"
        " levels of belief in either beneficial or harmful effects of the "
        "intervention, it is more likely that the outcome was influenced by "
        "knowledge of the intervention received. Examples may include "
        "patient-reported symptoms in trials of homeopathy, or assessments of "
        "recovery of function by a physiotherapist who delivered the "
        "intervention."
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
