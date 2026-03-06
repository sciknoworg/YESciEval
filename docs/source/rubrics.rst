Rubrics
=======

A total of **22** evaluation rubrics are defined as part of the YESciEval test framework,
organised into sub-categories under **Pointwise Evaluation**.

Each rubric can be used in two ways:

- **Basic** – pass only ``papers``, ``question``, and ``answer``.
- **With Injectors** – additionally pass a ``domain`` and one or both injectors
  (``VocabularyInjector``, ``ExampleInjector``) to augment the prompt with
  domain-specific terminology and curated example responses.

.. hint::

    Quick import of all rubrics:

    .. code-block:: python

        from yescieval import (
	            Informativeness, Correctness, Completeness,
	            Coherence, Relevancy, Integration,
	            Cohesion, Readability, Conciseness,
	            MechanisticUnderstanding, CausalReasoning, TemporalPrecision,
	            GapIdentification, ContextCoverage, MethodCoverage,
	            DimensionCoverage, ScopeCoverage, ScaleCoverage,
	            EpistemicCalibration, QuantitativeEvidenceAndUncertainty,
	            ExplicitUncertainty, StateOfTheArtAndNovelty,
        )


Pointwise Evaluation
--------------------

Pointwise evaluation is a rubric-based scoring method in which a judge assigns a
numerical score and a rationale to an answer for a given question under a specific rubric.

An example rating for pointwise evaluation is as follows:

.. code-block:: json

   {
     "rating": 4,
     "rationale": "The answer covers key aspects of how AI is applied in healthcare,
                   such as diagnostics and personalised medicine."
   }

For each rating level from 1 to 5, the rubric provides concrete definitions of what
each score means in context.  The LLM is expected to:

1. Provide a numerical score.
2. Provide a rationale explaining its decision.

----

Linguistic & Stylistic Quality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Concerns grammar, clarity, and adherence to academic writing conventions.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Rubric
     - Description
   * - **1. Cohesion**
     - Are the sentences connected appropriately to make the resulting synthesis cohesive?
   * - **2. Conciseness**
     - Is the answer short and clear, without redundant statements?
   * - **3. Readability**
     - Does the answer follow appropriate style and structure conventions for academic writing,
       particularly for readability?



.. tab:: Usage

  .. code-block:: python

     from yescieval.rubric.pointwise.stylistic import Cohesion

     papers = {
         "Paper 1 title": "abstract of paper 1 ...",
         "Paper 2 title": "abstract of paper 2 ...",
     }
     question = "What are the key findings on AI in these papers?"
     answer   = "The synthesis answer summarising the papers."

     rubric      = Cohesion(papers=papers, question=question, answer=answer)
     instruction = rubric.instruct()



Logical & Structural Integrity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Focuses on the reasoning and organisation of information.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Rubric
     - Description
   * - **4. Coherence**
     - Are the ideas connected soundly and logically?
   * - **5. Integration**
     - Are the sources structurally and linguistically well-integrated, using appropriate
       markers of provenance/quotation and logical connectors for each reference?
   * - **6. Relevancy**
     - Is the information in the answer relevant to the problem?



.. tab:: Usage

  .. code-block:: python

     from yescieval.rubric.pointwise.structural import Coherence

     rubric      = Coherence(papers=papers, question=question, answer=answer)
     instruction = rubric.instruct()


Evidence Fidelity
~~~~~~~~~~~~~~~~~~~~

Ensures that the response is both correct and useful.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Rubric
     - Description
   * - **7. Correctness**
     - Is the information in the answer a correct representation of the content of the
       provided abstracts?
   * - **8. Completeness**
     - Is the answer a comprehensive encapsulation of the relevant information in the
       provided abstracts?
   * - **9. Informativeness**
     - Is the answer a useful and informative reply to the problem?


.. tab:: Usage

  .. code-block:: python

     from yescieval.rubric.pointwise.fidelity import Correctness

     rubric      = Correctness(papers=papers, question=question, answer=answer)
     instruction = rubric.instruct()

Research Depth Assessment
~~~~~~~~~~~~~~~~~~~~~~~~~

Quantifies the mechanistic and analytical sophistication of synthesis outputs.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Rubric
     - Description
   * - **10. Mechanistic Understanding**
     - Is the answer explaining *how* and *why* the described outcomes occur by detailing
       underlying processes, interactions, or pathways, rather than only stating what happens?
   * - **11. Causal Reasoning**
     - Is the answer explicitly describing cause-effect relationships, rather than only
       reporting associations or trends?
   * - **12. Temporal Precision**
     - Is the answer using specific and meaningful time references, rather than vague
       temporal markers?



.. tab:: Basic Usage

  .. code-block:: python

     from yescieval.rubric.pointwise.depth import MechanisticUnderstanding

     rubric      = MechanisticUnderstanding(papers=papers, question=question, answer=answer)
     instruction = rubric.instruct()

     print(instruction)
     print(rubric.name)

.. tab:: Usage with Example and Vocabulary Injectors

  .. code-block:: python

     from yescieval import ExampleInjector, VocabularyInjector
     from yescieval.rubric.pointwise.depth import MechanisticUnderstanding

     # Step 1: Create a rubric with injectors
     rubric = MechanisticUnderstanding(
         papers=papers,
         question=question,
         answer=answer,
         domain="nlp",
         vocabulary=VocabularyInjector(),
         example=ExampleInjector(),
     )
     instruction_prompt = rubric.instruct()


Research Breadth Assessment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Evaluates the diversity of evidence across dimensions, scope, and methodological contexts.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Rubric
     - Description
   * - **13. Context Coverage**
     - Is the answer covering several distinct and relevant contexts related to the
       research question?
   * - **14. Method Coverage**
     - Is the answer addressing multiple distinct methods or interventions relevant to
       the research question?
   * - **15. Dimension Coverage**
     - Is the answer distributing attention across multiple distinct descriptive or
       evaluative dimensions relevant to the research question?
   * - **16. Scope Coverage**
     - Is the answer distributing attention across multiple distinct scopes of
       applicability or impact relevant to the research question?
   * - **17. Scale Coverage**
     - Is the answer distributing attention across multiple distinct scales of analysis,
       organisation, or application relevant to the research question?

.. tab:: Basic Usage

  .. code-block:: python

     from yescieval.rubric.pointwise.breadth import ContextCoverage

     rubric      = ContextCoverage(papers=papers, question=question, answer=answer)
     instruction = rubric.instruct()

     print(instruction)
     print(rubric.name)

.. tab:: Usage with Example and Vocabulary Injectors

  .. code-block:: python

     from yescieval import ExampleInjector, VocabularyInjector
     from yescieval.rubric.pointwise.breadth import ContextCoverage

     rubric = ContextCoverage(
         papers=papers,
         question=question,
         answer=answer,
         domain="ecology",
         vocabulary=VocabularyInjector(),
         example=ExampleInjector(),
     )
     instruction = rubric.instruct()


Scientific Rigor Assessment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assesses the evidentiary and methodological integrity of the synthesis.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Rubric
     - Description
   * - **18. Epistemic Calibration**
     - Is the answer aligning claim strength with evidence and clearly marking
       uncertainty or limitations where relevant?
   * - **19. Quantitative Evidence And Uncertainty**
     - Is the answer using and interpreting relevant quantitative evidence and
       uncertainty appropriately, or justifying when it is not applicable?
   * - **20. Explicit Uncertainty**
     - Is the answer explicitly mentioning limitations or uncertainty, using terms
       like "unknown," "limited evidence," or "unclear"?


.. tab:: Basic usage

  .. code-block:: python

     from yescieval.rubric.pointwise.rigor import EpistemicCalibration

     rubric      = EpistemicCalibration(papers=papers, question=question, answer=answer)
     instruction = rubric.instruct()

     print(instruction)
     print(rubric.name)

.. tab::  Usage with Example and Vocabulary Injectors

  .. code-block:: python

     from yescieval import ExampleInjector, VocabularyInjector
     from yescieval.rubric.pointwise.rigor import EpistemicCalibration

     rubric = EpistemicCalibration(
         papers=papers,
         question=question,
         answer=answer,
         domain="nlp",
         vocabulary=VocabularyInjector(),
         example=ExampleInjector(),
     )
     instruction = rubric.instruct()


Innovation Capacity Assessment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Evaluates the novelty of the synthesis.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Rubric
     - Description
   * - **21. State Of The Art And Novelty**
     - Is the answer identifying specific state-of-the-art and/or novel contributions
       relevant to the research question, using terms like "novel," "state-of-the-art"?

.. tab:: Basic Usage

  .. code-block:: python

     from yescieval.rubric.pointwise.innovation import StateOfTheArtAndNovelty

     rubric      = StateOfTheArtAndNovelty(papers=papers, question=question, answer=answer)
     instruction = rubric.instruct()

     print(instruction)
     print(rubric.name)

.. tab:: Usage with Example and Vocabulary Injectors

  .. code-block:: python

     from yescieval import ExampleInjector, VocabularyInjector
     from yescieval.rubric.pointwise.innovation import StateOfTheArtAndNovelty

     rubric = StateOfTheArtAndNovelty(
         papers=papers,
         question=question,
         answer=answer,
         domain="nlp",
         vocabulary=VocabularyInjector(),
         example=ExampleInjector(),
     )
     instruction = rubric.instruct()



Research Gap Assessment
~~~~~~~~~~~~~~~~~~~~~~~

Detects explicit acknowledgment of unanswered questions or understudied areas.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Rubric
     - Description
   * - **22. Gap Identification**
     - Is the answer pointing out unanswered questions or understudied areas, using
       terms like "research gap" or "understudied"?




.. tab:: Basic Usage

  .. code-block:: python

     from yescieval.rubric.pointwise.gap import GapIdentification

     rubric      = GapIdentification(papers=papers, question=question, answer=answer)
     instruction = rubric.instruct()

     print(instruction)
     print(rubric.name)

.. tab:: Usage with Example and Vocabulary Injectors

  .. code-block:: python

     from yescieval import ExampleInjector, VocabularyInjector
     from yescieval.rubric.pointwise.gap import GapIdentification

     rubric = GapIdentification(
         papers=papers,
         question=question,
         answer=answer,
         domain="ecology",
         vocabulary=VocabularyInjector(),
         example=ExampleInjector(),
     )
     instruction = rubric.instruct()


Injectors Reference
-------------------

Injectors allow you to augment rubric prompts with additional guidance, such as example responses or domain-specific vocabulary, to improve evaluation alignment. Each injector is rubric-specific, meaning different rubrics can receive different injected content. They are domain-dependent, so the examples and vocabulary injected are automatically selected based on the domain you specify (e.g., "nlp", "ecology"). Multiple injectors, such as examples and vocabulary, can be used together in a composable way. Available injectors are listed below:

- **Example Injector**: Injects curated example responses for the chosen rubric and domain.
- **Vocabulary Injector**: Injects domain and rubric-specific terminology to guide model reasoning.

Here is how to define the deep research rubric:

.. code-block:: python

   from yescieval.rubric.pointwise.depth import MechanisticUnderstanding

   rubric = MechanisticUnderstanding(
       papers=papers,
       question=question,
       answer=answer,
       domain="nlp",
       vocabulary=VocabularyInjector(),
       example=ExampleInjector()
   )

In this example, ``VocabularyInjector`` and ``ExampleInjector`` provide content aligned with the NLP domain for the *Mechanistic Understanding* rubric.

.. tab:: Injected Responses

	::

	   "MechanisticUnderstanding": [
	       {
	           "rating": "1",
	           "rationale": "The response reports results or model performance but does not explain how the model architecture or training process leads to those outcomes."
	       },
	       {
	           "rating": "4",
	           "rationale": "The response provides a clear mechanistic explanation of how the model works, describing the role of transformer-based architectures, the effects of pretraining and fine-tuning, and insights from ablation studies that show how specific components contribute to performance."
	       }
	   ]

.. tab::  Injected Vocabulary

	::

	   "training_terms": [
	      "pretraining", "fine-tuning", "instruction tuning", "rlhf", "dpo", "lora", "qlora", "quantization",
	      "distillation", "curriculum", "data augmentation", "continual learning"
	   ]

Here is an complete example of how evaluation on can be done:

.. code-block:: python

   from yescieval import CustomAutoJudge, ExampleInjector, VocabularyInjector
   from yescieval.rubric.pointwise.depth import MechanisticUnderstanding

   # Step 1: Create a rubric
   rubric = MechanisticUnderstanding(papers=papers,
                                     question=question,
                                     answer=answer,
                                     domain="nlp",
                                     vocabulary=VocabularyInjector(),
                                     example=ExampleInjector())
   instruction_prompt = rubric.instruct()

   # Step 2: Load the evaluation model (judge)
   judge = CustomAutoJudge()
   judge.from_pretrained(model_id="Qwen/Qwen3-8B", device="cpu", token="your_huggingface_token")

   # Step 3: Evaluate the answer
   result = judge.judge(rubric=rubric)
   print("Raw Evaluation Output:")
   print(result)


.. hint::

	There are specific domains incorporated in YESCiEval for injectors presented as following, however using injector is also optional!

	.. list-table::
	   :header-rows: 1
	   :widths: 50 30

	   * - Domain
	     - ID
	   * - **Natural Language Processing**
	     - ``nlp``
	   * - **Ecology**
	     - ``ecology``