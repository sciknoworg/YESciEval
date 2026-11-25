"""Baseline differences.

Source: RoB 2, 22 August 2019, Box 4, pp. 17-18.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class BaselineDifferences(RoB2Rubric):
    """Assess signaling question 1.3 for the specified trial result."""

    rubric_id: str = "1.3"
    rob2_domain_id: str = "D1"
    name: str = "Baseline differences"
    question: str = "Did baseline differences between intervention groups suggest a problem with the randomization process?"
    guidance: str = (
        "Note that differences that are compatible with chance do not lead to a "
        "risk of bias. A small number of differences identified as ‘statistically"
        " significant’ at the conventional 0.05 threshold should usually be "
        "considered to be compatible with chance.\n\n"
        "Answer ‘No’ if no imbalances are apparent or if any observed imbalances "
        "are compatible with chance.\n\n"
        "Answer ‘Yes’ if there are imbalances that indicate problems with the "
        "randomization process, including:\n"
        "(1) substantial differences between intervention group sizes, compared "
        "with the intended allocation ratio; or\n"
        "(2) a substantial excess in statistically significant differences in "
        "baseline characteristics between intervention groups, beyond that "
        "expected by chance; or\n"
        "(3) imbalance in one or more key prognostic factors, or baseline "
        "measures of outcome variables, that is very unlikely to be due to chance"
        " and for which the between-group difference is big enough to result in "
        "bias in the intervention effect estimate.\n\n"
        "Also answer ‘Yes’ if there are other reasons to suspect that the "
        "randomization process was problematic:\n"
        "(4) excessive similarity in baseline characteristics that is not "
        "compatible with chance.\n\n"
        "Answer ‘No information’ when there is no useful baseline information "
        "available (e.g. abstracts, or studies that reported only baseline "
        "characteristics of participants in the final analysis).\n\n"
        "The answer to this question should not influence answers to questions "
        "1.1 or 1.2. For example, if the trial has large baseline imbalances, but"
        " authors report adequate randomization methods, questions 1.1 and 1.2 "
        "should still be answered on the basis of the reported adequate methods, "
        "and any concerns about the imbalance should be raised in the answer to "
        "the question 1.3 and reflected in the domain-level risk-of-bias "
        "judgement.\n\n"
        "Trialists may undertake analyses that attempt to deal with flawed "
        "randomization by controlling for imbalances in prognostic factors at "
        "baseline. To remove the risk of bias caused by problems in the "
        "randomization process, it would be necessary to know, and measure, all "
        "the prognostic factors that were imbalanced at baseline. It is unlikely "
        "that all important prognostic factors are known and measured, so such "
        "analyses will at best reduce the risk of bias. If review authors wish to"
        " assess the risk of bias in a trial that controlled for baseline "
        "imbalances in order to mitigate failures of randomization, the study "
        "should be assessed using the ROBINS-I tool."
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
