
Evaluation Rubrics
===================

A total of nine evaluation rubrics were defined as part of the YESciEval test framework:

**Linguistic & Stylistic Quality** concerns grammar, clarity, and adherence to academic writing conventions.

.. table::

    +--------------------+-------------------------------------------------------------+
    | Evaluation Rubric   | Description                                                 |
    +====================+=============================================================+
    | **1. Cohesion:**    | Are the sentences connected appropriately to make the      |
    |                    | resulting synthesis cohesive?                               |
    +--------------------+-------------------------------------------------------------+
    | **2. Conciseness:** | Is the answer short and clear, without redundant statements?|
    +--------------------+-------------------------------------------------------------+
    | **3. Readability:** | Does the answer follow appropriate style and structure     |
    |                    | conventions for academic writing, particularly for          |
    |                    | readability?                                                |
    +--------------------+-------------------------------------------------------------+

**Logical & Structural Integrity** focuses on the reasoning and organization of information.

+--------------------+-------------------------------------------------------------+
| Evaluation Rubric   | Description                                                 |
+====================+=============================================================+
| **4. Coherence:**   | Are the ideas connected soundly and logically?             |
+--------------------+-------------------------------------------------------------+
| **5. Integration:** | Are the sources structurally and linguistically well-       |
|                    | integrated, using appropriate markers of provenance/        |
|                    | quotation and logical connectors for each reference?        |
+--------------------+-------------------------------------------------------------+
| **6. Relevancy:**   | Is the information in the answer relevant to the problem?  |
+--------------------+-------------------------------------------------------------+

**Content Accuracy & Informativeness** ensures that the response is both correct and useful.

+--------------------+-------------------------------------------------------------+
| Evaluation Rubric   | Description                                                 |
+====================+=============================================================+
| **7. Correctness:** | Is the information in the answer a correct representation   |
|                    | of the content of the provided abstracts?                   |
+--------------------+-------------------------------------------------------------+
| **8. Completeness:**| Is the answer a comprehensive encapsulation of the relevant|
|                    | information in the provided abstracts?                      |
+--------------------+-------------------------------------------------------------+
| **9. Informativeness:**| Is the answer a useful and informative reply to the       |
|                    | problem?                                                    |
+--------------------+-------------------------------------------------------------+


**Usage Example**

Here is a simple example of how to import rubrics in your code:

.. code-block:: python

    from yescieval import Informativeness, Correctness, Completeness,
                          Coherence, Relevancy, Integration,
                          Cohesion, Readability, Conciseness

And to use rubrics:

.. code-block:: python

    # Example inputs
    papers = {
        "Paper 1": "Summary of paper 1 content.",
        "Paper 2": "Summary of paper 2 content.",
        "Paper 3": "Summary of paper 3 content.",
        "Paper 4": "Summary of paper 4 content.",
        "Paper 5": "Summary of paper 5 content."
    }
    question = "What are the key findings on AI in these papers?"
    answer = "The synthesis answer summarizing the papers."

    # Instantiate a rubric, e.g. Coherence
    rubric = Coherence(papers=papers, question=question, answer=answer)
    instruction = rubric.instruct()

    print(instruction)
