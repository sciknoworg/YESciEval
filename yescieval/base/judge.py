from abc import ABC
from typing import Dict, Any
from pydantic import BaseModel
from . import Rubric


class Judge(ABC):

    def from_pretrained(self, model_id:str, device: str="auto", token:str =""):
        self.model, self.tokenizer = self._from_pretrained(model_id=model_id, device=device, token=token)

    def judge(self, rubric: Rubric, max_new_tokens: int=150) -> Dict[str, Dict[str, str]] | str | BaseModel:
        pass

    def _from_pretrained(self, model_id: str, device: str = "auto", token: str = "") -> [Any, Any]:
        pass

