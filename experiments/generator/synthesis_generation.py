from openai import OpenAI
import re
import pandas as pd
import json
import time
from api_keys import ACADEMICCLOUD_KEY


MODELS = ["qwen2.5-72b-instruct", "mistral-large-instruct", "meta-llama-3.1-70b-instruct", "meta-llama-3.1-8b-instruct"]
# "mistral-large-instruct", "meta-llama-3.1-70b-instruct", "meta-llama-3.1-8b-instruct"

DEFAULT_DELAY = 5


def prepare_data():
    filepath = "data/gpt-4_paper-wise.xlsx"
    df = pd.read_excel(filepath)
    df = df.iloc[:, :19]
    df.rename(columns={"research_problem": "research_question"}, inplace=True)

    # map research problems to questions
    problem_to_question_map = json.load(open("data/mapped_questions.json", "r"))
    for index, row in df.iterrows():
        problem = re.sub(r'\s+', ' ', row["research_question"]).strip()
        df.at[index, "research_question"] = problem_to_question_map[problem]

    df.to_excel("data/synthesized_papers.xlsx", index=False)


def synthesis_from_papers(filepath="data/synthesized_papers.xlsx"):
    df = pd.read_excel(filepath)

    base_url = "https://chat-ai.academiccloud.de/v1"
    # models = ["meta-llama-3.1-8b-instruct", "mistral-large-instruct", "meta-llama-3.1-70b-instruct", "qwen2.5-72b-instruct"] 

    # Start OpenAI client
    client = OpenAI(
        api_key = ACADEMICCLOUD_KEY,
        base_url = base_url
    )

    SYSTEM_PROMPT = "You are a scholarly assistant tasked with answering scientific questions by synthesizing information from the abstracts and titles of scholarly articles."

    for index, row in df.iterrows():
        print("###############################################")
        print(f"Processing row {index}")

        question = row["research_question"]
        papers_content = []
        for col_name, val in row[1:].items():
            if pd.isnull(val) or not col_name.startswith("paper"):
                break  
            
            papers_content.append(val)
        
        paper_string = ""
        for i, content in enumerate(papers_content):
            if i % 2 == 0:
                paper_string += f"Paper {(i//2) + 1}:\nTitle: {content}\n"
            else:
                paper_string += f"Abstract: {content}\n\n"
            

        # user_prompt_llm4syn = f"Generate a synthesis from the provided papers as content on the research question '{question}' into a concise single paragraph of no more than 200 words. Follow these instructions: \n - Only the titles and abstracts will be provided from up to five scientific papers which are to be used as the content for the synthesis. \n - The objective of this synthesis is to provide a paperwise analysis. Therefore, summarize each paper's contributions individually to the given research question above, noting significant findings or methodologies, or other such salient contribution facets. \n - Support each claim with citations, formatted as (1) or (3, 5) to refer to the respective papers' content, where the numbers correspond to the list of provided papers. \n - Ensure the output is formatted as a single cohesive paragraph without section headings, titles, abstracts, or any paper-like structure. The focus should be on integrating and synthesizing the content into a unified narrative. \n - Focus on essential information, maintaining clarity and precision. \n - Do not include additional information or exceed the specified word count of 200 words and the single paragraph synthesis output requirement.\n\n {paper_string}"

        user_prompt_bioasq = f"Generate an answer to the scientific question '{question}' from the provided papers into a concise single paragraph of 1 to 5 sentences. Follow these instructions: \n - Only the titles and abstracts will be provided from up to forty scientific papers which are to be used as the content for the answer sentence or sentences. \n - Comprehend the question. \n - The objective of your task is to answer the given question based on the evidence content from the respective papers. Therefore read all the papers' title and abstract and determine the portions of text where the answer is present. \n - Synthesize the answer based on evidence from the papers, avoiding repetition if the same information appears in multiple sources. \n - If you find the answer in multiple papers, paraphrase the answer once, cite all the sources from which the answer was obtained. In other words, support each answer sentence with citations, formatted as (1) or (3, 5) to refer to the respective papers' content, where the numbers correspond to the list of provided papers. \n - Ensure the output is formatted as a single cohesive paragraph without section headings, titles, abstracts, or any paper-like structure. The focus should be on integrating and synthesizing the content into a unified narrative that constitutes the answer. \n - Focus on essential information that directly answers the question, maintaining clarity and precision. \n - Do not include additional information or exceed the specified number of sentences of between 1 to 5 sentences in the expected answer output requirement.\n\n {paper_string}"

        user_prompt = user_prompt_bioasq

        for model in MODELS:
            if not pd.isnull(row[f"{model}_synthesis"]):
                continue

            print(f"Using model: {model}")

            retries = 0
            max_retries = 5
            delay = 60

            while retries < max_retries:
                try:
                    chat_completion = client.chat.completions.create(
                        messages=[{"role":"system","content": SYSTEM_PROMPT},{"role":"user","content": user_prompt}],
                        model= model,
                    )
                    df.at[index, f"{model}_synthesis"] = chat_completion.choices[0].message.content
                    break
                except Exception as e:
                    retries += 1
                    
                    print(f"Error: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay *= 2
            
            
            time.sleep(DEFAULT_DELAY)
                
        df.to_excel(filepath, index=False)
        # break
        

def check_models():
    client = OpenAI(
        api_key = ACADEMICCLOUD_KEY,
        base_url = "https://chat-ai.academiccloud.de/v1"
    )

    models = client.models.list()
    for model in models:
        print(model)  


def check_specific_model():
    client = OpenAI(
        api_key = ACADEMICCLOUD_KEY,
        base_url = "https://chat-ai.academiccloud.de/v1"
    )
    model = "qwen2.5-72b-instruct"

    chat_completion = client.chat.completions.create(
        messages=[{"role":"system","content": "You are a helpful assistant."},{"role":"user","content": "Ping"}], model= model,
    )
    print(chat_completion.choices[0].message.content)


def check_df():
    df1 = pd.read_excel("data/BioASQ_dataset_5_sentences.xlsx")
    df2 = pd.read_excel("data/BioASQ_dataset_5_eval.xlsx")
    for sheet_name in df1.keys():
        if df1[sheet_name].equals(df2[sheet_name]):
            print(f"Sheet {sheet_name} is equal")
        else:
            print(f"##### Sheet {sheet_name} is not equal #####")


def test():
    # count abstracts per question

    df = pd.read_excel("data/BioASQ_dataset_synthesis.xlsx")
    abstracts_count = {}

    for index, row in df.iterrows():
        i = 1
        while i < 41:
            if pd.isnull(row[f"paper_{i}_abstract"]):
                break
            i += 1
        if i-1 not in abstracts_count:
            abstracts_count[i-1] = 0
        abstracts_count[i-1] += 1
    abstracts_count = dict(sorted(abstracts_count.items(), reverse=True))
    print(sum(abstracts_count.values()))
    print(abstracts_count)


if __name__ == "__main__":
    prepare_data()
    
    filepath = "data/BioASQ_dataset.xlsx"
    synthesis_from_papers(filepath)
    
    # check_df()
    # check_models()
    # check_specific_model()
    
    # test()
    # base_model_access() 