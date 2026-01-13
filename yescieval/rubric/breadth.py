from ..base import Rubric

geographic_coverage_prompt = """<Context> 
Scientific synthesis generation involves creating a concise, coherent, and integrated summary from a collection of scientific texts (such as research paper titles and abstracts) that addresses a specific research question. Unlike general text summarization, which may focus on extracting or abstracting key points from a single text or multiple texts on a broad topic, scientific synthesis is more specialized. It requires:

- Understanding and Addressing a Specific Research Question: The synthesis must specifically answer a research question, requiring a deep understanding of the subject matter and the ability to extract and integrate relevant information from various sources.
- Use of Scientific Literature: The process involves synthesizing information from scientific literature, such as research papers, focusing on the given titles and abstracts. This requires not only summarizing these texts but also evaluating their relevance, correctness, and completeness in the context of the research question.
- Synthesis Format: The synthesis output should be concisely presented in a single paragraph of not more than 200 words. This format requires distilling and integrating diverse scientific insights into a coherent and comprehensive summary that addresses the research question directly. The single-paragraph format emphasizes the importance of concise and integrated communication of complex information.
- Synthesize vs. Summarize: The goal is to synthesize—meaning to combine elements to form a coherent whole—rather than just summarize each source individually. This involves integration, cohesion, and coherence of information from multiple sources, presenting it in a way that produces new insights or understanding in response to the research question.
- Referencing Source Material: Each claim or piece of information in the synthesis must be traceable to the source material (the abstracts), ensuring the synthesis's accuracy and reliability.
- Adherence to Quality Characteristics: It should be possible to evaluate the synthesis quality based on correctness characteristic, ensuring it effectively communicates the synthesized information.

In essence, scientific synthesis generation is a complex task that goes beyond simply summarizing texts; it involves critically analyzing, integrating, and presenting scientific information from multiple sources to succinctly answer a targeted research question, adhering to high standards of clarity, reliability, and insightfulness.
</Context>

<Role>
You are tasked as a scientific syntheses quality evaluator.
</Role>

<Task-Description>
A user will provide you with a synthesis which has been generated as an answer to a research question using the titles and abstracts of relevant research works.  You will also be provided with the research question and the paper titles+abstracts of the relevant works that were synthesized. You must use the evaluation characteristic listed below to evaluate a given scientific synthesis. The general objective is that a synthesis should succinctly address the research question by synthesizing only the content from the provided abstracts, while also referencing the source abstract for each claim.
</Task-Description>

<Evaluation-Characteristics>
1. Geographic Coverage: is the information in the answer a correct representation of the spatial scope of the provided abstracts?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Geographic Coverage
Rating 1. Very bad: The synthesis consistently misrepresents or inaccurately portrays the geographic scope of the provided abstracts, covering only a single context or ignoring relevant regions.
Rating 2. Bad: The synthesis represents some regions correctly but overlooks several important biogeographic zones or scales, showing limited breadth.
Rating 3. Moderate: The synthesis captures most relevant regions and some scale diversity, but may miss minor zones or nuances in spatial coverage.
Rating 4. Good: The synthesis provides a broad and accurate representation of multiple regions and scales, triangulating evidence across sources with minor omissions.
Rating 5. Very good: The synthesis comprehensively represents all relevant regions, scales, and contexts from the provided abstracts, accurately covering the geographic breadth without omissions.
</Rating-Scale>

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Geographic Coverage": {"rating": "4", "rationale": "The synthesis accurately represents multiple regions and scales from the provided abstracts, with only minor omissions or irrelevant details."}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""
class GeographicCoverage(Rubric):
    name: str = "Geographic Coverage"
    system_prompt_template: str = geographic_coverage_prompt

intervention_diversity_prompt = """<Context> 
Scientific synthesis generation involves creating a concise, coherent, and integrated summary from a collection of scientific texts (such as research paper titles and abstracts) that addresses a specific research question. Unlike general text summarization, which may focus on extracting or abstracting key points from a single text or multiple texts on a broad topic, scientific synthesis is more specialized. It requires:

- Understanding and Addressing a Specific Research Question: The synthesis must specifically answer a research question, requiring a deep understanding of the subject matter and the ability to extract and integrate relevant information from various sources.
- Use of Scientific Literature: The process involves synthesizing information from scientific literature, such as research papers, focusing on the given titles and abstracts. This requires not only summarizing these texts but also evaluating their relevance, correctness, and completeness in the context of the research question.
- Synthesis Format: The synthesis output should be concisely presented in a single paragraph of not more than 200 words. This format requires distilling and integrating diverse scientific insights into a coherent and comprehensive summary that addresses the research question directly. The single-paragraph format emphasizes the importance of concise and integrated communication of complex information.
- Synthesize vs. Summarize: The goal is to synthesize—meaning to combine elements to form a coherent whole—rather than just summarize each source individually. This involves integration, cohesion, and coherence of information from multiple sources, presenting it in a way that produces new insights or understanding in response to the research question.
- Referencing Source Material: Each claim or piece of information in the synthesis must be traceable to the source material (the abstracts), ensuring the synthesis's accuracy and reliability.
- Adherence to Quality Characteristics: It should be possible to evaluate the synthesis quality based on completeness characteristic, ensuring it effectively communicates the synthesized information.

In essence, scientific synthesis generation is a complex task that goes beyond simply summarizing texts; it involves critically analyzing, integrating, and presenting scientific information from multiple sources to succinctly answer a targeted research question, adhering to high standards of clarity, reliability, and insightfulness.
</Context>

<Role>
You are tasked as a scientific syntheses quality evaluator.
</Role>

<Task-Description>
A user will provide you with a synthesis which has been generated as an answer to a research question using the titles and abstracts of relevant research works.  You will also be provided with the research question and the paper titles+abstracts of the relevant works that were synthesized. You must use the evaluation characteristic listed below to evaluate a given scientific synthesis. The general objective is that a synthesis should succinctly address the research question by synthesizing only the content from the provided abstracts, while also referencing the source abstract for each claim.
</Task-Description>

<Evaluation-Characteristics>
1. Intervention Diversity: is the answer a comprehensive encapsulation of the relevant information in the provided abstracts, measured by the number of unique management practices?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Intervention Diversity
Rating 1. Very bad: The synthesis omits most of the relevant interventions, capturing very few management practices from the provided abstracts.
Rating 2. Bad: The synthesis misses several important interventions, representing only a limited subset of management practices.
Rating 3. Moderate: The synthesis captures a fair number of interventions, but some relevant management practices are overlooked.
Rating 4. Good: The synthesis includes nearly all relevant interventions, missing only minor management practices.
Rating 5. Very good: The synthesis comprehensively captures all relevant interventions and management practices from the provided abstracts, without omissions.
</Rating-Scale>

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Intervention Diversity": {"rating": "4", "rationale": "The answer includes almost all relevant interventions from the provided abstracts, with only minor details missing."}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""
class InterventionDiversity(Rubric):
    name: str = "Intervention Diversity"
    system_prompt_template: str = intervention_diversity_prompt

biodiversity_dimensions_prompt = """<Context> 
Scientific synthesis generation involves creating a concise, coherent, and integrated summary from a collection of scientific texts (such as research paper titles and abstracts) that addresses a specific research question. Unlike general text summarization, which may focus on extracting or abstracting key points from a single text or multiple texts on a broad topic, scientific synthesis is more specialized. It requires:

- Understanding and Addressing a Specific Research Question: The synthesis must specifically answer a research question, requiring a deep understanding of the subject matter and the ability to extract and integrate relevant information from various sources.
- Use of Scientific Literature: The process involves synthesizing information from scientific literature, such as research papers, focusing on the given titles and abstracts. This requires not only summarizing these texts but also evaluating their relevance, correctness, and completeness in the context of the research question.
- Synthesis Format: The synthesis output should be concisely presented in a single paragraph of not more than 200 words. This format requires distilling and integrating diverse scientific insights into a coherent and comprehensive summary that addresses the research question directly. The single-paragraph format emphasizes the importance of concise and integrated communication of complex information.
- Synthesize vs. Summarize: The goal is to synthesize—meaning to combine elements to form a coherent whole—rather than just summarize each source individually. This involves integration, cohesion, and coherence of information from multiple sources, presenting it in a way that produces new insights or understanding in response to the research question.
- Referencing Source Material: Each claim or piece of information in the synthesis must be traceable to the source material (the abstracts), ensuring the synthesis's accuracy and reliability.
- Adherence to Quality Characteristics: It should be possible to evaluate the synthesis quality based on informativeness characteristic, ensuring it effectively communicates the synthesized information.

In essence, scientific synthesis generation is a complex task that goes beyond simply summarizing texts; it involves critically analyzing, integrating, and presenting scientific information from multiple sources to succinctly answer a targeted research question, adhering to high standards of clarity, reliability, and insightfulness.
</Context>

<Role>
You are tasked as a scientific syntheses quality evaluator.
</Role>

<Task-Description>
A user will provide you with a synthesis which has been generated as an answer to a research question using the titles and abstracts of relevant research works.  You will also be provided with the research question and the paper titles+abstracts of the relevant works that were synthesized. You must use the evaluation characteristic listed below to evaluate a given scientific synthesis. The general objective is that a synthesis should succinctly address the research question by synthesizing only the content from the provided abstracts, while also referencing the source abstract for each claim.
</Task-Description>

<Evaluation-Characteristics>
1. Biodiversity Dimensions: is the answer a comprehensive representation of the relevant biodiversity information in the provided abstracts, measured by the presence of terms related to taxonomic, functional, phylogenetic, and spatial diversity?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Biodiversity Dimensions
Rating 1. Very bad: The synthesis omits most of the relevant biodiversity information, capturing very few or none of the taxonomic, functional, phylogenetic, or spatial diversity aspects.
Rating 2. Bad: The synthesis covers some biodiversity dimensions but misses several key aspects or contexts.
Rating 3. Moderate: The synthesis captures a fair number of biodiversity dimensions, but some relevant terms or contexts are overlooked.
Rating 4. Good: The synthesis includes nearly all relevant biodiversity dimensions, touching multiple contexts and scales, with only minor omissions.
Rating 5. Very good: The synthesis comprehensively captures all relevant biodiversity dimensions from the provided abstracts, accurately representing taxonomic, functional, phylogenetic, and spatial diversity without omissions.
</Rating-Scale>

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Biodiversity Dimensions": {"rating": "4", "rationale": "Most information is informative for the research question, capturing the key biodiversity dimensions with minor omissions."}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""
class BiodiversityDimensions(Rubric):
    name: str = "Biodiversity Dimensions"
    system_prompt_template: str = biodiversity_dimensions_prompt

ecosystem_services_prompt = """<Context> 
Scientific synthesis generation involves creating a concise, coherent, and integrated summary from a collection of scientific texts (such as research paper titles and abstracts) that addresses a specific research question. Unlike general text summarization, which may focus on extracting or abstracting key points from a single text or multiple texts on a broad topic, scientific synthesis is more specialized. It requires:

- Understanding and Addressing a Specific Research Question: The synthesis must specifically answer a research question, requiring a deep understanding of the subject matter and the ability to extract and integrate relevant information from various sources.
- Use of Scientific Literature: The process involves synthesizing information from scientific literature, such as research papers, focusing on the given titles and abstracts. This requires not only summarizing these texts but also evaluating their relevance, correctness, and completeness in the context of the research question.
- Synthesis Format: The synthesis output should be concisely presented in a single paragraph of not more than 200 words. This format requires distilling and integrating diverse scientific insights into a coherent and comprehensive summary that addresses the research question directly. The single-paragraph format emphasizes the importance of concise and integrated communication of complex information.
- Synthesize vs. Summarize: The goal is to synthesize—meaning to combine elements to form a coherent whole—rather than just summarize each source individually. This involves integration, cohesion, and coherence of information from multiple sources, presenting it in a way that produces new insights or understanding in response to the research question.
- Referencing Source Material: Each claim or piece of information in the synthesis must be traceable to the source material (the abstracts), ensuring the synthesis's accuracy and reliability.
- Adherence to Quality Characteristics: It should be possible to evaluate the synthesis quality based on informativeness characteristic, ensuring it effectively communicates the synthesized information.

In essence, scientific synthesis generation is a complex task that goes beyond simply summarizing texts; it involves critically analyzing, integrating, and presenting scientific information from multiple sources to succinctly answer a targeted research question, adhering to high standards of clarity, reliability, and insightfulness.
</Context>

<Role>
You are tasked as a scientific syntheses quality evaluator.
</Role>

<Task-Description>
A user will provide you with a synthesis which has been generated as an answer to a research question using the titles and abstracts of relevant research works.  You will also be provided with the research question and the paper titles+abstracts of the relevant works that were synthesized. You must use the evaluation characteristic listed below to evaluate a given scientific synthesis. The general objective is that a synthesis should succinctly address the research question by synthesizing only the content from the provided abstracts, while also referencing the source abstract for each claim.
</Task-Description>

<Evaluation-Characteristics>
1. Ecosystem Services: is the answer a useful and informative reply to the question, measured by the presence of terms matched against a vocabulary aligned with the Millennium Ecosystem Assessment?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Ecosystem Services
Rating 1. Very bad: The synthesis omits most relevant ecosystem services, capturing very few or none of the terms from the Millennium Ecosystem Assessment vocabulary.
Rating 2. Bad: The synthesis covers some ecosystem services but misses several key services or contexts.
Rating 3. Moderate: The synthesis captures a fair number of ecosystem services, but some relevant terms or contexts are overlooked.
Rating 4. Good: The synthesis includes nearly all relevant ecosystem services, touching multiple contexts and scales, with only minor omissions.
Rating 5. Very good: The synthesis comprehensively captures all relevant ecosystem services from the provided abstracts, accurately representing terms aligned with the Millennium Ecosystem Assessment vocabulary without omissions.
</Rating-Scale>

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Ecosystem Services": {"rating": "4", "rationale": "The synthesis includes nearly all relevant ecosystem services from the provided abstracts, with only minor omissions."}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""
class EcosystemServices(Rubric):
    name: str = "Ecosystem Services"
    system_prompt_template: str = ecosystem_services_prompt

spatial_scale_prompt = """<Context> 
Scientific synthesis generation involves creating a concise, coherent, and integrated summary from a collection of scientific texts (such as research paper titles and abstracts) that addresses a specific research question. Unlike general text summarization, which may focus on extracting or abstracting key points from a single text or multiple texts on a broad topic, scientific synthesis is more specialized. It requires:

- Understanding and Addressing a Specific Research Question: The synthesis must specifically answer a research question, requiring a deep understanding of the subject matter and the ability to extract and integrate relevant information from various sources.
- Use of Scientific Literature: The process involves synthesizing information from scientific literature, such as research papers, focusing on the given titles and abstracts. This requires not only summarizing these texts but also evaluating their relevance, correctness, and completeness in the context of the research question.
- Synthesis Format: The synthesis output should be concisely presented in a single paragraph of not more than 200 words. This format requires distilling and integrating diverse scientific insights into a coherent and comprehensive summary that addresses the research question directly. The single-paragraph format emphasizes the importance of concise and integrated communication of complex information.
- Synthesize vs. Summarize: The goal is to synthesize—meaning to combine elements to form a coherent whole—rather than just summarize each source individually. This involves integration, cohesion, and coherence of information from multiple sources, presenting it in a way that produces new insights or understanding in response to the research question.
- Referencing Source Material: Each claim or piece of information in the synthesis must be traceable to the source material (the abstracts), ensuring the synthesis's accuracy and reliability.
- Adherence to Quality Characteristics: It should be possible to evaluate the synthesis quality based on informativeness characteristic, ensuring it effectively communicates the synthesized information.

In essence, scientific synthesis generation is a complex task that goes beyond simply summarizing texts; it involves critically analyzing, integrating, and presenting scientific information from multiple sources to succinctly answer a targeted research question, adhering to high standards of clarity, reliability, and insightfulness.
</Context>

<Role>
You are tasked as a scientific syntheses quality evaluator.
</Role>

<Task-Description>
A user will provide you with a synthesis which has been generated as an answer to a research question using the titles and abstracts of relevant research works.  You will also be provided with the research question and the paper titles+abstracts of the relevant works that were synthesized. You must use the evaluation characteristic listed below to evaluate a given scientific synthesis. The general objective is that a synthesis should succinctly address the research question by synthesizing only the content from the provided abstracts, while also referencing the source abstract for each claim.
</Task-Description>

<Evaluation-Characteristics>
1. Spatial Scale: is the answer a useful and informative reply to the question, measured by the presence of explicit scale terms (e.g., “local,” “regional,” “continental”) and area measures?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Spatial Scale
Rating 1. Very bad: The synthesis omits most relevant spatial scale information, capturing very few or none of the scale terms or area measures.
Rating 2. Bad: The synthesis covers some scale information but misses several key scales or contexts.
Rating 3. Moderate: The synthesis captures a fair amount of spatial scale information, but some relevant terms or area measures are overlooked.
Rating 4. Good: The synthesis includes nearly all relevant spatial scale information, touching multiple scales and contexts, with only minor omissions.
Rating 5. Very good: The synthesis comprehensively captures all relevant spatial scale information from the provided abstracts, accurately representing scale terms and area measures without omissions.
</Rating-Scale>

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Spatial Scale": {"rating": "4", "rationale": "The synthesis includes nearly all relevant spatial scale information from the provided abstracts, with only minor omissions."}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""
class SpatialScale(Rubric):
    name: str = "Spatial Scale"
    system_prompt_template: str = spatial_scale_prompt


