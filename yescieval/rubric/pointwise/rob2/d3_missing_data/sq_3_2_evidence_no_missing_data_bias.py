"""Evidence against missing-data bias.

Source: RoB 2, 22 August 2019, Box 8, pp. 45-46.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class EvidenceNoMissingDataBias(RoB2Rubric):
    """Assess signaling question 3.2 for the specified trial result."""

    rubric_id: str = "3.2"
    rob2_domain_id: str = "D3"
    name: str = "Evidence against missing-data bias"
    question: str = (
        "Is there evidence that the result was not biased by missing outcome data?"
    )
    guidance: str = (
        "Evidence that the result was not biased by missing outcome data may come"
        " from: (1) analysis methods that correct for bias; or (2) sensitivity "
        "analyses showing that results are little changed under a range of "
        "plausible assumptions about the relationship between missingness in the "
        "outcome and its true value. However, imputing the outcome variable, "
        "either through methods such as ‘last-observation-carried-forward’ or via"
        " multiple imputation based only on intervention group, should not be "
        "assumed to correct for bias due to missing outcome data."
    )
    allowed_responses: set[RoB2SignalingResponse] = Field(
        default_factory=lambda: {
            RoB2SignalingResponse("Y"),
            RoB2SignalingResponse("PY"),
            RoB2SignalingResponse("PN"),
            RoB2SignalingResponse("N"),
        }
    )
