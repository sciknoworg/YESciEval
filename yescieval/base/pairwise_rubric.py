from abc import ABC
from .rubric import Rubric


class PairwiseRubric(Rubric, ABC):
    """
    Base class for pairwise (two-answer comparison) evaluation rubrics.
    Evaluates two answers (A and B) against a research question and set of papers.
    """
    eval_type: str = "pairwise"
    example_answer_b: str

    def verbalize_user_prompt(self) -> str:
        example_answer_b_block = f"<scientific-synthesis-B>{self.example_answer_b}</scientific-synthesis-B>\n\n"
        return self.user_prompt_template.format(
            example_answer_a=self.example_answer_a,
            answer_tag="scientific-synthesis-A",
            example_answer_b_block=example_answer_b_block,
            question=self.question,
            content=self.render_papers(),
        )