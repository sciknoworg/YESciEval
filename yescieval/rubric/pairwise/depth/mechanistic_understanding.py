from ....base import PairwiseRubric

mechanistic_understanding_pairwise_prompt = """<Context>
Scientific question answering and synthesis often require more than listing findings: high-quality scientific writing explains not only what is believed to be true, but also how and why it may be true. This is commonly expressed through mechanistic understanding, where the text describes processes, interactions, intermediate steps, or pathways that connect conditions or components to outcomes.

The responses may be short paragraphs or long-form reports. Mechanistic explanation should be evaluated independently of presentation style or length.

This rubric focuses exclusively on the presence and quality of mechanistic explanations within the provided text of two responses that are compared, emphasizing explanations of how and why phenomena occur rather than descriptions of what is observed. Other aspects of scientific quality (such as factual accuracy, evidential grounding, or completeness) are intentionally outside its scope and are assessed by separate evaluation criteria.
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
- Note that it is possible for both responses to receive the same rating, if they are equally comparably clear with coherent mechanistic explanations and provide complementary or identical insights.

Your judgment must be based solely on the provided question and comparing the two responses w.r.t. addressing the question and w.r.t. each other.
</Task-Description>

<Evaluation-Characteristic>
MechanisticUnderstanding: Does the response explain mechanisms relevant to the research question by describing processes, interactions, intermediate steps, or pathways (i.e., “how/why”), rather than only stating observations or outcomes (“what”)?
</Evaluation-Characteristic>

<Domain-Vocabulary-Examples>
Below are domain-specific terms and phrases that often signal mechanistic discussion. They are examples only: their presence is not required, and their presence alone is not sufficient for a high score.
{MECHANISTIC_VOCAB}
</Domain-Vocabulary-Examples>

<Rating-Scale>
For the characteristic above, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below.

MechanisticUnderstanding
Rating 1. Very bad: The response is purely descriptive, listing facts or outcomes with no meaningful “how/why” explanation relevant to the research question.
Rating 2. Bad: The response contains occasional mechanistic terms or phrases, but explanations are superficial, generic, or weakly connected to the research question.
Rating 3. Moderate: The response provides some mechanistic explanation with partial detail, but important steps, interactions, or pathways are missing, unclear, or inconsistently developed.
Rating 4. Good: The response offers clear mechanistic explanations with multiple concrete steps, interactions, or pathways that are relevant to the research question; minor gaps or imprecision may remain.
Rating 5. Very good: The response provides a detailed, coherent mechanistic account tightly aligned with the research question, explicitly articulating multiple intermediate steps or process-level linkages and clearly distinguishing mechanistic explanation (“how/why”) from descriptive reporting (“what”).
</Rating-Scale>

<Response-Format>
Return your evaluation strictly in JSON format:

{
  "MechanisticUnderstanding": {
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
Your evaluation must be based solely on the provided research question and responses. Do not reward length by itself; reward mechanistic clarity, relevance to the question, and explanatory coherence. This rubric does not assess factual correctness, evidential grounding, or completeness.
</Note>
"""

class MechanisticUnderstanding(PairwiseRubric):
    name: str = "MechanisticUnderstanding"
    system_prompt_template: str = mechanistic_understanding_pairwise_prompt
    