import pandas as pd
from api_keys import ACADEMICCLOUD_KEY
from openai import OpenAI
import time
import sys
import os


MODELS = ["qwen2.5-72b-instruct", "meta-llama-3.1-70b-instruct", "meta-llama-3.1-8b-instruct", "mistral-large-instruct"]
CRITERION_PATHS = ["rcic", "completeness", "integration", "cohesion", "readability", "conciseness"]
SYSTEM_PROMPT_FILE = "data/per_model_evaluation_system_prompt"
DEFAULT_DELAY = 2
MAX_RETRIES = 6


def build_user_prompt(row, max_papers):
    user_prompts = []
    user_prompt_text = "Evaluate and rate the quality of the following scientific synthesis according to the nine characteristics given in the system prompt."
    question = row["research_question"]
    content = format_paper_content(row, max_papers)

    for target_model in MODELS:
        synthesis = row[f"{target_model}_synthesis"]
        current_prompt = (
            f"{user_prompt_text}\n\n"
            f"<scientific-synthesis>{synthesis}</scientific-synthesis>\n\n"
            f"<research-question>{question}</research-question>\n\n"
            f"<paper-titles-and-abstracts>{content}</paper-titles-and-abstracts>\n\n###"
        )
        user_prompts.append((current_prompt, target_model))
    return user_prompts


def build_adversarial_user_prompt(row, max_papers, degree, criterion):
    user_prompts = []
    user_prompt_text = "Evaluate and rate the quality of the following scientific synthesis according to the characteristics given in the system prompt."
    question = row["research_question"]
    content = format_paper_content(row, max_papers)

    for target_model in MODELS:
        synthesis = row[f"{target_model}_{degree}_{criterion}"]
        current_prompt = (
            f"{user_prompt_text}\n\n"
            f"<scientific-synthesis>{synthesis}</scientific-synthesis>\n\n"
            f"<research-question>{question}</research-question>\n\n"
            f"<paper-titles-and-abstracts>{content}</paper-titles-and-abstracts>\n\n###"
        )
        user_prompts.append((current_prompt, target_model))
    return user_prompts


def format_paper_content(row, max_papers):
    paper_content = ""
    for i in range(max_papers):
        if pd.isna(row[f"paper_{i+1}_title"]):
            break

        title = row[f"paper_{i+1}_title"]
        abstract = row[f"paper_{i+1}_abstract"]
        paper_content += f"{i+1}. " + title + "\n\n" + abstract + "\n\n"
    return paper_content


def vanilla(synthesis_file, output_file, model, start_index=0, max_papers=5):
    client = OpenAI(
        api_key = ACADEMICCLOUD_KEY,
        base_url = "https://chat-ai.academiccloud.de/v1"
    )
    
    with open(SYSTEM_PROMPT_FILE, 'r') as f:
        system_prompt = f.read()
    
    df = pd.read_excel(synthesis_file)

    print("#" * 50)
    print(f"Starting evaluation for {model}")

    for index, row in df.iterrows():
        if index < start_index:
            continue

        print(f"Processing row {index+1}")
        user_prompts = build_user_prompt(row, max_papers)
        for user_prompt, target_model in user_prompts:
            print(f"Processing model {target_model}")
            message = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]

            retries = 0
            delay = 120
            while retries < MAX_RETRIES:
                try:
                    chat_completion = client.chat.completions.create(
                        model = model,
                        messages = message
                    )
                    df.at[index, f"{model}_evaluation_scores_{target_model}"] = chat_completion.choices[0].message.content
                    break
                
                except Exception as e:
                    print(f"Error: {e}. Retrying in {delay} seconds...")
                    retries += 1
                    time.sleep(delay)
                    delay *= 2
            
            time.sleep(DEFAULT_DELAY)
        
        df.to_excel(output_file, index=False)


def adversarial(synthesis_file, output_file, model, start_index, max_papers, system_prompt_file, degree, criterion):
    client = OpenAI(
        api_key = ACADEMICCLOUD_KEY,
        base_url = "https://chat-ai.academiccloud.de/v1"
    )
    
    with open(system_prompt_file, 'r') as f:
        system_prompt = f.read()
    
    df = pd.read_excel(synthesis_file)

    print("#" * 50)
    print(f"Starting evaluation for {model}")

    for index, row in df.iterrows():
        if index < start_index:
            continue

        print(f"Processing row {index+1}")
        user_prompts = build_adversarial_user_prompt(row, max_papers, degree, criterion)
        for user_prompt, target_model in user_prompts:
            print(f"Processing model {target_model}")
            message = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]

            retries = 0
            delay = 120
            while retries < MAX_RETRIES:
                try:
                    chat_completion = client.chat.completions.create(
                        model = model,
                        messages = message
                    )
                    df.at[index, f"{model}_evaluation_scores_{target_model}"] = chat_completion.choices[0].message.content
                    break
                
                except Exception as e:
                    print(f"Error: {e}. Retrying in {delay} seconds...")
                    retries += 1
                    if retries == MAX_RETRIES:
                        exit()

                    time.sleep(delay)
                    delay *= 2
            
            time.sleep(DEFAULT_DELAY)
        
        df.to_excel(output_file, index=False)



def test():
    df = pd.read_excel("data/BioASQ_dataset_synthesis_clean.xlsx")
    for index, row in df.iterrows():
        if index > 3:
            break
        print(row["paper_7_title"])
        print(type(row["paper_7_title"]))
        print(pd.isna(row["paper_7_title"]))


def regenerate_specific_row(criterion_path, model, degree, start_index, max_papers, criterion):
    if max_papers == 40:
        adversarial(f"data/BioASQ_dataset_adversarial_{degree}_per_model_evaluation_{criterion_path}_{model}.xlsx", f"data/BioASQ_dataset_adversarial_{degree}_per_model_evaluation_{criterion_path}_{model}.xlsx", model, start_index, max_papers, f"data/per_model_evaluation_system_prompt_{criterion_path}", degree, criterion)
    else:
        adversarial(f"data/llm4syn_dataset_adversarial_{degree}_per_model_evaluation_{criterion_path}_{model}.xlsx", f"data/llm4syn_dataset_adversarial_{degree}_per_model_evaluation_{criterion_path}_{model}.xlsx", model, start_index, max_papers, f"data/per_model_evaluation_system_prompt_{criterion_path}", degree, criterion)


if __name__ == "__main__":
    MODELS = ["qwen2.5-72b-instruct", "meta-llama-3.1-70b-instruct", "meta-llama-3.1-8b-instruct", "mistral-large-instruct"]
    CRITERION_PATHS = ["rcic", "completeness", "integration", "cohesion", "readability", "conciseness"]
    criteria = ["relevancy", "correctness", "informativeness", "coherence", "completeness", "integration", "cohesion", "readability", "conciseness"]
    

    model_index = int(sys.argv[1])
    start_index_1 = int(sys.argv[2])
    start_index_2 = int(sys.argv[3])
    start_index_3 = int(sys.argv[4])
    start_index_4 = int(sys.argv[5])
    criterion = "conciseness"

    # BioASQ dataset
    if start_index_1 >= 0:
        if os.path.exists(f"data/BioASQ_dataset_adversarial_subtle_per_model_evaluation_{criterion}_{MODELS[model_index]}.xlsx"):
            input_file = f"data/BioASQ_dataset_adversarial_subtle_per_model_evaluation_{criterion}_{MODELS[model_index]}.xlsx"
        else:
            input_file = "data/BioASQ_dataset_adversarial_subtle_clean.xlsx"

        adversarial(input_file, f"data/BioASQ_dataset_adversarial_subtle_per_model_evaluation_{criterion}_{MODELS[model_index]}.xlsx", MODELS[model_index], start_index_1, 40, f"data/per_model_evaluation_system_prompt_{criterion}", "subtle", criterion)
    if start_index_2 >= 0:
        if os.path.exists(f"data/BioASQ_dataset_adversarial_extreme_per_model_evaluation_{criterion}_{MODELS[model_index]}.xlsx"):
            input_file = f"data/BioASQ_dataset_adversarial_extreme_per_model_evaluation_{criterion}_{MODELS[model_index]}.xlsx"
        else:
            input_file = "data/BioASQ_dataset_adversarial_extreme_clean.xlsx"

        adversarial(input_file, f"data/BioASQ_dataset_adversarial_extreme_per_model_evaluation_{criterion}_{MODELS[model_index]}.xlsx", MODELS[model_index], start_index_2, 40, f"data/per_model_evaluation_system_prompt_{criterion}", "extreme", criterion)

    # LLMs4Syn dataset
    if start_index_3 >= 0:
        if os.path.exists(f"data/llm4syn_dataset_adversarial_subtle_per_model_evaluation_{criterion}_{MODELS[model_index]}.xlsx"):
            input_file = f"data/llm4syn_dataset_adversarial_subtle_per_model_evaluation_{criterion}_{MODELS[model_index]}.xlsx"
        else:
            input_file = "data/llm4syn_dataset_adversarial_subtle_clean.xlsx"

        adversarial(input_file, f"data/llm4syn_dataset_adversarial_subtle_per_model_evaluation_{criterion}_{MODELS[model_index]}.xlsx", MODELS[model_index], start_index_3, 5, f"data/per_model_evaluation_system_prompt_{criterion}", "subtle", criterion)
    if start_index_4 >= 0:
        if os.path.exists(f"data/llm4syn_dataset_adversarial_extreme_per_model_evaluation_{criterion}_{MODELS[model_index]}.xlsx"):
            input_file = f"data/llm4syn_dataset_adversarial_extreme_per_model_evaluation_{criterion}_{MODELS[model_index]}.xlsx"
        else:
            input_file = "data/llm4syn_dataset_adversarial_extreme_clean.xlsx"

        adversarial(input_file, f"data/llm4syn_dataset_adversarial_extreme_per_model_evaluation_{criterion}_{MODELS[model_index]}.xlsx", MODELS[model_index], start_index_4, 5, f"data/per_model_evaluation_system_prompt_{criterion}", "extreme", criterion)

    
    # model checkpoints:    model_i, BQ_subtle, BQ_extreme, LLM4Syn_subtle, LLM4Syn_extreme
    # qwen2.5-72b-instruct: 0, 0, 0, 0, 0  
    # meta-llama-3.1-70b-instruct: 1, -1, -1, 292, 0
    # meta-llama-3.1-8b-instruct: 2, 0, 0, 0, 0
    # mistral-large-instruct: 3, 0, 0, 0, 0
