"""Random allocation sequence.

Source: RoB 2, 22 August 2019, Box 4, pp. 17-18.
https://drive.google.com/file/d/19R9savfPdCHC8XLz2iiMvL_71lPJERWK/view
Question wording follows the tool. Guidance is the official RoB 2 text, transcribed from the reference files.
"""

from pydantic import Field

from .....base import RoB2Rubric, RoB2SignalingResponse


class RandomSequence(RoB2Rubric):
    """Assess signaling question 1.1 for the specified trial result."""

    rubric_id: str = "1.1"
    rob2_domain_id: str = "D1"
    name: str = "Random allocation sequence"
    question: str = "Was the allocation sequence random?"
    guidance: str = (
        "Answer ‘Yes’ if a random component was used in the sequence generation "
        "process. Examples include computer-generated random numbers; reference "
        "to a random number table; coin tossing; shuffling cards or envelopes; "
        "throwing dice; or drawing lots. Minimization is generally implemented "
        "with a random element (at least when the scores are equal), so an "
        "allocation sequence that is generated using minimization should "
        "generally be considered to be random.\n\n"
        "Answer ‘No’ if no random element was used in generating the allocation "
        "sequence or the sequence is predictable. Examples include alternation; "
        "methods based on dates (of birth or admission); patient record numbers; "
        "allocation decisions made by clinicians or participants; allocation "
        "based on the availability of the intervention; or any other systematic "
        "or haphazard method.\n\n"
        "Answer ‘No information’ if the only information about randomization "
        "methods is a statement that the study is randomized.\n\n"
        "In some situations a judgement may be made to answer ‘Probably no’ or "
        "‘Probably yes’. For example, in the context of a large trial run by an"
        " experienced clinical trials unit, absence of specific information about"
        " generation of the randomization sequence, in a paper published in a "
        "journal with rigorously enforced word count limits, is likely to result "
        "in a response of ‘Probably yes’ rather than ‘No information’. "
        "Alternatively, if other (contemporary) trials by the same investigator "
        "team have clearly used non-random sequences, it might be reasonable to "
        "assume that the current study was done using similar methods."
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
