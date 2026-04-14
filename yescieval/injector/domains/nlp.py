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
    ],
    "epistemic_calibration": [
        "may", "might", "could", "possibly", "potentially", "plausibly", "suggests", "consistent with", "unlikely", "likely",
        "uncertain", "inconclusive", "mixed evidence", "limited evidence", "assumption", "we assume", "hypothesis", "speculate",
        "extrapolate", "understudied", "warrants further research", "future work", "limitation", "caveat", "confounding", "bias"
    ],
    "quant_uncertainty_vocab": [
        "mean", "median", "standard deviation", "std", "standard error", "SE", "confidence interval", "CI", "bootstrap",
        "p-value", "paired t-test", "McNemar", "Wilcoxon", "cross-validation", "held-out", "train/dev/test",
        "across seeds", "random seed", "mean±std", "ablation", "robustness", "OOD"
    ],
    "uncertainty_terms": [
        "uncertain", "unclear", "unknown", "not known", "not clear", "poorly understood",
        "remains unclear", "remains unknown", "open question", "open problem",
        "inconclusive", "ambiguous", "lack of evidence", "limited evidence",
        "insufficient data", "data is limited", "not well understood", "not fully understood",
        "hard to determine", "difficult to assess"
    ]
}

example_responses = {
    "pointwise": {
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
        },
        "Rigor": {
            "EpistemicCalibration": [
                {
                    "rating": "1",
                    "rationale": "The response presents claims as definitive throughout, with no meaningful qualification, uncertainty marking, or acknowledgment of assumptions/limitations, even when such caution is warranted."
                },
                {
                    "rating": "4",
                    "rationale": "The response generally calibrates claim strength, distinguishing supported results from uncertain ones (e.g., performance improves on English benchmarks, but generalization to multilingual settings remains unclear due to limited evaluation), with only minor vague hedging in a few places."
                }   
            ],
            "QuantitativeEvidenceAndUncertainty": [
                {
                    "rating": "1",
                    "rationale": "The response does not provide any quantitative evidence or statistical analysis to support claims, and it does not acknowledge uncertainty or variability in the results."
                },
                {
                    "rating": "4",
                    "rationale": "The response appropriately uses quantitative results (e.g., reports F1 score improvements over baselines and notes variance across datasets) and connects them to the research question; it also acknowledges uncertainty and limitations (e.g., performance drops on out-of-domain data and results are based on a limited set of benchmarks), with only minor gaps in cross-study comparison or robustness analysis."
                }
            ],
            "ExplicitUncertainty": [
                {
                    "rating": "1",
                    "rationale": "The response does not explicitly acknowledge any uncertainty, unknowns, or open questions related to the research question; it presents findings as definitive and well-established."
                },
                {
                    "rating": "4",
                    "rationale": "The response explicitly acknowledges uncertainty, unknowns, or open questions related to the research question; it uses clear language to indicate what is not known or understood, and it highlights areas where evidence is limited or inconclusive, with only minor gaps in explicit acknowledgment of uncertainty."
                }  
            ]   
        }
 },
    "pairwise": { 
        "Depth": {
            "MechanisticUnderstanding": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response reports NLP model outputs or benchmark scores but does not explain how components such as attention mechanisms, embeddings, or training objectives produce those results."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response explains how transformer components like self-attention, positional encoding, and layer normalization interact during forward and backward passes, and how pretraining objectives and fine-tuning shape representation learning and downstream task performance."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response describes improvements in NLP tasks such as translation or classification without explaining the internal processes or architectural factors responsible for those improvements."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response traces how tokenization, embedding spaces, and multi-head attention enable contextual representation, and explains how gradient updates during fine-tuning adjust weights to capture task-specific linguistic patterns."
                    }
                ]
            },
            "CausalReasoning": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response presents correlations between model design choices and performance metrics but does not explain causal relationships between them."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response explicitly explains how increasing model depth or attention heads improves context modeling, which in turn leads to better sequence understanding and higher task accuracy."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response lists observed improvements in NLP benchmarks without establishing how specific training or architectural decisions caused those changes."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response uses clear cause-effect reasoning to show how pretraining on large corpora enables transfer learning, which subsequently improves performance on low-resource downstream tasks due to richer contextual representations."
                    }
                ]
            },
            "TemporalPrecision": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response refers to training or evaluation timeframes vaguely, such as after training or over time, without specifying exact durations or intervals."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response specifies detailed timelines, such as training conducted over 3 epochs lasting 48 hours, with evaluations every 1,000 steps and fine-tuning completed within a 2-week period."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response describes temporal aspects of model development or evaluation in general terms like early stages or later phases without concrete timing details."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response provides precise temporal markers, such as pretraining performed between January and March 2023, followed by fine-tuning over 10 days and evaluation checkpoints recorded every 500 iterations."
                    }
                ]
            }
        },
        "Breadth": {
            "ContextCoverage": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response focuses exclusively on a single NLP task (e.g., machine translation) and does not reference any other related tasks or application settings such as summarization, question answering, or sentiment analysis, resulting in very limited contextual breadth."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response covers multiple NLP tasks and application settings, such as machine translation, text summarization, question answering, and sentiment analysis, and distributes discussion across them rather than concentrating on a single task."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response is restricted to one specific NLP application setting (e.g., named entity recognition in a single domain) and does not consider alternative NLP tasks or broader application contexts, leading to narrow contextual coverage."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response spans multiple NLP application settings across different problem types, including sequence labeling tasks (e.g., NER), generation tasks (e.g., summarization), and understanding tasks (e.g., question answering), demonstrating broad contextual coverage across NLP."
                    }
                ]
            },
            "MethodCoverage": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response relies exclusively on a single NLP modeling approach, such as fine-tuning a pretrained transformer, without considering alternative training paradigms or learning strategies relevant to the task."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response covers multiple NLP training and modeling approaches, including pretraining, supervised fine-tuning, instruction tuning, transfer learning, and reinforcement learning from human feedback, demonstrating broad methodological coverage."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response is limited to a single modeling strategy, such as zero-shot prompting with a large language model, and does not consider other training or adaptation methods, resulting in narrow methodological breadth."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response integrates a diverse set of NLP methods, including pretraining, fine-tuning, instruction tuning, parameter-efficient fine-tuning (e.g., LoRA/adapters), and reinforcement learning from human feedback, and contrasts their roles across different NLP tasks."
                    }
                ]
            },
            "DimensionCoverage": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response evaluates model performance using only a single evaluation metric, such as accuracy, without considering other NLP evaluation dimensions like precision, recall, F1-score, or generation quality metrics."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response evaluates model performance across multiple NLP evaluation dimensions, including classification metrics (accuracy, precision, recall, F1-score) and generation metrics (BLEU, ROUGE, perplexity), providing a broader assessment of model quality."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response relies on a single evaluation perspective, such as BLEU score for all tasks, without incorporating complementary evaluation dimensions or task-specific metrics."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response integrates multiple evaluation dimensions across NLP tasks, including token-level metrics (precision, recall, F1), sequence-level metrics (BLEU, ROUGE), and probabilistic measures (perplexity), offering a comprehensive multi-perspective evaluation."
                    }
                ]
            },
            "ScopeCoverage": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response is limited to a single linguistic setting, such as evaluating only English-language NLP data, and does not consider how the findings generalize to other languages or cross-lingual scenarios."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response covers multiple linguistic scopes, including high-resource languages (e.g., English and German), medium-resource languages (e.g., French), and low-resource settings, as well as multilingual and cross-lingual transfer scenarios, demonstrating broad applicability across language conditions."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response is restricted to a single language and domain setting (e.g., English news classification) and does not explore performance variation across other linguistic or domain-specific contexts, resulting in narrow scope coverage."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response spans diverse linguistic and domain scopes, including multiple languages (e.g., English, German, French, and Chinese), different domains (e.g., news, biomedical, and social media text), and cross-lingual transfer settings, reflecting comprehensive scope coverage."
                    }
                ]
            },
            "ScaleCoverage": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response considers only a single computational scale, such as evaluating a fixed-size language model under one deployment setting, without examining how performance varies with model size or computational constraints."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response covers multiple computational scales in NLP, including small, medium, and large language models, and analyzes how performance and efficiency change with model size, compute resources (e.g., GPUs/TPUs), and deployment constraints such as latency and memory usage."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response evaluates the model under a single inference setting, such as cloud-based deployment only, without considering other computational environments or scaling conditions."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response integrates multiple computational scales in NLP, including training-scale variation (small vs. large parameter models), deployment environments (edge devices, cloud servers), and efficiency considerations such as throughput, latency, and memory consumption across these settings."
                    }
                ]
            }
}        
        
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
    "novelty_indicators_vocab_block": {"label": "State of the Art and Novelty Indicators", "keys": ["novelty_indicators"]},
    "epistemic_calibration_vocab_block": {"label": "Epistemic Calibration", "keys": ["epistemic_calibration"]},
    "quant_uncertainty_vocab_block": {"label": "Quantitative Evidence and Uncertainty", "keys": ["quant_uncertainty_vocab"]},
    "uncertainty_vocab_block": {"label": "Explicit Uncertainty", "keys": ["uncertainty_terms"]}
}

class NLP(Domain):
    examples: Dict[str, Dict] = example_responses
    vocab: Dict[str, Dict] = vocabulary
    ID: str = 'nlp'
    verbalized: str = "NLP"
    vocab_block_specs: Dict[str, Dict[str, object]] = vocab_block_specs
