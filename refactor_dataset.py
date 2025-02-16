import os
import pandas as pd
import re
from openai import OpenAI
from typing import List
from pydantic import BaseModel
import time
from tqdm import tqdm
import math

from sciqaeval import config, utils

client = OpenAI(api_key=config.openai_key)

synthesizers = [
    "meta-llama-3.1-8b-instruct",
    "meta-llama-3.1-70b-instruct",
    "qwen2.5-72b-instruct",
    "mistral-large-instruct"
]

instruction = ("You are given a detailed evaluation of a scientific synthesis across various characteristics. "
               "Your task is to extract and structure the evaluation information for specific characteristic. "
               "Do not generate generate new rational.")


class Rationale(BaseModel):
    rationale: str

def find_rational_using_openai(quality, moderated_synthesis_evaluation_rating, synthesizer_scores_str):
    prompt = f"""Given a evaluation of the synthesis, now extract rationale for {quality} with rating of {moderated_synthesis_evaluation_rating}: \n

Text:
{synthesizer_scores_str}
"""
    messages = [
        {"role": "system", "content": instruction},
        {"role": "user", "content": prompt}
    ]
    while True:
        try:
            completion = client.beta.chat.completions.parse(
                model='gpt-4o-mini',
                messages=messages,
                response_format=Rationale,
                temperature=0,
            )
            return [completion.choices[0].message.parsed.rationale]
        except:
            time.sleep(5)
            
def find_rational(quality, moderated_synthesis_evaluation_rating, synthesizer_scores_str):
    patterns = [
        r'"(?P<category>\w+)":\s*\{\s*"rating":\s*"?(?P<rating>\d+)"?,\s*"rationale":\s*"(?P<rationale>[^"]+)"\s*\}',
        r'\*\*([\w\s]+):\*\*\s*\{rating:\s*(\d),\s*rationale:\s*"([^"]+)"\}',
        r'(\*\*[\w\s]+\*\*)\sRating:\s(\d)\sRationale:\s([^\*]+)',
        r'\*\*(.*?)\*\*:\s*\{rating:\s*(\d+),\s*rationale:\s*"([^"]+)"\}',
        r'(\*\*[\w\s]+):\*\*\s*{rating:\s*(\d+),\s*rationale:\s*"([^"]+)"\}'
    ]
    synthesizer_scores_str = re.sub(r'[\n\s]+', ' ', synthesizer_scores_str)
    moderated_synthesis_evaluation_rationale = []
    for pattern in patterns:
        matches = re.findall(pattern, str(synthesizer_scores_str))
        for category, rating, rationale in matches:
            category = category.replace("*", "").replace(":", "")
            if category == quality and int(rating) == moderated_synthesis_evaluation_rating:
                moderated_synthesis_evaluation_rationale.append(rationale)
    if len(moderated_synthesis_evaluation_rationale) == 0:
        rationale = find_rational_using_openai(quality=quality,
                                               moderated_synthesis_evaluation_rating=moderated_synthesis_evaluation_rating,
                                               synthesizer_scores_str=synthesizer_scores_str)
        moderated_synthesis_evaluation_rationale = rationale
    return moderated_synthesis_evaluation_rationale


def refactor(dataset_name, config, split='train', evaluator = "meta-llama-3.1-8b-instruct", root_dir = "dataset"):
    data_file_prefix = "llm4syn" if dataset_name == "ORKG-Synthesis" else "BioASQ"
    sample_id_column = "sample_id" if dataset_name == "ORKG-Synthesis" else "research_question"
    criteria = config.criteria
    papers_no = config.papers_no if dataset_name == "ORKG-Synthesis" else config.paper_no_bioasqa
    
    evaluator_files = {
        "extreme": os.path.join(root_dir, dataset_name, split, "adversarial_extreme", f'{data_file_prefix}_extreme_{evaluator}_clean.xlsx'),
        "subtle":  os.path.join(root_dir, dataset_name, split, "adversarial_subtle",  f'{data_file_prefix}_subtle_{evaluator}_clean.xlsx'),
        "original": os.path.join(root_dir, dataset_name, split, "original_synthesis", f'{data_file_prefix}_dataset_synthesis_per_model_evaluation_{evaluator}_clean.xlsx')
    }
    dataset = []
    error_in_rationale = 0

    for eval_type, path in evaluator_files.items():
        df = pd.read_excel(path)
        print("working on:", eval_type, " from path:", path)
        for df_index in tqdm(range(df.shape[0])):
            research_question = df['research_question'].tolist()[df_index]

            papers = []
            for title, abstract in zip([f'paper_{str(paper_idx + 1)}_title' for paper_idx in range(papers_no)],
                                       [f'paper_{str(paper_idx + 1)}_abstract' for paper_idx in range(papers_no)]):
                try:
                    if math.isnan(df[title].tolist()[df_index]) or math.isnan(df[abstract].tolist()[df_index]) :
                        continue
                except:
                    if len(df[title].tolist()[df_index]) != 0 and len(df[abstract].tolist()[df_index]) != 0:
                        papers.append({"title": str(df[title].tolist()[df_index]), "abstract": str(df[abstract].tolist()[df_index])})
            sample_id = df[sample_id_column].tolist()[df_index]
            for synthesizer in synthesizers:
                synthesis = df[f"{synthesizer}_synthesis"].tolist()[df_index]

                for quality in criteria:
                    synthesizer_scores_str = df[f"{evaluator}_evaluation_scores_{synthesizer}"].tolist()[df_index]
                    synthesis_evaluation_rating = df[f"{evaluator}_{synthesizer}_{quality}"].tolist()[df_index]
                    
                    if eval_type != 'original':
                        synthesizer_synthesis = df[f"{synthesizer}_{eval_type}_{quality.lower()}"].tolist()[df_index]
                    else:
                        synthesizer_synthesis = df[f"{synthesizer}_synthesis"].tolist()[df_index]

                    synthesis_evaluation_rationale = find_rational(quality, synthesis_evaluation_rating, synthesizer_scores_str) 
                    if len(synthesis_evaluation_rationale) == 0:
                        error_in_rationale += 1

                    dataset.append({
                        "sample_id": sample_id,
                        "eval_type": eval_type,
                        "quality": quality,
                        "synthesizer_model": synthesizer,
                        "evaluator_model": evaluator,
                        "research_question": research_question,
                        "synthesizer_synthesis": synthesizer_synthesis,
                        "synthesis_evaluation_rating": synthesis_evaluation_rating,
                        "synthesis_evaluation_rationale": synthesis_evaluation_rationale,
                        "papers": papers,
                        "original-synthesis": synthesis,
                        "evaluation": synthesizer_scores_str
                    })
    if evaluator == 'meta-llama-3.1-8b-instruct' and split == 'test':
        utils.save_json(data=dataset, file_path= os.path.join(root_dir, dataset_name, f"{data_file_prefix}_{split}_refactored_dataset.json"))
    else:
        utils.save_json(data=dataset, file_path= os.path.join(root_dir, dataset_name, f"{data_file_prefix}_{split}_{evaluator}_refactored_dataset.json"))
    print(f"{data_file_prefix} size:", len(dataset))
    print(f"{data_file_prefix} error in rationale:", error_in_rationale)



print("refactor ORKG-Synthesis-train....")
refactor(dataset_name="ORKG-Synthesis", config=config, split='train')
print("refactor ORKG-Synthesis-test....")
refactor(dataset_name="ORKG-Synthesis",  config=config, split='test')
refactor(dataset_name="ORKG-Synthesis", config=config, split='train', evaluator="meta-llama-3.1-70b-instruct")
refactor(dataset_name="ORKG-Synthesis", config=config, split='test', evaluator="meta-llama-3.1-70b-instruct")
refactor(dataset_name="ORKG-Synthesis", config=config, split='train', evaluator="qwen2.5-72b-instruct")
refactor(dataset_name="ORKG-Synthesis", config=config, split='test', evaluator="qwen2.5-72b-instruct")
refactor(dataset_name="ORKG-Synthesis", config=config, split='train', evaluator="mistral-large-instruct")
refactor(dataset_name="ORKG-Synthesis", config=config, split='test', evaluator="mistral-large-instruct")


print("refactor BioASQ-train....")
refactor(dataset_name="BioASQ", config=config, split='train')
print("refactor BioASQ-test....")
refactor(dataset_name="BioASQ", config=config, split='test')
refactor(dataset_name="BioASQ", config=config, split='train', evaluator="meta-llama-3.1-70b-instruct")
refactor(dataset_name="BioASQ", config=config, split='test', evaluator="meta-llama-3.1-70b-instruct")
refactor(dataset_name="BioASQ", config=config, split='train', evaluator="qwen2.5-72b-instruct")
refactor(dataset_name="BioASQ", config=config, split='test', evaluator="qwen2.5-72b-instruct")
refactor(dataset_name="BioASQ", config=config, split='train', evaluator="mistral-large-instruct")
refactor(dataset_name="BioASQ", config=config, split='test', evaluator="mistral-large-instruct")
