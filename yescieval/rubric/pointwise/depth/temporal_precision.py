from ....base import PointwiseRubric

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

<Evaluation-Characteristic>
TemporalPrecision: Does the response use specific, bounded, and meaningful temporal expressions (e.g., dates, durations, intervals, year ranges) when discussing time-relevant aspects of the research question, rather than vague temporal markers?
</Evaluation-Characteristic>

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

class TemporalPrecision(PointwiseRubric):
    name: str = "TemporalPrecision"
    system_prompt_template: str = temporal_precision_prompt