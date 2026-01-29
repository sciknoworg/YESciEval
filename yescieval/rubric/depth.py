from ..base import Rubric

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

<Evaluation-Characteristics>
MechanisticUnderstanding: Does the response explain mechanisms relevant to the research question by describing processes, interactions, intermediate steps, or pathways (i.e., “how/why”), rather than only stating observations or outcomes (“what”)?
</Evaluation-Characteristics>

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
    system_prompt_template: str = mechanistic_understanding_prompt

causal_reasoning_prompt = """<Context>
Scientific question answering and synthesis often require more than listing findings: high-quality scientific writing explains not only what is believed to be true, but also how and why it may be true. One important aspect of this is causal reasoning, where the text articulates cause–effect relationships, conditions, mediators, moderators, and causal chains, rather than only describing associations or co-occurrences.

The response may be a single paragraph or a long-form report with multiple sections. There are no strict requirements on length or formatting; causal reasoning should be evaluated independently of presentation style.

This rubric focuses exclusively on the presence and quality of causal reasoning within the provided text, emphasizing language and structure that express why something happens (cause → effect) rather than only what is observed or correlated. Other aspects of scientific quality (such as factual accuracy, evidential grounding, or completeness) are intentionally outside its scope and are assessed by separate evaluation criteria.
</Context>

<Role>
You are tasked as a scientific writing quality evaluator.
</Role>

<Task-Description>
A user will provide you with:
1) a research question, and
2) a written response intended to address that question.

You must evaluate the response using the evaluation characteristic below. Focus on whether the response expresses causal relationships relevant to the research question (cause–effect, mediators/moderators, conditions), rather than only descriptive or correlational statements. Your judgment should be based solely on the provided question and response.
</Task-Description>

<Evaluation-Characteristics>
CausalReasoning: Does the response demonstrate causal reasoning relevant to the research question by explicitly articulating cause–effect relationships (including causal chains, mediators, moderators, or conditional causal statements), rather than only reporting associations, trends, or co-occurrences?
</Evaluation-Characteristics>

<Domain-Vocabulary-Examples>
Below are examples of causal connectives and expressions that often signal causal reasoning (across domains). They are examples only: their presence is not required, and their presence alone is not sufficient for a high score.

{CAUSAL_VOCAB}
</Domain-Vocabulary-Examples>

<Rating-Scale>
For the characteristic above, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below.

CausalReasoning
Rating 1. Very bad: The response is purely descriptive or correlational, offering no meaningful cause–effect statements relevant to the research question.
Rating 2. Bad: The response uses occasional causal words (e.g., “leads to”, “because”) but causal links are unclear, generic, or asserted without coherent cause–effect structure (often indistinguishable from correlation).
Rating 3. Moderate: The response includes some clear causal claims relevant to the question, but they are limited in number, shallow (single-step), inconsistently developed, or mixed with ambiguous association language.
Rating 4. Good: The response provides clear cause–effect reasoning with multiple relevant causal links and some structure (e.g., conditions, mediators/moderators, or short causal chains); minor ambiguity or gaps may remain.
Rating 5. Very good: The response demonstrates strong causal reasoning throughout, using explicit and coherent cause–effect structure aligned to the research question, including multiple well-articulated causal chains and/or conditional pathways (e.g., A → B → C; “A affects C via B”; “A increases B only under condition D”), and clearly distinguishes causation from association.

</Rating-Scale>

<Response-Format>
Rate the quality from 1 (very bad) to 5 (very good). Provide a short rationale that points to specific parts of the response demonstrating the presence or absence of causal reasoning relevant to the research question.

Return your response in JSON format:
{
  "CausalReasoning": {"rating": "", "rationale": ""}
}
</Response-Format>

<Example-Responses>

{EXAMPLE_RESPONSES}

</Example-Responses>

<Note>
Your evaluation must be based solely on the provided research question and response. Do not reward length by itself; reward clarity and coherence of causal structure, relevance to the question, and explicit differentiation between causation and association. This rubric does not assess factual correctness, evidential grounding, or completeness.
</Note>"""

class CausalReasoning(Rubric):
    name: str = "CausalReasoning"
    system_prompt_template: str = causal_reasoning_prompt

temporal_precision_prompt = """<Context>
Scientific question answering and synthesis often require more than listing findings: high-quality scientific writing is precise about time when time matters. Temporal precision refers to how clearly the text specifies when something occurs, over what duration, or across what interval. Precise temporal expressions include calendar dates, numeric durations, bounded year ranges, or clearly delimited intervals; vague temporal markers include expressions like “historically”, “recently”, “long-term”, or “soon” without further specification.

The response may be a single paragraph or a long-form report with multiple sections. There are no strict requirements on length or formatting; temporal precision should be evaluated independently of presentation style.

This rubric focuses exclusively on the presence and quality of temporal precision within the provided text, emphasizing specific and bounded time expressions (when/for how long/over what interval) rather than vague temporal language. Other aspects of scientific quality (such as factual accuracy, evidential grounding, or completeness) are intentionally outside its scope and are assessed by separate evaluation criteria.
</Context>

<Role>
You are tasked as a scientific writing quality evaluator.
</Role>

<Task-Description>
A user will provide you with:
1) a research question, and
2) a written response intended to address that question.

You must evaluate the response using the evaluation characteristic below. Focus on whether the response uses specific, bounded temporal expressions when making temporally-relevant statements, rather than relying on vague time markers. Your judgment should be based solely on the provided question and response.
</Task-Description>

<Evaluation-Characteristics>
TemporalPrecision: Does the response use specific, bounded, and meaningful temporal expressions (e.g., dates, durations, intervals, year ranges) when discussing time-relevant aspects of the research question, rather than vague temporal markers?
</Evaluation-Characteristics>

<Domain-Vocabulary-Examples>
Below are examples of temporal expressions. They are examples only: their presence is not required, and their presence alone is not sufficient for a high score.

{TEMPORAL_VOCAB}
</Domain-Vocabulary-Examples>

<Rating-Scale>
For the characteristic above, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below.

TemporalPrecision
Rating 1. Very bad: The response uses time-related language only vaguely (or not at all when time is relevant), relying on unspecific markers such as “historically” or “long-term” without any bounded dates, durations, or intervals.
Rating 2. Bad: The response includes a few temporal references, but they are mostly vague or inconsistently specified; precise dates/durations/intervals are rare and do not meaningfully clarify timing.
Rating 3. Moderate: The response provides some specific temporal expressions (dates, durations, ranges), but many temporal references remain vague, or precision is applied only in isolated parts of the response.
Rating 4. Good: The response frequently uses specific, bounded temporal expressions that help interpret timing and change (dates, durations, intervals, ranges), with only minor reliance on vague temporal markers.
Rating 5. Very good: The response is consistently temporally precise wherever time is relevant, using specific and bounded expressions (dates, numeric durations, delimited intervals/ranges) and minimizing vague markers; temporal comparisons and sequences are clearly specified (e.g., pre/post, before/after, within X–Y, from A to B).

</Rating-Scale>

<Response-Format>
Rate the quality from 1 (very bad) to 5 (very good). Provide a short rationale that points to specific parts of the response demonstrating temporal specificity or vagueness.

Return your response in JSON format:
{
  "TemporalPrecision": {"rating": "", "rationale": ""}
}
</Response-Format>

<Example-Responses>

{EXAMPLE_RESPONSES}

</Example-Responses>

<Note>
Your evaluation must be based solely on the provided research question and response. Do not reward length by itself; reward specificity of temporal expressions and clarity of temporal sequencing when time is relevant. This rubric does not assess factual correctness, evidential grounding, or completeness.
</Note>"""

class TemporalPrecision(Rubric):
    name: str = "TemporalPrecision"
    system_prompt_template: str = temporal_precision_prompt

