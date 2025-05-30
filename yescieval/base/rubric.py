from abc import ABC
from pydantic import BaseModel
from typing import Dict, List



class Rubric(BaseModel, ABC):
    """
    Abstract base class for evaluation rubrics.
    Subclasses must implement `verbalize`.
    """
    system_prompt_template: str
    papers: Dict[str, str]
    question: str
    answer: str
    user_prompt_template: str = ("Evaluate and rate the quality of the following scientific synthesis "
                             "according to the characteristics given in the system prompt.\n"
                             "\n<scientific-synthesis>{answer}</scientific-synthesis>\n"
                             "\n<research-question>{question}</research-question>\n"
                             "\n<paper-titles-and-abstracts>\n{content}</paper-titles-and-abstracts>\n\n###")

    def render_papers(self) -> str:
        paper_content = ""
        for idx, (title, abstract) in enumerate(self.papers.items()):
            paper_content += f"{idx + 1}. " + title + "\n\n" + abstract + "\n\n"
        return paper_content

    def verbalize(self):
        return self.user_prompt_template.format(answer=self.answer,
                                                question=self.question,
                                                content=self.render_papers())

    def instruct(self) -> List[Dict[str, str]]:
        message = [
            {"role": "system", "content":  self.system_prompt_template},
            {"role": "user", "content": self.verbalize()},
        ]
        return message

