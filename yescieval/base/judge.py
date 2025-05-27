from abc import ABC
from typing import Dict
from . import Parser, Rubric


class Judge(ABC):
    def from_pretrained(self, model_id:str, device: str="auto"):
        pass

    def judge(self, rubric: Rubric, parser: Parser = Parser) -> Dict[str, Dict[str, str]]:
        pass
