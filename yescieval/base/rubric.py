from abc import ABC
from pydantic import BaseModel
from typing import Dict, List, Optional
from ..injector import ExampleInjector, VocabularyInjector

class Rubric(BaseModel, ABC):
    """
    Abstract base class for evaluation rubrics.
    Subclasses must implement `verbalize`.
    """
    system_prompt_template: str
    name: str = "Rubric"
    papers: Dict[str, str]
    question: str
    example_answer_a: str
    user_prompt_template: str = ("Evaluate and rate the quality of the following scientific synthesis "
                                 "according to the characteristics given in the system prompt.\n"
                                 "\n<{answer_tag}>{example_answer_a}</{answer_tag}>\n"
                                 "{example_answer_b_block}"
                                 "\n<research-question>{question}</research-question>\n"
                                 "\n<paper-titles-and-abstracts>\n{content}</paper-titles-and-abstracts>\n\n###")

    domain: Optional[str] = None
    vocabulary: Optional[VocabularyInjector] = None
    example: Optional[ExampleInjector] = None

    model_config = {"arbitrary_types_allowed": True} # Not used in the class but unable to generate
                                                     # pydantic-core schema for vocab and example injectors

    def render_papers(self) -> str:
        paper_content = ""
        for idx, (title, abstract) in enumerate(self.papers.items()):
            paper_content += f"{idx + 1}. {title}\n\n{abstract}\n\n"
        return paper_content

    def verbalize_user_prompt(self):
        raise NotImplementedError

    def verbalize_system_prompt(self):
        system_prompt_template = self.system_prompt_template
        if self.domain:
            if self.vocabulary:
                system_prompt_template = self.vocabulary.format_prompt(prompt=system_prompt_template, domain=self.domain)
            if self.example:
                system_prompt_template = self.example.format_prompt(prompt=system_prompt_template,
                                                                      domain=self.domain,
                                                                      rubric_id=self.name,
                                                                      eval_type=self.eval_type)
        return system_prompt_template

    def instruct(self) -> List[Dict[str, str]]:
        message = [
            {"role": "system", "content":  self.verbalize_system_prompt()},
            {"role": "user", "content": self.verbalize_user_prompt()},
        ]
        return message


class PointwiseRubric(Rubric):
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
 
 
class PairwiseRubric(Rubric):
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
 