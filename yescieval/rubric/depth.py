from ..base import Rubric

mechanistic_understanding_prompt = """<Context> 
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
1. Mechanistic Understanding: does the answer reflect understanding of ecological processes by explicitly mentioning recognized mechanisms such as feedbacks, nutrient cycling, or trophic cascades?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Mechanistic Understanding
Rating 1. Very bad: The synthesis contains only vague statements (e.g., “X affects Y”) with no explanation of how or why; no causal language or mechanisms.
Rating 2. Bad: The synthesis mentions a relationship but remains single-step; mechanisms are implied but not described; no mediators or temporal aspects.
Rating 3. Moderate: The synthesis identifies at least one mechanism or causal link but lacks depth; limited causal connectors and no explicit assumptions or timing.
Rating 4. Good: The synthesis describes multi-step mechanisms (driver → mediator → outcome) using causal language; may include some temporal or conditional detail.
Rating 5. Very good: The information in the synthesis provides detailed, explicit multi-step causal mechanisms with clear mediators, temporal specificity, and stated assumptions or boundary conditions.

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Mechanistic Understanding": {"rating": "4", "rationale": "The answer explains a clear multi-step ecological mechanism using causal language, but some temporal or boundary details are only briefly addressed."}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""
class MechanisticUnderstanding(Rubric):
    name: str = "Mechanistic Understanding"
    system_prompt_template: str = mechanistic_understanding_prompt

causal_reasoning_prompt = """<Context> 
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
1. Causal Reasoning: does the answer explicitly express cause–effect relationships using causal connectives (e.g., “because,” “due to”), result indicators (e.g., “results in,” “induces”), or mechanistic verbs (e.g., “drives,” “regulates”) when describing ecological processes?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Causal Reasoning
Rating 1. Very bad: The synthesis uses vague statements (e.g., “X affects Y”) with no causal connectors,
Rating 2. Bad: The synthesis identifies a cause–effect relationship but only as a single-step claim; causal language is minimal and mediators are ignored.
Rating 3. Moderate: The synthesis includes explicit causal connectors or verbs and at least one cause–effect link, but remains shallow.
Rating 4. Good: The synthesis describes multi-step causal chains (driver → mediator → outcome) using clear causal language.
Rating 5. Very good: The synthesis presents detailed, explicit multi-step causal reasoning with clear mediators, temporal specificity, and stated assumptions or boundary conditions.
</Rating-Scale>

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Causal Reasoning": {"rating": "4", "rationale": "The answer uses clear causal connectors and describes a multi-step cause–effect relationship."}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""
class CausalReasoning(Rubric):
    name: str = "Causal Reasoning"
    system_prompt_template: str = causal_reasoning_prompt

temporal_precision_prompt = """<Context> 
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
1. Temporal Precision: does the answer include specific and explicit temporal references, such as quantified time intervals or dated events, rather than vague or unspecific timing?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Temporal Precision
Rating 1. Very bad: The synthesis contains no temporal references; timing is entirely vague or absent.
Rating 2. Bad: The answer includes implicit or generic timing (e.g., “over time,” “eventually”) but no specific intervals, dates, or durations.
Rating 3. Moderate: The answer provides at least one explicit temporal reference (e.g., a rough duration or time window) but lacks consistency or clear linkage to effects.
Rating 4. Good: The answer includes multiple specific temporal references (e.g., quantified intervals or dated events) that are clearly tied to described processes or outcomes.
Rating 5. Very good: The answer demonstrates high temporal precision, with detailed and explicit timeframes (lags, durations, windows, or dates) systematically linked to multi-step processes and their effects.
</Rating-Scale>

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Temporal Precision": {"rating": "4", "rationale": "The answer includes several specific timeframes or durations that are clearly linked to the described processes, though some timing details could be more precise."}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""
class TemporalPrecision(Rubric):
    name: str = "Temporal Precision"
    system_prompt_template: str = temporal_precision_prompt

