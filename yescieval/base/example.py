import json
from typing import Dict, Any


class ExampleLoader:
    """
    Loads rubric-specific example responses and injects them
    into prompt templates based on domain and rubric name.
    """

    DOMAIN_MAP = {
        "nlp": "NLP",
        "ecology": "Ecology",
    }

    CATEGORIES = ("Depth", "Breadth")
    PLACEHOLDER = "{EXAMPLE_RESPONSES}"
    EMPTY_VALUE = "{}"

    def __init__(self, file_path: str):
        self.data = self._load_examples(file_path)

    def _normalize_domain(self, domain: str) -> str:
        return domain.strip().lower()

    def _load_examples(self, file_path: str) -> Dict[str, Any]:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, dict):
            raise ValueError("Example file must contain a JSON object at top level")

        return data

    def get_example_data(self, domain: str, rubric_name: str) -> Dict[str, Any]:
        """
        Returns:
            {rubric_name: <example_object>} if found,
            {} otherwise.
        """
        domain = self._normalize_domain(domain)
        topic_key = self.DOMAIN_MAP.get(domain)

        if not topic_key:
            return {}

        topic_data = self.data.get(topic_key, {})

        for category in self.CATEGORIES:
            category_data = topic_data.get(category, {})
            if rubric_name in category_data:
                return {rubric_name: category_data[rubric_name]}

        return {}

    def fill_prompt(self, template: str, domain: str, rubric_name: str) -> str:
        """
        Injects example responses JSON into the template.
        """
        example_data = self.get_example_data(domain, rubric_name)

        if not example_data:
            return template.replace(self.PLACEHOLDER, self.EMPTY_VALUE)

        example_json = json.dumps(example_data, indent=4)
        return template.replace(self.PLACEHOLDER, example_json)
