
Rubrics
===================

A total of **21** evaluation rubrics were defined as part of the YESciEval test framework within two categories presented as following:

.. hint::


	Here is a simple example of how to import rubrics in your code:

	.. code-block:: python

	    from yescieval import Informativeness, Correctness, Completeness, Coherence, Relevancy,
	                          Integration, Cohesion, Readability, Conciseness,
	                          MechanisticUnderstanding, CausalReasoning, TemporalPrecision, GapIdentification,
	                          StatisticalSophistication, CitationPractices, UncertaintyAcknowledgment,
	                          SpeculativeStatements, NoveltyIndicators

	The rubrics are presented as following:


Question Answering
---------------------------------

Linguistic & Stylistic Quality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following ``Linguistic & Stylistic Quality`` concerns grammar, clarity, and adherence to academic writing conventions.


.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Evaluation Rubric
     - Description
   * - **1. Cohesion:**
     - Are the sentences connected appropriately to make the resulting synthesis cohesive?
   * - **2. Conciseness:**
     - Is the answer short and clear, without redundant statements?
   * - **3. Readability:**
     - Does the answer follow appropriate style and structure conventions for academic writing, particularly for readability?

Logical & Structural Integrity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Following ``Logical & Structural Integrity`` focuses on the reasoning and organization of information.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Evaluation Rubric
     - Description
   * - **4. Coherence:**
     - Are the ideas connected soundly and logically?
   * - **5. Integration:**
     - Are the sources structurally and linguistically well-integrated, using appropriate markers of provenance/quotation and logical connectors for each reference?
   * - **6. Relevancy:**
     - Is the information in the answer relevant to the problem?

Evidence Fidelity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following ``Evidence Fidelity`` ensures that the response is both correct and useful.


.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Evaluation Rubric
     - Description
   * - **7. Correctness:**
     - Is the information in the answer a correct representation of the content of the provided abstracts?
   * - **8. Completeness:**
     - Is the answer a comprehensive encapsulation of the relevant information in the provided abstracts?
   * - **9. Informativeness:**
     - Is the answer a useful and informative reply to the problem?

Usage
~~~~~~~~~~~~~~~~~

.. code-block:: python

    from yescieval import Coherence

    papers = {
        "Paper 1 title": "abstract of paper 1 ...",
        "Paper 2 title": "abstract of paper 2 ...",
        "Paper 3 title": "abstract of paper 3 ...",
        "Paper 4 title": "abstract of paper 4 ...",
        "Paper 5 title": "abstract of paper 5 ..."
    }
    question = "What are the key findings on AI in these papers?"
    answer = "The synthesis answer summarizing the papers."

    # Instantiate a rubric, e.g. Coherence
    rubric = Coherence(papers=papers, question=question, answer=answer)
    instruction = rubric.instruct()

    print(instruction)
    print(rubric.name)


Deep Research
-------------------

Research Depth Assessment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following ``Research Depth Assessment`` quantifies the mechanistic and analytical sophistication of synthesis outputs.


.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Evaluation Rubric
     - Description
   * - **10. Mechanistic Understanding:**
     - Does the answer show understanding of ecological processes, using indicators like “feedback,” “nutrient cycling,” or “trophic cascade”?
   * - **11. Causal Reasoning:**
     - Does the answer show clear cause-effect relationships using words like “because,” “results in,” or “drives”?
   * - **12. Temporal Precision:**
     - Does the answer include specific time references, like intervals (“within 6 months”) or dates (“1990–2020”)?


Research Breadth Assessment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following ``Research Breadth Assessment`` evaluates the diversity of evidence across dimensions, scope, and methodological contexts.


.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Evaluation Rubric
     - Description
   * - **13. Context Coverage:**
     - Does the answer demonstrate breadth by addressing several distinct and relevant contexts related to the research question?
   * - **14. Method Coverage:**
     - Does the answer address multiple distinct methods or interventions relevant to the research question?
   * - **15. Dimension Coverage:**
     - Does the answer distribute attention across multiple distinct descriptive or evaluative dimensions relevant to the research question?
   * - **16. Scope Coverage:**
     - Does the answer distribute attention across multiple distinct scopes of applicability or impact relevant to the research question?
   * - **17. Scale Coverage:**
     - Does the answer distribute attention across multiple distinct scales relevant to the research question?

Scientific Rigor Assessment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following ``Scientific Rigor Assessment`` assesses the evidentiary and methodological integrity of the synthesis.


.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Evaluation Rubric
     - Description
   * - **18. Quantitative Evidence And Uncertainty:**
     - Does the answer appropriately handle quantitative evidence and uncertainty relevant to the research question?
   * - **19. Epistemic Calibration:**
     - Does the answer clearly align claim strength with evidential support by marking uncertainty, assumptions, and limitations where relevant?

Innovation Capacity Assessment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following ``Innovation Capacity Assessment`` evaluates the novelty of the synthesis.


.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Evaluation Rubric
     - Description
   * - **20. State-Of-The-Art And Novelty :**
     - Does the response identify and contextualize relevant state-of-the-art or novel contributions relative to prior work?


Research Gap Assessment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following ``Research Gap Assessment`` detects explicit acknowledgment of unanswered questions or understudied areas in the synthesis.


.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Evaluation Rubric
     - Description
   * - **21. Gap Identification:**
     - Does the answer point out unanswered questions or understudied areas, using terms like “research gap” or “understudied”?


Usage
~~~~~~~~~~~~~~

Injectors allow you to augment rubric prompts with additional guidance, such as example responses or domain-specific vocabulary, to improve evaluation alignment. Each injector is rubric-specific, meaning different rubrics can receive different injected content. They are domain-dependent, so the examples and vocabulary injected are automatically selected based on the domain you specify (e.g., "nlp", "ecology"). Multiple injectors, such as examples and vocabulary, can be used together in a composable way. Available injectors are listed below:

- **Example Injector**: Injects curated example responses for the chosen rubric and domain.
- **Vocabulary Injector**: Injects domain and rubric-specific terminology to guide model reasoning.

Here is how to define the deep research rubric:

.. code-block:: python

   from yescieval import MechanisticUnderstanding

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

   from yescieval import MechanisticUnderstanding, CustomAutoJudge, ExampleInjector, VocabularyInjector

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