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
    user_prompt_template: str

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
    answer: str
    user_prompt_template: str = ("Evaluate and rate the quality of the following scientific synthesis "
                                 "according to the characteristics given in the system prompt.\n"
                                 "\n<scientific-synthesis>\n{answer}\n</scientific-synthesis>\n"
                                 "\n<research-question>\n{question}\n</research-question>\n"
                                 "\n<paper-titles-and-abstracts>\n{content}\n</paper-titles-and-abstracts>\n\n###")

    def verbalize_user_prompt(self) -> str:
        return self.user_prompt_template.format(
            question=self.question,
            answer=self.answer,
            content=self.render_papers(),
        )
 
 
class PairwiseRubric(Rubric):
    """
    Base class for pairwise (two-answer comparison) evaluation rubrics.
    Evaluates two answers (A and B) against a research question and set of papers.
    """
    eval_type: str = "pairwise"
    answer_a: str
    answer_b: str
    user_prompt_template: str = ("Evaluate and rate the quality of the following scientific synthesis "
                                 "according to the characteristics given in the system prompt.\n"
                                 "\n<scientific-synthesis-A>\n{answer_a}\n</scientific-synthesis-A>\n"
                                 "\n<scientific-synthesis-B>\n{answer_b}\n</scientific-synthesis-B>\n"
                                 "\n<research-question>\n{question}\n</research-question>\n"
                                 "\n<paper-titles-and-abstracts>\n{content}\n</paper-titles-and-abstracts>\n\n###")
 
    def verbalize_user_prompt(self) -> str:
        return self.user_prompt_template.format(
            question=self.question,
            answer_a=self.answer_a,
            answer_b=self.answer_b,
            content=self.render_papers(),
        )
 