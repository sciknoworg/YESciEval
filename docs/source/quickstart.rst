Quickstart
=================

YESciEval is a library designed to evaluate the quality of synthesized scientific answers using predefined rubrics and advanced LLM-based judgment models. This guide walks you through how to evaluate answers based on **informativeness** using a pretrained judge and parse LLM output into structured JSON.


**Example: Evaluating an Answer Using Informativeness + AskAutoJudge**

.. code-block:: python

   from yescieval import Informativeness, AskAutoJudge, GPTParser

   # Sample papers used in form of {"title": "abstract", ... }
   papers = {
       "A Study on AI": "This paper discusses recent advances in artificial intelligence, including deep learning.",
       "Machine Learning Basics": "An overview of supervised learning methods such as decision trees and SVMs.",
       "Neural Networks Explained": "Explains backpropagation and gradient descent for training networks.",
       "Ethics in AI": "Explores ethical concerns in automated decision-making systems.",
       "Applications of AI in Healthcare": "Details how AI improves diagnostics and personalized medicine."
   }

   # Input question and synthesized answer
   question = "How is AI used in modern healthcare systems?"
   answer = (
       "AI is being used in healthcare for diagnosing diseases, predicting patient outcomes, "
       "and assisting in treatment planning. It also supports personalized medicine and medical imaging."
   )

   # Step 1: Create a rubric
   rubric = Informativeness(papers=papers, question=question, answer=answer)
   instruction_prompt = rubric.instruct()

   # Step 2: Load the evaluation model (judge)
   judge = AskAutoJudge()
   judge.from_pretrained(token="your_huggingface_token", device="cpu")

   # Step 3: Evaluate the answer
   result = judge.evaluate(rubric=rubric)

   print("Raw Evaluation Output:")
   print(result)

.. tip::

    - Ensure your Hugging Face model token has access to the model (e.g., ``YESciEval-ASK-Llama-3.1-8B``).
    - Use the ``device="cuda"`` if running on GPU for better performance.
    - Add more rubrics such as ``Informativeness``, ``Relevancy``, etc for multi-criteria evaluation.

**Parsing Raw Output with GPTParser**

If the model outputs unstructured or loosely structured text, you can use GPTParser to parse it into valid JSON.

.. code-block:: python

   from yescieval import GPTParser

   raw_output = "` {rating: `4`, rational: The answer covers key aspects of how AI is applied in healthcare, such as diagnostics and personalized medicine.} `"

   parser = GPTParser(openai_key="your_openai_key")

   parsed = parser.parse(raw_output=raw_output)

   print("Parsed Output:")
   print(parsed)

**Expected Output Format**

.. code-block:: json

   {
     "rating": 4,
     "rationale": "The answer covers key aspects of how AI is applied in healthcare, such as diagnostics and personalized medicine."
   }

.. hint:: Key Components

    +------------------+-------------------------------------------------------+
    | Component        | Purpose                                               |
    +==================+=======================================================+
    | Informativeness  | Defines rubric to evaluate relevance to source papers |
    +------------------+-------------------------------------------------------+
    | AskAutoJudge     | Loads and uses a judgment model to evaluate answers   |
    +------------------+-------------------------------------------------------+
    | GPTParser        | Parses loosely formatted text from LLMs into JSON     |
    +------------------+-------------------------------------------------------+


