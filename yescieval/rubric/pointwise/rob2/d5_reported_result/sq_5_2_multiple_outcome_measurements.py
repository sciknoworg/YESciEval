"""Selection among outcome measurements.

Source: RoB 2, 22 August 2019, Box 11, pp. 63-65.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class MultipleOutcomeMeasurements(RoB2Rubric):
    """Assess signaling question 5.2 for the specified trial result."""

    rubric_id: str = "5.2"
    rob2_domain_id: str = "D5"
    name: str = "Selection among outcome measurements"
    question: str = "Is the numerical result being assessed likely to have been selected, on the basis of the results, from multiple eligible outcome measurements (e.g. scales, definitions, time points) within the outcome domain?"
    guidance: str = (
        "A particular outcome domain (i.e. a true state or endpoint of interest) "
        "may be measured in multiple ways. For example, the domain pain may be "
        "measured using multiple scales (e.g. a visual analogue scale and the "
        "McGill Pain Questionnaire), each at multiple time points (e.g. 3, 6 and "
        "12 weeks post-treatment). If multiple measurements were made, but only "
        "one or a subset is reported on the basis of the results (e.g. "
        "statistical significance), there is a high risk of bias in the fully "
        "reported result. Attention should be restricted to outcome measurements "
        "that are eligible for consideration by the RoB 2 tool user. For example,"
        " if only a result using a specific measurement scale is eligible for "
        "inclusion in a meta-analysis (e.g. Hamilton Depression Rating Scale), "
        "and this is reported by the trial, then there would not be an issue of "
        "selection even if this result was reported (on the basis of the results)"
        " in preference to the result from a different measurement scale (e.g. "
        "Beck Depression Inventory).\n\n"
        "Answer ‘Yes’ or ‘Probably yes’ if:\n"
        "There is clear evidence (usually through examination of a trial protocol"
        " or statistical analysis plan) that a domain was measured in multiple "
        "eligible ways, but data for only one or a subset of measures is fully "
        "reported (without justification), and the fully reported result is "
        "likely to have been selected on the basis of the results. Selection on "
        "the basis of the results can arise from a desire for findings to be "
        "newsworthy, sufficiently noteworthy to merit publication, or to confirm "
        "a prior hypothesis. For example, trialists who have a preconception, or "
        "vested interest in showing, that an experimental intervention is "
        "beneficial may be inclined to report outcome measurements selectively "
        "that are favourable to the experimental intervention.\n\n"
        "Answer ‘No’ or ‘Probably no’ if:\n"
        "There is clear evidence (usually through examination of a trial protocol"
        " or statistical analysis plan) that all eligible reported results for "
        "the outcome domain correspond to all intended outcome measurements.\n"
        "or\n"
        "There is only one possible way in which the outcome domain can be "
        "measured (hence there is no opportunity to select from multiple "
        "measures).\n"
        "or\n"
        "Outcome measurements are inconsistent across different reports on the "
        "same trial, but the trialists have provided the reason for the "
        "inconsistency and it is not related to the nature of the results.\n\n"
        "Answer ‘No information’ if:\n"
        "Analysis intentions are not available, or the analysis intentions are "
        "not reported in sufficient detail to enable an assessment, and there is "
        "more than one way in which the outcome domain could have been measured."
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
