from sciqaeval import config, utils, llm_loader
from sciqaeval.prompt import Prompts
from sciqaeval.dataset import SciQAEvalSFTDataset
import os
from datasets import Dataset
from transformers import TrainingArguments
from trl import SFTTrainer
from trl import setup_chat_format
from datetime import date

date_string: str = date.today().strftime("%d %b %Y")

# orkg-synthesis-adv  --> max_length: 5292
# orkg-synthesis-org  --> max_length: 4645

# bioasq-adv  --> max_length:9448
# bioasq-org  --> max_length:8874

prompts = Prompts()

dataset_sft_obj = SciQAEvalSFTDataset(prompts)

remove_columns = ['sample_id', 'eval_type', 'quality', 'synthesizer_model', 'evaluator_model', 
                  'research_question', 'synthesizer_synthesis', 'synthesis_evaluation_rating', 
                  'synthesis_evaluation_rationale', 'papers', 'original-synthesis', 'evaluation']


metadata = [
    # ["orkg-synthesis-org", 4645, 1], # Done
    
    ["bioasq-org", 8874, 1]  # 
]

num_train_epochs = 5

for data_key, max_len, batch_size in metadata:
    output_dir = f"assets/sft-{data_key}"
    print(data_key, max_len, batch_size)
    path = config.datasets_path[data_key]
    dataset = utils.read_json(path)
    
    model, tokenizer, peft_params = llm_loader.load_qlora_model(model_id=config.evaluator_model_id, 
                                                                token=config.huggingface_key)
    if tokenizer.chat_template is None:
        model, tokenizer = setup_chat_format(model, tokenizer)
    
    def preprocess_chat_data(examples):
        input_ids = []
        attention_masks = []
        labels = []

        for research_question, synthesis, papers, quality, rationale, rating in zip(examples['research_question'], 
                                                                                    examples['synthesizer_synthesis'], 
                                                                                    examples['papers'],
                                                                                    examples['quality'],
                                                                                    examples['synthesis_evaluation_rationale'],
                                                                                    examples['synthesis_evaluation_rating']):
            example_dict = {
                'research_question': research_question,
                'synthesizer_synthesis': synthesis,
                'papers': papers,
                'quality': quality,
                'synthesis_evaluation_rationale': rationale,
                'synthesis_evaluation_rating': rating
            }

            conversation, label = dataset_sft_obj.preprocess_chat_data_sft(example_dict)

            # Format the conversation into a string
            formatted_input = tokenizer.apply_chat_template(conversation, date_string=date_string, 
                                                            tokenize=False, add_generation_prompt=True)
            # Tokenize the input conversation
            tokenized_input = tokenizer(formatted_input)#, max_length=max_len, padding="max_length")
            # Tokenize the label  truncation=True, 
            # tokenized_label = tokenizer(label)#,  max_length=300, padding="max_length")
            # Append results to the respective lists
            input_ids.append(tokenized_input["input_ids"])
            attention_masks.append(tokenized_input["attention_mask"])
            # labels.append(tokenized_label["input_ids"])

        # Return all tokenized outputs as a dictionary
        return {
            "input_ids": input_ids, 
            "attention_mask": attention_masks, 
            # "labels": labels
        }

    train = Dataset.from_list(dataset)
    preprocess_train = train.map(preprocess_chat_data, batched=True, remove_columns=remove_columns)
    
    tks = [len(sample['input_ids']) for sample in preprocess_train]
    print("max tokens formatted_input:", max(tks))
    # tks = [len(sample['labels']) for sample in preprocess_train]
    # print("max tokens labels:", max(tks))
    
    max_length = max_len
    training_params = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=num_train_epochs,
        per_device_train_batch_size=batch_size,
        gradient_accumulation_steps=batch_size,
        optim="paged_adamw_8bit",
        save_steps=500,
        logging_steps=100,
        learning_rate=2e-4,
        weight_decay=0.001,
        fp16=False,
        bf16=False,
        max_grad_norm=0.3,
        max_steps=-1,
        warmup_ratio=0.03,
        group_by_length=True,
        report_to="tensorboard",
        # max_seq_length=max_len,
    )

    # Initialize the trainer
    trainer = SFTTrainer(
        model=model,
        train_dataset=preprocess_train,
        peft_config=peft_params,
        # dataset_text_field="input_ids",  # Specify the correct field for text
        # max_seq_length=max_len,
        tokenizer=tokenizer,
        args=training_params,
    )
    
    # Train the model
    trainer.train()

    # Save the model
    trainer.save_model(output_dir)