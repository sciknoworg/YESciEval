import pandas as pd
import re
import json


MODELS = ["qwen2.5-72b-instruct", "meta-llama-3.1-70b-instruct", "meta-llama-3.1-8b-instruct", "mistral-large-instruct"]
EVALUATION_CRITERIA = ["Relevancy", "Correctness", "Completeness", "Informativeness", "Integration", "Cohesion", "Coherence", "Readability", "Conciseness"]
CRITERION_PATHS = ["rcic", "completeness", "integration", "cohesion", "readability", "conciseness"]


def create_clean_json(file_path, eval_model, criteria=EVALUATION_CRITERIA):
    df = pd.read_excel(file_path)
    
    # Add new columns for each evaluation criterion
    for target_model in MODELS:
        for criterion in criteria:
            df[f"{eval_model}_{target_model}_{criterion}"] = None
    
    for index, row in df.iterrows():

        for target_model in MODELS:
            evaluation = row[f"{eval_model}_evaluation_scores_{target_model}"]
            evaluation = load_json(evaluation, criteria)

            # evaluation = json.loads(evaluation)
            # row[f"{eval_model}_evaluation_scores_{target_model}"] = evaluation
            # Populate new columns with evaluation criteria
            
            for criterion in criteria:
                # set_criterion(df, criterion, evaluation, index, eval_model, target_model)
                try:
                    df.at[index, f"{eval_model}_{target_model}_{criterion}"] = evaluation[criterion]["rating"]
                except KeyError:
                    print(f"Error decoding JSON attribute: {criterion}")

    
    df.to_excel(file_path[:-5] + "_clean.xlsx", index=False)


def load_json(text, criteria=EVALUATION_CRITERIA):
    # try return regular text
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            rating = json.loads(match.group())
            if all(criterion in rating for criterion in criteria):
                return rating
        except json.JSONDecodeError:
            print("invalid JSON")

    # Manually search for each criterion in the text and create a JSON from scratch
    evaluation = {}
    for criterion in criteria:
        match = re.search(rf'{criterion}[\*\:\s\n",}}’‘\'â€˜™]*(?:[{{"\'\s’‘â€˜“”]*rating[=\'":\s’‘â€˜™“”]*"?([1-5])\}}?|\b([1-5])\b)|characteristic[\*\:\s\n",]*[{{"\'\s’‘“”â€˜]*rating[\'":\s’‘“”â€˜™]*([1-5])}}?', text, re.IGNORECASE)
        if match:
            evaluation[criterion] = {"rating": match.group(1) or match.group(2) or match.group(3)}
        else:
            evaluation[criterion] = {"rating": None}

    return evaluation


def check_for_empty_cells(df, model):
    for index, row in df.iterrows():
        for column in df.columns:
            if column.startswith(model) and pd.isna(row[column]):
                print(f"Empty cell in {column} at index {index+2}")


def check_model_cleanliness(model):
    for criterion in CRITERION_PATHS:
        print("############################################")
        print(f"##########  {criterion}  ##########")
        print("##########  BioASQ Extreme ##########")
        check_for_empty_cells(pd.read_excel(f"data/safe/{criterion}/BioASQ_dataset_adversarial_extreme_per_model_evaluation_{criterion}_{model}_clean.xlsx"), model)
        print("##########  BioASQ Subtle  ##########")
        check_for_empty_cells(pd.read_excel(f"data/safe/{criterion}/BioASQ_dataset_adversarial_subtle_per_model_evaluation_{criterion}_{model}_clean.xlsx"), model)
        print("##########  LLMs4Syn Extreme  ##########")
        check_for_empty_cells(pd.read_excel(f"data/safe/{criterion}/llm4syn_dataset_adversarial_extreme_per_model_evaluation_{criterion}_{model}_clean.xlsx"), model)
        print("##########  LLMs4Syn Subtle  ##########")
        check_for_empty_cells(pd.read_excel(f"data/safe/{criterion}/llm4syn_dataset_adversarial_subtle_per_model_evaluation_{criterion}_{model}_clean.xlsx"), model)


def check_original_synthesis_cleanliness(model):
    print("##########  BioASQ Synthesis ##########")
    check_for_empty_cells(pd.read_excel(f"data/safe/synthesis_evaluation/BioASQ_dataset_synthesis_per_model_evaluation_{model}_clean.xlsx"), model)
    print("##########  LLMs4Syn Synthesis ##########")
    check_for_empty_cells(pd.read_excel(f"data/safe/synthesis_evaluation/llm4syn_dataset_synthesis_per_model_evaluation_{model}_clean.xlsx"), model)


def clean_original_synthesis():
    for model in MODELS[1:3]:
        create_clean_json(f"data/safe/synthesis_evaluation/BioASQ_dataset_synthesis_per_model_evaluation_{model}.xlsx", model)
        create_clean_json(f"data/safe/synthesis_evaluation/llm4syn_dataset_synthesis_per_model_evaluation_{model}.xlsx", model)
    

def create_clean_jsons(criteria, criterion_path):
    for model in MODELS[1:2]:
        create_clean_json(f"data/safe/{criterion_path}/BioASQ_dataset_adversarial_extreme_per_model_evaluation_{criterion_path}_{model}.xlsx", model, criteria)
        create_clean_json(f"data/safe/{criterion_path}/BioASQ_dataset_adversarial_subtle_per_model_evaluation_{criterion_path}_{model}.xlsx", model, criteria)
        create_clean_json(f"data/safe/{criterion_path}/llm4syn_dataset_adversarial_extreme_per_model_evaluation_{criterion_path}_{model}.xlsx", model, criteria)
        create_clean_json(f"data/safe/{criterion_path}/llm4syn_dataset_adversarial_subtle_per_model_evaluation_{criterion_path}_{model}.xlsx", model, criteria)


def combine_bioasq_extreme(eval_model):
    criterion_path = ["rcic", "completeness", "integration", "cohesion", "readability", "conciseness"]

    df = pd.read_excel(f"data/safe/rcic/BioASQ_dataset_adversarial_extreme_per_model_evaluation_rcic_{eval_model}_clean.xlsx")

    for crit in criterion_path[1:]:
        df2 = pd.read_excel(f"data/safe/{crit}/BioASQ_dataset_adversarial_extreme_per_model_evaluation_{crit}_{eval_model}_clean.xlsx")

        for index, row in df2.iterrows():
            df.at[index, f"{eval_model}_evaluation_scores_qwen2.5-72b-instruct"] += row[f"{eval_model}_evaluation_scores_qwen2.5-72b-instruct"]
            df.at[index, f"{eval_model}_evaluation_scores_meta-llama-3.1-70b-instruct"] += row[f"{eval_model}_evaluation_scores_meta-llama-3.1-70b-instruct"]
            df.at[index, f"{eval_model}_evaluation_scores_meta-llama-3.1-8b-instruct"] += row[f"{eval_model}_evaluation_scores_meta-llama-3.1-8b-instruct"]
            df.at[index, f"{eval_model}_evaluation_scores_mistral-large-instruct"] += row[f"{eval_model}_evaluation_scores_mistral-large-instruct"]
        
        df2_last_4 = df2.iloc[:, -4:]
        for col in df2_last_4.columns:
            df[col] = df2_last_4[col]

    df = pd.concat([df.iloc[:, :-80], df.reindex(sorted(df.columns[-80:-76]), axis=1), df.reindex(sorted(df.columns[-76:-40]), axis=1), df.reindex(sorted(df.columns[-40:-36]), axis=1), df.reindex(sorted(df.columns[-36:]) , axis=1)], axis=1)
    df.to_excel(f"data/safe/cleaned/adversarial_extreme/BioASQ_extreme_{eval_model}_clean.xlsx", index=False)


def combine_bioasq_subtle(eval_model):
    criterion_path = ["rcic", "completeness", "integration", "cohesion", "readability", "conciseness"]

    df = pd.read_excel(f"data/safe/rcic/BioASQ_dataset_adversarial_subtle_per_model_evaluation_rcic_{eval_model}_clean.xlsx")

    for crit in criterion_path[1:]:
        df2 = pd.read_excel(f"data/safe/{crit}/BioASQ_dataset_adversarial_subtle_per_model_evaluation_{crit}_{eval_model}_clean.xlsx")

        for index, row in df2.iterrows():
            df.at[index, f"{eval_model}_evaluation_scores_qwen2.5-72b-instruct"] += row[f"{eval_model}_evaluation_scores_qwen2.5-72b-instruct"]
            df.at[index, f"{eval_model}_evaluation_scores_meta-llama-3.1-70b-instruct"] += row[f"{eval_model}_evaluation_scores_meta-llama-3.1-70b-instruct"]
            df.at[index, f"{eval_model}_evaluation_scores_meta-llama-3.1-8b-instruct"] += row[f"{eval_model}_evaluation_scores_meta-llama-3.1-8b-instruct"]
            df.at[index, f"{eval_model}_evaluation_scores_mistral-large-instruct"] += row[f"{eval_model}_evaluation_scores_mistral-large-instruct"]
        
        df2_last_4 = df2.iloc[:, -4:]
        for col in df2_last_4.columns:
            df[col] = df2_last_4[col]

    df = pd.concat([df.iloc[:, :-80], df.reindex(sorted(df.columns[-80:-76]), axis=1), df.reindex(sorted(df.columns[-76:-40]), axis=1), df.reindex(sorted(df.columns[-40:-36]), axis=1), df.reindex(sorted(df.columns[-36:]) , axis=1)], axis=1)
    df.to_excel(f"data/safe/cleaned/adversarial_subtle/BioASQ_subtle_{eval_model}_clean.xlsx", index=False)


def combine_llm4syn_extreme(eval_model):
    criterion_path = ["rcic", "completeness", "integration", "cohesion", "readability", "conciseness"]

    df = pd.read_excel(f"data/safe/rcic/llm4syn_dataset_adversarial_extreme_per_model_evaluation_rcic_{eval_model}_clean.xlsx")

    for crit in criterion_path[1:]:
        df2 = pd.read_excel(f"data/safe/{crit}/llm4syn_dataset_adversarial_extreme_per_model_evaluation_{crit}_{eval_model}_clean.xlsx")

        for index, row in df2.iterrows():
            df.at[index, f"{eval_model}_evaluation_scores_qwen2.5-72b-instruct"] += row[f"{eval_model}_evaluation_scores_qwen2.5-72b-instruct"]
            df.at[index, f"{eval_model}_evaluation_scores_meta-llama-3.1-70b-instruct"] += row[f"{eval_model}_evaluation_scores_meta-llama-3.1-70b-instruct"]
            df.at[index, f"{eval_model}_evaluation_scores_meta-llama-3.1-8b-instruct"] += row[f"{eval_model}_evaluation_scores_meta-llama-3.1-8b-instruct"]
            df.at[index, f"{eval_model}_evaluation_scores_mistral-large-instruct"] += row[f"{eval_model}_evaluation_scores_mistral-large-instruct"]
        
        df2_last_4 = df2.iloc[:, -4:]
        for col in df2_last_4.columns:
            df[col] = df2_last_4[col]

    df = pd.concat([df.iloc[:, :-80], df.reindex(sorted(df.columns[-80:-76]), axis=1), df.reindex(sorted(df.columns[-76:-40]), axis=1), df.reindex(sorted(df.columns[-40:-36]), axis=1), df.reindex(sorted(df.columns[-36:]) , axis=1)], axis=1)
    df.to_excel(f"data/safe/cleaned/adversarial_extreme/llm4syn_extreme_{eval_model}_clean.xlsx", index=False)


def combine_llm4syn_subtle(eval_model):
    criterion_path = ["rcic", "completeness", "integration", "cohesion", "readability", "conciseness"]

    df = pd.read_excel(f"data/safe/rcic/llm4syn_dataset_adversarial_subtle_per_model_evaluation_rcic_{eval_model}_clean.xlsx")

    for crit in criterion_path[1:]:
        df2 = pd.read_excel(f"data/safe/{crit}/llm4syn_dataset_adversarial_subtle_per_model_evaluation_{crit}_{eval_model}_clean.xlsx")

        for index, row in df2.iterrows():
            df.at[index, f"{eval_model}_evaluation_scores_qwen2.5-72b-instruct"] += row[f"{eval_model}_evaluation_scores_qwen2.5-72b-instruct"]
            df.at[index, f"{eval_model}_evaluation_scores_meta-llama-3.1-70b-instruct"] += row[f"{eval_model}_evaluation_scores_meta-llama-3.1-70b-instruct"]
            df.at[index, f"{eval_model}_evaluation_scores_meta-llama-3.1-8b-instruct"] += row[f"{eval_model}_evaluation_scores_meta-llama-3.1-8b-instruct"]
            df.at[index, f"{eval_model}_evaluation_scores_mistral-large-instruct"] += row[f"{eval_model}_evaluation_scores_mistral-large-instruct"]
        
        df2_last_4 = df2.iloc[:, -4:]
        for col in df2_last_4.columns:
            df[col] = df2_last_4[col]

    df = pd.concat([df.iloc[:, :-80], df.reindex(sorted(df.columns[-80:-76]), axis=1), df.reindex(sorted(df.columns[-76:-40]), axis=1), df.reindex(sorted(df.columns[-40:-36]), axis=1), df.reindex(sorted(df.columns[-36:]) , axis=1)], axis=1)
    df.to_excel(f"data/safe/cleaned/adversarial_subtle/llm4syn_subtle_{eval_model}_clean.xlsx", index=False)


def combine_dataframes(eval_model):
    combine_bioasq_extreme(eval_model)
    combine_bioasq_subtle(eval_model)
    combine_llm4syn_extreme(eval_model)
    combine_llm4syn_subtle(eval_model)


if __name__ == "__main__":
    # EVALUATION_CRITERIA = ["Relevancy", "Correctness", "Completeness", "Informativeness", "Integration", "Cohesion", "Coherence", "Readability", "Conciseness"]
    # MODELS = ["qwen2.5-72b-instruct", "meta-llama-3.1-70b-instruct", "meta-llama-3.1-8b-instruct", "mistral-large-instruct"]
    # CRITERION_PATHS = ["rcic", "completeness", "integration", "cohesion", "readability", "conciseness"]
    criteria = ["Relevancy", "Correctness", "Informativeness", "Coherence", "Completeness", "Integration", "Cohesion", "Readability", "Conciseness"]
    
    
    # create_clean_jsons(criteria[-1:], CRITERION_PATHS[-1])
    # check_model_cleanliness(MODELS[1])
    
    # clean_original_synthesis()
    check_original_synthesis_cleanliness(MODELS[2])

    #  combine_dataframes(MODELS[1])
    



