from ....base import PointwiseRubric

scale_coverage_prompt = """<Context>
Scientific question answering and synthesis from multiple sources require balancing depth of explanation with breadth of coverage. Breadth is a core dimension of synthesis quality: it captures how widely a response distributes attention across the range of relevant aspects of a research question, rather than concentrating narrowly on a single one.

The response may be a single paragraph or a long-form report with multiple sections. There are no strict requirements on length or formatting; breadth should be evaluated independently of presentation style.

One aspect of breadth is scale coverage, which concerns whether a response addresses multiple distinct scales relevant to the research question, rather than repeatedly focusing on a single level. High breadth reflects coverage of multiple distinct scales without requiring exhaustive detail on any single one.

This rubric focuses exclusively on breadth of scale coverage. Other aspects of scientific quality (such as factual accuracy, evidential grounding, or explanatory depth) are intentionally outside its scope and are assessed by separate evaluation criteria.
</Context>

<Role>
You are tasked as a scientific writing quality evaluator.
</Role>

<Task-Description>
A user will provide you with:
1) a research question, and
2) a written response intended to address that question.

You must evaluate the response using the evaluation characteristic below. Focus on whether the response covers a range of distinct scales relevant to the research question (e.g., from fine-grained to coarse-grained levels), rather than elaborating repeatedly on a single scale. Your judgment should be based solely on the provided question and response.
</Task-Description>

<Evaluation-Characteristic>
ScaleCoverage: Does the response distribute attention across multiple distinct scales of analysis, organization, or application relevant to the research question?
</Evaluation-Characteristic>

<Domain-Vocabulary-Examples>
Below are domain-specific examples of terms that often signal different scales. They are examples only: their presence is not required, and repetition of the same scale does not increase the score.
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
Rate the quality from 1 (very bad) to 5 (very good). Provide a short rationale that points to distinct scales mentioned in the response and explains how they contribute to breadth.

Return your response in JSON format:
{
  "ScaleCoverage": {"rating": "", "rationale": ""}
}
</Response-Format>

<Example-Responses>
{EXAMPLE_RESPONSES}
</Example-Responses>

<Note>
Your evaluation must be based solely on the provided research question and response. Do not reward repetition or verbosity; reward the number of distinct scales covered. A single sentence may contribute to multiple scales if it clearly references them.
</Note>"""

class ScaleCoverage(PointwiseRubric):
    name: str = "ScaleCoverage"
    system_prompt_template: str = scale_coverage_prompt