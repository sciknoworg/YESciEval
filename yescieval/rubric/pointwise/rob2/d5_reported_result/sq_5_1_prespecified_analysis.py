"""Prespecified analysis plan.

Source: RoB 2, 22 August 2019, Box 11, pp. 63-65.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class PrespecifiedAnalysis(RoB2Rubric):
    """Assess signaling question 5.1 for the specified trial result."""

    rubric_id: str = "5.1"
    rob2_domain_id: str = "D5"
    name: str = "Prespecified analysis plan"
    question: str = "Were the data that produced this result analysed in accordance with a pre-specified analysis plan that was finalized before unblinded outcome data were available for analysis?"
    guidance: str = (
        "If the researchers’ pre-specified intentions are available in sufficient"
        " detail, then planned outcome measurements and analyses can be compared "
        "with those presented in the published report(s). To avoid the "
        "possibility of selection of the reported result, finalization of the "
        "analysis intentions must precede availability of unblinded outcome data "
        "to the trial investigators.\n\n"
        "Changes to analysis plans that were made before unblinded outcome data "
        "were available, or that were clearly unrelated to the results (e.g. due "
        "to a broken machine making data collection impossible) do not raise "
        "concerns about bias in selection of the reported result."
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
