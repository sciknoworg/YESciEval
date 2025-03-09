import pandas as pd
from sklearn.model_selection import train_test_split
import os
from sciqaeval import utils, config

root_dir = "dataset"
test_size = config.test_size

for dataset_name, dataset_prefix in [('BioASQ', 'BioASQ'), ('ORKG-Synthesis', 'llm4syn')]:
    dataset_path = os.path.join(root_dir, dataset_name, "all", f"{dataset_prefix}_dataset_synthesis.xlsx")
    df = pd.read_excel(dataset_path)
    print(f"\n{dataset_name} Shape:", df.shape)
    ID ='research_question' if dataset_name == 'BioASQ' else 'sample_id'
    identifier = df[ID].tolist()
    train_id, test_id = train_test_split(identifier, test_size=test_size)
    print(f"train size: {len(train_id)}, test size: {len(test_id)}")
    train_test_split_data = {"train": train_id, "test": test_id}
    utils.save_json(data=train_test_split_data,  file_path=os.path.join(root_dir, dataset_name, "train_test_split_ids.json"))
    for split_dir in ["train", "test"]:
        split_dir_path = os.path.join(root_dir, dataset_name, split_dir)
        utils.mkdir(split_dir_path)
        for dataset_variant_dir in ['adversarial_extreme', 'adversarial_subtle', 'original_synthesis']:
            dataset_variant_dir_input_path = os.path.join(root_dir, dataset_name, "all", dataset_variant_dir)
            dataset_variant_dir_output_path = os.path.join(root_dir, dataset_name, split_dir, dataset_variant_dir)
            utils.mkdir(dataset_variant_dir_output_path)
            for file in os.listdir(dataset_variant_dir_input_path):
                if not file.endswith(".xlsx"):
                    continue
                file_input_path = os.path.join(dataset_variant_dir_input_path, file)
                file_output_path = os.path.join(dataset_variant_dir_output_path, file)
                data = pd.read_excel(file_input_path)
                data_df = data[data[ID].isin(train_test_split_data[split_dir])]
                data_df.to_excel(file_output_path, index=False)
        for adv_text in ['adversarial_extreme_clean', 'adversarial_subtle_clean', 'synthesis']:
            adv_text_input_path = os.path.join(root_dir, dataset_name, "all", f'{dataset_prefix}_dataset_{adv_text}.xlsx')
            adv_text_output_path = os.path.join(root_dir, dataset_name,  split_dir, f'{dataset_prefix}_dataset_{adv_text}.xlsx')
            data = pd.read_excel(adv_text_input_path)
            data_df = data[data[ID].isin(train_test_split_data[split_dir])]
            data_df.to_excel(adv_text_output_path, index=False)