from ...base import Rubric


scope_coverage_prompt = """<Context>
Scientific question answering and synthesis from multiple sources require balancing depth of explanation with breadth of coverage. Breadth is a core dimension of synthesis quality: it captures how widely a response distributes attention across the range of relevant aspects of a research question, rather than concentrating narrowly on a single one.

The response may be a single paragraph or a long-form report with multiple sections. There are no strict requirements on length or formatting; breadth should be evaluated independently of presentation style.

One aspect of breadth is scope coverage, which concerns whether a response addresses multiple distinct scopes of applicability, impact, or relevance associated with the research question, rather than repeatedly focusing on a single scope. High breadth reflects coverage of multiple distinct scopes without requiring exhaustive detail on any single one.

This rubric focuses exclusively on breadth of scope coverage. Other aspects of scientific quality (such as factual accuracy, evidential grounding, or explanatory depth) are intentionally outside its scope and are assessed by separate evaluation criteria.
</Context>

<Role>
You are tasked as a scientific writing quality evaluator.
</Role>

<Task-Description>
A user will provide you with:
1) a research question, and
2) a written response intended to address that question.

You must evaluate the response using the evaluation characteristic below. Focus on whether the response covers a range of distinct scopes relevant to the research question (e.g., different beneficiary groups, functional roles, or applicability ranges), rather than elaborating repeatedly on a single scope. Your judgment should be based solely on the provided question and response.
</Task-Description>

<Evaluation-Characteristics>
ScopeCoverage: Does the response distribute attention across multiple distinct scopes of applicability, impact, or relevance associated with the research question?
</Evaluation-Characteristics>

<Domain-Vocabulary-Examples>
Below are domain-specific examples of terms that often signal different scopes. They are examples only: their presence is not required, and repetition of the same scope does not increase the score.
{SCOPE_VOCAB}
</Domain-Vocabulary-Examples>

<Rating-Scale>
For the characteristic above, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below.

ScopeCoverage  
Rating 1. Very bad: The response focuses almost entirely on a single scope of applicability or impact, with no meaningful indication of alternative scopes.  
Rating 2. Bad: The response mentions more than one scope, but coverage is very limited or strongly skewed toward a single dominant scope.  
Rating 3. Moderate: The response covers several distinct scopes relevant to the research question, but breadth is uneven or some important scopes are missing.  
Rating 4. Good: The response covers a broad range of distinct and relevant scopes, distributing attention reasonably well across them, with only minor omissions.  
Rating 5. Very good: The response demonstrates wide scope coverage, clearly addressing many distinct and relevant scopes and distributing attention across them rather than concentrating on any single one.

</Rating-Scale>

<Response-Format>
Rate the quality from 1 (very bad) to 5 (very good). Provide a short rationale that points to distinct scopes mentioned in the response and explains how they contribute to breadth.

Return your response in JSON format:
{
  "ScopeCoverage": {"rating": "", "rationale": ""}
}
</Response-Format>

<Example-Responses>
{EXAMPLE_RESPONSES}
</Example-Responses>

<Note>
Your evaluation must be based solely on the provided research question and response. Do not reward repetition or verbosity; reward the number of distinct scopes covered. A single sentence may contribute to multiple scopes if it clearly references them.
</Note>"""

class ScopeCoverage(Rubric):
    name: str = "ScopeCoverage"
    system_prompt_template: str = scope_coverage_prompt