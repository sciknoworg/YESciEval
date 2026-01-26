
Rubrics
===================

A total of twelve (12) evaluation rubrics were defined as part of the YESciEval test framework.

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


Usage Example
--------------------------

Here is a simple example of how to import rubrics in your code:

.. code-block:: python

    from yescieval import Informativeness, Correctness, Completeness, Coherence, Relevancy,
                          Integration, Cohesion, Readability, Conciseness,
                          MechanisticUnderstanding, CausalReasoning, TemporalPrecision

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
    rubric = Coherence(papers=papers, question=question, answer=answer, domain="nlp", vocabulary=VocabularyInjector(), example=ExampleInjector())
    instruction = rubric.instruct()

    print(instruction)
    print(rubric.name)
