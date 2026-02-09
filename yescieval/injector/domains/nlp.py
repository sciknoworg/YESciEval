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
      "within 2-5 years", "lag of ~6 months", "after 3 months", "before 12 weeks", "1998-2004", "June 2012", "every 2 weeks"
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
    ],
    "gap_identification": [
      "remains unclear", "unknown", "limited evidence", "mixed results", "understudied", "few studies", "lack of benchmark", "no standard evaluation",
      "dataset bias", "annotation bias", "label noise", "generalization gap", "out-of-distribution", "OOD",
      "low-resource languages", "domain shift", "not evaluated", "unexplored", "open question", "unresolved"
    ],
    "novelty_indicators": [
      "state of the art", "SOTA", "new benchmark", "new dataset", "new architecture", "novel architecture",
      "training objective", "pretraining", "fine-tuning", "instruction tuning", "RLHF", "DPO",
      "retrieval-augmented", "RAG", "agentic", "tool use", "function calling", "multimodal", 
      "vision-language", "few-shot", "zero-shot", "scaling law", "parameter-efficient", "LoRA",
      "distillation", "quantization", "compared to baselines", "outperforms prior work", "improves over", "ablation"
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
    },
    "Breadth": {
        "ContextCoverage": [
            {
                "rating": "1",
                "rationale": "The response focuses entirely on a single NLP task or application setting and does not mention any alternative tasks relevant to the research question."
            },
            {
                "rating": "4",
                "rationale": "The response addresses multiple distinct NLP tasks or application settings and distributes attention across them rather than concentrating on a single task."
            }
        ],
        "MethodCoverage": [
            {
                "rating": "1",
                "rationale": "The response focuses entirely on a single training or modeling approach (e.g., fine-tuning) and does not mention any alternative methods or settings relevant to the research question."
            },
            {
                "rating": "4",
                "rationale": "The response addresses multiple distinct methods or settings, such as pretraining, fine-tuning, instruction tuning, and reinforcement learning from human feedback, rather than concentrating on a single approach."
            }
        ],
        "DimensionCoverage": [
            {
                "rating": "1",
                "rationale": "The response relies on a single evaluation dimension and does not indicate consideration of alternative evaluation perspectives."
            },
            {
                "rating": "4",
                "rationale": "The response evaluates performance across multiple dimensions, using metrics such as accuracy, precision, recall, F1, BLEU, ROUGE, and perplexity, providing a more complete assessment rather than relying on a single metric."
            }
        ],
        "ScopeCoverage": [
            {
                "rating": "1",
                "rationale": "The response is limited to a single, narrowly defined scope and does not indicate that the findings generalize across different linguistic settings or usage scenarios."
            },
            {
                "rating": "4",
                "rationale": "The response covers a wide range of linguistic scopes, including multiple languages such as English, German, French, and Chinese, as well as multilingual, cross-lingual, and low-resource settings, distributing attention across these distinct applicability scopes with only minor omissions."
            }
        ],
        "ScaleCoverage": [
            {
                "rating": "1",
                "rationale": "The response considers only a single computational scale and does not indicate how the approach behaves under different resource or deployment settings."
            },
            {
                "rating": "4",
                "rationale": "The response discusses multiple computational scales, including model size in terms of parameters and billion-parameter regimes, compute resources such as GPUs and TPUs, and efficiency-related aspects like inference time, latency, throughput, and memory footprint, providing a multi-scale perspective."
            }
        ]
    },
    "Gap": {
        "GapIdentification": [
            {
                "rating": "1",
                "rationale": "The response is purely descriptive, summarizing existing findings or benchmark results (e.g., model architectures, datasets, or reported scores) with no identification of missing, unknown, inconsistent, or unresolved aspects relevant to the research question."
            },
            {
                "rating": "4",
                "rationale": "The response clearly identifies specific gaps or limitations in the evidence base that are relevant to the research question (e.g., missing evaluations, underexplored domains or tasks, lack of ablation studies, limited robustness or generalization analysis, dataset biases, or conflicting benchmark results) and provides some explanation of why these gaps matter; minor ambiguity or imprecision may remain."
            }
        ]
    },
    "Innovation": {
        "StateOfTheArtAndNovelty": [
            {
                "rating": "1",
                "rationale": "The response gives a generic overview of common NLP methods without identifying any specific state-of-the-art systems or novel contributions; or it uses buzzwords like SOTA or state of the art without explaining what is new."
            },
            {
                "rating": "4",
                "rationale": "The response identifies concrete state-of-the-art or novel NLP contributions (e.g., a new dataset or benchmark, a new or modified model architecture, RAG, instruction tuning, RLHF/DPO, multimodal models, or parameter-efficient methods like LoRA) and briefly explains what improvement or new capability they provide, with minor gaps in comparison or detail."
            }
        ]
    }
}

vocab_block_specs = {
    "mechanistic_vocab_block": {"label": "Mechanistic terms", "keys": ["training_terms", "arch_terms", "ablation_terms"]},
    "causal_vocab_block": {"label": "Causal connectives / triggers", "keys": ["causal_terms"]},
    "temporal_vocab_block": {"label": "Temporal expressions", "keys": ["temporal_terms"]},
    "context_coverage_vocab_block": {"label": "Context Coverage", "keys": ["tasks"]},
    "method_coverage_vocab_block": {"label": "Method Coverage", "keys": ["training_terms", "arch_terms"]},
    "dimension_coverage_vocab_block": {"label": "Dimension Coverage", "keys": ["eval_metrics"]},
    "scope_coverage_vocab_block": {"label": "Scope Coverage", "keys": ["languages"]},
    "scale_coverage_vocab_block": {"label": "Scale Coverage", "keys": ["compute_terms"]},
    "gap_identification_vocab_block": {"label": "Gap Identification", "keys": ["gap_identification"]},
    "novelty_indicators_vocab_block": {"label": "State of the Art and Novelty Indicators", "keys": ["novelty_indicators"]}
}

class NLP(Domain):
    examples: Dict[str, Dict]  = example_responses
    vocab: Dict[str, Dict] = vocabulary
    ID: str = 'nlp'
    verbalized: str = "NLP"
    vocab_block_specs: Dict[str, Dict[str, object]] = vocab_block_specs
