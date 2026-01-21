import json
from pathlib import Path
from typing import Dict


class VocabLoader:
    """
    Loads multiple vocabularies and fills placeholders in prompts
    based on the selected domain.
    """

    PLACEHOLDERS = {
        "{MECHANISTIC_VOCAB}": "mechanistic_vocab_block",
        "{CAUSAL_VOCAB}": "causal_vocab_block",
        "{TEMPORAL_VOCAB}": "temporal_vocab_block",
    }

    def __init__(self, domain_to_file: Dict[str, str]):
        """
        domain_to_file: {"nlp": "vocab/nlp_dictionary.json", "ecology": "vocab/ecology_dictionary.json"}
        """
        self.domain_to_file = {
            self._normalize_domain(k): v for k, v in domain_to_file.items()
        }
        self.vocabs: Dict[str, Dict] = {}

        for domain, file_path in self.domain_to_file.items():
            self.vocabs[domain] = self._load_vocab(file_path)

    def _normalize_domain(self, domain: str) -> str:
        return domain.strip().lower()

    def _load_vocab(self, file_path: str) -> Dict:
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Vocabulary file not found: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError(f"Invalid vocabulary format: {file_path}")
        return data

    def _clean_terms(self, terms) -> list[str]:

        seen = set()
        cleaned = []
        for t in terms:
            if not isinstance(t, str):
                continue
            t = t.strip()
            if not t or t in seen:
                continue
            seen.add(t)
            cleaned.append(t)
        return cleaned


    def mechanistic_vocab_block(self, domain: str) -> str:
        domain = self._normalize_domain(domain)
        V = self.vocabs.get(domain, {})

        if domain == "ecology":
            terms = V.get("mechanistic_terms", [])
            label = "Mechanistic terms (Ecology)"
        elif domain == "nlp":
            terms = (
                V.get("training_terms", [])
                + V.get("arch_terms", [])
                + V.get("ablation_terms", [])
            )
            label = "Mechanistic terms (NLP)"
        else:
            terms = V.get("mechanistic_terms", [])
            label = "Mechanistic terms"

        terms = self._clean_terms(terms)
        return f"{label}: " + ", ".join(terms)

    def causal_vocab_block(self, domain: str) -> str:
        domain = self._normalize_domain(domain)
        V = self.vocabs.get(domain, {})
        terms = self._clean_terms(V.get("causal_terms", []))
        return "Causal connectives / triggers: " + ", ".join(terms)

    def temporal_vocab_block(self, domain: str) -> str:
        domain = self._normalize_domain(domain)
        V = self.vocabs.get(domain, {})
        terms = self._clean_terms(V.get("temporal_terms", []))
        return "Temporal expressions: " + ", ".join(terms)

    def fill_prompt(self, prompt_template: str, domain: str) -> str:
        """
        Replaces known placeholders in the prompt with vocab blocks
        based on the domain.
        """
        prompt = prompt_template
        domain = self._normalize_domain(domain)

        for placeholder, method_name in self.PLACEHOLDERS.items():
            if placeholder in prompt:
                block_fn = getattr(self, method_name)
                prompt = prompt.replace(placeholder, block_fn(domain))

        return prompt
