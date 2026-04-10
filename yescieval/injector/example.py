import json
from abc import ABC
from typing import Any

from .domains import example_responses

class ExampleInjector(ABC):
    """
    Loads rubric-specific example responses and injects them
    into prompt templates based on domain and rubric name.
    """
    examples_placeholder = "{EXAMPLE_RESPONSES}"
    empty_placeholder = "{}"

    def format_example(self, domain: str, rubric_id: str, eval_type: str = "pointwise") -> Any:
        """
        Returns:
            {rubric_id: <example_object>} if found,
            {} otherwise.
        """
        domain_id = domain.strip().lower()
        domain_data = example_responses.get(domain_id, {})
        if not domain_data:
            return None
        eval_data = domain_data.get(eval_type, {}) # pointwise or pairwise
        if not eval_data:
            return None
        for _, rubrics in eval_data.items():
            if rubric_id in rubrics:
                return json.dumps({rubric_id: rubrics[rubric_id]}, indent=4)
        return None


    def format_prompt(self, prompt: str, domain: str, rubric_id: str, eval_type: str = "pointwise") -> str:
        """
        Injects example responses JSON into the template.
        """
        examples = self.format_example(domain, rubric_id, eval_type)
        if examples:
            return prompt.replace(self.examples_placeholder, examples)
        return prompt.replace(self.examples_placeholder, self.empty_placeholder)
