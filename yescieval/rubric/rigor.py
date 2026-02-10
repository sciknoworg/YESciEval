from ..base import Rubric

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

<Evaluation-Characteristics>
EpistemicCalibration: Does the response appropriately calibrate claim strength by clearly distinguishing well-supported claims from uncertain, inferred, assumed, or hypothetical content, and by explicitly and meaningfully marking uncertainty/limitations where relevant to the research question?
</Evaluation-Characteristics>

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

from ..base import Rubric

quantitative_evidence_and_uncertainty_prompt = """<Context>
Scientific question answering and synthesis often require more than listing findings: high-quality scientific writing demonstrates rigorous reasoning using quantitative evidence and an appropriate treatment of uncertainty. In synthesis settings (e.g., reports that summarize multiple papers), this is commonly expressed through careful use and interpretation of source-reported quantitative results (e.g., effect sizes, confidence intervals, variability measures), and through explicit reasoning about robustness, heterogeneity, and limitations of the evidence base.

Importantly, not every research question or evidence base requires (or supports) statistical detail. Some questions are primarily conceptual, mechanistic, methodological, or qualitative; in such cases, it can be rigorous to state that quantitative estimates are unavailable, incomparable, or not applicable—and to explain why (e.g., heterogeneous outcomes/metrics, qualitative designs, sparse data).

The response may be a single paragraph or a long-form report with multiple sections. There are no strict requirements on length or formatting; quantitative evidence and uncertainty handling should be evaluated independently of presentation style.

This rubric focuses exclusively on the presence and quality of quantitative evidence handling and uncertainty reasoning within the provided text, emphasizing appropriate use, interpretation, and limitation-aware reasoning rather than mere mention of statistical terms or ungrounded numerical claims. Other aspects of scientific quality (such as mechanistic understanding, factual accuracy, evidential grounding, or completeness) are intentionally outside its scope and are assessed by separate evaluation criteria.
</Context>

<Role>
You are tasked as a scientific writing quality evaluator.
</Role>

<Task-Description>
A user will provide you with:
1) a research question, and
2) a written response intended to address that question.

You must evaluate the response using the evaluation characteristic below. Focus on whether the response demonstrates rigorous quantitative reasoning and uncertainty awareness appropriate to the research question and the type of synthesis, rather than merely reporting outcomes or sprinkling statistical jargon. Your judgment should be based solely on the provided question and response.
</Task-Description>

<Evaluation-Characteristics>
QuantitativeEvidenceAndUncertainty: Does the response appropriately use and interpret quantitative evidence and uncertainty (e.g., effect sizes, confidence intervals, variability, robustness, heterogeneity) in a way that is relevant to the research question? If such quantitative treatment is not needed or not supported by the evidence base, does the response explicitly and reasonably justify why?
</Evaluation-Characteristics>

<Domain-Vocabulary-Examples>
Below are domain-specific terms and phrases that often signal quantitative evidence handling and uncertainty reasoning. They are examples only: their presence is not required, and their presence alone is not sufficient for a high score.
{QUANT_UNCERTAINTY_VOCAB}
</Domain-Vocabulary-Examples>

<Rating-Scale>
For the characteristic above, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below.

QuantitativeEvidenceAndUncertainty
Rating 1. Very bad: The response is purely descriptive, reporting claims or outcomes with no meaningful quantitative evidence use or uncertainty reasoning, even when the question clearly calls for it; or it makes unqualified quantitative-sounding claims without interpretation.
Rating 2. Bad: The response contains occasional quantitative/statistical terms or numbers, but interpretation is superficial, generic, misapplied, or weakly connected to the research question; uncertainty/robustness is largely ignored when relevant.
Rating 3. Moderate: The response demonstrates some relevant quantitative reasoning and/or acknowledges uncertainty, but key interpretations, caveats (e.g., variability, assumptions, comparability), or cross-study considerations (e.g., heterogeneity) are missing, unclear, or inconsistently applied. If quantitative treatment is not needed, the response may gesture at this but without a clear justification.
Rating 4. Good: The response uses and interprets quantitative evidence appropriately where relevant and connects it to the research question; it discusses uncertainty/robustness with reasonable clarity (e.g., variability, confidence, limitations, heterogeneity) and avoids overclaiming. If quantitative treatment is not needed or not supported, it states this clearly and provides a reasonable explanation.
Rating 5. Very good: The response demonstrates strong quantitative rigor and uncertainty awareness tightly aligned with the research question, correctly interpreting multiple relevant quantitative indicators (e.g., effect magnitude and uncertainty), explicitly addressing key assumptions/limitations and cross-study heterogeneity/robustness where applicable, and clearly distinguishing what is supported by quantitative evidence from what is not. If quantitative treatment is not needed or not supported, it provides a precise, well-reasoned justification and adjusts conclusions accordingly.

</Rating-Scale>

<Response-Format>
Rate the quality from 1 (very bad) to 5 (very good). Provide a short rationale that points to specific parts of the response demonstrating appropriate (or inappropriate/absent) use and interpretation of quantitative evidence and uncertainty, or a clear justification for why such treatment is not needed or not supported.

Return your response in JSON format:
{
  "QuantitativeEvidenceAndUncertainty": {"rating": "", "rationale": ""}
}
</Response-Format>

<Example-Responses>
{EXAMPLE_RESPONSES}
</Example-Responses>

<Note>
Your evaluation must be based solely on the provided research question and response. Do not reward verbosity or statistical jargon by itself; reward relevant quantitative interpretation, uncertainty/robustness awareness, appropriate caveats, and clarity in connecting quantitative evidence to conclusions. This rubric does not assess mechanistic understanding, factual correctness, evidential grounding, or completeness.
</Note>"""

class QuantitativeEvidenceAndUncertainty(Rubric):
    name: str = "QuantitativeEvidenceAndUncertainty"
    system_prompt_template: str = quantitative_evidence_and_uncertainty_prompt

explicit_uncertainty_prompt =  """<Context>
Scientific question answering and synthesis often require more than listing findings: high-quality scientific writing communicates to the reader when conclusions or underlying knowledge remain uncertain, unclear, or unknown.

The response may be a single paragraph or a long-form report with multiple sections. There are no strict requirements on length or formatting; explicit uncertainty should be evaluated independently of presentation style.

This rubric focuses exclusively on whether the provided text explicitly identifies knowledge as uncertain, unclear, or unknown, rather than treating all statements as resolved. Other aspects of scientific quality (such as factual completeness, causal reasoning, or relevancy) are intentionally outside its scope and are assessed by separate evaluation criteria.
</Context>

<Role>
You are tasked as a scientific writing quality evaluator.
</Role>

<Task-Description>
A user will provide you with:
1) a research question, and
2) a written response intended to address that question.

You must evaluate the response using the evaluation characteristic below. Focus on the explicit indication of uncertainty, unclear points, or unknown aspects, rather than on fully resolved statements. Your judgment should be based solely on the provided question and response.
</Task-Description>

<Evaluation-Characteristics>
ExplicitUncertainty: Does the response clearly indicate what is uncertain, unclear, or unknown in relation to the research question, rather than presenting all findings as settled or certain?
</Evaluation-Characteristics>

<Domain-Vocabulary-Examples>
Below are domain-specific terms and phrases that often signal uncertainty discussion. They are examples only: their presence is not required, and their presence alone is not sufficient for a high score.
{UNCERTAINTY_VOCAB}
</Domain-Vocabulary-Examples>

<Rating-Scale>
For the characteristic above, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below.

Rating 1. Very bad: The response provides no indication of uncertainty, all statements are presented as settled, with no acknowledgment of what is uncertain, unclear, or unknown.
Rating 2. Bad: The response occasionally signals uncertainty, but markers of what is uncertain, unclear, or unknown are vague, or weakly connected to the research question.
Rating 3. Moderate: The response identifies some aspects that are uncertain, unclear, or unknown, but important elements are missing, inconsistently marked, or only partially explained.
Rating 4. Good: The response clearly signals multiple uncertainties, unclear points, or unknown aspects relevant to the research question, minor gaps or imprecision in the explicit marking may remain.
Rating 5. Very good: The response provides a detailed, coherent account of what is uncertain, unclear, or unknown, explicitly and consistently marking multiple aspects of unresolved knowledge and clearly distinguishing these from statements presented as certain or settled.
</Rating-Scale>

<Response-Format>
Rate the quality from 1 (very bad) to 5 (very good). Provide a short rationale that points to specific parts of the response demonstrating the presence or absence of uncertainty relevant to the research question.

Return your response in JSON format:
{
  "ExplicitUncertainty": {"rating": "", "rationale": ""}
}
</Response-Format>

<Example-Responses>
{EXAMPLE_RESPONSES}
</Example-Responses>

<Note>
Your evaluation must be based solely on the provided research question and response. Do not reward length by itself; reward clear and relevant identification of what is uncertain, unclear, or unknown. This rubric does not assess factual completeness, causal reasoning, or relevancy.
</Note>"""

class ExplicitUncertainty(Rubric):
    name: str = "Explicit Uncertainty"
    system_prompt_template: str = explicit_uncertainty_prompt

