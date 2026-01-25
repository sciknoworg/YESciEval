from abc import ABC
from pydantic import BaseModel
from typing import Dict

class Domain(BaseModel, ABC):
    examples: Dict[str, Dict] = None
    vocab: Dict[str, Dict] = None
    ID: str = None
    verbalized: str = None