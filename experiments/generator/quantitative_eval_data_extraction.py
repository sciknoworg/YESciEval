import pandas as pd
import seaborn as sns
from collections import defaultdict
import matplotlib.pyplot as plt


METRICS = ["bertscoreF1", "moverscore", "wmd_specter", "wmd_scibert", "bleu", "rouge1F1", "rouge2F1", "rouge4F1", "rougeLF1", "nist", "meteor", "wer"]
CONVERSION = {"meta-llama-3.1-70b-instruct": "Llama 70B", "meta-llama-3.1-8b-instruct": "Llama 8B", "mistral-large-instruct": "Mistral", "qwen2.5-72b-instruct": "Qwen" }

def generate_table(file_path, start_i):
    df = pd.read_excel(file_path)

    mean_dict = defaultdict(list)
    for col in df.columns[start_i:]:
        split_col = col.split("_")
        metric = split_col[0]
        i = 1
        if metric == "wmd":
            metric += "_" + split_col[1]
            i += 1
        reference = CONVERSION[split_col[i]]
        candidate = CONVERSION[split_col[i+1]]

        mean_dict[metric].append((reference, candidate, df[col].mean()))

    for metric, values in mean_dict.items():

        data = pd.DataFrame(values, columns=["Reference", "Candidate", "Mean Score"])
        matrix = data.pivot(index="Reference", columns="Candidate", values="Mean Score")

        # Plot the heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(matrix, annot=True, annot_kws={"size": 15}, cmap="YlGnBu", fmt=".2f", linewidths=0.5)
        plt.xticks(rotation=45)
        plt.title(f"Heatmap for {metric}", fontsize=16)
        plt.xlabel("Candidate", fontsize=14)
        plt.ylabel("Reference", fontsize=14)
        plt.tight_layout()
        plt.savefig(f"data/temp/clean_plots/{file_path.split("/")[-1].split("_")[0]}_{metric}.png")
        plt.close()
        # plt.show()
        


def main():
    generate_table("data/quantitative_eval_scores/BioASQ_dataset_quantitative.xlsx", 85)
    generate_table("data/quantitative_eval_scores/ORKGSyn_dataset_quantitative.xlsx", 23)


if __name__ == "__main__":
    main()