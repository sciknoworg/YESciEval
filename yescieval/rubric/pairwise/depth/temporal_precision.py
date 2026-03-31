from ....base import Rubric

temporal_precision_pairwise_prompt = """<Context>
Scientific question answering and synthesis often require more than listing findings: high-quality scientific writing is precise about time when time matters. Temporal precision refers to how clearly the text specifies when something occurs, over what duration, or across what interval. Precise temporal expressions include calendar dates, numeric durations, bounded year ranges, or clearly delimited intervals; vague temporal markers include expressions like “historically”, “recently”, “long-term”, or “soon” without further specification.

The responses may be short paragraphs or long-form reports. Temporal precision should be evaluated independently of presentation style or length.

This rubric focuses exclusively on the presence and quality of temporal precision within the provided text of two responses that are compared, emphasizing specific and bounded time expressions (when/for how long/over what interval) rather than vague temporal language. Other aspects of scientific quality (such as factual accuracy, evidential grounding, or completeness) are intentionally outside its scope.
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
- Note that it is possible for both responses to receive the same rating, if they are equally comparably clear with reasonable temporal precision and provide complementary or identical insights.

Your judgment must be based solely on the provided question and comparing the two responses w.r.t. addressing the question and w.r.t. each other.
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
Return your evaluation strictly in JSON format:

{
  "TemporalPrecision": {
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
Your evaluation must be based solely on the provided research question and responses. Do not reward length by itself; reward specificity of temporal expressions and clarity of temporal sequencing when time is relevant. This rubric does not assess factual correctness, evidential grounding, or completeness.
</Note>
"""

class TemporalPrecision(Rubric):
    name: str = "TemporalPrecision"
    system_prompt_template: str = temporal_precision_pairwise_prompt