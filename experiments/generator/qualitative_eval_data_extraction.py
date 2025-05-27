import pandas as pd
import numpy as np


MODELS = ["qwen2.5-72b-instruct", "meta-llama-3.1-70b-instruct", "meta-llama-3.1-8b-instruct", "mistral-large-instruct"]
EVALUATION_CRITERIA = ["Relevancy", "Correctness", "Completeness", "Informativeness", "Integration", "Cohesion", "Coherence", "Readability", "Conciseness"]
SHORT_NAMES = ["Qwen", "Llama 70B", "Llama 8B", "Mistral"]


def get_average_scores(degree):
    # get the average scores for each model for each criterion

    folder_path = f"data/safe/cleaned/{degree}"
    average_scores = {}
    bioasq_average = {}
    llms4syn_average = {}
    for model in MODELS:
        BioASQ_scores = get_average_score_per_criterion(f"{folder_path}/BioASQ_{degree}_{model}_clean.xlsx", model)
        avg_model_score = np.mean([BioASQ_scores[target_model]["Average"] for target_model in MODELS])
        BioASQ_scores["Average"] = avg_model_score
        bioasq_average[model] = {t_mod: BioASQ_scores[t_mod]["Average"] for t_mod in MODELS}

        LLMs4Syn_scores = get_average_score_per_criterion(f"{folder_path}/llm4syn_{degree}_{model}_clean.xlsx", model)
        avg_model_score = np.mean([LLMs4Syn_scores[target_model]["Average"] for target_model in MODELS])
        LLMs4Syn_scores["Average"] = avg_model_score
        llms4syn_average[model] = {t_mod: LLMs4Syn_scores[t_mod]["Average"] for t_mod in MODELS}

        average_scores[model] = {"BioASQ": BioASQ_scores, "LLMs4Syn": LLMs4Syn_scores}
    
    new_index = {MODELS[i]: "Eval " + SHORT_NAMES[i] for i in range(len(MODELS))}
    new_columns = {MODELS[i]: SHORT_NAMES[i] for i in range(len(MODELS))}
    out_df = pd.DataFrame(bioasq_average).T
    out_df = out_df.round(4)
    out_df.rename(index= new_index, columns=new_columns, inplace=True)
    out_df.to_csv(f"{folder_path}/bioasq_average.csv")
    out_df = pd.DataFrame(llms4syn_average).T
    out_df = out_df.round(4)
    out_df.rename(index= new_index, columns=new_columns, inplace=True)
    out_df.to_csv(f"{folder_path}/llms4syn_average.csv")

    return average_scores


def get_average_score_per_criterion(path, model):
    # get the average score for each criterion for the given model

    df = pd.read_excel(path)
    average_scores = {}
    for target_model in MODELS:
        model_scores = {}
        for criterion in EVALUATION_CRITERIA:
            model_scores[criterion] = df[f"{model}_{target_model}_{criterion}"].mean(skipna=True)
        model_scores["Average"] = sum(model_scores.values()) / len(model_scores)
        average_scores[target_model] = model_scores

    
    out_df = pd.DataFrame(average_scores)
    out_df = out_df.round(4)
    new_columns = {MODELS[i]: SHORT_NAMES[i] for i in range(len(MODELS))}
    out_df.rename(columns=new_columns, inplace=True)
    out_df.to_csv(f"{path[:-5]}_scores.csv")
            
    return average_scores


def check_low_scores(syn_scores, subtle_scores, extreme_scores):

    for model in MODELS:
        print(f"######## {model} ########")
        print(f"Original Synthesis: BioASQ - {syn_scores[model]['BioASQ']['Average']} | LLMs4Syn - {syn_scores[model]['LLMs4Syn']['Average']}")
        print(f"Subtle Adversarial: BioASQ - {subtle_scores[model]['BioASQ']['Average']} | LLMs4Syn - {subtle_scores[model]['LLMs4Syn']['Average']}")
        print(f"Extreme Adversarial: BioASQ - {extreme_scores[model]['BioASQ']['Average']} | LLMs4Syn - {extreme_scores[model]['LLMs4Syn']['Average']}")
        

def check_self_bias(syn_scores, subtle_scores, extreme_scores):
    for target_model in MODELS:
        print(f"######## {target_model} ########")
        print("Original Synthesis: BioASQ")
        for model in MODELS:
            print(f"{syn_scores[model]['BioASQ'][target_model]['Average']}")
        print("Original Synthesis: LLMs4Syn")
        for model in MODELS:
            print(f"{syn_scores[model]['LLMs4Syn'][target_model]['Average']}")


def create_average_score_per_criterion_table(syn_scores, subtle_scores, extreme_scores):
    out = {}
    for model in MODELS:
        
        out["Original BioASQ"] = get_average_score_per_criterion_per_model(model, syn_scores, "BioASQ")
        out["Original LLMs4Syn"] = get_average_score_per_criterion_per_model(model, syn_scores, "LLMs4Syn")
        out["Subtle BioASQ"] = get_average_score_per_criterion_per_model(model, subtle_scores, "BioASQ")
        out["Subtle LLMs4Syn"] = get_average_score_per_criterion_per_model(model, subtle_scores, "LLMs4Syn")
        out["Extreme BioASQ"] = get_average_score_per_criterion_per_model(model, extreme_scores, "BioASQ")
        out["Extreme LLMs4Syn"] = get_average_score_per_criterion_per_model(model, extreme_scores, "LLMs4Syn")

        df = pd.DataFrame(out)
        df = df.round(4)
        df.to_csv(f"data/safe/cleaned/synthesis/ScoresPerCriterion_{model}_synthesis.csv")


def get_average_score_per_criterion_per_model(model, scores, dataset):
    table = {}
    for criterion in EVALUATION_CRITERIA:
        sum = 0
        for target_model in MODELS:
            sum += scores[model][dataset][target_model][criterion]
        table[criterion] = sum / len(MODELS)
    return table


def manual_mean(path, model):
    # get the average score for each criterion for the given model
    df = pd.read_excel(path)
    average_scores = {}
    for target_model in MODELS:
        model_scores = {}
        for criterion in EVALUATION_CRITERIA:
            count = 0
            addition = 0
            for val in df[f"{model}_{target_model}_{criterion}"]:
                if not pd.isna(val):
                    count += 1
                    addition += int(val)
            model_scores[criterion] = addition / count

        average_scores[target_model] = model_scores
            
    return average_scores


def main():
    syn_scores = get_average_scores("synthesis")
    subtle_scores = get_average_scores("subtle")
    extreme_scores = get_average_scores("extreme")

    # check_low_scores(syn_scores, subtle_scores, extreme_scores) 
    # check_self_bias(syn_scores, subtle_scores, extreme_scores)
    create_average_score_per_criterion_table(syn_scores, subtle_scores, extreme_scores)


def test():
    df = pd.read_excel("data/safe/cleaned/synthesis/BioASQ_synthesis_qwen2.5-72b-instruct_clean.xlsx")
    for index, row in df.iterrows():
        count = 0
        for i in range(1, 41):
            if not pd.isna(row[f"paper_{i}_abstract"]):
                count += 1
            else:
                break
        print(count)

if __name__ == "__main__":
    main()

    # test()


# RQ1: adversarial = low scores: 
# Which LLM consistently provided low scores in the extreme adversarial scenario? Which LLM consistently provided low scores in the subtle adversarial scenario? 
# 
# RQ2: change of scores from normal to extreme: 
# out-of-the-box for each LLM did we observe the behavior change as evaluators in the normal, and adversarial scenarios: subtle & extreme? This can be discussed w.r.t. each LLM tested.
#
# RQ3: self-bias:
# did the LLM behavior change when it self-evaluated versus other-evaluated? - for normal synthesis - for subtle adversarial - for the extreme adversarial
# 
# RQ4: criteria differences:
# do some criteria have generally lower scores than others -> was the adversarial created content too difficult to spot?
