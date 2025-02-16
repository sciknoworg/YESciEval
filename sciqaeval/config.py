from dotenv import find_dotenv, load_dotenv
import os

_ = load_dotenv(find_dotenv())

test_size = 0.3

evaluator = "meta-llama-3.1-8b-instruct"

evaluator_model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"

synthesizers = [
    "meta-llama-3.1-8b-instruct",
    "meta-llama-3.1-70b-instruct",
    "qwen2.5-72b-instruct",
    "mistral-large-instruct"
]

root_dir = "dataset"

papers_no = 5

paper_no_bioasqa = 14

openai_key = os.environ['OPENAI_KEY']
huggingface_key = os.environ['HUGGINGFACE_ACCESS_TOKEN']

criteria = ['Coherence', 
            'Cohesion', 
            'Completeness',
            'Conciseness', 
            'Correctness',
            'Informativeness', 
            'Integration', 
            'Readability', 
            'Relevancy']

# datasets_path = {
#     "bioasq-test":"dataset/BioASQ/BioASQ-test-refactored-dataset.json",
#     "bioasq-train":"dataset/BioASQ/BioASQ-train-refactored-dataset.json",
#     "orkg-synthesis-test": "dataset/ORKG-Synthesis/llm4syn-test-refactored-dataset.json",
#     "orkg-synthesis-train": "dataset/ORKG-Synthesis/llm4syn-train-refactored-dataset.json",   
# }

datasets_path = {
    "bioasq-test":"dataset/BioASQ/BioASQ-test-refactored-dataset.json",
    "bioasq-train-llama":"dataset/BioASQ/BioASQ-train-refactored-dataset.json",
    "bioasq-combined":"dataset/BioASQ/BioASQ_train_combined_refactored_dataset.json",
    "bioasq-adv": "dataset/BioASQ/BioASQ_ADV_train_combined_refactored_dataset.json",
    "bioasq-org": "dataset/BioASQ/BioASQ_ORG_train_combined_refactored_dataset.json",
    "bioasq-rlhf-adv": "dataset/BioASQ/BioASQ_RLHF_train_combined_refactored_dataset.json",
    "bioasq-rlhf-adv-org": "dataset/BioASQ/BioASQ_RLHF_ADV+ORG_train_combined_refactored_dataset.json",
    
    "orkg-synthesis-test": "dataset/ORKG-Synthesis/llm4syn-test-refactored-dataset.json",
    "orkg-synthesis-train-llama": "dataset/ORKG-Synthesis/llm4syn-train-refactored-dataset.json",   
    "orkg-synthesis-combined": "dataset/ORKG-Synthesis/llm4syn_train_combined_refactored_dataset.json",
    "orkg-synthesis-adv": "dataset/ORKG-Synthesis/llm4syn_ADV_train_combined_refactored_dataset.json",
    "orkg-synthesis-org": "dataset/ORKG-Synthesis/llm4syn_ORG_train_combined_refactored_dataset.json",
    "orkg-synthesis-rlhf-adv": "dataset/ORKG-Synthesis/llm4syn_RLHF_train_combined_refactored_dataset.json",
    "orkg-synthesis-rlhf-adv-org": "dataset/ORKG-Synthesis/llm4syn_RLHF_ADV+ORG_train_combined_refactored_dataset.json"
}


datasets_train_path = {
    "bioasq": [f"dataset/BioASQ/BioASQ_train_{synthesizer}_refactored_dataset.json" for synthesizer in synthesizers],
    "orkg-synthesis": [f"dataset/ORKG-Synthesis/llm4syn_train_{synthesizer}_refactored_dataset.json" for synthesizer in synthesizers]
}

desirable_adv_rating_thresholds = {
    "extreme": 1,
    "subtle": 3,
    "original": 5
}