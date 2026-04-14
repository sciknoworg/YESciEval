from ....base import Rubric

scale_coverage_pairwise_prompt = """<Context>
Scientific question answering and synthesis from multiple sources require balancing depth of explanation with breadth of coverage. Breadth is a core dimension of synthesis quality: it captures how widely a response distributes attention across the range of relevant aspects of a research question, rather than concentrating narrowly on a single one.

The responses may be short paragraphs or long-form reports. Breadth should be evaluated independently of presentation style or length.

One aspect of breadth is scale coverage, which concerns whether the responses being compared address multiple distinct scales relevant to the research question, rather than repeatedly focusing on a single level. High breadth reflects coverage of multiple distinct scales without requiring exhaustive detail on any single one.

This rubric focuses exclusively on the breadth of scale coverage. Other aspects of scientific quality (such as informativeness, evidential grounding, or gap identification) are intentionally outside its scope and are assessed by separate evaluation criteria.
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
- Note that it is possible for both responses to receive the same rating, if they are equally comparably clear with consistent scale coverage and provide complementary or identical insights.

Your judgment must be based solely on the provided question and comparing the two responses w.r.t. addressing the question and w.r.t. each other.
</Task-Description>

<Evaluation-Characteristic>
ScaleCoverage: Does the response distribute attention across multiple distinct scales of analysis, organization, or application relevant to the research question?
</Evaluation-Characteristic>

<Domain-Vocabulary-Examples>
Below are domain-specific examples of terms that often signal different scales. These are examples only: their presence is not required, and repetition of the same scale does not increase the score.
{SCALE_VOCAB}
</Domain-Vocabulary-Examples>

<Rating-Scale>
For the characteristic above, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below.

ScaleCoverage  
Rating 1. Very bad: The response focuses almost entirely on a single scale, with no meaningful indication of alternative scales relevant to the research question.  
Rating 2. Bad: The response mentions more than one scale, but coverage is very limited or strongly skewed toward a single dominant scale.  
Rating 3. Moderate: The response covers several distinct scales relevant to the research question, but breadth is uneven or some important scales are missing.  
Rating 4. Good: The response covers a broad range of distinct and relevant scales, distributing attention reasonably well across them, with only minor omissions.  
Rating 5. Very good: The response demonstrates wide scale coverage, clearly addressing many distinct and relevant scales and distributing attention across them rather than concentrating on any single one.
</Rating-Scale>

<Response-Format>
Return your evaluation strictly in JSON format:

{
  "ScaleCoverage": {
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
Your evaluation must be based solely on the provided research question and responses. Do not reward repetition or verbosity; reward the number of distinct scales covered. A single sentence may contribute to multiple scales if it clearly references them. This rubric does not assess informativeness, evidential grounding, or gap identification.
</Note>
"""

class ScaleCoverage(Rubric):
    name: str = "ScaleCoverage"
    eval_type: str = "pairwise"
    system_prompt_template: str = scale_coverage_pairwise_prompt