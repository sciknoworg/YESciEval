from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import get_peft_model, LoraConfig, TaskType, prepare_model_for_kbit_training
import torch


def load_qlora_model(model_id, token):
    tokenizer = AutoTokenizer.from_pretrained(model_id, padding_side="left", token=token)
    tokenizer.pad_token = tokenizer.eos_token
    quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=False,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
    )
    
    # Load the base model in 4-bit precision
    model = AutoModelForCausalLM.from_pretrained(model_id, 
                                                 quantization_config=quant_config, 
                                                 device_map={"": 0},
                                                 token=token)
    
    # Define LoRA configuration
    peft_params = LoraConfig(
        task_type=TaskType.CAUSAL_LM,  # Task type: causal language modeling
        r=8,  # LoRA rank
        lora_alpha=16,  # LoRA scaling factor
        target_modules=["q_proj", "v_proj"],  # Target modules for adaptation
        lora_dropout=0.05,  # Dropout rate
        bias="none",  # Bias strategy
        )
    # Add LoRA layers to the base model
    qlora_model = get_peft_model(model, peft_params)
    
    return qlora_model, tokenizer, peft_params




def load_tuned_model(model_id, token):
    tokenizer = AutoTokenizer.from_pretrained(model_id, padding_side="left", token=token)
    tokenizer.pad_token = tokenizer.eos_token
    quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=False,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
    )
    
    # Load the base model in 4-bit precision
    model = AutoModelForCausalLM.from_pretrained(model_id, 
                                                 quantization_config=quant_config, 
                                                 # load_in_8bit=True,
                                                 device_map="balanced",
                                                 token=token)
    
    return model, tokenizer


def load_rlhf_model(model_id, token, device_map):
    tokenizer = AutoTokenizer.from_pretrained(model_id, padding_side="left", token=token)
    tokenizer.pad_token = tokenizer.eos_token
    quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=False,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
    )
    
    # Load the base model in 4-bit precision
    model = AutoModelForCausalLM.from_pretrained(model_id, 
                                                 quantization_config=quant_config, 
                                                 # load_in_8bit=True,
                                                 attn_implementation="eager",
                                                 device_map = device_map,
                                                 token=token)
    # Define LoRA configuration
    peft_params = LoraConfig(
        task_type=TaskType.CAUSAL_LM,  # Task type: causal language modeling
        r=8,  # LoRA rank
        lora_alpha=16,  # LoRA scaling factor
        target_modules=["q_proj", "v_proj"],  # Target modules for adaptation
        lora_dropout=0.05,  # Dropout rate
        bias="none",  # Bias strategy
        )
    model = prepare_model_for_kbit_training(model)
    return model, tokenizer, peft_params
