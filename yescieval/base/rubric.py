from abc import ABC
from pydantic import BaseModel
from typing import Dict, List, Optional
from .vocab import VocabLoader
from .example import ExampleLoader

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
    vocab_manager: Optional[VocabLoader] = None
    example_manager: Optional[ExampleLoader] = None
    model_config = {"arbitrary_types_allowed": True}


    def render_papers(self) -> str:
        paper_content = ""
        for idx, (title, abstract) in enumerate(self.papers.items()):
            paper_content += f"{idx + 1}. {title}\n\n{abstract}\n\n"
        return paper_content

    def preprocess_user_prompt(self, template: str) -> str:
        """
        Fills vocabulary and example placeholders in the system prompt.
        """
        filled = template

        if self.vocab_manager and self.domain:
            filled = self.vocab_manager.fill_prompt(filled, self.domain)
            
        if self.example_manager and self.domain:
            
            filled = self.example_manager.fill_prompt(
                template=filled, 
                domain=self.domain, 
                rubric_name=self.name
            )
            
        return filled

    def verbalize(self) -> str:
        """
        Fill placeholders first, then format with answer, question, and papers.
        """
        filled_template = self.preprocess_user_prompt(self.user_prompt_template)
        return filled_template.format(
            answer=self.answer,
            question=self.question,
            content=self.render_papers()
        )

    def instruct(self) -> List[Dict[str, str]]:
        return [
            {"role": "system", "content": self.system_prompt_template},
            {"role": "user", "content": self.verbalize()},
        ]
