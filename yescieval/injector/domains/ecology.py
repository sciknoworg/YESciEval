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
    "uncertainty_terms": ["uncertain", "unclear", "unknown"],
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
    ]
}

example_responses = {
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
    "gap_identification_vocab_block": {"label": "Gap Identification", "keys": ["gap_identification"]}
}

class Ecology(Domain):
    examples: Dict[str, Dict] = example_responses
    vocab: Dict[str, Dict] = vocabulary
    ID: str = "ecology"
    verbalized: str = "Ecology"
    vocab_block_specs: Dict[str, Dict[str, object]] = vocab_block_specs