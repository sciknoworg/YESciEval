"""Likely outcome-dependent missingness.

Source: RoB 2, 22 August 2019, Box 8, pp. 45-46.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class MissingnessLikelyDepended(RoB2Rubric):
    """Assess signaling question 3.4 for the specified trial result."""

    rubric_id: str = "3.4"
    rob2_domain_id: str = "D3"
    name: str = "Likely outcome-dependent missingness"
    question: str = (
        "Is it likely that missingness in the outcome depended on its true value?"
    )
    guidance: str = (
        "This question distinguishes between situations in which (i) missingness "
        "in the outcome could depend on its true value (assessed as ‘Some "
        "concerns’) from those in which (ii) it is likely that missingness in the"
        " outcome depended on its true value (assessed as ‘High risk of bias’). "
        "Five reasons for answering ‘Yes’ are:\n\n"
        "1. Differences between intervention groups in the proportions of missing"
        " outcome data. If there is a difference between the effects of the "
        "experimental and comparator interventions on the outcome, and the "
        "missingness in the outcome is influenced by its true value, then the "
        "proportions of missing outcome data are likely to differ between "
        "intervention groups. Such a difference suggests a risk of bias due to "
        "missing outcome data, because the trial result will be sensitive to "
        "missingness in the outcome being related to its true value. For "
        "time-to-event-data, the analogue is that rates of censoring (loss to "
        "follow-up) differ between the intervention groups.\n"
        "2. Reported reasons for missing outcome data provide evidence that "
        "missingness in the outcome depends on its true value;\n"
        "3. Reported reasons for missing outcome data differ between the "
        "intervention groups;\n"
        "4. The circumstances of the trial make it likely that missingness in the"
        " outcome depends on its true value. For example, in trials of "
        "interventions to treat schizophrenia it is widely understood that "
        "continuing symptoms make drop out more likely.\n"
        "5. In time-to-event analyses, participants’ follow up is censored when "
        "they stop or change their assigned intervention, for example because of "
        "drug toxicity or, in cancer trials, when participants switch to "
        "second-line chemotherapy.\n\n"
        "Answer ‘No’ if the analysis accounted for participant characteristics "
        "that are likely to explain the relationship between missingness in the "
        "outcome and its true value."
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
