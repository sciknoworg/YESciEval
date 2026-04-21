from ....base import PairwiseRubric

epistemic_calibration_pairwise_prompt = """<Context>
Scientific question answering and synthesis often require more than listing findings: high-quality scientific writing is epistemically calibrated. It distinguishes what is well-supported by evidence from what is uncertain, inferred, assumed, or hypothetical. In synthesis settings, this includes clearly marking speculative or low-confidence claims and appropriately qualifying conclusions when evidence is limited, mixed, indirect, or not comparable.

Importantly, Uncertainty marking should be specific and meaningful—not generic hedging. Strong calibration flags, which claim is uncertain and, when possible, why (e.g., limited data, conflicting results, methodological constraints, extrapolation beyond the studied setting). Overuse of vague hedges (“might/could”) without a clear scope does not indicate high rigor.

The responses may be short paragraphs or long-form reports. Epistemic calibration should be evaluated independently of presentation style or length.

This rubric focuses exclusively on the presence and quality of epistemic calibration within the provided text of two responses that are compared, whether uncertainty, assumptions, or hypotheses are explicitly and appropriately marked, and whether the strength of language matches the strength of support. Other aspects of scientific quality (such as factual accuracy, mechanistic understanding, evidential grounding, or completeness) are intentionally outside its scope and are assessed by separate evaluation criteria.
</Context>

<Role>
You are tasked as a scientific writing quality evaluator performing a pairwise comparison between two texts.
</Role>

<Task-Description>
A user will provide:
1) a research question, and
2) Two written responses (Response A and Response B) intended to address that question.

Your task is to:
- First, independently evaluate each response using the evaluation characteristic below.
- Then perform a pairwise comparison of the two responses using the evaluation characteristic below.
- Then grade each response with a comparative rating from 1 (very bad) to 5 (very good) compared to the other response and a subsequent rationale for each comparative response rating.
- Note that it is possible for both responses to receive the same rating, if they are equally comparably clear with meaningful epistemic calibration and provide complementary or identical insights.

Your judgment must be based solely on the provided question and comparing the two responses w.r.t. addressing the question and w.r.t. each other.
</Task-Description>

<Evaluation-Characteristic>
EpistemicCalibration: Does the response appropriately calibrate claim strength by clearly distinguishing well-supported claims from uncertain, inferred, assumed, or hypothetical content, and by explicitly and meaningfully marking uncertainty/limitations where relevant to the research question?
</Evaluation-Characteristic>

<Domain-Vocabulary-Examples>
Below are terms and phrases that often signal epistemic calibration. They are examples only: their presence is not required, and their presence alone is not sufficient for a high score.
{EPISTEMIC_CALIBRATION_VOCAB}
</Domain-Vocabulary-Examples>

<Rating-Scale>
For the characteristic above, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below.

EpistemicCalibration
Rating 1. Very bad: The response presents claims as definitive throughout, with no meaningful qualification, uncertainty marking, or acknowledgment of assumptions/limitations, even when such caution is warranted.
Rating 2. Bad: The response occasionally signals uncertainty or speculation, but markings are vague (generic “might/could”), inconsistently applied, or poorly scoped; claim strength often does not match the level of support.
Rating 3. Moderate: The response includes some clearly marked uncertainty/assumptions/limitations relevant to the question, but calibration is uneven: important claims remain unqualified, or uncertainty is flagged without a clear scope or rationale.
Rating 4. Good: The response is generally well-calibrated: it distinguishes supported claims from uncertain or hypothetical ones, uses appropriately qualified language, and marks key limitations or mixed evidence with reasonable specificity; minor gaps or occasional vague hedging may remain.
Rating 5. Very good: The response demonstrates strong epistemic calibration throughout: it consistently aligns claim strength with support, explicitly marks uncertainty/assumptions/limitations with clear scope (what is uncertain and why), distinguishes inference/hypothesis from established findings, and avoids both overclaiming and empty hedging.
</Rating-Scale>

<Response-Format>
Return your evaluation strictly in JSON format:

{
  "EpistemicCalibration": {
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
Your evaluation must be based solely on the provided research question and responses. Do not reward verbosity or hedge words alone; reward meaningful, well-scoped calibration of claims, clear marking of uncertainty/assumptions/limitations, and appropriate alignment between language strength and support. This rubric does not assess factual correctness, evidential grounding, mechanistic understanding, or completeness.
</Note>
"""

class EpistemicCalibration(PairwiseRubric):
    name: str = "EpistemicCalibration"
    system_prompt_template: str = epistemic_calibration_pairwise_prompt