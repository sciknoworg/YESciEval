from typing import Dict
from .nlp import NLP
from .ecology import Ecology

domains = [NLP(), Ecology()]

vocabs: Dict[str, Dict] = {domain.ID: domain.vocab for domain in domains}

example_responses: Dict[str, Dict] = {domain.ID: domain.examples for domain in domains}

verbalized_domains: Dict[str, str] = {domain.ID: domain.verbalized for domain in domains}