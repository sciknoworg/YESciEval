from ....base import PairwiseRubric

explicit_uncertainty_pairwise_prompt = """<Context>
Scientific question answering and synthesis often require more than listing findings: high-quality scientific writing clearly communicates when conclusions or underlying knowledge remain uncertain, unclear, or unknown.

The responses may be short paragraphs or long-form reports. Explicit uncertainty should be evaluated independently of presentation style or length.

This rubric focuses exclusively on whether the provided text of two responses that are compared explicitly identifies knowledge as uncertain, unclear, or unknown in relation to the research question. Other aspects of scientific quality (such as factual completeness, causal reasoning, or relevancy) are intentionally outside its scope and are assessed by separate evaluation criteria.
</Context>

<Role>
You are tasked as a scientific writing quality evaluator performing a pairwise comparison between two texts.
</Role>

<Task-Description>
A user will provide:
1) a research question, and
2) Two written responses (Response A and Response B) intended to address that question.

Your task is to:
- First, independently evaluate each response using the evaluation characteristic below.
- Then perform a pairwise comparison of the two responses using the evaluation characteristic below.
- Then grade each response with a comparative rating from 1 (very bad) to 5 (very good) compared to the other response and a subsequent rationale for each comparative response rating.
- Note that it is possible for both responses to receive the same rating if they are equally comparably clear with systematic uncertainties and provide complementary or identical insights.

Your judgment must be based solely on the provided question and comparing the two responses w.r.t. addressing the question and w.r.t. each other.
</Task-Description>

<Evaluation-Characteristic>
ExplicitUncertainty: Does the response clearly indicate what is uncertain, unclear, or unknown in relation to the research question, rather than presenting all findings as settled or certain?
</Evaluation-Characteristic>

<Domain-Vocabulary-Examples>
Below are domain-specific terms and phrases that often signal explicit uncertainty discussion. These are examples only: their presence is not required, and their presence alone is not sufficient for a high score.
{UNCERTAINTY_VOCAB}
</Domain-Vocabulary-Examples>

<Rating-Scale>
For the characteristic above, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below.

Rating 1. Very bad: The response provides no indication of uncertainty; all statements are presented as settled, with no acknowledgment of what is uncertain, unclear, or unknown.
Rating 2. Bad: The response occasionally signals uncertainty, but markers of what is uncertain, unclear, or unknown are vague, or weakly connected to the research question.
Rating 3. Moderate: The response identifies some aspects that are uncertain, unclear, or unknown, but important elements are missing, inconsistently marked, or only partially explained.
Rating 4. Good: The response clearly signals multiple uncertainties, unclear points, or unknown aspects relevant to the research question, minor gaps or imprecision in the explicit marking may remain.
Rating 5. Very good: The response provides a detailed, coherent account of what is uncertain, unclear, or unknown, explicitly and consistently marking multiple aspects of unresolved knowledge and clearly distinguishing these from statements presented as certain or settled.
</Rating-Scale>

<Response-Format>
Return your evaluation strictly in JSON format:

{
  "ExplicitUncertainty": {
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
Your evaluation must be based solely on the provided research question and responses. Do not reward length by itself; reward clear and relevant identification of what is uncertain, unclear, or unknown. This rubric does not assess factual completeness, causal reasoning, or relevancy.
</Note>
"""

class ExplicitUncertainty(PairwiseRubric):
    name: str = "ExplicitUncertainty"
    system_prompt_template: str = explicit_uncertainty_pairwise_prompt
