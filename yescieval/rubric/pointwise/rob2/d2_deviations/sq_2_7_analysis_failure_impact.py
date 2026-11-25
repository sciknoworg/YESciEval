"""Impact of analysis departures.

Source: RoB 2, 22 August 2019, Box 6, pp. 28-29; effect of assignment to intervention.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class AnalysisFailureImpact(RoB2Rubric):
    """Assess signaling question 2.7 for the specified trial result."""

    rubric_id: str = "2.7"
    rob2_domain_id: str = "D2"
    name: str = "Impact of analysis departures"
    question: str = "Was there potential for a substantial impact (on the result) of the failure to analyse participants in the group to which they were randomized?"
    guidance: str = (
        "This question addresses whether the number of participants who were "
        "analysed in the wrong intervention group, or excluded from the analysis,"
        " was sufficient that there could have been a substantial impact on the "
        "result. It is not possible to specify a precise rule: there may be "
        "potential for substantial impact even if fewer than 5% of participants "
        "were analysed in the wrong group or excluded, if the outcome is rare or "
        "if exclusions are strongly related to prognostic factors."
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
