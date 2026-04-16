from abc import ABC
from .rubric import Rubric
 
 
class PointwiseRubric(Rubric, ABC):
    """
    Base class for pointwise (single-answer) evaluation rubrics.
    Evaluates a single answer against a research question and set of papers.
    """
    eval_type: str = "pointwise"
 
    def verbalize_user_prompt(self) -> str:
        return self.user_prompt_template.format(
            example_answer_a=self.example_answer_a,
            answer_tag="scientific-synthesis",
            example_answer_b_block="",
            question=self.question,
            content=self.render_papers(),
        )
 