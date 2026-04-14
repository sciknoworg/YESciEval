from ....base import Rubric

dimension_coverage_pairwise_prompt = """<Context>
Scientific question answering and synthesis from multiple sources require balancing depth with breadth of coverage. Breadth captures how widely a response distributes attention across the range of relevant descriptive or evaluative dimensions of a research question, rather than concentrating narrowly on a single one.

The responses may be short paragraphs or long-form reports. Breadth should be evaluated independently of presentation style or length.

This rubric focuses exclusively on breadth of dimension coverage: whether the responses being compared address multiple distinct dimensions rather than repeatedly elaborating on the same one. Other aspects of scientific quality (such as completeness, evidential grounding, or mechanistic understanding) are intentionally outside its scope and are assessed by separate evaluation criteria.
</Context>

<Role>
You are tasked as a scientific writing quality evaluator performing a pairwise comparison between two texts.
</Role>

<Task-Description>
A user will provide:
1) a research question, and
2) two written responses (Response A and Response B) intended to address that question.

Your task is to:
- First, independently evaluate each response using the evaluation characteristic below.
- Then perform a pairwise comparison of the two responses using the evaluation characteristic below.
- Then grade each response with a comparative rating from 1 (very bad) to 5 (very good) compared to the other response and a subsequent rationale for each comparative response rating.
- Note that it is possible for both responses to receive the same rating, if they are equally comparably clear with logical dimension coverage and provide complementary or identical insights.

Your judgment must be based solely on the provided question and comparing the two responses w.r.t. addressing the question and w.r.t. each other.
</Task-Description>

<Evaluation-Characteristic>
DimensionCoverage: Does the response distribute attention across multiple distinct descriptive or evaluative dimensions relevant to the research question?
</Evaluation-Characteristic>

<Domain-Vocabulary-Examples>
Below are domain-specific examples of terms that often signal different dimensions. These are examples only: their presence is not required, and repetition of the same dimension does not increase the score.
{DIMENSION_VOCAB}
</Domain-Vocabulary-Examples>

<Rating-Scale>
For the characteristic above, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below.

DimensionCoverage  
Rating 1. Very bad: The response focuses almost entirely on a single dimension, with no meaningful indication of alternative dimensions.  
Rating 2. Bad: The response mentions more than one dimension, but coverage is very limited or strongly skewed toward a single dominant one.  
Rating 3. Moderate: The response covers several distinct dimensions relevant to the research question, but breadth is uneven or some important dimensions are missing.  
Rating 4. Good: The response covers a broad range of distinct and relevant dimensions, distributing attention reasonably well across them, with only minor omissions.  
Rating 5. Very good: The response demonstrates wide dimension coverage, clearly addressing many distinct and relevant dimensions and distributing attention across them rather than concentrating on any single one.
</Rating-Scale>

<Response-Format>
Return your evaluation strictly in JSON format:

{
  "DimensionCoverage": {
    "ResponseA": {
      "rating": "",
      "rationale": ""
    },
    "ResponseB": {
      "rating": "",
      "rationale": ""
    }
  }
}

where:
- "rating" is a number from 1 to 5.
- "rationale" is the comparative evaluation rating justification.

</Response-Format>

<Example-Responses>
{EXAMPLE_RESPONSES}
</Example-Responses>

<Note>
Your evaluation must be based solely on the provided research question and responses. Do not reward repetition or verbosity; reward the number of distinct dimensions covered. A single sentence may contribute to multiple dimensions if it clearly references them. This rubric does not assess completeness, evidential grounding, or mechanistic understanding.
</Note>
"""

class DimensionCoverage(Rubric):
    name: str = "DimensionCoverage"
    eval_type: str = "pairwise"
    system_prompt_template: str = dimension_coverage_pairwise_prompt