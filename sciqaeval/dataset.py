from typing import List, Dict
import math
from collections import defaultdict

class SciQAEvalDataset:
    
    def __init__(self, config):
        self.config = config
    
    def build_dataset_dict(self, dataset, data_type):
        dataset_dict = defaultdict(list)
        for data in dataset:
            if data['eval_type'] == data_type:
                dataset_dict[data['sample_id']].append(data)
        return dataset_dict
        
    def get_valid_pairs(self, ratings, indexes, threshold=1):
        valid_pairs = []
        for i in indexes:
            for j in indexes:
                if i != j and ratings[i] <= threshold and ratings[j] > threshold:
                    valid_pairs.append((i, j))
        return valid_pairs
    
    def build_rlhf_curated_dataset(self, dataset_dict, threshold):
        freq = defaultdict(int)
        curated_dataset = []
        for sample_id, sample in dataset_dict.items():
            criteria_dict = defaultdict(list)
            for synthesis in sample:
                criteria_dict[synthesis['quality']].append(synthesis)
            for criteria, criteria_rating in criteria_dict.items():
                ratings = [rating['synthesis_evaluation_rating'] for rating in criteria_rating]
                indexes = [index for index in range(len(criteria_rating))]
                valid_pairs = self.get_valid_pairs(ratings, indexes, threshold=threshold)
                for chosen_idx, rejected_idx in valid_pairs:
                    curated_dataset.append({"chosen": criteria_rating[chosen_idx], 
                                            "reject": criteria_rating[rejected_idx],
                                            "criteria": criteria})
                    freq[criteria] += 1
        print(dict(freq))
        return curated_dataset

    def get_rlhf_dataset(self, dataset, data_type: str):
        desirable_rating_threshold = self.config.desirable_adv_rating_thresholds[data_type]
        dataset_dict = self.build_dataset_dict(dataset, data_type)
        curated_dataset = self.build_rlhf_curated_dataset(dataset_dict, desirable_rating_threshold)
        return curated_dataset
    
    def build_sft_curated_dataset(self, dataset_dict, threshold):
        freq = defaultdict(int)
        curated_dataset = []
        for sample_id, sample in dataset_dict.items():
            criteria_dict = defaultdict(list)
            for synthesis in sample:
                criteria_dict[synthesis['quality']].append(synthesis)
            for criteria, criteria_rating in criteria_dict.items():
                for rating in criteria_rating:
                    if rating['synthesis_evaluation_rating'] <= threshold:
                        curated_dataset.append(rating)
                        freq[criteria] += 1
        print(dict(freq))
        return curated_dataset
    
    def get_sft_dataset(self, dataset, data_type: str):
        desirable_rating_threshold = self.config.desirable_adv_rating_thresholds[data_type]
        dataset_dict = self.build_dataset_dict(dataset, data_type)
        curated_dataset = self.build_sft_curated_dataset(dataset_dict, desirable_rating_threshold)
        return curated_dataset
    
    def build_rlhf_with_original(self, dataset):
        dataset_dict = self.build_dataset_dict(dataset, "original")
        subtle_dict = self.build_dataset_dict(dataset, "subtle")
        extreme_dict = self.build_dataset_dict(dataset, "extreme")
        
        curated_dataset = []
        freq = defaultdict(int)
        
        for sample_id, original_samples in dataset_dict.items():
            if sample_id not in subtle_dict and sample_id not in extreme_dict:
                continue  # Skip if no adversarial samples exist
            
            criteria_dict = defaultdict(list)
            for original in original_samples:
                criteria_dict[original['quality']].append(original)
            
            for criteria, chosen_samples in criteria_dict.items():
                reject_samples = []
                
                if sample_id in subtle_dict:
                    reject_samples.extend([
                        s for s in subtle_dict[sample_id] 
                        if s['quality'] == criteria and s['synthesis_evaluation_rating'] <= 3
                    ])
                
                if sample_id in extreme_dict:
                    reject_samples.extend([
                        e for e in extreme_dict[sample_id] 
                        if e['quality'] == criteria and e['synthesis_evaluation_rating'] <= 1
                    ])
                
                for chosen in chosen_samples:
                    for reject in reject_samples:
                        curated_dataset.append({
                            "chosen": chosen,
                            "reject": reject,
                            "criteria": criteria
                        })
                        freq[criteria] += 1
        
        print(dict(freq))
        return curated_dataset
    
class SciQAEvalSFTDataset:
    def __init__(self, prompts, quality_limit=1000):
        self.prompts = prompts
        self.quality_counts = defaultdict(lambda: defaultdict(int))
        self.quality_limit = quality_limit

    def build_user_prompt(self, dataset_dict):
        question = dataset_dict['research_question']
        synthesis = dataset_dict['synthesizer_synthesis']
        user_prompt_text = "Evaluate and rate the quality of the following scientific synthesis according to the characteristics given in the system prompt."
        content = self.format_paper_content(dataset_dict['papers'])
        current_prompt = f"{user_prompt_text}\n\n<scientific-synthesis>{synthesis}</scientific-synthesis>\n\n<research-question>{question}</research-question>\n\n<paper-titles-and-abstracts>\n{content}</paper-titles-and-abstracts>\n\n###"
        return current_prompt

    def format_paper_content(self, papers):
        paper_content = ""
        for idx, paper in enumerate(papers):
            title, abstract = paper["title"], paper["abstract"]
            paper_content += f"{idx+1}. " + title + "\n\n" + abstract + "\n\n"
        return paper_content

    def build_output(self, dataset_dict):
        criteria = dataset_dict['quality']
        rationale = dataset_dict['synthesis_evaluation_rationale'][0]
        rating =  dataset_dict['synthesis_evaluation_rating']
        output = f'{{"{criteria}": {{"rating": {rating}, "rationale": "{rationale}"}}}}'
        return output

    def preprocess_chat_data_sft(self, dataset_dict):
        user_prompt = self.build_user_prompt(dataset_dict)
        system_prompt = self.prompts.get_prompt(dataset_dict['quality'])
        output = self.build_output(dataset_dict)
        message = [
            {"role": "system", "content": system_prompt}, 
            {"role": "user", "content": user_prompt},
            {"role": "assistant", "content": output}
        ]
        return message, output
    
    def preprocess_chat_data_rlhf(self, dataset_dict):
        user_prompt = self.build_user_prompt(dataset_dict['chosen'])
        system_prompt = self.prompts.get_prompt(dataset_dict['criteria'])
        
        chosen_output = self.build_output(dataset_dict['chosen'])
        reject_output = self.build_output(dataset_dict['reject'])
        
        message = {
            "prompt": [
                # {"role": "user", "content": system_prompt + "\n\n" + user_prompt}  
                        {"role": "system", "content": system_prompt}, 
                       {"role": "user", "content": user_prompt}
                      ],
            "chosen": [{"role": "assistant", "content": chosen_output}],
            "rejected": [{"role": "assistant", "content": reject_output}],
        }
        return message
    
    def preprocess_chat_data_inf(self, dataset_dict):
        user_prompt = self.build_user_prompt(dataset_dict)
        system_prompt = self.prompts.get_prompt(dataset_dict['quality'])
        message = [
            {"role": "system", "content": system_prompt}, 
            {"role": "user", "content": user_prompt}
        ]
        return message
    

    def preprocess_chatdata_rlhf_filtered(self, dataset_dict, tokenizer, max_length_threshold):
        quality = dataset_dict['chosen']['quality']
        eval_type = dataset_dict['chosen']['eval_type']
        
        user_prompt = self.build_user_prompt(dataset_dict['chosen'])
        system_prompt = self.prompts.get_prompt(dataset_dict['criteria'])
        
        chosen_output = self.build_output(dataset_dict['chosen'])
        reject_output = self.build_output(dataset_dict['reject'])

        
        if self.quality_counts[eval_type][quality] >= self.quality_limit:
            return None  # Skip this sample if the limit is reached

        formatted_input = tokenizer.apply_chat_template([{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}], 
                                                         tokenize=False, add_generation_prompt=True) 
        if len(tokenizer(formatted_input).input_ids) > max_length_threshold:
            return None # Skip this sample if the prompt size is above max lenght threshold!

        self.quality_counts[eval_type][quality] += 1
        
        message = {
            "prompt": [
                {"role": "system", "content": system_prompt}, 
                {"role": "user", "content": user_prompt}
            ],
            "chosen": [{"role": "assistant", "content": chosen_output}],
            "rejected": [{"role": "assistant", "content": reject_output}],
        }
        return message

    