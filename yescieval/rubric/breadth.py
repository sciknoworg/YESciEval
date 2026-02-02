from ..base import Rubric

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

<Evaluation-Characteristics>
ContextCoverage: Does the response distribute attention across multiple distinct and relevant contexts (rather than concentrating narrowly on one), thereby demonstrating breadth of coverage with respect to the research question?
</Evaluation-Characteristics>

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
    system_prompt_template: str = context_coverage_prompt


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

<Evaluation-Characteristics>
MethodCoverage: Does the response distribute attention across multiple distinct methods, interventions, or experimental/operational settings relevant to the research question?
</Evaluation-Characteristics>

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

class MethodCoverage(Rubric):
    name: str = "MethodCoverage"
    system_prompt_template: str = method_coverage_prompt

dimension_coverage_prompt = """<Context>
Scientific question answering and synthesis from multiple sources require balancing depth of explanation with breadth of coverage. Breadth is a core dimension of synthesis quality: it captures how widely a response distributes attention across the range of relevant aspects of a research question, rather than concentrating narrowly on a single one.

The response may be a single paragraph or a long-form report with multiple sections. There are no strict requirements on length or formatting; breadth should be evaluated independently of presentation style.

One aspect of breadth is dimension coverage, which concerns whether a response addresses multiple distinct descriptive or evaluative dimensions relevant to the research question, rather than repeatedly focusing on the same one. High breadth reflects coverage of multiple distinct dimensions without requiring exhaustive detail on any single one.

This rubric focuses exclusively on breadth of dimension coverage. Other aspects of scientific quality (such as factual accuracy, evidential grounding, or explanatory depth) are intentionally outside its scope and are assessed by separate evaluation criteria.
</Context>

<Role>
You are tasked as a scientific writing quality evaluator.
</Role>

<Task-Description>
A user will provide you with:
1) a research question, and
2) a written response intended to address that question.

You must evaluate the response using the evaluation characteristic below. Focus on whether the response covers a range of distinct dimensions relevant to the research question, rather than elaborating repeatedly on a single dimension. Your judgment should be based solely on the provided question and response.
</Task-Description>

<Evaluation-Characteristics>
DimensionCoverage: Does the response distribute attention across multiple distinct descriptive or evaluative dimensions relevant to the research question?
</Evaluation-Characteristics>

<Domain-Vocabulary-Examples>
Below are domain-specific examples of terms that often signal different dimensions. They are examples only: their presence is not required, and repetition of the same dimension does not increase the score.

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
Rate the quality from 1 (very bad) to 5 (very good). Provide a short rationale that points to distinct dimensions mentioned in the response and explains how they contribute to breadth.

Return your response in JSON format:
{
  "DimensionCoverage": {"rating": "", "rationale": ""}
}
</Response-Format>

<Example-Responses>
{EXAMPLE_RESPONSES}
</Example-Responses>

<Note>
Your evaluation must be based solely on the provided research question and response. Do not reward repetition or verbosity; reward the number of distinct dimensions covered. A single sentence may contribute to multiple dimensions if it clearly references them.
</Note>"""

class DimensionCoverage(Rubric):
    name: str = "DimensionCoverage"
    system_prompt_template: str = dimension_coverage_prompt

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

<Evaluation-Characteristics>
ScaleCoverage: Does the response distribute attention across multiple distinct scales of analysis, organization, or application relevant to the research question?
</Evaluation-Characteristics>

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

class ScaleCoverage(Rubric):
    name: str = "ScaleCoverage"
    system_prompt_template: str = scale_coverage_prompt
