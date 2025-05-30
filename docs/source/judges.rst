Judges
================

YESciEval provides two pre-trained judge models designed to evaluate scientific text syntheses based on different domains and datasets:

- **Ask Judge**: A multidisciplinary YESciEval judge fine-tuned on the ORKGSyn dataset from the Open Research Knowledge Graph.

- **BioASQ Judge**: A biomedical YESciEval judge fine-tuned on the BioASQ dataset from the BioASQ challenge.

.. hint:: Available YESciEval judge 🤗 Hugging Face:

    - `Ask Judge on Hugging Face <https://huggingface.co/SciKnowOrg/YESciEval-ASK-Llama-3.1-8B>`_
    - `BioASQ Judge on Hugging Face <https://huggingface.co/SciKnowOrg/YESciEval-BioASQ-Llama-3.1-8B>`_


Using YESciEval Judges
------------------------

The following example demonstrates how to create an evaluation rubric, load a judge model, and evaluate an answer.

.. code-block:: python

    from yescieval import Readability, AutoJudge

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
    rubric = Readability(papers=papers, question=question, answer=answer)
    instruction_prompt = rubric.instruct()

    # Step 2: Load the evaluation model (judge)
    judge = AutoJudge()
    judge.from_pretrained(model_id="SciKnowOrg/YESciEval-ASK-Llama-3.1-8B",
                          token="your_huggingface_token",
                          device="cpu")

    # Step 3: Evaluate the answer
    result = judge.evaluate(rubric=rubric)

    print("Raw Evaluation Output:")
    print(result)

Specialized Judges vs. Custom Models
--------------------------------------

.. list-table:: Judge Class Overview
   :header-rows: 1

   * - Class Name
     - Description
   * - AutoJudge
     - Base class for loading and running evaluation models (judges) with PEFT adapters.
   * - AskAutoJudge
     - Multidisciplinary judge tuned on the ORKGSyn dataset from the Open Research Knowledge Graph.
   * - BioASQAutoJudge
     - Biomedical domain judge tuned on the BioASQ dataset from the BioASQ challenge.

The difference between **AskAutoJudge** and **BioASQAutoJudge** compared to **AutoJudge** is that these specialized judges have their own predefined model paths on Hugging Face, making it easier to load the respective domain-specific models.

Custom Judge
--------------------

The `AutoJudge` class provides flexibility to load any compatible LLM model from Hugging Face by specifying the model ID. This allows you to use any pre-trained or fine-tuned model beyond the default specialized judges using YESciEval.

For example, you can load a model and evaluate a rubric like this:

.. code-block:: python

    # Initialize and load a custom model by specifying its Hugging Face model ID
    judge = AutoJudge()
    judge.from_pretrained(model_id="Qwen/Qwen3-8B", device="cpu", token="your_huggingface_token")

    # Evaluate the rubric using the loaded model
    result = judge.evaluate(rubric=rubric)

    print(result)

This approach allows full control over which model is used for evaluation, supporting any LLM..
