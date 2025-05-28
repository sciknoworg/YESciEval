## Adversarial Corpus Construction Heuristics

The adversarial corpora in YESciEval are designed to assess the robustness of LLM-as-a-judge models through two levels of perturbation:


**Subtle Adversarial Dataset** Here, reference texts are minimally altered, making it challenging for models to detect changes. These alterations mimic realistic errors that may go unnoticed in automated evaluations.

**Extreme Adversarial Dataset** This dataset involves substantial modifications to reference texts, making the adversarial setting apparent and straightforward for models to identify. The evaluations should result in significantly lower scores.

### Evaluation Rubric Table

A total of nine evaluation rubrics were defined. For each rubric, specific adversarial perturbations were designed as part of the YESciEval test framework, as detailed below.


**Linguistic & Stylistic Quality** concerns grammar, clarity, and adherence to academic writing conventions. 

| Evaluation Rubric | Heuristic Rationale | Subtle Heuristic | Extreme Heuristic |
|-------------------|---------------------|------------------|-------------------|
| **1. Cohesion:** Are the sentences connected appropriately to make the resulting synthesis cohesive? | Perturb the synthesis output to make it incohesive by changing the places of the sentences in the discourse. | Swap the positions of the last two sentences. | Randomly shuffle all sentences. |
| **2. Conciseness:** Is the answer short and clear, without redundant statements? | Perturb conciseness by adding LLM-generated valid redundant sentences that unnecessarily repeat ideas already mentioned. | Use the LLM to generate a redundant version of the last sentence and append it to the response. | Append a redundant version after every sentence in the original response. |
| **3. Readability:** Does the answer follow appropriate style and structure conventions for academic writing, particularly for readability? | Add stylistically informal sentences that do not follow academic writing norms. | Append a snippet from a casual blog post. | Append a sentence from an informal tweet. |

**Logical & Structural Integrity** focuses on the reasoning and organization of information.

| Evaluation Rubric | Heuristic Rationale | Subtle Heuristic | Extreme Heuristic |
|-------------------|---------------------|------------------|-------------------|
| **4. Coherence:** Are the ideas connected soundly and logically? | Add sentences that convey unrelated ideas to break the logical flow. | Append a sentence from a different synthesis paragraph within the same domain. | Append a sentence from an unrelated sports news article. |
| **5. Integration:** Are the sources structurally and linguistically well-integrated, using appropriate markers of provenance/quotation and logical connectors for each reference? | Drop valid in-sentence connectors like logical conjunctions and provenance markers. | Remove the first logical connector (e.g., "however", "therefore"). | Remove all logical connectors. |
| **6. Relevancy:** Is the information in the answer relevant to the problem? | Add sentences that are not relevant to the problem in question. | Append a sentence from a different synthesis paragraph within the same domain. | Append a sentence from an unrelated sports news article. |

**Content Accuracy & Informativeness** ensures that the response is both correct and useful.

| Evaluation Rubric | Heuristic Rationale | Subtle Heuristic | Extreme Heuristic |
|-------------------|---------------------|------------------|-------------------|
| **7. Correctness:** Is the information in the answer a correct representation of the content of the provided abstracts? | Add content from sources other than the provided abstracts. | Append a sentence from a different synthesis paragraph within the same domain. | Append a sentence from an unrelated sports news article. |
| **8. Completeness:** Is the answer a comprehensive encapsulation of the relevant information in the provided abstracts? | Drop key sentences or add irrelevant ones to reduce comprehensiveness. | Remove the last sentence from the synthesis. | Remove the last sentence and append a sentence from an unrelated sports news article. |
| **9. Informativeness:** Is the answer a useful and informative reply to the problem? | Add non-informative content deliberately. | Append a sentence from a different synthesis paragraph within the same domain. | Append a sentence from an unrelated sports news article. |


