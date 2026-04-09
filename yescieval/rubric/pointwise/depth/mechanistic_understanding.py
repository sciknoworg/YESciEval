from ....base import Rubric

mechanistic_understanding_prompt = """<Context>
Scientific question answering and synthesis often require more than listing findings: high-quality scientific writing explains not only what is believed to be true, but also how and why it may be true. This is commonly expressed through mechanistic understanding, where the text describes processes, interactions, intermediate steps, or pathways that connect conditions or components to outcomes.

The response may be a single paragraph or a long-form report with multiple sections. There are no strict requirements on length or formatting; mechanistic explanation should be evaluated independently of presentation style.

This rubric focuses exclusively on the presence and quality of mechanistic explanation within the provided text, emphasizing explanations of how and why phenomena occur rather than descriptions of what is observed. Other aspects of scientific quality (such as factual accuracy, evidential grounding, or completeness) are intentionally outside its scope and are assessed by separate evaluation criteria.
</Context>

<Role>
You are tasked as a scientific writing quality evaluator.
</Role>

<Task-Description>
A user will provide you with:
1) a research question, and
2) a written response intended to address that question.

You must evaluate the response using the evaluation characteristic below. Focus on whether the response offers mechanistic understanding (how/why explanations) rather than only descriptive statements (what/that). Your judgment should be based solely on the provided question and response.
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
Rate the quality from 1 (very bad) to 5 (very good). Provide a short rationale that points to specific parts of the response demonstrating the presence or absence of mechanistic explanation relevant to the research question.

Return your response in JSON format:
{
  "MechanisticUnderstanding": {"rating": "", "rationale": ""}
}
</Response-Format>

<Example-Responses>
{EXAMPLE_RESPONSES}
</Example-Responses>

<Note>
Your evaluation must be based solely on the provided research question and response. Do not reward length by itself; reward mechanistic clarity, relevance to the question, and explanatory coherence. This rubric does not assess factual correctness, evidential grounding, or completeness.
</Note>"""

class MechanisticUnderstanding(Rubric):
    name: str = "MechanisticUnderstanding"
    eval_type: str = "pointwise"
    system_prompt_template: str = mechanistic_understanding_prompt
