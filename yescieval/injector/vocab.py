from abc import ABC
from typing import Dict, List
from .domains import vocabs, verbalized_domains

class VocabularyInjector(ABC):
    """
    Loads multiple vocabularies and fills placeholders in prompts
    based on the selected domain.
    """
    placeholders: Dict[str, str] = {
        "{MECHANISTIC_VOCAB}": "mechanistic_vocab_block",
        "{CAUSAL_VOCAB}": "causal_vocab_block",
        "{TEMPORAL_VOCAB}": "temporal_vocab_block",
        "{CONTEXT_VOCAB}": "context_coverage_vocab_block",
        "{METHOD_VOCAB}": "method_coverage_vocab_block",
        "{DIMENSION_VOCAB}": "dimension_coverage_vocab_block",
        "{SCOPE_VOCAB}": "scope_coverage_vocab_block",
        "{SCALE_VOCAB}": "scale_coverage_vocab_block",       
    }

    def _clean_terms(self, terms) -> List[str]:
        seen_terms = set()
        cleaned_terms = []
        for term in terms:
            if not isinstance(term, str):
                continue
            term = term.strip()
            if not term or term in seen_terms:
                continue
            seen_terms.add(term)
            cleaned_terms.append(term)
        return cleaned_terms
    
    def _get_domain_vocab(self, domain_id: str) -> dict:
        return vocabs.get(domain_id, {}) or {}

    def mechanistic_vocab_block(self, domain_id: str) -> str:
        terms = vocabs[domain_id].get("mechanistic_terms")
        label = "Mechanistic terms"
        label += f" ({verbalized_domains.get(domain_id)})" if verbalized_domains.get(domain_id) else ""
        if domain_id == "nlp":
            terms = (vocabs[domain_id].get("training_terms") +
                     vocabs[domain_id].get("arch_terms") +
                     vocabs[domain_id].get("ablation_terms"))
        terms = self._clean_terms(terms)
        return f"{label}: " + ", ".join(terms)

    def causal_vocab_block(self, domain_id: str) -> str:
        terms = self._clean_terms(vocabs[domain_id].get("causal_terms"))
        return "Causal connectives / triggers: " + ", ".join(terms)

    def temporal_vocab_block(self, domain_id: str) -> str:
        terms = self._clean_terms(vocabs[domain_id].get("temporal_terms"))
        return "Temporal expressions: " + ", ".join(terms)
    
    def context_coverage_vocab_block(self, domain_id: str) -> str:
        domain_vocab = self._get_domain_vocab(domain_id)
        label = "Context Coverage"
        if verbalized_domains.get(domain_id):
            label += f" ({verbalized_domains[domain_id]})"
        if domain_id == "ecology":
            terms = domain_vocab.get("regions", [])
        elif domain_id == "nlp":
            terms = domain_vocab.get("tasks", [])
        else:
            terms = []
        terms = self._clean_terms(terms)
        return f"{label}: " + ", ".join(terms)
    
    def method_coverage_vocab_block(self, domain_id: str) -> str:
        domain_vocab = self._get_domain_vocab(domain_id)
        label = "Method Coverage"
        if verbalized_domains.get(domain_id):
            label += f" ({verbalized_domains[domain_id]})"
        if domain_id == "nlp":
            terms = (
                domain_vocab.get("training_terms", []) +
                domain_vocab.get("arch_terms", [])
            )
        elif domain_id == "ecology":
            terms = domain_vocab.get("interventions", [])
        else:
            terms = []
        terms = self._clean_terms(terms)
        return f"{label}: " + ", ".join(terms)
    
    def dimension_coverage_vocab_block(self, domain_id: str) -> str:
        domain_vocab = self._get_domain_vocab(domain_id)
        label = "Dimension Coverage"
        if verbalized_domains.get(domain_id):
            label += f" ({verbalized_domains[domain_id]})"
        if domain_id == "ecology":
            terms = domain_vocab.get("diversity_dimensions", [])
        elif domain_id == "nlp":
            terms = domain_vocab.get("eval_metrics", [])
        else:
            return ""
        terms = self._clean_terms(terms)
        return f"{label}: " + ", ".join(terms)
    
    def scope_coverage_vocab_block(self, domain_id: str) -> str:
        domain_vocab = self._get_domain_vocab(domain_id)
        label = "Scope Coverage"
        if verbalized_domains.get(domain_id):
            label += f" ({verbalized_domains[domain_id]})"
        if domain_id == "ecology":
            terms = domain_vocab.get("ecosystem_services", [])
        elif domain_id == "nlp":
            terms = domain_vocab.get("languages", [])
        else:
            return ""
        terms = self._clean_terms(terms)
        return f"{label}: " + ", ".join(terms)
    
    def scale_coverage_vocab_block(self, domain_id: str) -> str:
        domain_vocab = self._get_domain_vocab(domain_id)
        label = "Scale Coverage"
        if verbalized_domains.get(domain_id):
            label += f" ({verbalized_domains[domain_id]})"
        if domain_id == "ecology":
            terms = domain_vocab.get("scale_terms", [])
        elif domain_id == "nlp":
            terms = domain_vocab.get("compute_terms", [])
        else:
            return ""
        terms = self._clean_terms(terms)
        return f"{label}: " + ", ".join(terms)

    def format_prompt(self, prompt: str, domain: str) -> str:
        """
        Replaces known placeholders in the prompt with vocab blocks
        based on the domain.
        """
        domain_id = domain.strip().lower()
        for placeholder, method in self.placeholders.items():
            if placeholder in prompt:
                block_fn = getattr(self, method)
                prompt = prompt.replace(placeholder, block_fn(domain_id))
        return prompt
