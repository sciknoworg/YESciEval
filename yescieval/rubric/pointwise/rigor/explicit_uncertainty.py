from ....base import PointwiseRubric

explicit_uncertainty_prompt =  """<Context>
Scientific question answering and synthesis often require more than listing findings: high-quality scientific writing communicates to the reader when conclusions or underlying knowledge remain uncertain, unclear, or unknown.

The response may be a single paragraph or a long-form report with multiple sections. There are no strict requirements on length or formatting; explicit uncertainty should be evaluated independently of presentation style.

This rubric focuses exclusively on whether the provided text explicitly identifies knowledge as uncertain, unclear, or unknown, rather than treating all statements as resolved. Other aspects of scientific quality (such as factual completeness, causal reasoning, or relevancy) are intentionally outside its scope and are assessed by separate evaluation criteria.
</Context>

<Role>
You are tasked as a scientific writing quality evaluator.
</Role>

<Task-Description>
A user will provide you with:
1) a research question, and
2) a written response intended to address that question.

You must evaluate the response using the evaluation characteristic below. Focus on the explicit indication of uncertainty, unclear points, or unknown aspects, rather than on fully resolved statements. Your judgment should be based solely on the provided question and response.
</Task-Description>

<Evaluation-Characteristic>
ExplicitUncertainty: Does the response clearly indicate what is uncertain, unclear, or unknown in relation to the research question, rather than presenting all findings as settled or certain?
</Evaluation-Characteristic>

<Domain-Vocabulary-Examples>
Below are domain-specific terms and phrases that often signal uncertainty discussion. They are examples only: their presence is not required, and their presence alone is not sufficient for a high score.
{UNCERTAINTY_VOCAB}
</Domain-Vocabulary-Examples>

<Rating-Scale>
For the characteristic above, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below.

Rating 1. Very bad: The response provides no indication of uncertainty, all statements are presented as settled, with no acknowledgment of what is uncertain, unclear, or unknown.
Rating 2. Bad: The response occasionally signals uncertainty, but markers of what is uncertain, unclear, or unknown are vague, or weakly connected to the research question.
Rating 3. Moderate: The response identifies some aspects that are uncertain, unclear, or unknown, but important elements are missing, inconsistently marked, or only partially explained.
Rating 4. Good: The response clearly signals multiple uncertainties, unclear points, or unknown aspects relevant to the research question, minor gaps or imprecision in the explicit marking may remain.
Rating 5. Very good: The response provides a detailed, coherent account of what is uncertain, unclear, or unknown, explicitly and consistently marking multiple aspects of unresolved knowledge and clearly distinguishing these from statements presented as certain or settled.
</Rating-Scale>

<Response-Format>
Rate the quality from 1 (very bad) to 5 (very good). Provide a short rationale that points to specific parts of the response demonstrating the presence or absence of uncertainty relevant to the research question.

Return your response in JSON format:
{
  "ExplicitUncertainty": {"rating": "", "rationale": ""}
}
</Response-Format>

<Example-Responses>
{EXAMPLE_RESPONSES}
</Example-Responses>

<Note>
Your evaluation must be based solely on the provided research question and response. Do not reward length by itself; reward clear and relevant identification of what is uncertain, unclear, or unknown. This rubric does not assess factual completeness, causal reasoning, or relevancy.
</Note>"""

class ExplicitUncertainty(PointwiseRubric):
    name: str = "ExplicitUncertainty"
    system_prompt_template: str = explicit_uncertainty_prompt
