"""Possible outcome-dependent missingness.

Source: RoB 2, 22 August 2019, Box 8, pp. 45-46.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class MissingnessCouldDepend(RoB2Rubric):
    """Assess signaling question 3.3 for the specified trial result."""

    rubric_id: str = "3.3"
    rob2_domain_id: str = "D3"
    name: str = "Possible outcome-dependent missingness"
    question: str = "Could missingness in the outcome depend on its true value?"
    guidance: str = (
        "If loss to follow up, or withdrawal from the study, could be related to "
        "participants’ health status, then it is possible that missingness in the"
        " outcome was influenced by its true value. However, if all missing "
        "outcome data occurred for documented reasons that are unrelated to the "
        "outcome then the risk of bias due to missing outcome data will be low "
        "(for example, failure of a measuring device or interruptions to routine "
        "data collection).\n\n"
        "In time-to-event analyses, participants censored during trial follow-up,"
        " for example because they withdrew from the study, should be regarded as"
        " having missing outcome data, even though some of their follow up is "
        "included in the analysis. Note that such participants may be shown as "
        "included in analyses in CONSORT flow diagrams."
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
