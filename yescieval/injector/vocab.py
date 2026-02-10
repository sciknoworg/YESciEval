from abc import ABC
from typing import Dict, List
from .domains import verbalized_domains, vocab_block_specs, vocabs

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
        "{GAP_IDENTIFICATION_VOCAB}": "gap_identification_vocab_block",
        "{NOVELTY_INDICATORS_VOCAB}": "novelty_indicators_vocab_block",
        "{EPISTEMIC_CALIBRATION_VOCAB}": "epistemic_calibration_vocab_block",
        "{QUANT_UNCERTAINTY_VOCAB}": "quant_uncertainty_vocab_block",
        "{UNCERTAINTY_VOCAB}": "uncertainty_vocab_block"   
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
    
    def _build_vocab_block(self, domain_id: str, block_name: str) -> str:
        spec = vocab_block_specs.get(domain_id, {}).get(block_name, {})
        keys = spec.get("keys", [])
        terms = []
        domain_vocab = vocabs.get(domain_id, {})
        for key in keys:
            terms.extend(domain_vocab.get(key, []) or [])
        terms = self._clean_terms(terms)
        if not terms:
            return ""
        label = spec.get("label", block_name.replace("_", " ").title())
        if verbalized_domains.get(domain_id):
            label += f" ({verbalized_domains[domain_id]})"
        return f"{label}: " + ", ".join(terms)

    def format_prompt(self, prompt: str, domain: str) -> str:
        """
        Replaces known placeholders in the prompt with vocab blocks
        based on the domain.
        """
        domain_id = domain.strip().lower()
        for placeholder, block_name in self.placeholders.items():
            if placeholder in prompt:
                vocab_block = self._build_vocab_block(domain_id, block_name)
                prompt = prompt.replace(placeholder, vocab_block)
        return prompt