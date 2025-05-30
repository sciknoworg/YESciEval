<div align="center">
     <img src="https://raw.githubusercontent.com/sciknoworg/YESciEval/main/images/logo.png" alt="OntoLearner Logo" width="500"/>
</div>

<div align="center">
 <a href="https://badge.fury.io/py/YESciEval"><img src="https://badge.fury.io/py/YESciEval.svg" alt="PyPI version"></a>
 <a href="https://huggingface.co/collections/SciKnowOrg/yescieval-judges-6839d27aac00da416d25ee66"><img src="https://img.shields.io/badge/huggingface-YESciEval-blue?logo=huggingface" alt="YESciEval HF"></a>
 <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
 <a href="https://yescieval.readthedocs.io/"><img src="https://app.readthedocs.org/projects/yescieval/badge/" alt="Documentation Status"></a>


</div>

Large Language Models (LLMs) have become pivotal in powering scientific question-answering across modern search engines, yet their evaluation robustness remains largely underexplored. To address this gap, we introduce **YESciEval** — an open-source framework that leverages fine-grained rubric-based assessments combined with reinforcement learning to reduce optimism bias in LLM evaluators.

YESciEval provides a comprehensive library for evaluating the quality of synthesized scientific answers using predefined rubrics and sophisticated LLM-based judgment models. This framework enables you to assess answers on key criteria by utilizing pretrained judges and parsing LLM outputs into structured JSON formats for detailed analysis.


## Installation

```bash
pip install yescieval
```


## Judges

Specialized Judges within YESciEval are:

| Judge      | Domain                             | Dataset Used                                                                                    | 🤗 Hugging Face                                                                                  |
|----------------|------------------------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| **Ask Judge**  | Multidisciplinary (33 disciplines) | [ORKGSyn (Open Research Knowledge Graph)](https://data.uni-hannover.de/dataset/yescieval-corpus) | [SciKnowOrg/YESciEval-ASK-Llama-3.1-8B](https://huggingface.co/SciKnowOrg/YESciEval-ASK-Llama-3.1-8B)       |
| **BioASQ Judge**| Biomedical                         | [BioASQ](https://data.uni-hannover.de/dataset/yescieval-corpus)                                                                             | [SciKnowOrg/YESciEval-BioASQ-Llama-3.1-8B](https://huggingface.co/SciKnowOrg/YESciEval-BioASQ-Llama-3.1-8B) |


## Quickstart Example

```python
from yescieval import Readability, AutoJudge

# Sample papers
papers = {
    "A Study on AI": "This paper discusses recent advances in artificial intelligence, including deep learning.",
    "Machine Learning Basics": "An overview of supervised learning methods such as decision trees and SVMs.",
    "Neural Networks Explained": "Explains backpropagation and gradient descent for training networks.",
    "Ethics in AI": "Explores ethical concerns in automated decision-making systems.",
    "Applications of AI in Healthcare": "Details how AI improves diagnostics and personalized medicine."
}

# Question and synthesized answer
question = "How is AI used in modern healthcare systems?"
answer = (
    "AI is being used in healthcare for diagnosing diseases, predicting patient outcomes, "
    "and assisting in treatment planning. It also supports personalized medicine and medical imaging."
)

# Step 1: Create a rubric
rubric = Readability(papers=papers, question=question, answer=answer)

# Step 2: Load a judge model (Ask Judge by default)
judge = AutoJudge()
judge.from_pretrained(
    model_id="SciKnowOrg/YESciEval-ASK-Llama-3.1-8B",
    token="your_huggingface_token",
    device="cpu"
)

# Step 3: Evaluate the answer
result = judge.evaluate(rubric=rubric)
print("Raw Evaluation Output:")
print(result)
```

| Class Name        | Description                                                                                  |
| ----------------- | -------------------------------------------------------------------------------------------- |
| `AutoJudge`       | Base class for loading and running evaluation models with PEFT adapters.                     |
| `AskAutoJudge`    | Multidisciplinary judge tuned on the ORKGSyn dataset from the Open Research Knowledge Graph. |
| `BioASQAutoJudge` | Biomedical domain judge tuned on the BioASQ dataset from the BioASQ challenge.               |


## Citation

If you use YESciEval in your research, please cite:

```bibtex
@misc{yescieval2025,
  title={YESciEval: Scientific Text Evaluation with LLM Judges},
  author={Your Name or Organization},
  year={2025},
  howpublished={\url{https://github.com/YourRepo/yescieval}},
}
```


## 📃 License

This work is licensed under a [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT).




