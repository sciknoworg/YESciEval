import os
from datasets import Dataset
from trl import CPOConfig, CPOTrainer
from peft import get_peft_model, LoraConfig, TaskType, prepare_model_for_kbit_training
import torch
from accelerate import Accelerator
from tqdm import tqdm

from sciqaeval import config, utils, llm_loader
from sciqaeval.prompt import Prompts
from sciqaeval.dataset import SciQAEvalSFTDataset

accelerator = Accelerator(mixed_precision='fp16')
device_map = {"": accelerator.process_index}
prompts = Prompts()

metadata = [
    # SFT (ORG) + RL (ADV)
    ["orkg-synthesis-rlhf-adv", "assets/sft-orkg-synthesis-org", "assets/rlhf-orkg-synthesis-adv", 1, 4500, 150, 100]
    ["bioasq-rlhf-adv", "assets/sft-bioasq-org", "assets/rlhf-bioasq-adv", 1, 4500, 150, 100],
    
    # SFT (ORG) + RL (ADV)
    ["orkg-synthesis-rlhf-adv-org", "assets/sft-orkg-synthesis-org", "assets/rlhf-orkg-synthesis-adv-org", 1, 4500, 150, 100],
    ["bioasq-rlhf-adv-org", "assets/sft-bioasq-org", "assets/rlhf-bioasq-adv-org", 1, 4500, 150, 100]
    
]
num_train_epochs = 2
learning_rate = 2e-4

for data_key, model_path, output_dir, batch_size, max_prompt_length, max_completion_length, quality_limit in metadata:
    max_length = max_prompt_length + max_completion_length
    path = config.datasets_path[data_key]
    dataset = utils.read_json(path)
    dataset_obj = SciQAEvalSFTDataset(prompts, quality_limit=quality_limit)
    model, tokenizer, peft_config = llm_loader.load_rlhf_model(model_id=model_path, 
                                                               token=config.huggingface_key, 
                                                               device_map=device_map)
    model = prepare_model_for_kbit_training(model)
    def prepare_dataset(examples, max_length_threshold):
        data = []
        for example in tqdm(examples):
            conversation = dataset_obj.preprocess_chatdata_rlhf_filtered(example, tokenizer, max_length_threshold)
            if conversation is not None:
                data.append(conversation)
        return data
    dataset = prepare_dataset(dataset, max_prompt_length)
    dataset_lst = Dataset.from_list(dataset)
    print(dataset_lst)
    # def format_data(row):
    #     return row
    # dataset_lst = dataset_lst.map(format_data, num_proc= os.cpu_count())
    training_args = CPOConfig(
        output_dir=output_dir,
        learning_rate=learning_rate,
        num_train_epochs=num_train_epochs,
        per_device_train_batch_size=batch_size,
        gradient_accumulation_steps=batch_size,
        max_length=max_length,
        fp16=True,
        # bf16=True,
        max_completion_length = max_completion_length,
        max_prompt_length = max_prompt_length,
        gradient_checkpointing_kwargs = {"use_reentrant": True},
        remove_unused_columns=False,
    )
    trainer = CPOTrainer(
        model,
        args=training_args,
        train_dataset=dataset_lst,
        processing_class=tokenizer,
        peft_config=peft_config
    )
    trainer.train()
    trainer.save_model(output_dir)