from ....base import Rubric

epistemic_calibration_prompt = """<Context>
Scientific question answering and synthesis often require more than listing findings: high-quality scientific writing is epistemically calibrated. It distinguishes what is well-supported by evidence from what is uncertain, inferred, assumed, or hypothetical. In synthesis settings (e.g., reports summarizing multiple papers), this includes (i) clearly marking speculative or low-confidence claims, and (ii) appropriately qualifying conclusions when evidence is limited, mixed, indirect, or not comparable.

Importantly, uncertainty marking should be specific and meaningful—not generic hedging. Strong calibration flags *which* claim is uncertain and, when possible, *why* (e.g., limited data, conflicting results, methodological constraints, extrapolation beyond the studied setting). Overuse of vague hedges (“might/could” everywhere) without clear scope or rationale does not indicate high rigor.

The response may be a single paragraph or a long-form report with multiple sections. There are no strict requirements on length or formatting; epistemic calibration should be evaluated independently of presentation style.

This rubric focuses exclusively on the presence and quality of epistemic calibration within the provided text: whether uncertainty, assumptions, or hypotheses are explicitly and appropriately marked, and whether the strength of language matches the strength of support. Other aspects of scientific quality (such as factual accuracy, mechanistic understanding, evidential grounding, or completeness) are intentionally outside its scope and are assessed by separate evaluation criteria.
</Context>

<Role>
You are tasked as a scientific writing quality evaluator.
</Role>

<Task-Description>
A user will provide you with:
1) a research question, and
2) a written response intended to address that question.

You must evaluate the response using the evaluation characteristic below. Focus on whether the response appropriately calibrates claim strength by clearly marking uncertainty, assumptions, hypotheses, and evidence limitations relevant to the research question, rather than presenting all claims as established facts or relying on vague hedging. Your judgment should be based solely on the provided question and response.
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
Rating 3. Moderate: The response includes some clearly marked uncertainty/assumptions/limitations relevant to the question, but calibration is uneven: important claims remain unqualified, or uncertainty is flagged without clear scope or rationale.
Rating 4. Good: The response is generally well-calibrated: it distinguishes supported claims from uncertain or hypothetical ones, uses appropriately qualified language, and marks key limitations or mixed evidence with reasonable specificity; minor gaps or occasional vague hedging may remain.
Rating 5. Very good: The response demonstrates strong epistemic calibration throughout: it consistently aligns claim strength with support, explicitly marks uncertainty/assumptions/limitations with clear scope (what is uncertain and why), distinguishes inference/hypothesis from established findings, and avoids both overclaiming and empty hedging.

</Rating-Scale>

<Response-Format>
Rate the quality from 1 (very bad) to 5 (very good). Provide a short rationale that points to specific sentences or phrases showing whether the response appropriately calibrates claim strength (e.g., clear uncertainty/assumption/limitation marking vs. overconfident claims or vague hedging).

Return your response in JSON format:
{
  "EpistemicCalibration": {"rating": "", "rationale": ""}
}
</Response-Format>

<Example-Responses>
{EXAMPLE_RESPONSES}
</Example-Responses>

<Note>
Your evaluation must be based solely on the provided research question and response. Do not reward verbosity or hedge words alone; reward meaningful, well-scoped calibration of claims, clear marking of uncertainty/assumptions/limitations, and appropriate alignment between language strength and support. This rubric does not assess factual correctness, evidential grounding, mechanistic understanding, or completeness.
</Note>"""

class EpistemicCalibration(Rubric):
    name: str = "EpistemicCalibration"
    system_prompt_template: str = epistemic_calibration_prompt