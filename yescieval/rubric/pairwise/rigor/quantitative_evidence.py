from ....base import PairwiseRubric

quantitative_evidence_and_uncertainty_pairwise_prompt = """<Context>
Scientific question answering and synthesis often require rigorous reasoning using quantitative evidence and appropriate treatment of uncertainty. In synthesis settings (e.g., reports that summarize multiple papers), this is commonly expressed through careful use and interpretation of source-reported quantitative results (e.g., effect sizes, confidence intervals, variability measures), and through explicit reasoning about robustness, heterogeneity, and limitations of the evidence base.

Importantly, not every research question requires (or supports) statistical detail. Some questions are conceptual, mechanistic, methodological, or qualitative. In such cases, it can be rigorous to explicitly state that quantitative estimates are unavailable, incomparable, or not applicable—and to explain why (e.g., heterogeneous outcomes, qualitative designs, sparse or indirect data).

The responses may be short paragraphs or long-form reports. Quantitative evidence handling and uncertainty reasoning should be evaluated independently of presentation style or length.

This rubric focuses exclusively on the presence and quality of quantitative reasoning and uncertainty handling in the two responses being compared,  emphasizing appropriate use, interpretation, and limitation-aware reasoning rather than mere mention of statistical terms or ungrounded numerical claims. Other aspects of scientific quality (such as mechanistic understanding, factual accuracy, evidential grounding, or completeness) are intentionally outside its scope and are assessed by separate evaluation criteria.
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
- Note that it is possible for both responses to receive the same rating, if they are equally comparably clear with consistent quantitative reasoning and uncertainty handling and provide complementary or identical insights.

Your judgment must be based solely on the provided question and comparing the two responses w.r.t. addressing the question and w.r.t. each other.
</Task-Description>

<Evaluation-Characteristic>
QuantitativeEvidenceAndUncertainty: Does the response appropriately use and interpret quantitative evidence and uncertainty (e.g., effect sizes, confidence intervals, variability, robustness, heterogeneity) in a way that is relevant to the research question? If such quantitative treatment is not needed or not supported by the evidence base, does the response explicitly and reasonably justify why?
</Evaluation-Characteristic>

<Domain-Vocabulary-Examples>
Below are domain-specific terms and phrases that often signal quantitative evidence handling and uncertainty reasoning. These are examples only: their presence is not required, and their presence alone is not sufficient for a high score.
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
Return your evaluation strictly in JSON format:

{
  "QuantitativeEvidenceAndUncertainty": {
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
Your evaluation must be based solely on the provided research question and responses. Do not reward verbosity or statistical jargon by itself; reward relevant quantitative interpretation, uncertainty/robustness awareness, appropriate caveats, and clarity in connecting quantitative evidence to conclusions. This rubric does not assess mechanistic understanding, factual correctness, evidential grounding, or completeness.
</Note>
"""

class QuantitativeEvidenceAndUncertainty(PairwiseRubric):
    name: str = "QuantitativeEvidenceAndUncertainty"
    system_prompt_template: str = quantitative_evidence_and_uncertainty_pairwise_prompt