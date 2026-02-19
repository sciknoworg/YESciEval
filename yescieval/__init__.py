from pathlib import Path

__version__ = (Path(__file__).parent / "VERSION").read_text().strip()

from .base import Rubric, Parser
from .injector import ExampleInjector, VocabularyInjector
from .judge import AutoJudge, AskAutoJudge, BioASQAutoJudge, CustomAutoJudge, GPTCustomAutoJudge
from .parser import GPTParser
from .pointwise.breadth import (ContextCoverage, ScopeCoverage, MethodCoverage, DimensionCoverage, ScaleCoverage)
from .pointwise.depth import (MechanisticUnderstanding, CausalReasoning, TemporalPrecision)
from .pointwise.fidelity import (Informativeness, Correctness, Completeness)
from .pointwise.gap import GapIdentification
from .pointwise.innovation import StateOfTheArtAndNovelty
from .pointwise.rigor import (EpistemicCalibration, QuantitativeEvidenceAndUncertainty, ExplicitUncertainty)
from .pointwise.structural import (Coherence, Integration, Relevancy)
from .pointwise.stylistic import (Cohesion, Readability, Conciseness)
