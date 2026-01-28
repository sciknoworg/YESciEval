Quickstart
=================

YESciEval is a library designed to evaluate the quality of synthesized scientific answers using predefined rubrics and advanced LLM-based judgment models. This guide walks you through how to evaluate answers based on **informativeness** and **mechanistic understanding** using a pretrained & a custom judge and parse LLM output into structured JSON.


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
   result = judge.judge(rubric=rubric)

   print("Raw Evaluation Output:")
   print(result)

.. tip::

    - Ensure your Hugging Face model token has access to the model (e.g., ``YESciEval-ASK-Llama-3.1-8B``).
    - Use the ``device="cuda"`` if running on GPU for better performance.
    - Add more rubrics such as ``Informativeness``, ``Relevancy``, etc for multi-criteria evaluation.


Customizing Rubric Prompts with Injectors
-----------------------------------------

Injectors allow you to augment rubric prompts with additional guidance, such as example responses or domain-specific vocabulary, to improve evaluation alignment. Each injector is rubric-specific, meaning different rubrics can receive different injected content. They are domain-dependent, so the examples and vocabulary injected are automatically selected based on the domain you specify (e.g., "nlp", "ecology"). Multiple injectors, such as examples and vocabulary, can be used together in a composable way. Available injectors are listed below:

- **Example Injector**: Injects curated example responses for the chosen rubric and domain.
- **Vocabulary Injector**: Injects domain and rubric-specific terminology to guide model reasoning.

**Usage Example**

.. code-block:: python

   rubric = MechanisticUnderstanding(
       papers=papers,
       question=question,
       answer=answer,
       domain="nlp",
       vocabulary=VocabularyInjector(),
       example=ExampleInjector()
   )

In this example, ``VocabularyInjector`` and ``ExampleInjector`` provide content aligned with the NLP domain for the *Mechanistic Understanding* rubric.

**Example Injected Responses for Mechanistic Understanding**

.. code-block:: json

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

**Example Injected Vocabulary for Mechanistic Understanding in the NLP Domain**

.. code-block:: json

   "training_terms": [
      "pretraining", "fine-tuning", "instruction tuning", "rlhf", "dpo", "lora", "qlora", "quantization",
      "distillation", "curriculum", "data augmentation", "continual learning"
   ]

**Example: Evaluating an Answer Using MechanisticUnderstanding + CustomAutoJudge**

.. code-block:: python

   from yescieval import MechanisticUnderstanding, CustomAutoJudge, ExampleInjector, VocabularyInjector

   # Step 1: Create a rubric
   rubric = MechanisticUnderstanding(papers=papers, question=question, answer=answer, domain="nlp", vocabulary=VocabularyInjector(), example=ExampleInjector())
   instruction_prompt = rubric.instruct()

   # Step 2: Load the evaluation model (judge)
   judge = CustomAutoJudge()
   judge.from_pretrained(model_id="Qwen/Qwen3-8B", device="cpu", token="your_huggingface_token")

   # Step 3: Evaluate the answer
   result = judge.judge(rubric=rubric)
   print("Raw Evaluation Output:")
   print(result)



**Parsing Raw Output with GPTParser**

If the model outputs unstructured or loosely structured text, you can use GPTParser to parse it into valid JSON.

.. code-block:: python

   from yescieval import GPTParser

   raw_output = "` {rating: `4`, rational: The answer covers key aspects of how AI is applied in healthcare, such as diagnostics and personalized medicine.} `"

   parser = GPTParser(openai_key="your_openai_key")

   parsed = parser.parse(raw_output=raw_output)

   print("Parsed Output:")
   print(parsed.model_dump())

**Expected Output Format**

.. code-block:: json

   {
     "rating": 4,
     "rationale": "The answer covers key aspects of how AI is applied in healthcare, such as diagnostics and personalized medicine."
   }

The output schema is as a following (if you do not prefer to use ``.model_dump()``) to be able to use like ``result.rating`` to access the rating value or ``result.rationale`` to access the textual explanation for rating.

.. code-block::

	{
		'properties': {
			'rating': {
				'description': 'Rating from 1 to 5',
				'maximum': 5,
				'minimum': 1,
				'title': 'Rating',
				'type': 'integer'
			},
			'rationale': {
				'description': 'Textual explanation for the rating',
				'title': 'Rationale',
				'type': 'string'
			}
		},
		'required': ['rating', 'rationale'],
		'title': 'RubricLikertScale',
		'type': 'object'
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


