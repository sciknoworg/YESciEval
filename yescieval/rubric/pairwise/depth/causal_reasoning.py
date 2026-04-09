from ....base import Rubric

causal_reasoning_pairwise_prompt = """<Context>
Scientific question answering and synthesis often require more than listing findings: high-quality scientific writing explains not only what is believed to be true, but also why it may be true. One important aspect of this is causal reasoning, where the text articulates cause-effect relationships, conditions, mediators, moderators, and causal chains, rather than only describing associations or co-occurrences.

The responses may be short paragraphs or long-form reports. Causal reasoning should be evaluated independently of presentation style or length.

This rubric focuses exclusively on the presence and quality of causal reasoning within the provided text of two responses that are compared, emphasizing language and structure that express why something happens (cause → effect) rather than only what is observed or correlated. Other aspects of scientific quality (such as factual accuracy, evidential grounding, or completeness) are intentionally outside its scope.
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
- Note that it is possible for both responses to receive the same rating, if they are equally comparably clear with comprehensible causal reasoning and provide complementary or identical insights.

Your judgment must be based solely on the provided question and comparing the two responses w.r.t. addressing the question and w.r.t. each other.
</Task-Description>

<Evaluation-Characteristic>
CausalReasoning: Does the response demonstrate causal reasoning relevant to the research question by explicitly articulating cause-effect relationships (including causal chains, mediators, moderators, or conditional causal statements), rather than only reporting associations, trends, or co-occurrences?
</Evaluation-Characteristic>

<Domain-Vocabulary-Examples>
Below are examples of causal connectives and expressions that often signal causal reasoning (across domains). They are examples only: their presence is not required, and their presence alone is not sufficient for a high score.
{CAUSAL_VOCAB}
</Domain-Vocabulary-Examples>

<Rating-Scale>
For the characteristic above, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below.

CausalReasoning
Rating 1. Very bad: The response is purely descriptive or correlational, offering no meaningful cause-effect statements relevant to the research question.
Rating 2. Bad: The response uses occasional causal words (e.g., “leads to”, “because”) but causal links are unclear, generic, or asserted without coherent cause-effect structure (often indistinguishable from correlation).
Rating 3. Moderate: The response includes some clear causal claims relevant to the question, but they are limited in number, shallow (single-step), inconsistently developed, or mixed with ambiguous association language.
Rating 4. Good: The response provides clear cause-effect reasoning with multiple relevant causal links and some structure (e.g., conditions, mediators/moderators, or short causal chains); minor ambiguity or gaps may remain.
Rating 5. Very good: The response demonstrates strong causal reasoning throughout, using explicit and coherent cause-effect structure aligned to the research question, including multiple well-articulated causal chains and/or conditional pathways (e.g., A → B → C; “A affects C via B”; “A increases B only under condition D”), and clearly distinguishes causation from association.

</Rating-Scale>

<Response-Format>
Return your evaluation strictly in JSON format:

{
  "CausalReasoning": {
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
Your evaluation must be based solely on the provided research question and responses. Do not reward length by itself; reward clarity and coherence of causal structure, relevance to the question, and explicit differentiation between causation and association. This rubric does not assess factual correctness, evidential grounding, or completeness.
</Note>
"""

class CausalReasoning(Rubric):
    name: str = "CausalReasoning"
    eval_type: str = "pairwise"
    system_prompt_template: str = causal_reasoning_pairwise_prompt
    