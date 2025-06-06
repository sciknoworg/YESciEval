from abc import ABC, abstractmethod
from typing import Dict, Any
from pydantic import BaseModel, Field


class RubricLikertScale(BaseModel):
    rating: int = Field(..., ge=1, le=5, description="Rating from 1 to 5")
    rationale: str = Field(..., description="Textual explanation for the rating")


class Parser(ABC):
    """
    Abstract base class for parsing model outputs into structured characteristic evaluations.

    Each characteristic maps to a CharacteristicScore with a rating and rationale.
    """
    @abstractmethod
    def parse(self, raw_output: str) -> Any:
        """
        Parse the raw model output into structured characteristic evaluations.

        Args:
            raw_output (str): The text generated by the model.

        Returns:
            Dict[str, CharacteristicScore]: Mapping from characteristic name to its score and rationale.
        """
        return raw_output
