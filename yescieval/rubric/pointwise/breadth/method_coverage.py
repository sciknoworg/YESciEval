from ....base import PointwiseRubric

method_coverage_prompt = """<Context>
Scientific question answering and synthesis from multiple sources require balancing depth of explanation with breadth of coverage. Breadth is a core dimension of synthesis quality: it captures how widely a response distributes attention across the range of relevant aspects of a research question, rather than concentrating narrowly on a single one.

The response may be a single paragraph or a long-form report with multiple sections. There are no strict requirements on length or formatting; breadth should be evaluated independently of presentation style.

One aspect of breadth is method coverage, which concerns whether a response addresses multiple distinct methods, interventions, or experimental or operational settings relevant to the research question, rather than repeatedly focusing on the same approach. High breadth reflects coverage of multiple distinct methods without requiring exhaustive detail on any single one. This rubric focuses exclusively on breadth of method or intervention coverage. Other aspects of scientific quality (such as factual accuracy, evidential grounding, or explanatory depth) are intentionally outside its scope and are assessed by separate evaluation criteria.
</Context>

<Role>
You are tasked as a scientific writing quality evaluator.
</Role>

<Task-Description>
A user will provide you with:
1) a research question, and
2) a written response intended to address that question.

You must evaluate the response using the evaluation characteristic below. Focus on whether the response covers a range of distinct methods, interventions, or settings relevant to the research question, rather than elaborating repeatedly on a single method. Your judgment should be based solely on the provided question and response.
</Task-Description>

<Evaluation-Characteristic>
MethodCoverage: Does the response distribute attention across multiple distinct methods, interventions, or experimental/operational settings relevant to the research question?
</Evaluation-Characteristic>

<Domain-Vocabulary-Examples>
Below are domain-specific examples of terms that often signal different methods or interventions. They are examples only: their presence is not required, and repetition of the same method does not increase the score.
{METHOD_VOCAB}
</Domain-Vocabulary-Examples>

<Rating-Scale>
For the characteristic above, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below.

MethodCoverage  
Rating 1. Very bad: The response focuses almost entirely on a single method or intervention, with no meaningful indication of alternative approaches.  
Rating 2. Bad: The response mentions more than one method or intervention, but coverage is very limited or strongly skewed toward a single dominant approach.  
Rating 3. Moderate: The response covers several distinct methods or interventions relevant to the research question, but breadth is uneven or some important approaches are missing.  
Rating 4. Good: The response covers a broad range of distinct and relevant methods or interventions, distributing attention reasonably well across them, with only minor omissions.  
Rating 5. Very good: The response demonstrates wide method coverage, clearly addressing many distinct and relevant methods or interventions and distributing attention across them rather than concentrating on any single one.

</Rating-Scale>

<Response-Format>
Rate the quality from 1 (very bad) to 5 (very good). Provide a short rationale that points to distinct methods or interventions mentioned in the response and explains how they contribute to breadth.

Return your response in JSON format:
{
  "MethodCoverage": {"rating": "", "rationale": ""}
}
</Response-Format>

<Example-Responses>
{EXAMPLE_RESPONSES}
</Example-Responses>

<Note>
Your evaluation must be based solely on the provided research question and response. Do not reward repetition or verbosity; reward the number of distinct methods or interventions covered. A single sentence may contribute to multiple methods if it clearly references them.
</Note>"""

class MethodCoverage(PointwiseRubric):
    name: str = "MethodCoverage"
    system_prompt_template: str = method_coverage_prompt