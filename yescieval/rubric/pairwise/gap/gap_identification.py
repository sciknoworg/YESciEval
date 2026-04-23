from ....base import PairwiseRubric

gap_identification_pairwise_prompt = """<Context>
Scientific question answering and synthesis often require more than listing findings: high-quality scientific writing identifies what remains unknown, insufficiently addressed, or unresolved in existing research. This is commonly expressed through gap identification, where the text specifies limitations, missing knowledge, unresolved inconsistencies, or missing connections in prior work and explains why they matter for the research question.

Gap identification can refer to (a) field-level gaps across the literature (e.g., missing populations/settings, inconsistent measures, lack of comparative studies, limited external validity), and/or (b) recurring study-level limitations that materially constrain conclusions when framed as evidence-base limitations. High-quality gap statements are specific and scoped (what is missing, where, and why), rather than generic (“more research is needed”). If gap emphasis is not central to the user's question, it should not be forced; however, when included, it should remain relevant and well-defined.

The responses may be short paragraphs or long-form reports. Gap identification should be evaluated independently of presentation style or length.

This rubric focuses exclusively on the presence and quality of gap identification within the provided text of two responses that are compared, emphasizing explicit and relevant statements of limitations, unanswered questions, or missing connections in prior work rather than summaries of what is already known. Other aspects of scientific quality (such as factual accuracy, evidential grounding, completeness, or innovation) are intentionally outside its scope and are assessed by separate evaluation criteria.
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
- Note that it is possible for both responses to receive the same rating, if they are equally comparably clear with systematic gap identification and provide complementary or identical insights.

Your judgment must be based solely on the provided question and comparing the two responses w.r.t. addressing the question and w.r.t. each other.
</Task-Description>

<Evaluation-Characteristic>
GapIdentification: Does the response identify gaps relevant to the research question by specifying limitations, missing knowledge, unresolved issues, or missing connections in prior work (preferably at the evidence-base/field level), rather than only describing existing findings?
</Evaluation-Characteristic>

<Domain-Vocabulary-Examples>
Below are terms and phrases that often signal gap identification. They are examples only: their presence is not required, and their presence alone is not sufficient for a high score.
{GAP_IDENTIFICATION_VOCAB}
</Domain-Vocabulary-Examples>

<Rating-Scale>
For the characteristic above, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below.

GapIdentification
Rating 1. Very bad: The response is purely descriptive, summarizing existing findings or observations with no identification of missing, unknown, inconsistent, or unresolved aspects relevant to the research question.
Rating 2. Bad: The response refers to gaps only in a vague or generic manner (e.g., “more research is needed”) without clearly specifying what is missing or unresolved in the context of the research question.
Rating 3. Moderate: The response identifies one or more potential gaps with partial clarity, but the nature, scope, location (where in the literature), or relevance of the gaps is incomplete, unclear, or inconsistently articulated.
Rating 4. Good: The response clearly identifies specific gaps or limitations in the evidence base that are relevant to the research question (e.g., missing comparisons, populations, settings, measures, time horizons, or conflicting results) and provides some explanation of why they matter; minor ambiguity or imprecision may remain.
Rating 5. Very good: The response explicitly and clearly identifies well-defined gaps or unanswered questions, specifying what is missing, where it occurs in the evidence base (or across studies), and why it matters for the research question, without relying on vague statements. Gap statements are appropriately scoped (avoiding absolute claims like “no research exists” unless clearly justified within the response).
</Rating-Scale>

<Response-Format>
Return your evaluation strictly in JSON format:

{
  "GapIdentification": {
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
Your evaluation must be based solely on the provided research question and responses. Do not reward keyword mentions alone. Reward distinct, clearly described gaps in existing knowledge that are relevant to the research question and appropriately scoped. This rubric does not assess factual correctness, evidential grounding, completeness, or innovation.
</Note>
"""

class GapIdentification(PairwiseRubric):
    name: str = "GapIdentification"
    system_prompt_template: str = gap_identification_pairwise_prompt