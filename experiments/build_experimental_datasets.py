from sciqaeval import config, utils
from sciqaeval.dataset import SciQAEvalDataset
import os

def build_experimental_sets(path, root_dir, data_file_prefix):
    dataset = utils.read_json(path)
    
    print("Working on: ", root_dir)
    print("--------------------------------------------------------")
    print("Dataset size is:", len(dataset))
    print("Dataset keys:", dataset[0].keys())
    data_obj = SciQAEvalDataset(config=config)

    print("----------------------------EXP-1 SFT (ORG) ----------------------------")
    original_data = data_obj.get_sft_dataset(dataset, data_type='original')
    print("original_data size:", len(original_data))
    org_sft_out = os.path.join(root_dir, f"{data_file_prefix}_ORG_train_combined_refactored_dataset.json")
    print("Saving data at:", org_sft_out)
    utils.save_json(data=original_data, file_path=org_sft_out)
    
    print("----------------------------EXP-2 RLHF (ADV) ----------------------------")
    extrem_data = data_obj.get_rlhf_dataset(dataset, data_type='extreme')
    print("extrem_data size:", len(extrem_data))
    subtle_data = data_obj.get_rlhf_dataset(dataset, data_type='subtle')
    print("subtle_data size:", len(subtle_data))
    exp1_rlhf =  extrem_data + subtle_data
    print("total size for exp1_rlhf:", len(exp1_rlhf))
    exp1_rlhf_out = os.path.join(root_dir, f"{data_file_prefix}_RLHF_train_combined_refactored_dataset.json")
    print("Saving data at:", exp1_rlhf_out)
    utils.save_json(data=exp1_rlhf, file_path=exp1_rlhf_out)
    
    print("----------------------------EXP-3 RLHF (ADV+ORG) ----------------------------")
    extrem_data = data_obj.get_rlhf_dataset(dataset, data_type='extreme')
    print("extrem_data size:", len(extrem_data))
    subtle_data = data_obj.get_rlhf_dataset(dataset, data_type='subtle')
    print("subtle_data size:", len(subtle_data))
    original_data = data_obj.build_rlhf_with_original(dataset)
    print("original_data size:", len(original_data))
    exp2_rlhf =  extrem_data + subtle_data + original_data
    print("total size for exp2_rlhf:", len(exp2_rlhf))
    exp2_rlhf_out = os.path.join(root_dir, f"{data_file_prefix}_RLHF_ADV+ORG_train_combined_refactored_dataset.json")
    print("Saving data at:", exp2_rlhf_out)
    utils.save_json(data=exp2_rlhf, file_path=exp2_rlhf_out)
    
    
dataset_name = "ORKG-Synthesis"
path = config.datasets_path['orkg-synthesis-combined'] if dataset_name == "ORKG-Synthesis" else config.datasets_path['bioasq-combined']
data_file_prefix = "llm4syn" if dataset_name == "ORKG-Synthesis" else "BioASQ"
root_dir = os.path.join("dataset", dataset_name)
build_experimental_sets(path, root_dir, data_file_prefix)

dataset_name = "BioASQ"
path = config.datasets_path['orkg-synthesis-combined'] if dataset_name == "ORKG-Synthesis" else config.datasets_path['bioasq-combined']
data_file_prefix = "llm4syn" if dataset_name == "ORKG-Synthesis" else "BioASQ"
root_dir = os.path.join("dataset", dataset_name)
build_experimental_sets(path, root_dir, data_file_prefix)