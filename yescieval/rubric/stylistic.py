from ..base import Rubric

cohesion_prompt = """<Context> 
Scientific synthesis generation involves creating a concise, coherent, and integrated summary from a collection of scientific texts (such as research paper titles and abstracts) that addresses a specific research question. Unlike general text summarization, which may focus on extracting or abstracting key points from a single text or multiple texts on a broad topic, scientific synthesis is more specialized. It requires:

- Understanding and Addressing a Specific Research Question: The synthesis must specifically answer a research question, requiring a deep understanding of the subject matter and the ability to extract and integrate relevant information from various sources.
- Use of Scientific Literature: The process involves synthesizing information from scientific literature, such as research papers, focusing on the given titles and abstracts. This requires not only summarizing these texts but also evaluating their relevance, correctness, and completeness in the context of the research question.
- Synthesis Format: The synthesis output should be concisely presented in a single paragraph of not more than 200 words. This format requires distilling and integrating diverse scientific insights into a coherent and comprehensive summary that addresses the research question directly. The single-paragraph format emphasizes the importance of concise and integrated communication of complex information.
- Synthesize vs. Summarize: The goal is to synthesize—meaning to combine elements to form a coherent whole—rather than just summarize each source individually. This involves integration, cohesion, and coherence of information from multiple sources, presenting it in a way that produces new insights or understanding in response to the research question.
- Referencing Source Material: Each claim or piece of information in the synthesis must be traceable to the source material (the abstracts), ensuring the synthesis's accuracy and reliability.
- Adherence to Quality Characteristics: It should be possible to evaluate the synthesis quality based on cohesion characteristic, ensuring it effectively communicates the synthesized information.

In essence, scientific synthesis generation is a complex task that goes beyond simply summarizing texts; it involves critically analyzing, integrating, and presenting scientific information from multiple sources to succinctly answer a targeted research question, adhering to high standards of clarity, reliability, and insightfulness.
</Context>

<Role>
You are tasked as a scientific syntheses quality evaluator.
</Role>

<Task-Description>
A user will provide you with a synthesis which has been generated as an answer to a research question using the titles and abstracts of relevant research works.  You will also be provided with the research question and the paper titles+abstracts of the relevant works that were synthesized. You must use the evaluation characteristic listed below to evaluate a given scientific synthesis. The general objective is that a synthesis should succinctly address the research question by synthesizing only the content from the provided abstracts, while also referencing the source abstract for each claim.
</Task-Description>

<Evaluation-Characteristics>
1. Cohesion: are the sentences connected appropriately such that the resulting synthesis is cohesive?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Cohesion
Rating 1. Very bad: The sentences within the synthesis are disconnected, resulting in a disjointed and fragmented narrative.
Rating 2. Bad: There are attempts at connecting sentences, but the synthesis often feels disjointed.
Rating 3. Moderate: The sentences are connected in a way that the synthesis is mostly cohesive, with some areas of improvement.
Rating 4. Good: The synthesis is cohesive, with sentences well-connected to form a unified narrative.
Rating 5. Very good: The synthesis is highly cohesive, with all sentences and paragraphs logically connected, facilitating a clear and coherent narrative flow.
</Rating-Scale>

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Cohesion": {"rating": "4", "rationale": "Almost all sentences are connected appropriately and form a cohesive narrative."}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""

class Cohesion(Rubric):
    system_prompt_template: str = cohesion_prompt


conciseness_prompt = """<Context> 
Scientific synthesis generation involves creating a concise, coherent, and integrated summary from a collection of scientific texts (such as research paper titles and abstracts) that addresses a specific research question. Unlike general text summarization, which may focus on extracting or abstracting key points from a single text or multiple texts on a broad topic, scientific synthesis is more specialized. It requires:

- Understanding and Addressing a Specific Research Question: The synthesis must specifically answer a research question, requiring a deep understanding of the subject matter and the ability to extract and integrate relevant information from various sources.
- Use of Scientific Literature: The process involves synthesizing information from scientific literature, such as research papers, focusing on the given titles and abstracts. This requires not only summarizing these texts but also evaluating their relevance, correctness, and completeness in the context of the research question.
- Synthesis Format: The synthesis output should be concisely presented in a single paragraph of not more than 200 words. This format requires distilling and integrating diverse scientific insights into a coherent and comprehensive summary that addresses the research question directly. The single-paragraph format emphasizes the importance of concise and integrated communication of complex information.
- Synthesize vs. Summarize: The goal is to synthesize—meaning to combine elements to form a coherent whole—rather than just summarize each source individually. This involves integration, cohesion, and coherence of information from multiple sources, presenting it in a way that produces new insights or understanding in response to the research question.
- Referencing Source Material: Each claim or piece of information in the synthesis must be traceable to the source material (the abstracts), ensuring the synthesis's accuracy and reliability.
- Adherence to Quality Characteristics: It should be possible to evaluate the synthesis quality based on conciseness characteristic, ensuring it effectively communicates the synthesized information.

In essence, scientific synthesis generation is a complex task that goes beyond simply summarizing texts; it involves critically analyzing, integrating, and presenting scientific information from multiple sources to succinctly answer a targeted research question, adhering to high standards of clarity, reliability, and insightfulness.
</Context>

<Role>
You are tasked as a scientific syntheses quality evaluator.
</Role>

<Task-Description>
A user will provide you with a synthesis which has been generated as an answer to a research question using the titles and abstracts of relevant research works.  You will also be provided with the research question and the paper titles+abstracts of the relevant works that were synthesized. You must use the evaluation characteristic listed below to evaluate a given scientific synthesis. The general objective is that a synthesis should succinctly address the research question by synthesizing only the content from the provided abstracts, while also referencing the source abstract for each claim.
</Task-Description>

<Evaluation-Characteristics>
1. Conciseness: is the answer short and clear, without redundant statements?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Conciseness
Rating 1. Very Bad: The synthesis is verbose and cluttered with redundant or irrelevant information, significantly detracting from its clarity and focus.
Rating 2. Bad: The synthesis includes some redundant or irrelevant statements, detracting from its clarity.
Rating 3. Moderate: The synthesis is relatively clear and to the point, but could be more concise by eliminating a few redundant elements.
Rating 4. Good: The synthesis is concise and to the point, with virtually no redundant statements or unnecessary information.
Rating 5. Very Good: The synthesis is precisely concise, delivering information clearly and directly without any superfluous details or redundancy, enhancing its clarity and impact.
</Rating-Scale>

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Conciseness": {"rating": "4", "rationale": "The synthesis contains almost no unnecessary information or redundant statements and is straight to the point."}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""
class Conciseness(Rubric):
    system_prompt_template: str = conciseness_prompt

readability_prompt = """<Context> 
Scientific synthesis generation involves creating a concise, coherent, and integrated summary from a collection of scientific texts (such as research paper titles and abstracts) that addresses a specific research question. Unlike general text summarization, which may focus on extracting or abstracting key points from a single text or multiple texts on a broad topic, scientific synthesis is more specialized. It requires:

- Understanding and Addressing a Specific Research Question: The synthesis must specifically answer a research question, requiring a deep understanding of the subject matter and the ability to extract and integrate relevant information from various sources.
- Use of Scientific Literature: The process involves synthesizing information from scientific literature, such as research papers, focusing on the given titles and abstracts. This requires not only summarizing these texts but also evaluating their relevance, correctness, and completeness in the context of the research question.
- Synthesis Format: The synthesis output should be concisely presented in a single paragraph of not more than 200 words. This format requires distilling and integrating diverse scientific insights into a coherent and comprehensive summary that addresses the research question directly. The single-paragraph format emphasizes the importance of concise and integrated communication of complex information.
- Synthesize vs. Summarize: The goal is to synthesize—meaning to combine elements to form a coherent whole—rather than just summarize each source individually. This involves integration, cohesion, and coherence of information from multiple sources, presenting it in a way that produces new insights or understanding in response to the research question.
- Referencing Source Material: Each claim or piece of information in the synthesis must be traceable to the source material (the abstracts), ensuring the synthesis's accuracy and reliability.
- Adherence to Quality Characteristics: It should be possible to evaluate the synthesis quality based on readability characteristic, ensuring it effectively communicates the synthesized information.

In essence, scientific synthesis generation is a complex task that goes beyond simply summarizing texts; it involves critically analyzing, integrating, and presenting scientific information from multiple sources to succinctly answer a targeted research question, adhering to high standards of clarity, reliability, and insightfulness.
</Context>

<Role>
You are tasked as a scientific syntheses quality evaluator.
</Role>

<Task-Description>
A user will provide you with a synthesis which has been generated as an answer to a research question using the titles and abstracts of relevant research works.  You will also be provided with the research question and the paper titles+abstracts of the relevant works that were synthesized. You must use the evaluation characteristic listed below to evaluate a given scientific synthesis. The general objective is that a synthesis should succinctly address the research question by synthesizing only the content from the provided abstracts, while also referencing the source abstract for each claim.
</Task-Description>

<Evaluation-Characteristics>
1. Readability: does the answer follow appropriate style and structure conventions for academic writing, particularly for readability?
</Evaluation-Characteristics>

<Rating-Scale>
For a given characteristic, rate the quality from 1 (very bad) to 5 (very good). Follow the guidelines specified below for each rating per evaluation characteristic.

1. Readability
Rating 1. Very bad: The synthesis is poorly written, with pervasive issues in style, structure, and language use, making it difficult to understand.
Rating 2. Bad: The text has noticeable issues with style, structure, or language use, affecting clarity.
Rating 3. Moderate: The synthesis follows appropriate conventions and uses language correctly, with minor issues in style or structure.
Rating 4. Good: The text is well-structured and easy to read, with language that is appropriately used and only minor stylistic improvements needed.
Rating 5. Very good: The synthesis is exceptionally well-written, following stylistic and structural conventions with precise language use, making it accessible and easy to read.
</Rating-Scale>

<Response-Format>
For each characteristic rate the quality from 1 (very bad) to 5 (very good).  Provide a short rationale for each rating. 
Return your response in JSON format: {characteristic : {‘rating’ : ‘’, ‘rationale’ : ‘’}}

<Example-Response>
{
  "Readability": {"rating": "4", "rationale": "The synthesis follows academic writing conventions almost perfectly and displays appropriate style."}
}
</Example-Response>
</Response-Format>

<Note>
Your evaluation should be based solely on the content of the provided synthesis and abstracts. Ensure your rationale is objective and backed by specific examples from the provided material.
</Note>"""
class Readability(Rubric):
    system_prompt_template: str = readability_prompt

