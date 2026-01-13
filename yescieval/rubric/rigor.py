from ..base import Rubric

statistical_sophistication_prompt = """<Context> 
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
1. Statistical Sophistication: Does the answer reflect quantitative depth through the use of inferential statistics or analysis methods described in the abstracts?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Statistical Sophistication
Rating 1. Very bad: The synthesis includes claims made without any statistics or methods; no mention of uncertainty or limitations; no reproducibility signals.
Rating 2. Bad: The synthesis contains very minimal methodological detail; very few statistics; limitations/uncertainty mostly ignored; reproducibility rarely addressed.
Rating 3. Moderate: The synthesis includes some statistics or method details; mentions limitations or uncertainty in passing; limited reproducibility information.
Rating 4. Good: The synthesis provides clear methods and statistics; acknowledges key limitations and uncertainties; provides some reproducibility signals (eg: data,code or baselines).
Rating 5. Very good: The information in the synthesis includes detailed and transparent methodology; robust statistics; thoroughly discusses limitations and uncertainty; strong reproducibility signals provided.
</Rating-Scale>

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Statistical Sophistication": {"rating": "3", "rationale": "The synthesis provides some methodological details and basic statistics, but does not fully discuss limitations or reproducibility.""}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""
class StatisticalSophistication(Rubric):
    name: str = "Statistical Sophistication"
    system_prompt_template: str = statistical_sophistication_prompt

citation_practices_prompt = """<Context> 
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
1. Citation Practices: is the answer supported by appropriate references, using parenthetical or narrative citations, for the relevant information in the provided abstracts?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Citation Practices
Rating 1. Very bad: The synthesis has no citations present; claims are unsupported.
Rating 2. Bad: Very few citations; many claims lack references; citation style inconsistent.
Rating 3. Moderate: The synthesis has some claims supported with citations; occasional missing or unclear references.
Rating 4. Good: The synthesis has most claims that are supported by citations; proper use of parenthetical or narrative style.
Rating 5. Very good: The synthesis includes all relevant claims supported by clear, correctly formatted citations; references fully cover the sources in the abstracts.
</Rating-Scale>

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Citation Practices": {"rating": "3", "rationale": "Some claims are supported with citations, but several important points lack references or use inconsistent citation style."}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""
class CitationPractices(Rubric):
    name: str = "Citation Practices"
    system_prompt_template: str = citation_practices_prompt

uncertainty_acknowledgement_prompt = """<Context> 
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
1. Uncertainty Acknowledgement: does the answer explicitly discuss limitations, uncertainty, or gaps in evidence (e.g., using terms like “unknown,” “limited evidence,” or “unclear”)?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Uncertainty Acknowledgement
Rating 1. Very bad: The synthesis offers no mention of uncertainty, limitations, or gaps in evidence.
Rating 2. Bad: The answer provides very limited acknowledgement of uncertainty; most claims presented as certain.
Rating 3. Moderate: The answer has some uncertainty or limitations mentioned, but coverage is incomplete or vague.
Rating 4. Good: The answer has clear acknowledgement of key uncertainties, limitations, or potential biases.
Rating 5. Very good: The synthesis has thorough discussion of uncertainty, limitations, and potential biases for all relevant claims; clearly signals gaps in evidence.
</Rating-Scale>

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Uncertainty Acknowledgement": {"rating": "4", "rationale": "The answer clearly acknowledges key uncertainties and limitations in the study."}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""
class UncertaintyAcknowledgment(Rubric):
    name: str = "Uncertainty Acknowledgement"
    system_prompt_template: str = uncertainty_acknowledgement_prompt

