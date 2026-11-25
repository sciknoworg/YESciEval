"""Selection among eligible analyses.

Source: RoB 2, 22 August 2019, Box 11, pp. 63-65.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class MultipleEligibleAnalyses(RoB2Rubric):
    """Assess signaling question 5.3 for the specified trial result."""

    rubric_id: str = "5.3"
    rob2_domain_id: str = "D5"
    name: str = "Selection among eligible analyses"
    question: str = "Is the numerical result being assessed likely to have been selected, on the basis of the results, from multiple eligible analyses of the data?"
    guidance: str = (
        "A particular outcome measurement may be analysed in multiple ways. "
        "Examples include: unadjusted and adjusted models; final value vs change "
        "from baseline vs analysis of covariance; transformations of variables; "
        "different definitions of composite outcomes (e.g. ‘major adverse "
        "event’); conversion of continuously scaled outcome to categorical data "
        "with different cut-points; different sets of covariates for adjustment; "
        "and different strategies for dealing with missing data. Application of "
        "multiple methods generates multiple effect estimates for a specific "
        "outcome measurement. If multiple estimates are generated but only one or"
        " a subset is reported on the basis of the results (e.g. statistical "
        "significance), there is a high risk of bias in the fully reported "
        "result. Attention should be restricted to analyses that are eligible for"
        " consideration by the RoB 2 tool user. For example, if only the result "
        "from an analysis of post-intervention values is eligible for inclusion "
        "in a meta-analysis (e.g. at 12 weeks after randomization), and this is "
        "reported by the trial, then there would not be an issue of selection "
        "even if this result was reported (on the basis of the results) in "
        "preference to the result from an analysis of changes from baseline.\n\n"
        "Answer ‘Yes’ or ‘Probably yes’ if:\n"
        "There is clear evidence (usually through examination of a trial protocol"
        " or statistical analysis plan) that a measurement was analysed in "
        "multiple eligible ways, but data for only one or a subset of analyses is"
        " fully reported (without justification), and the fully reported result "
        "is likely to have been selected on the basis of the results. Selection "
        "on the basis of the results arises from a desire for findings to be "
        "newsworthy, sufficiently noteworthy to merit publication, or to confirm "
        "a prior hypothesis. For example, trialists who have a preconception or "
        "vested interest in showing that an experimental intervention is "
        "beneficial may be inclined to selectively report analyses that are "
        "favourable to the experimental intervention.\n\n"
        "Answer ‘No’ or ‘Probably no’ if:\n"
        "There is clear evidence (usually through examination of a trial protocol"
        " or statistical analysis plan) that all eligible reported results for "
        "the outcome measurement correspond to all intended analyses.\n"
        "or\n"
        "There is only one possible way in which the outcome measurement can be "
        "analysed (hence there is no opportunity to select from multiple "
        "analyses).\n"
        "or\n"
        "Analyses are inconsistent across different reports on the same trial, "
        "but the trialists have provided the reason for the inconsistency and it "
        "is not related to the nature of the results.\n\n"
        "Answer ‘No information’ if:\n"
        "Analysis intentions are not available, or the analysis intentions are "
        "not reported in sufficient detail to enable an assessment, and there is "
        "more than one way in which the outcome measurement could have been "
        "analysed."
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
