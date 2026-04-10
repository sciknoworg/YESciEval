from ....base import Rubric

context_coverage_prompt = """<Context>
Scientific question answering and synthesis from multiple sources require balancing depth of explanation with breadth of coverage. Breadth is a core dimension of synthesis quality: it captures how widely a response distributes attention across the range of contexts that are relevant to a research question, rather than concentrating narrowly on a single setting.

The response may be a single paragraph or a long-form report with multiple sections. There are no strict requirements on length or formatting; breadth should be evaluated independently of presentation style.

One aspect of breadth is contextual coverage, which concerns whether a response addresses multiple distinct contexts relevant to the research question, rather than repeatedly elaborating on the same one. High breadth reflects coverage of multiple distinct and pertinent contexts without requiring exhaustive detail on any individual context. A response can exhibit high breadth even when individual contexts are treated concisely, as long as attention is distributed across them.
</Context>

<Role>
You are tasked as a scientific writing quality evaluator.
</Role>

<Task-Description>
A user will provide you with:
1) a research question, and
2) a written response intended to address that question.

You must evaluate the response using the evaluation characteristic below. Focus on whether the response covers multiple distinct contexts relevant to the research question, rather than repeatedly elaborating on a single context. Your judgment should be based solely on the provided question and response.
</Task-Description>

<Evaluation-Characteristic>
ContextCoverage: Does the response distribute attention across multiple distinct and relevant contexts (rather than concentrating narrowly on one), thereby demonstrating breadth of coverage with respect to the research question?
</Evaluation-Characteristic>

<Domain-Vocabulary-Examples>
Below are domain-specific examples of terms that often signal different contexts. They are examples only: their presence is not required, and repetition of the same context does not increase the score.
{CONTEXT_VOCAB}
</Domain-Vocabulary-Examples>

<Rating-Scale>
For the characteristic above, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below.

ContextCoverage
Rating 1. Very bad: The response focuses almost entirely on a single context, with no meaningful indication of alternative contexts relevant to the research question.
Rating 2. Bad: The response mentions more than one context, but coverage is very limited or heavily skewed toward a single dominant context.
Rating 3. Moderate: The response covers several distinct contexts relevant to the research question, but breadth is uneven or some important contexts are missing.
Rating 4. Good: The response covers a broad range of distinct and relevant contexts, distributing attention reasonably well across them, with only minor omissions.
Rating 5. Very good: The response demonstrates wide contextual breadth, clearly covering many distinct and relevant contexts and distributing attention across them rather than concentrating on any single one.

</Rating-Scale>

<Response-Format>
Rate the quality from 1 (very bad) to 5 (very good). Provide a short rationale that points to distinct contexts mentioned in the response and explains how they contribute to breadth.

Return your response in JSON format:
{
  "ContextCoverage": {"rating": "", "rationale": ""}
}
</Response-Format>

<Example-Responses>
{EXAMPLE_RESPONSES}
</Example-Responses>

<Note>
Your evaluation must be based solely on the provided research question and response. Do not reward repetition or verbosity; reward the number of distinct contexts covered. A single sentence may contribute to multiple contexts if it clearly references them. This rubric does not assess correctness, evidential grounding, or explanatory depth.
</Note>"""

class ContextCoverage(Rubric):
    name: str = "ContextCoverage"
    eval_type: str = "pointwise"
    system_prompt_template: str = context_coverage_prompt

