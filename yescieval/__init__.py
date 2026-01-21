from pathlib import Path

__version__ = (Path(__file__).parent / "VERSION").read_text().strip()

from .base import Rubric, Parser, Judge, VocabLoader, ExampleLoader
from .rubric import (Informativeness, Correctness, Completeness, Coherence, Relevancy,
                    Integration, Cohesion, Readability, Conciseness,
                    MechanisticUnderstanding, CausalReasoning, TemporalPrecision, GapIdentification, 
                    StatisticalSophistication, CitationPractices, UncertaintyAcknowledgment, 
                    SpeculativeStatements, NoveltyIndicators)
from .judge import AutoJudge, AskAutoJudge, BioASQAutoJudge, CustomAutoJudge, GPTCustomAutoJudge
from .parser import GPTParser

