from abc import ABC
from pydantic import BaseModel
from typing import Dict, Optional

class Domain(BaseModel, ABC):
    examples: Dict[str, Dict] = None
    vocab: Dict[str, Dict] = None
    ID: str = None
    verbalized: str = None
    vocab_block_specs: Optional[Dict[str, Dict[str, object]]] = None