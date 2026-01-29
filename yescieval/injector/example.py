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

    def format_example(self, domain: str, rubric_id: str) -> Any:
        """
        Returns:
            {rubric_id: <example_object>} if found,
            {} otherwise.
        """
        domain_id = domain.strip().lower()
        domain_example_responses = example_responses.get(domain_id, None)
        if domain_example_responses:
            for _, rubrics in domain_example_responses.items():
                for rubric, example_response in rubrics.items():
                    if rubric_id == rubric:
                        return json.dumps({rubric_id: example_response}, indent=4)
        return None

    def format_prompt(self, prompt: str, domain: str, rubric_id: str) -> str:
        """
        Injects example responses JSON into the template.
        """
        examples = self.format_example(domain, rubric_id)
        if examples:
            return prompt.replace(self.examples_placeholder, examples)
        return prompt.replace(self.examples_placeholder, self.empty_placeholder)
