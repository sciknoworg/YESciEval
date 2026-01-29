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
    answer: str
    user_prompt_template: str = ("Evaluate and rate the quality of the following scientific synthesis "
                                 "according to the characteristics given in the system prompt.\n"
                                 "\n<scientific-synthesis>{answer}</scientific-synthesis>\n"
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
        return self.user_prompt_template.format(answer=self.answer,
                                                question=self.question,
                                                content=self.render_papers())

    def verbalize_system_prompt(self):
        system_prompt_template = self.system_prompt_template
        if self.domain:
            if self.vocabulary:
                system_prompt_template = self.vocabulary.format_prompt(prompt=system_prompt_template, domain=self.domain)
            if self.example:
                system_prompt_template = self.example.format_prompt(prompt=system_prompt_template,
                                                                      domain=self.domain,
                                                                      rubric_id=self.name)
        return system_prompt_template

    def instruct(self) -> List[Dict[str, str]]:
        message = [
            {"role": "system", "content":  self.verbalize_system_prompt()},
            {"role": "user", "content": self.verbalize_user_prompt()},
        ]
        return message

