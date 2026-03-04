from pathlib import Path

__version__ = (Path(__file__).parent / "VERSION").read_text().strip()

from .base import Rubric, Parser
from .injector import ExampleInjector, VocabularyInjector
from .judge import AutoJudge, AskAutoJudge, BioASQAutoJudge, CustomAutoJudge, GPTCustomAutoJudge
from .parser import GPTParser
from .rubric.pointwise.breadth import ContextCoverage, ScopeCoverage, MethodCoverage, DimensionCoverage, ScaleCoverage
from .rubric.pointwise.depth import MechanisticUnderstanding, CausalReasoning, TemporalPrecision
from .rubric.pointwise.fidelity import Informativeness, Correctness, Completeness
from .rubric.pointwise.gap import GapIdentification
from .rubric.pointwise.innovation import StateOfTheArtAndNovelty
from .rubric.pointwise.rigor import EpistemicCalibration, QuantitativeEvidenceAndUncertainty, ExplicitUncertainty
from .rubric.pointwise.structural import Coherence, Integration, Relevancy
from .rubric.pointwise.stylistic import Cohesion, Readability, Conciseness
