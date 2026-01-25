from typing import Dict
from ...base.domain import Domain

vocabulary = {
    "tasks": [
        "classification", "sentiment", "ner", "named entity recognition", "pos", "part of speech", "parsing",
        "constituency parsing", "dependency parsing", "qa", "question answering", "open-domain qa", "closed-book qa",
        "summarization", "abstractive summarization", "extractive summarization", "translation", "machine translation",
        "mt", "retrieval", "dense retrieval", "bm25", "reranking", "re-ranking", "dialogue", "dialog", "conversation",
        "chat", "generation", "text generation", "story generation", "code generation", "coreference",
        "coreference resolution", "slot filling", "nli", "natural language inference", "sts",
        "semantic textual similarity", "entailment"
    ],
    "datasets": [
      "glue", "superglue", "squad", "squad2", "mnli", "qqp", "qnli", "cola", "sst", "sst-2", "stsb", "wmt",
      "cnn/daily mail", "cnn dm", "xsum", "gigaword", "coqa", "hotpotqa", "msmarco", "triviaqa", "belebele", "mmlu",
      "hellaswag", "truthfulqa", "gsm8k", "humaneval", "arc", "piqa", "boolq", "openbookqa"
    ],
    "languages": [
      "english", "german", "deutsch", "french", "spanish", "italian", "chinese", "japanese", "korean", "arabic", "hindi",
      "multilingual", "cross-lingual", "low-resource"
    ],
    "temporal_terms" :[
      "within 2–5 years", "lag of ~6 months", "after 3 months", "before 12 weeks", "1998–2004", "June 2012", "every 2 weeks"
    ],
    "eval_metrics": [
      "accuracy", "f1", "precision", "recall", "bleu", "chrf", "rouge", "meteor", "bertscore", "perplexity",
      "exact match", "em"
    ],
    "arch_terms": [
      "transformer", "encoder-decoder", "decoder-only", "bert", "albert", "roberta", "t5", "gpt", "llama", "mistral",
      "lstm", "gru", "cnn"
    ],
    "training_terms": [
      "pretraining", "fine-tuning", "instruction tuning", "rlhf", "dpo", "lora", "qlora", "quantization",
      "distillation", "curriculum", "data augmentation", "continual learning"
    ],
    "ablation_terms": [
      "ablation", "ablation study", "component analysis", "feature ablation", "module ablation"
    ],
    "compute_terms": [
      "gpu", "tpu", "flops", "parameters", "params", "billion parameters", "inference time", "throughput",
      "latency", "memory footprint"
    ],
    "causal_terms": [
      "because", "due to", "caused by", "results in", "leads to", "triggers", "induces", "therefore", "consequently",
      "as a result", "hence", "thus", "via", "through", "mediates", "modulates", "drives", "regulates"
    ],
    "rigor_stats": [
      "p-value", "p<", "p >", "significant", "confidence interval", "ci", "t-test", "anova", "regression",
      "bootstrap", "cross-validation", "held-out", "standard deviation", "std", "mean", "median"
    ],
    "stats_terms": [
      "p-value", "confidence interval", "t-test", "anova", "regression", "effect size", "variance",
      "standard deviation", "standard error", "r-squared"
    ],
    "uncertainty_terms": [
      "uncertain", "unclear", "unknown"
    ],
    "innovation_terms": [
      "novel", "innovative", "breakthrough", "pioneering", "cutting-edge", "emerging", "frontier", "state-of-the-art",
      "advanced", "experimental", "proof-of-concept", "first", "unprecedented"
    ],
    "speculative_terms": [
      "speculative", "hypothetical", "flagged"
    ],
    "gap_terms": [
      "research gap", "knowledge gap", "data gap"
    ],
    "repro_terms": [
      "open source", "code available", "github", "weights", "checkpoint", "seed", "license", "hyperparameter",
      "learning rate", "batch size"
    ],
    "safety_terms": [
      "bias", "fairness", "toxicity", "privacy", "safety", "data leakage", "red teaming", "harmful content"
    ]
}

example_responses = {
    "Depth": {
        "MechanisticUnderstanding": [
            {
                "rating": "1",
                "rationale": "The response reports results or model performance but does not explain how the model architecture or training process leads to those outcomes."
            },
            {
                "rating": "4",
                "rationale": "The response provides a clear mechanistic explanation of how the model works, describing the role of transformer-based architectures, the effects of pretraining and fine-tuning, and insights from ablation studies that show how specific components contribute to performance."
            }
        ],
        "CausalReasoning": [
            {
                "rating": "1",
                "rationale": "The response reports results or observations but does not provide explicit cause-effect explanations linking methods or design choices to outcomes."
            },
            {
                "rating": "4",
                "rationale": "The response provides structured cause-effect reasoning, explaining how architectural or training choices lead to performance differences, for example noting that improvements occur because certain components modulate information flow, which consequently drives better generalization through specific training mechanisms."
            }
        ],
        "TemporalPrecision": [
            {
                "rating": "1",
                "rationale": "The response mentions time only in broad or unspecific ways and does not provide clear dates, durations, or intervals relevant to the discussion."
            },
            {
                "rating": "4",
                "rationale": "The response includes precise temporal details, such as model behavior observed after 3 months of training, performance changes within 2-5 years of development, or evaluations conducted every 2 weeks, with references to specific time ranges like 1998-2004 or June 2012."
            }
        ]
    }
}

class NLP(Domain):
    examples: Dict[str, Dict]  = example_responses
    vocab: Dict[str, Dict] = vocabulary
    ID: str = 'nlp'
    verbalized: str = "NLP"