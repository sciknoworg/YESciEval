"""Availability of outcome data.

Source: RoB 2, 22 August 2019, Box 8, pp. 45-46.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class OutcomeDataAvailability(RoB2Rubric):
    """Assess signaling question 3.1 for the specified trial result."""

    rubric_id: str = "3.1"
    rob2_domain_id: str = "D3"
    name: str = "Availability of outcome data"
    question: str = "Were data for this outcome available for all, or nearly all, participants randomized?"
    guidance: str = (
        "The appropriate study population for an analysis of the intention to "
        "treat effect is all randomized participants.\n\n"
        "“Nearly all” should be interpreted as that the number of participants "
        "with missing outcome data is sufficiently small that their outcomes, "
        "whatever they were, could have made no important difference to the "
        "estimated effect of intervention.\n\n"
        "For continuous outcomes, availability of data from 95% of the "
        "participants will often be sufficient. For dichotomous outcomes, the "
        "proportion required is directly linked to the risk of the event. If the "
        "observed number of events is much greater than the number of "
        "participants with missing outcome data, the bias would necessarily be "
        "small.\n\n"
        "Only answer ‘No information’ if the trial report provides no information"
        " about the extent of missing outcome data. This situation will usually "
        "lead to a judgement that there is a high risk of bias due to missing "
        "outcome data.\n\n"
        "Note that imputed data should be regarded as missing data, and not "
        "considered as ‘outcome data’ in the context of this question."
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
