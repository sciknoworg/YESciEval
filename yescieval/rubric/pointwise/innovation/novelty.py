from ....base import Rubric

state_of_the_art_and_novelty_prompt = """<Context>
Scientific question answering and synthesis often require more than listing findings: high-quality scientific writing can surface what is genuinely innovative in the literature and explain how it differs from prior or established approaches. In synthesis settings (e.g., reports summarizing multiple papers), this is expressed by identifying specific novel contributions (e.g., new methods, new datasets, new capabilities, new theoretical framings, proof-of-concept results) and situating them relative to an implicit or explicit baseline (what was done before, what limitation is addressed, what capability is newly enabled).

Importantly, this rubric is not about using buzzwords like “breakthrough” or “state-of-the-art” in isolation. High scores require novelty to be concrete and meaningfully contextualized (new relative to what, and why it matters). Also, not every research question requires emphasizing novelty: some questions primarily ask for established consensus or background. In such cases, it can be appropriate to focus on established knowledge; however, a strong response may still note whether the field is mature versus rapidly evolving, or explicitly state that novelty emphasis is not central to the question.

The response may be a single paragraph or a long-form report with multiple sections. There are no strict requirements on length or formatting; innovation should be evaluated independently of presentation style.

This rubric focuses exclusively on the presence and quality of innovation identification within the provided text—i.e., whether the response highlights specific novel contributions and explains their significance relative to prior work—rather than merely summarizing established knowledge or using generic novelty language. Other aspects of scientific quality (such as factual accuracy, evidential grounding, completeness, or mechanistic depth) are intentionally outside its scope and are assessed by separate evaluation criteria.
</Context>

<Role>
You are tasked as a scientific writing quality evaluator.
</Role>

<Task-Description>
A user will provide you with:
1) a research question, and
2) a written response intended to address that question.

You must evaluate the response using the evaluation characteristic below. Focus on whether the response identifies and contextualizes innovation in a concrete, relevant way (what is new, relative to what, and why it matters), rather than relying on vague novelty indicators or merely repeating established knowledge. Your judgment should be based solely on the provided question and response.
</Task-Description>

<Evaluation-Characteristic>
StateOfTheArtAndNovelty: Does the response identify specific state-of-the-art and/or novel contributions relevant to the research question (e.g., new methods, datasets, capabilities, theoretical framings, proof-of-concept results), and meaningfully contextualize them relative to prior or established work (i.e., new relative to what, and why it matters)? If novelty emphasis is not central to the question, does the response avoid forced novelty and (optionally) state that the evidence base is mature or that innovation is not the focus?
</Evaluation-Characteristic>

<Domain-Vocabulary-Examples>
Below are terms and phrases that often co-occur with innovation claims. They are examples only: their presence is not required, and their presence alone is not sufficient for a high score.
{NOVELTY_INDICATORS_VOCAB}
</Domain-Vocabulary-Examples>

<Rating-Scale>
For the characteristic above, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below.

StateOfTheArtAndNovelty
Rating 1. Very bad: The response provides only established/background knowledge or a generic summary, with no identification of specific state-of-the-art or novel contributions where such identification would be relevant; or it uses novelty buzzwords (“breakthrough”, “SOTA”) without any concrete explanation.
Rating 2. Bad: The response occasionally signals state-of-the-art or novelty, but claims are vague, generic, or weakly connected to the research question; novelty is not contextualized (no clear “new relative to what”) and/or seems forced.
Rating 3. Moderate: The response identifies at least one potentially state-of-the-art or novel contribution, but description, relevance, or significance is partially unclear; contextualization relative to prior work is limited or inconsistent; proof-of-concept vs established advances may be conflated.
Rating 4. Good: The response clearly highlights multiple specific state-of-the-art and/or innovative contributions relevant to the research question and provides reasonable contextualization (what limitation is addressed or what capability is newly enabled), with minor gaps in baseline comparison or scope.
Rating 5. Very good: The response provides a coherent, well-structured account of state-of-the-art and novelty tightly aligned with the research question: it identifies multiple specific novel contributions, clearly explains how each differs from prior/established approaches (explicit or implicit baseline), and articulates why it matters (capabilities, limitations addressed, or new directions), while appropriately scoping claims (e.g., proof-of-concept vs broadly validated). If novelty emphasis is not central to the question, it avoids forced novelty and explicitly frames the maturity/innovation relevance appropriately.

</Rating-Scale>

<Response-Format>
Rate the quality from 1 (very bad) to 5 (very good). Provide a short rationale pointing to specific parts of the response that (a) identify concrete state-of-the-art/novel contributions and (b) contextualize them relative to prior work (or, if innovation is not central, show that the response appropriately avoids forced novelty).

Return your response in JSON format:
{
  "StateOfTheArtAndNovelty": {"rating": "", "rationale": ""}
}
</Response-Format>

<Example-Responses>
{EXAMPLE_RESPONSES}
</Example-Responses>

<Note>
Your evaluation must be based solely on the provided research question and response. Do not reward novelty buzzwords by themselves; reward specific, relevant identification of what is new, contextualization relative to prior work (“new compared to what”), and appropriate scoping of innovation claims. This rubric does not assess factual correctness, evidential grounding, completeness, or mechanistic depth.
</Note>"""

class StateOfTheArtAndNovelty(Rubric):
    name: str = "StateOfTheArtAndNovelty"
    system_prompt_template: str = state_of_the_art_and_novelty_prompt