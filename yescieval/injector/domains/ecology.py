from typing import Dict
from ...base.domain import Domain

vocabulary = {
    "regions": [
        "Europe", "North America", "South America", "Asia", "Africa", "Australia", "Mediterranean", "Alpine",
        "Tropical", "Arctic", "Boreal", "Temperate", "Subtropical", "Arid", "Wetland", "Coastal", "Marine",
        "Freshwater", "Terrestrial", "Montane", "Savanna", "Tundra", "Desert", "Grassland", "Rainforest",
        "Riparian", "Peatland", "Mangrove", "Coral reef"
    ],
    "interventions": [
        "fertilizer", "stocking", "mowing", "grazing", "irrigation", "organic", "controlled burn", "prescribed burn",
        "restoration", "reforestation", "afforestation", "rewilding", "habitat creation", "invasive species control",
        "predator control", "captive breeding", "protected area", "translocation", "assisted migration", "biochar",
        "liming", "mulching", "cover cropping", "selective logging", "thinning", "buffer strips", "fencing",
        "corridor", "wetland creation"
    ],
    "mechanistic_terms": [
        "mechanism", "pathway", "feedback", "trophic", "nutrient cycling", "energy flow", "predation", "competition",
        "mutualism", "facilitation", "inhibition", "succession", "disturbance", "resilience", "adaptation",
        "selection pressure", "gene flow", "decomposition", "mineralization", "nitrification", "photosynthesis",
        "respiration", "herbivory", "allelopathy", "keystone", "hysteresis", "tipping point"
    ],
    "diversity_dimensions": [
        "taxonomic", "functional", "phylogenetic", "alpha", "beta", "gamma", "species richness", "evenness",
        "dominance", "endemism", "rarity", "abundance", "biomass", "density", "coverage", "trait diversity",
        "genetic diversity", "structural diversity", "shannon", "simpson", "hill numbers"
    ],
    "temporal_terms" :[
        "within 2-5 years", "lag of ~6 months", "after 3 months", "before 12 weeks", "1998-2004",
        "June 2012", "every 2 weeks"
    ],
    "ecosystem_services": [
        "provisioning", "regulating", "supporting", "cultural", "carbon sequestration", "pollination", "pest control",
        "water purification", "soil formation", "nutrient retention", "climate regulation", "flood control",
        "erosion control", "recreation", "aesthetic value", "food production", "timber", "fiber", "fuel",
        "genetic resources", "biochemicals", "fresh water"
    ],
    "scale_terms": ["individual", "population", "community", "ecosystem", "landscape", "patch", "local", "regional", "global"],
    "causal_terms": [
        "because", "due to", "caused by", "results in", "leads to", "triggers", "induces", "therefore", "consequently",
        "as a result", "hence", "thus", "accordingly", "owing to", "through", "via", "by means of",
        "mediates", "modulates", "drives", "regulates"
    ],
    "innovation_terms": [
        "novel", "innovative", "breakthrough", "pioneering", "cutting-edge",
        "emerging", "frontier", "state-of-the-art", "advanced", "experimental",
        "proof-of-concept", "first", "unprecedented"
    ],
    "speculative_terms": ["speculative", "hypothetical", "flagged"],
    "gap_terms": ["research gap", "knowledge gap", "data gap"],
    "stats_terms": [
        "mean", "median", "variance", "standard deviation", "standard error", "confidence interval", "ci",
        "p-value", "significant", "regression", "anova", "t-test", "chi-square", "effect size", "meta-analysis",
        "model comparison", "r-squared"
    ],
    "conservation_terms": [
        "endangered", "extinction", "habitat loss", "fragmentation", "restoration", "landscape connectivity", "corridor", "buffer zone"
    ],
    "climate_terms": [
        "climate change", "global warming", "drought", "heatwave", "extreme weather", "phenology", "range shift",
        "sea level rise", "ocean acidification", "greenhouse gas", "carbon dioxide", "thermal stress", "precipitation"
    ],
    "complexity_terms": ["nonlinear", "emergent", "synergistic", "interconnected", "complex", "multifaceted"],
    "gap_identification": [
        "remains unclear", "unknown", "not well understood", "limited evidence", "mixed findings", "inconsistent results", "lack of consensus",
        "understudied", "data scarce", "few studies", "limited sample size", "short time horizon", "lack of longitudinal data",
        "geographic bias", "taxonomic bias", "context dependence", "limited external validity", "missing comparison", "unresolved"
    ],
    "novelty_indicators": [
        "first to", "novel", "new approach", "new method", "recent advances", "state of the art", "cutting-edge",
        "proof-of-concept", "pilot study", "new dataset", "long-term dataset", "high-resolution data",
        "remote sensing", "satellite", "LiDAR", "eDNA", "metabarcoding", "new sampling protocol", "new monitoring approach",
        "hierarchical model", "Bayesian", "causal inference", "counterfactual", "difference-in-differences", "instrumental variable",
        "meta-analysis", "systematic review", "scenario analysis", "climate projection", "compared to previous studies",
        "unlike prior work", "addresses a limitation"
    ],
    "epistemic_calibration": [
        "may", "might", "could", "possibly", "potentially", "plausibly", "suggests", "consistent with", "unlikely", "likely",
        "uncertain", "inconclusive", "mixed evidence", "limited evidence", "assumption", "we assume", "hypothesis", "speculate",
        "extrapolate", "understudied", "warrants further research", "future work", "limitation", "caveat", "confounding", "bias"
    ],
    "quant_uncertainty_vocab": [
        "effect size", "odds ratio", "risk ratio", "hazard ratio", "confidence interval", "CI", "credible interval",
        "standard error", "SE", "standard deviation", "SD", "variance", "p-value", "sample size", "n =",
        "regression", "mixed-effects", "random effects", "GLMM", "AIC", "model comparison", "R-squared",
        "meta-analysis", "heterogeneity", "I-squared", "sensitivity analysis"
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
                    "rationale": "The response mainly describes outcomes or observations and does not explain the underlying mechanisms or processes driving them."
                },
                {
                    "rating": "4",
                    "rationale": "The response explains ecological mechanisms by describing pathways and feedbacks such as nutrient cycling and energy flow, and how interactions like predation, competition, and mutualism influence ecosystem dynamics, resilience, and responses to disturbance."
                }
            ],
            "CausalReasoning": [
                {
                    "rating": "1",
                    "rationale": "The response describes ecological patterns or outcomes but does not clearly explain why they occur or how one factor leads to another."
                },
                {
                    "rating": "4",
                    "rationale": "The response presents clear cause-effect reasoning, explaining how changes in ecological factors drive outcomes, for example describing how disturbances lead to shifts in community structure, which consequently regulate ecosystem processes through specific mediating interactions."
                }
            ],
            "TemporalPrecision": [
                {
                    "rating": "1",
                    "rationale": "The response refers to timing only in vague terms, such as long-term or historical trends, without specifying concrete dates, durations, or time intervals."
                },
                {
                    "rating": "4",
                    "rationale": "The response uses specific and bounded temporal expressions, for example describing changes occurring within 2-5 years, after 3 months, or every 2 weeks, and referencing defined time periods such as 1998-2004 or June 2012."
                }
            ]
        },
        "Breadth": {
            "ContextCoverage": [
                {
                    "rating": "1",
                    "rationale": "The response discusses only a single ecological setting and does not reference any alternative regions or biomes relevant to the research question."
                },
                {
                    "rating": "4",
                    "rationale": "The response covers multiple distinct ecological contexts, such as different regions and ecosystem types, and distributes attention across them rather than focusing on a single setting."
                }
            ],
            "MethodCoverage": [
                {
                    "rating": "1",
                    "rationale": "The response focuses exclusively on a single management or intervention approach (e.g., controlled burning) and does not reference any alternative methods relevant to the research question."
                },
                {
                    "rating": "4",
                    "rationale": "The response discusses multiple distinct interventions or management approaches, such as controlled burning, grazing management, habitat restoration, and protected areas, distributing attention across them rather than focusing on a single method."
                }
            ],
            "DimensionCoverage": [
                {
                    "rating": "1",
                    "rationale": "The response focuses on a single ecological dimension and does not meaningfully address other relevant dimensions."
                },
                {
                    "rating": "4",
                    "rationale": "The response covers multiple ecological dimensions, including taxonomic, functional, and phylogenetic diversity, as well as measures such as species richness, evenness, abundance, and genetic and structural diversity, rather than focusing on just one single dimension."
                }
            ],
            "ScopeCoverage": [
                {
                    "rating": "1",
                    "rationale": "The response addresses only a very narrow aspect of ecological impact and remains vague, providing little indication that the findings apply beyond a single, limited scope."
                },
                {
                    "rating": "4",
                    "rationale": "The response discusses several types of ecosystem services, from provisioning and regulating services to supporting and cultural services, rather than focusing on just one single, limited scope"
                }
            ],
            "ScaleCoverage": [
                {
                    "rating": "1",
                    "rationale": "The response focuses on a single ecological scale and does not meaningfully consider how the findings apply at other relevant scales."
                },
                {
                    "rating": "4",
                    "rationale": "The response addresses multiple ecological scales, ranging from the individual and population level to community and ecosystem scales, and also considers broader spatial scales such as local, regional, and global contexts, rather than focusing on just one scale."
                }
            ]
        },
        "Gap": {
            "GapIdentification": [
                {
                    "rating": "1",
                    "rationale": "The response is purely descriptive, summarizing existing ecological findings, observations, or reported patterns (e.g., species distributions, biodiversity metrics, or observed correlations) without identifying any missing, unknown, inconsistent, or unresolved aspects relevant to the research question."
                },
                {
                    "rating": "4",
                    "rationale": "The response clearly identifies specific gaps or limitations in the ecological evidence base that are relevant to the research question (e.g., missing data for certain regions, taxa, or time periods; limited experimental studies; or conflicting empirical findings) and provides some explanation of why these gaps matter; minor ambiguity or imprecision may remain."
                }
            ]
        },
        "Innovation": {
            "StateOfTheArtAndNovelty": [
                {
                    "rating": "1",
                    "rationale": "The response gives a generic overview of known ecological findings or methods without identifying any specific state-of-the-art approaches or novel contributions; or it uses buzzwords like state of the art or cutting-edge without explaining what is new."
                },
                {
                    "rating": "4",
                    "rationale": "The response identifies concrete state-of-the-art or novel ecological contributions (e.g., new datasets, long-term or high-resolution data, remote sensing such as satellite or LiDAR, eDNA/metabarcoding, or new modeling or monitoring approaches) and briefly explains what improvement or new capability they provide, with minor gaps in comparison or detail."
                }
            ]
        },
        "Rigor": { 
            "EpistemicCalibration": [ 
                {
                    "rating": "1",
                    "rationale": "The response makes strong claims about ecological findings or implications without acknowledging any uncertainty, limitations, assumptions, or alternative explanations."
                },
                {
                    "rating": "4",
                    "rationale": "The response demonstrates good epistemic calibration by acknowledging uncertainty, limitations, assumptions, and alternative explanations relevant to the ecological findings or implications, uses appropriately qualified language; minor gaps or occasional vague hedging may remain."
                }
            ],
            "QuantitativeEvidenceAndUncertainty": [
                {
                    "rating": "1",
                    "rationale": "The response summarizes ecological patterns in qualitative terms (e.g., species declined or abundance increased) without providing or interpreting any quantitative measures such as population change rates, effect sizes, or variability, and does not address uncertainty, sampling limitations, or heterogeneity across sites."
                },
                {
                    "rating": "4",
                    "rationale": "The response uses relevant quantitative evidence (e.g., percentage changes in population abundance, reported confidence intervals, or variation across sites) and links these to the research question; it discusses uncertainty and limitations (e.g., short time series, site-specific variability, or mixed results across studies) and avoids overgeneralization, with only minor gaps in robustness or comparability discussion."
                }      
            ],
            "ExplicitUncertainty": [ 
                {
                    "rating": "1",
                    "rationale": "The response does not explicitly acknowledge any uncertainty, limitations, or assumptions related to the ecological findings or implications."
                },
                {
                    "rating": "4",
                    "rationale": "The response explicitly acknowledges uncertainty, limitations, and assumptions related to the ecological findings or implications, using clear language to identify areas of ambiguity, unresolved questions, or potential confounding factors."
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
                        "rationale": "The response lists observed changes in species abundance or community composition but does not explain the ecological processes or mechanisms responsible for those changes."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response explains how trophic interactions and nutrient cycling feedbacks drive changes in community structure, linking predation pressure and competition to shifts in ecosystem resilience and energy flow."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response describes the outcomes of an ecological intervention but offers no explanation of the biological or physical pathways through which those outcomes arise."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response traces the mechanistic pathway from disturbance through successional stages, describing how facilitation and inhibition among species regulate decomposition, mineralization, and the restoration of ecosystem function."
                    }
                ]
            },
            "CausalReasoning": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response notes associations between ecological variables but does not articulate any causal direction or explain how one factor produces or constrains another."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response explicitly states how reductions in keystone predator populations trigger trophic cascades, which consequently lead to overgrazing, soil erosion, and loss of structural diversity."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response describes co-occurring ecological trends without establishing whether or how they are causally linked."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response uses causal language to explain how altered hydrological regimes drive changes in nutrient retention, which in turn modulates primary productivity and regulates downstream water quality."
                    }
                ]
            },
            "TemporalPrecision": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response refers only to broad timescales such as over decades or in recent years without specifying any concrete dates, durations, or intervals."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response anchors ecological changes to defined periods, noting that recovery was observed within 2-5 years post-restoration and that monitoring was conducted every 2 weeks between 1998 and 2004."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response describes temporal dynamics in qualitative terms only, such as gradual or rapid change, without providing any specific dates or time intervals."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response specifies that population recovery lagged approximately 6 months behind habitat restoration and references a defined monitoring window beginning in June 2012 and running for 12 weeks post-intervention."
                    }
                ]
            }
        },
        "Breadth": {
            "ContextCoverage": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response is narrowly scoped to a single ecological context (e.g., one biome or geographic region) and does not acknowledge variation across other relevant ecosystems, limiting its applicability to broader ecological conditions."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response spans multiple ecological contexts, incorporating examples from different biomes (e.g., tropical, temperate, and arid systems) and geographic regions, demonstrating an effort to generalize findings across diverse environmental settings."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response focuses on a localized or case-specific ecological scenario without extending the discussion to comparable systems or alternative environmental conditions, resulting in minimal contextual breadth."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response integrates a wide range of ecological settings, including variations in climate zones, habitat types, and spatial scales, and explicitly contrasts these contexts to highlight differences and commonalities."
                    }
                ]
            },
            "MethodCoverage": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response is restricted to a single ecological intervention or management strategy (e.g., only habitat restoration) and does not acknowledge alternative methods, limiting the scope of possible approaches relevant to the problem."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response covers a diverse set of ecological methods, including multiple intervention strategies (e.g., restoration, conservation zoning, species reintroduction, and land-use management), demonstrating broad awareness of different approaches applicable across ecological contexts."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response centers on one specific methodological approach without considering other viable ecological interventions or management strategies, resulting in a narrow and methodologically limited perspective."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response incorporates a wide spectrum of ecological methods and not only lists them but also differentiates their roles, trade-offs, and suitability across scenarios (e.g., comparing passive vs. active restoration, or policy-based vs. field-based interventions), reflecting comprehensive methodological breadth."
                    }
                ]
            },
            "DimensionCoverage": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response is limited to a single ecological dimension (e.g., only species richness) and does not extend the analysis to other relevant dimensions such as functional traits, genetic variation, or ecosystem structure, resulting in a narrow perspective."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response addresses multiple ecological dimensions, including taxonomic, functional, and structural aspects of biodiversity (e.g., species richness, trait diversity, and habitat complexity), demonstrating broad consideration of different ways ecological systems can be characterized."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response focuses exclusively on one dimension of ecological analysis without incorporating complementary dimensions, thereby overlooking the multidimensional nature of ecological systems."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response integrates a comprehensive set of ecological dimensions—such as taxonomic, functional, phylogenetic, and genetic diversity—and explicitly relates them to different ecological processes and scales, highlighting their complementary roles in understanding ecosystem complexity."
                    }
                ]
            },
            "ScopeCoverage": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response is confined to a narrowly defined aspect of ecological impact (e.g., a single ecosystem service or outcome) and does not extend the discussion to broader system-level implications, limiting its overall scope."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response spans a broad range of ecological impacts, covering multiple categories of ecosystem services (e.g., provisioning, regulating, and supporting) and demonstrating awareness of diverse ecological outcomes beyond a single focus area."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response addresses a highly specific or localized ecological outcome without situating it within a wider set of impacts or system-level considerations, resulting in minimal scope coverage."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response adopts a wide ecological scope by integrating multiple types of ecosystem services (provisioning, regulating, supporting, and cultural) and explicitly linking them to broader ecological and socio-ecological systems, reflecting comprehensive coverage of impacts."
                    }
                ]
            },
            "ScaleCoverage": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response is limited to a single ecological scale (e.g., only population-level dynamics) and does not consider how processes or patterns may differ across other biological or spatial scales, resulting in restricted breadth."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response encompasses multiple ecological scales, including organismal, population, community, and ecosystem levels, as well as different spatial extents (e.g., local and regional), demonstrating broad coverage across scales."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response focuses narrowly on one scale of analysis without acknowledging cross-scale interactions or broader spatial and temporal dimensions, limiting its overall scope."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response integrates a wide range of ecological scales—from individual to ecosystem and from local to global—and explicitly considers cross-scale interactions and temporal dynamics (e.g., short-term vs. long-term processes), reflecting comprehensive scale coverage."
                    }
                ]
            }
        },
        "Rigor": {
            "EpistemicCalibration": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response makes strong, unqualified claims about ecological findings or implications without acknowledging any uncertainty, limitations, assumptions, or alternative explanations. No hedging language is used, and the response presents contested or context-dependent ecological conclusions as established fact."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response demonstrates good epistemic calibration by acknowledging uncertainty, limitations, assumptions, and alternative explanations relevant to the ecological findings or implications. It uses appropriately qualified language (e.g., 'evidence suggests,' 'under these conditions,' 'one possible explanation') when discussing population dynamics, species interactions, or environmental impacts, though minor gaps or occasional vague hedging may remain."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response presents ecological claims with unwarranted confidence, asserting definitive cause-effect relationships between species populations and environmental factors without acknowledging data limitations, methodological assumptions, or competing explanations, giving the impression that findings are more settled than they are."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response is well-calibrated, consistently qualifying ecological claims with appropriate uncertainty (e.g., 'current evidence indicates,' 'this may vary by context,' 'alternative mechanisms could include') and acknowledging the limitations of cited studies or models. Cross-scale and context-dependent nuances are noted where relevant, with only minor instances of vague or missing hedging."
                    }
                ]
            },
            "QuantitativeEvidenceAndUncertainty": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response summarizes ecological patterns in purely qualitative terms (e.g., 'species declined' or 'abundance increased') without providing or interpreting any quantitative measures such as population change rates, effect sizes, or variability estimates. No uncertainty, sampling limitations, or heterogeneity across sites or time periods is addressed, leaving the ecological claims unsubstantiated and imprecise."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response uses relevant quantitative evidence (e.g., percentage changes in population abundance, reported confidence intervals, or effect sizes across sites) and links these figures to the research question. It discusses uncertainty and limitations such as short time series, site-specific variability, or mixed results across studies, and avoids overgeneralization, with only minor gaps in robustness or comparability discussion."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response describes ecological findings using only vague directional language (e.g., 'populations were lower' or 'diversity improved') without citing any quantitative data, statistical measures, or confidence ranges. Sampling limitations, measurement uncertainty, and cross-site heterogeneity are entirely absent, making it impossible to assess the strength or reliability of the ecological claims."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response integrates quantitative evidence effectively (e.g., referencing reported rates of habitat loss, species richness indices, or variation across study sites) and connects these to the broader ecological question. Uncertainty is explicitly acknowledged through discussion of data limitations such as short monitoring periods, uneven sampling effort, or inconsistent results across regions, and conclusions are appropriately hedged to avoid overgeneralization, with only minor omissions in comparability or robustness."
                    }
                ]
            },
            "ExplicitUncertainty": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response does not explicitly acknowledge any uncertainty, limitations, or assumptions related to the ecological findings or implications. For example, it presents conclusions about species population trends or habitat dynamics as fully settled without noting data gaps, confounding environmental variables, or the site-specific nature of the findings."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response explicitly acknowledges uncertainty, limitations, and assumptions related to the ecological findings or implications, using clear language to identify areas of ambiguity, unresolved questions, or potential confounding factors (e.g., noting that observed population declines may reflect sampling artifacts, that results are contingent on local climate conditions, or that long-term trends remain unclear due to short monitoring periods)."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response presents ecological claims and implications without explicitly identifying any limitations, assumptions, or areas of uncertainty. Findings related to ecosystem dynamics, species interactions, or environmental impacts are stated as definitive conclusions, with no mention of confounding factors, measurement limitations, or unresolved ecological questions."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response clearly and explicitly flags uncertainty, limitations, and assumptions throughout, using direct language to identify ambiguous or unresolved aspects of the ecological findings (e.g., acknowledging that causal mechanisms between disturbance regimes and biodiversity loss remain debated, that extrapolation across biomes may not be valid, or that study designs preclude ruling out alternative explanations). Potential confounding factors are named and their implications for interpreting results are discussed."
                    }
                ]
            }
        },
        "Gap": {
            "GapIdentification": {
                "ResponseA": [
                    {
                        "rating": "1",
                        "rationale": "The response only describes known ecological patterns and findings. It does not point out any missing data, unanswered questions, or limitations. It also does not mention underrepresented species, regions, or conflicting results."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response clearly identifies important gaps, such as missing long-term data for soil invertebrates in semi-arid regions, limited studies in tropical and boreal systems, and conflicting results on predator reintroduction. It explains why these gaps matter, though one point slightly mixes data gaps with methodological issues."
                    }
                ],
                "ResponseB": [
                    {
                        "rating": "1",
                        "rationale": "The response gives general observations about deforestation and habitat fragmentation but does not identify any missing information, open questions, or conflicting evidence. It assumes the existing knowledge is complete."
                    },
                    {
                        "rating": "4",
                        "rationale": "The response identifies clear gaps, such as lack of controlled studies on edge effects in freshwater areas, missing long-term data for migratory invertebrates, and differences between remote sensing and field data. It explains how these gaps affect conclusions, though it could be more specific about affected species or regions."
                    }
                ]
            }
        }    
    }
}


vocab_block_specs = {
    "mechanistic_vocab_block": {"label": "Mechanistic terms", "keys": ["mechanistic_terms"]},
    "causal_vocab_block": {"label": "Causal connectives / triggers", "keys": ["causal_terms"]},
    "temporal_vocab_block": {"label": "Temporal expressions", "keys": ["temporal_terms"]},
    "context_coverage_vocab_block": {"label": "Context Coverage", "keys": ["regions"]},
    "method_coverage_vocab_block": {"label": "Method Coverage", "keys": ["interventions"]},
    "dimension_coverage_vocab_block": {"label": "Dimension Coverage", "keys": ["diversity_dimensions"]},
    "scope_coverage_vocab_block": {"label": "Scope Coverage", "keys": ["ecosystem_services"]},
    "scale_coverage_vocab_block": {"label": "Scale Coverage", "keys": ["scale_terms"]},
    "gap_identification_vocab_block": {"label": "Gap Identification", "keys": ["gap_identification"]},
    "novelty_indicators_vocab_block": {"label": "State of the Art and Novelty Indicators", "keys": ["novelty_indicators"]},
    "epistemic_calibration_vocab_block": {"label": "Epistemic Calibration", "keys": ["epistemic_calibration"]},
    "quant_uncertainty_vocab_block": {"label": "Quantitative Evidence and Uncertainty", "keys": ["quant_uncertainty_vocab"]},
    "uncertainty_vocab_block": {"label": "Explicit Uncertainty", "keys": ["uncertainty_terms"]}
}

class Ecology(Domain):
    examples: Dict[str, Dict] = example_responses
    vocab: Dict[str, Dict] = vocabulary
    ID: str = "ecology"
    verbalized: str = "Ecology"
    vocab_block_specs: Dict[str, Dict[str, object]] = vocab_block_specs