
Rubrics
===================

A total of twenty three (23) evaluation rubrics were defined as part of the YESciEval test framework.

Linguistic & Stylistic Quality
---------------------------------

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
---------------------------------
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

Content Accuracy & Informativeness
---------------------------------

Following ``Content Accuracy & Informativeness`` ensures that the response is both correct and useful.


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

Research Depth Assessment
---------------------------------

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
---------------------------------

Following ``Research Breadth Assessment`` evaluates the diversity of evidence across spatial, ecological, and methodological contexts.


.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Evaluation Rubric
     - Description
   * - **13. Geographic Coverage:**
     - Does the answer cover multiple biogeographic zones, such as “Tropical” or “Boreal”?
   * - **14. Intervention Diversity:**
     - Does the answer include a variety of management practices?
   * - **15. Biodiversity Dimensions:**
     - Does the answer mention different aspects of biodiversity, like taxonomic, functional, phylogenetic, or spatial diversity?
   * - **16. Ecosystem Services:**
     - Does the answer include relevant ecosystem services, based on the Millennium Ecosystem Assessment vocabulary?
   * - **17. Spatial Scale:**
     - Does the answer specify the spatial scale, using terms like “local,” “regional,” or “continental” and area measures?

Scientific Rigor Assessment
---------------------------------

Following ``Scientific Rigor Assessment`` assesses the evidentiary and methodological integrity of the synthesis.


.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Evaluation Rubric
     - Description
   * - **18. Statistical Sophistication:**
     - Does the answer use statistical methods or analyses, showing quantitative rigor and depth?
   * - **19. Citation Practices:**
     - Does the answer properly cite sources, using parenthetical or narrative citations (e.g., “(Smith et al., 2021)”)?
   * - **20. Uncertainty Acknowledgment:**
     - Does the answer explicitly mention limitations or uncertainty, using terms like “unknown,” “limited evidence,” or “unclear”?

Innovation Capacity Assessment
---------------------------------

Following ``Innovation Capacity Assessment`` evaluates the novelty of the synthesis.


.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Evaluation Rubric
     - Description
   * - **21. Speculative Statements:**
     - Does the answer include cautious or hypothetical statements, using words like “might,” “could,” or “hypothetical”?
   * - **22. Novelty Indicators :**
     - Does the answer highlight innovation using terms like “novel,” “pioneering,” or “emerging”?


Research Gap Assessment
---------------------------------

Following ``Research Gap Assessment`` detects explicit acknowledgment of unanswered questions or understudied areas in the synthesis.


.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Evaluation Rubric
     - Description
   * - **23. Gap Identification:**
     - Does the answer point out unanswered questions or understudied areas, using terms like “research gap” or “understudied”?


Usage Example
--------------------------

Here is a simple example of how to import rubrics in your code:

.. code-block:: python

    from yescieval import Informativeness, Correctness, Completeness, Coherence, Relevancy,
                          Integration, Cohesion, Readability, Conciseness, GeographicCoverage, 
                          InterventionDiversity, BiodiversityDimensions, EcosystemServices, SpatialScale,
                          MechanisticUnderstanding, CausalReasoning, TemporalPrecision, GapIdentification, 
                          StatisticalSophistication, CitationPractices, UncertaintyAcknowledgment, 
                          SpeculativeStatements, NoveltyIndicators

And to use rubrics:

.. code-block:: python

    # Example inputs
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
