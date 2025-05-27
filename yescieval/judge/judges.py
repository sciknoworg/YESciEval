from ..base import Judge, Parser, Rubric
from typing import Dict

class AutoJudge(Judge):

    def from_pretrained(self, model_id:str, device:str="auto"):
        pass

    def judge(self, rubric: Rubric, parser: Parser=Parser) -> Dict[str, Dict[str, str]]:
        pass
