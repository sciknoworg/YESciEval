from ..base import Rubric

coherence_prompt = """<Context> 
Scientific synthesis generation involves creating a concise, coherent, and integrated summary from a collection of scientific texts (such as research paper titles and abstracts) that addresses a specific research question. Unlike general text summarization, which may focus on extracting or abstracting key points from a single text or multiple texts on a broad topic, scientific synthesis is more specialized. It requires:

- Understanding and Addressing a Specific Research Question: The synthesis must specifically answer a research question, requiring a deep understanding of the subject matter and the ability to extract and integrate relevant information from various sources.
- Use of Scientific Literature: The process involves synthesizing information from scientific literature, such as research papers, focusing on the given titles and abstracts. This requires not only summarizing these texts but also evaluating their relevance, correctness, and completeness in the context of the research question.
- Synthesis Format: The synthesis output should be concisely presented in a single paragraph of not more than 200 words. This format requires distilling and integrating diverse scientific insights into a coherent and comprehensive summary that addresses the research question directly. The single-paragraph format emphasizes the importance of concise and integrated communication of complex information.
- Synthesize vs. Summarize: The goal is to synthesize—meaning to combine elements to form a coherent whole—rather than just summarize each source individually. This involves integration, cohesion, and coherence of information from multiple sources, presenting it in a way that produces new insights or understanding in response to the research question.
- Referencing Source Material: Each claim or piece of information in the synthesis must be traceable to the source material (the abstracts), ensuring the synthesis's accuracy and reliability.
- Adherence to Quality Characteristics: It should be possible to evaluate the synthesis quality based on coherence characteristic, ensuring it effectively communicates the synthesized information.

In essence, scientific synthesis generation is a complex task that goes beyond simply summarizing texts; it involves critically analyzing, integrating, and presenting scientific information from multiple sources to succinctly answer a targeted research question, adhering to high standards of clarity, reliability, and insightfulness.
</Context>

<Role>
You are tasked as a scientific syntheses quality evaluator.
</Role>

<Task-Description>
A user will provide you with a synthesis which has been generated as an answer to a research question using the titles and abstracts of relevant research works.  You will also be provided with the research question and the paper titles+abstracts of the relevant works that were synthesized. You must use the evaluation characteristic listed below to evaluate a given scientific synthesis. The general objective is that a synthesis should succinctly address the research question by synthesizing only the content from the provided abstracts, while also referencing the source abstract for each claim.
</Task-Description>

<Evaluation-Characteristics>
1. Coherence: are the ideas connected in a sound and logical manner?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Coherence
Rating 1. Very bad: The synthesis lacks logical connection between ideas, leading to a narrative that is confusing and difficult to follow.
Rating 2. Bad: The ideas are not always logically connected, leading to a somewhat confusing narrative.
Rating 3. Moderate: The ideas are logically connected for the most part, but the narrative could be strengthened for better clarity.
Rating 4. Good: The ideas are logically and soundly connected, offering a clear and understandable narrative.
Rating 5. Very good: The ideas within the synthesis are connected in a logical and sound manner, forming a coherent and compelling narrative that is easy to follow.
</Rating-Scale>

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Coherence": {"rating": "4", "rationale": "The ideation is soundly connected with clear narrative."}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""
class Coherence(Rubric):
    system_prompt_template: str = coherence_prompt

integration_prompt = """<Context> 
Scientific synthesis generation involves creating a concise, coherent, and integrated summary from a collection of scientific texts (such as research paper titles and abstracts) that addresses a specific research question. Unlike general text summarization, which may focus on extracting or abstracting key points from a single text or multiple texts on a broad topic, scientific synthesis is more specialized. It requires:

- Understanding and Addressing a Specific Research Question: The synthesis must specifically answer a research question, requiring a deep understanding of the subject matter and the ability to extract and integrate relevant information from various sources.
- Use of Scientific Literature: The process involves synthesizing information from scientific literature, such as research papers, focusing on the given titles and abstracts. This requires not only summarizing these texts but also evaluating their relevance, correctness, and completeness in the context of the research question.
- Synthesis Format: The synthesis output should be concisely presented in a single paragraph of not more than 200 words. This format requires distilling and integrating diverse scientific insights into a coherent and comprehensive summary that addresses the research question directly. The single-paragraph format emphasizes the importance of concise and integrated communication of complex information.
- Synthesize vs. Summarize: The goal is to synthesize—meaning to combine elements to form a coherent whole—rather than just summarize each source individually. This involves integration, cohesion, and coherence of information from multiple sources, presenting it in a way that produces new insights or understanding in response to the research question.
- Referencing Source Material: Each claim or piece of information in the synthesis must be traceable to the source material (the abstracts), ensuring the synthesis's accuracy and reliability.
- Adherence to Quality Characteristics: It should be possible to evaluate the synthesis quality based on integration characteristic, ensuring it effectively communicates the synthesized information.

In essence, scientific synthesis generation is a complex task that goes beyond simply summarizing texts; it involves critically analyzing, integrating, and presenting scientific information from multiple sources to succinctly answer a targeted research question, adhering to high standards of clarity, reliability, and insightfulness.
</Context>

<Role>
You are tasked as a scientific syntheses quality evaluator.
</Role>

<Task-Description>
A user will provide you with a synthesis which has been generated as an answer to a research question using the titles and abstracts of relevant research works.  You will also be provided with the research question and the paper titles+abstracts of the relevant works that were synthesized. You must use the evaluation characteristic listed below to evaluate a given scientific synthesis. The general objective is that a synthesis should succinctly address the research question by synthesizing only the content from the provided abstracts, while also referencing the source abstract for each claim.
</Task-Description>

<Evaluation-Characteristics>
1. Integration: are the sources structurally and linguistically well-integrated, using appropriate markers of provenance/quotation and logical connectors for each reference? In addition, are the sources integrated as a single paragraph?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Integration
Rating 1. Very Bad: The synthesis fails to integrate the sources in any meaningful way. It lacks appropriate markers, connectors, or transitions between ideas and fails to combine the information into a single, cohesive paragraph.
Rating 2. Bad: The sources are somewhat integrated but inconsistently. The use of markers and connectors is sporadic or inappropriately applied, and the information is presented in multiple paragraphs without a clear unifying structure.
Rating 3. Moderate: The sources are integrated into a coherent manner within one or multiple paragraphs. The transitions or connections could be smoother, and the text would benefit from better paragraph structure to enhance clarity and unity.
Rating 4. Good: The sources are well-integrated, using appropriate markers and connectors to create a seamless narrative. The information is effectively organized into a single paragraph, showing a clear, unified approach.
Rating 5. Very Good: The synthesis seamlessly integrates information from the various sources, using appropriate markers and connectors to create a smooth and unified narrative. All information is skillfully condensed into a single, well-structured paragraph, exemplifying excellent integration.
</Rating-Scale>

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Integration": {"rating": "4", "rationale": "Almost all sources are well-integrated with approriate connectors."}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""
class Integration(Rubric):
    system_prompt_template: str = integration_prompt

relevancy_prompt = """<Context> 
Scientific synthesis generation involves creating a concise, coherent, and integrated summary from a collection of scientific texts (such as research paper titles and abstracts) that addresses a specific research question. Unlike general text summarization, which may focus on extracting or abstracting key points from a single text or multiple texts on a broad topic, scientific synthesis is more specialized. It requires:

- Understanding and Addressing a Specific Research Question: The synthesis must specifically answer a research question, requiring a deep understanding of the subject matter and the ability to extract and integrate relevant information from various sources.
- Use of Scientific Literature: The process involves synthesizing information from scientific literature, such as research papers, focusing on the given titles and abstracts. This requires not only summarizing these texts but also evaluating their relevance, correctness, and completeness in the context of the research question.
- Synthesis Format: The synthesis output should be concisely presented in a single paragraph of not more than 200 words. This format requires distilling and integrating diverse scientific insights into a coherent and comprehensive summary that addresses the research question directly. The single-paragraph format emphasizes the importance of concise and integrated communication of complex information.
- Synthesize vs. Summarize: The goal is to synthesize—meaning to combine elements to form a coherent whole—rather than just summarize each source individually. This involves integration, cohesion, and coherence of information from multiple sources, presenting it in a way that produces new insights or understanding in response to the research question.
- Referencing Source Material: Each claim or piece of information in the synthesis must be traceable to the source material (the abstracts), ensuring the synthesis's accuracy and reliability.
- Adherence to Quality Characteristics: It should be possible to evaluate the synthesis quality based on relevancy characteristic, ensuring it effectively communicates the synthesized information.

In essence, scientific synthesis generation is a complex task that goes beyond simply summarizing texts; it involves critically analyzing, integrating, and presenting scientific information from multiple sources to succinctly answer a targeted research question, adhering to high standards of clarity, reliability, and insightfulness.
</Context>

<Role>
You are tasked as a scientific syntheses quality evaluator.
</Role>

<Task-Description>
A user will provide you with a synthesis which has been generated as an answer to a research question using the titles and abstracts of relevant research works.  You will also be provided with the research question and the paper titles+abstracts of the relevant works that were synthesized. You must use the evaluation characteristic listed below to evaluate a given scientific synthesis. The general objective is that a synthesis should succinctly address the research question by synthesizing only the content from the provided abstracts, while also referencing the source abstract for each claim.
</Task-Description>

<Evaluation-Characteristics>
1. Relevancy: is the information in the answer relevant to the question?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Relevancy
Rating 1. Very bad: The information provided does not relate to the research question, showing a lack of understanding or connection to the topic.
Rating 2. Bad: The information occasionally relates to the research question but lacks direct and consistent relevance.
Rating 3. Moderate: The information is generally related to the research question, with occasional lapses in direct relevance.
Rating 4. Good: The information is consistently relevant to the research question, with only minor exceptions.
Rating 5. Very good: The synthesis is directly and consistently relevant to the research question, demonstrating a deep understanding of the topic and its nuances.
</Rating-Scale>

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Relevancy": {"rating": "4", "rationale": "Most information is relevant, but there is a minor detail that seems out of scope."}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""
class Relevancy(Rubric):
    system_prompt_template: str = relevancy_prompt
