"""Deviations caused by the trial context.

Source: RoB 2, 22 August 2019, Box 6, pp. 28-29; effect of assignment to intervention.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class TrialContextDeviations(RoB2Rubric):
    """Assess signaling question 2.3 for the specified trial result."""

    rubric_id: str = "2.3"
    rob2_domain_id: str = "D2"
    name: str = "Deviations caused by the trial context"
    question: str = "Were there deviations from the intended intervention that arose because of the trial context?"
    guidance: str = (
        "For the effect of assignment to intervention, this domain assesses "
        "problems that arise when changes from assigned intervention that are "
        "inconsistent with the trial protocol arose because of the trial context."
        " We use the term trial context to refer to effects of recruitment and "
        "engagement activities on trial participants and when trial personnel "
        "(carers or people delivering the interventions) undermine the "
        "implementation of the trial protocol in ways that would not happen "
        "outside the trial. For example, the process of securing informed consent"
        " may lead participants subsequently assigned to the comparator group to "
        "feel unlucky and therefore seek the experimental intervention, or other "
        "interventions that improve their prognosis.\n\n"
        "Answer ‘Yes’ or ‘Probably yes’ only if there is evidence, or strong "
        "reason to believe, that the trial context led to failure to implement "
        "the protocol interventions or to implementation of interventions not "
        "allowed by the protocol.\n\n"
        "Answer ‘No’ or ‘Probably no’ if there were changes from assigned "
        "intervention that are inconsistent with the trial protocol, such as "
        "non-adherence to intervention, but these are consistent with what could "
        "occur outside the trial context.\n\n"
        "Answer ‘No’ or ‘Probably no’ for changes to intervention that are "
        "consistent with the trial protocol, for example cessation of a drug "
        "intervention because of acute toxicity or use of additional "
        "interventions whose aim is to treat consequences of one of the intended "
        "interventions.\n\n"
        "If blinding is compromised because participants report side effects or "
        "toxicities that are specific to one of the interventions, answer ‘Yes’ "
        "or ‘Probably yes’ only if there were changes from assigned intervention "
        "that are inconsistent with the trial protocol and arose because of the "
        "trial context.\n\n"
        "The answer ‘No information’ may be appropriate, because trialists do not"
        " always report whether deviations arose because of the trial context."
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
