
## 🗃️ ScienceQ&A Dataset

The `dataset/` directory contains data for the **BioASQ** and **ORKG-Synthesis** datasets, organized into `train` and `test` sets. Each set consists of three categories: `adversarial-extreme`, `adversarial-subtle`, and `benign`. The `dataset/` directory structured as follows:
```angular2html
dataset/
├── BioASQ
│   ├── test/
│   │   ├── adversarial_extreme/
│   │   ├── adversarial_subtle/
│   │   ├── original_synthesis/
│   │   ├── BioASQ_dataset_adversarial_extreme_clean.xlsx
│   │   ├── BioASQ_dataset_adversarial_subtle_clean.xlsx
│   │   └── BioASQ_dataset_synthesis.xlsx
│   ├── train/
│   │   ├── adversarial_extreme/
│   │   ├── adversarial_subtle/
│   │   ├── original_synthesis/
│   │   ├── BioASQ_dataset_adversarial_extreme_clean.xlsx
│   │   ├── BioASQ_dataset_adversarial_subtle_clean.xlsx
│   │   └── BioASQ_dataset_synthesis.xlsx
│   └── train_test_split_ids.json
└── ORKG-Synthesis
    ├── test
    │   ├── adversarial_extreme/
    │   ├── adversarial_subtle/
    │   ├── original_synthesis/
    │   ├── llm4syn_dataset_adversarial_extreme_clean.xlsx
    │   ├── llm4syn_dataset_adversarial_subtle_clean.xlsx
    │   ├── llm4syn_dataset_synthesis.xlsx
    │   └── original_synthesis
    ├── train
    │   ├── adversarial_extreme/
    │   ├── adversarial_subtle/
    │   ├── original_synthesis/
    │   ├── llm4syn_dataset_adversarial_extreme_clean.xlsx
    │   ├── llm4syn_dataset_adversarial_subtle_clean.xlsx
    │   └── llm4syn_dataset_synthesis.xlsx
    └── train_test_split_ids.json
```

### 📕 How to run the experimentation?  

**HINT**: Using the YESciEval is an optimal way of doing this.

The first step is to generate adversarial sets using the `generator/` directory. However, these sets are already available in the repository. To fine-tune your judge model, follow these steps:  

1. 🤖 **Supervised Fine-Tuning (SFT):**  Run the supervised fine-tuning model with the following command:  
```cmd
   python supervised_finetuning.py
```
2. 🤖 **Reinforcement Learning (RL)** Fine-Tuning: After completing SFT, continue fine-tuning using reinforcement learning:

```cmd
python reinforcement_learning.py
```
3.   📊 **Inference and Evaluation**: To evaluate and use your judge model, run any of the `*_inference.py` scripts:
```cmd
python your_inference_script.py
```
