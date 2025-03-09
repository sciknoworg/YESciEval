from sciqaeval import config, utils, llm_loader
from sciqaeval.prompt import Prompts
from sciqaeval.dataset import SciQAEvalSFTDataset
from datetime import date
from tqdm import tqdm
from openai import OpenAI
import time
from concurrent.futures import ThreadPoolExecutor

date_string: str = date.today().strftime("%d %b %Y")

def process_batch(model, tokenizer, batch_samples):
    """Process a batch of inputs."""
    conversations = [dataset_sft_obj.preprocess_chat_data_inf(sample) for sample in batch_samples]
    inputs = tokenizer.apply_chat_template(
        conversations,
        add_generation_prompt=True,
        return_dict=True,
        return_tensors="pt",
        padding=True,
        truncation=True,
    )
    inputs.to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens, pad_token_id=tokenizer.eos_token_id)
    outputs_texts = [
        tokenizer.decode(output[len(input_ids):], skip_special_tokens=True)
        for output, input_ids in zip(outputs, inputs["input_ids"])
    ]
    return outputs_texts

def gpt4o_eval(outputs_texts):
    """Use GPT-4o API to extract evaluation outputs only in a parallel mode."""
    def call_api(text):
        while True:
            try:
                completion = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": text}],
                    functions=functions
                )
                return eval(completion.choices[0].message.function_call.arguments)
            except:
                time.sleep(3)
    with ThreadPoolExecutor(max_workers=4) as executor:  # Adjust workers based on API limits
        results = list(executor.map(call_api, outputs_texts))
    return results

prompts = Prompts()
dataset_sft_obj = SciQAEvalSFTDataset(prompts)
client = OpenAI(api_key=config.openai_key)
functions = [
  {
    "name": "evaluate_characteristic",
    "description": "Extracting the exact `rating` and `rationale` from the given text.",
    "parameters": {
      "type": "object",
      "properties": {
        "rating": {
          "type": "number",
          "description": "A numerical rating assigned to the characteristic in the text.",
          "minimum": 1,
          "maximum": 5
        },
        "rationale": {
          "type": "string",
          "description": "The explanation for the assigned rating."
        }
      },
      "required": ["rating", "rationale"]
    }
  }
]
metadata = [
    # SFT (ORG)
    ["assets/sft-orkg-synthesis-org",  "orkg-synthesis-test", "assets/sft-orkg-synthesis-org-test.json"],
    ["assets/sft-bioasq-org",  "bioasq-test", "assets/sft-bioasq-org-test.json"],
    # SFT (ORG) + RL (ADV)
    ["assets/rlhf-orkg-synthesis-adv",  "orkg-synthesis-test", "assets/rlhf-orkg-synthesis-adv-test.json"],
    ["assets/rlhf-bioasq-adv",  "bioasq-test", "assets/rlhf-bioasq-adv-test.json"],
    # SFT (ORG) + RL (ADV + ORG)
    ["assets/rlhf-orkg-synthesis-adv-org",  "orkg-synthesis-test", "assets/rlhf-orkg-synthesis-adv-org-test.json"],
    ["assets/rlhf-bioasq-adv-org",  "bioasq-test", "assets/rlhf-bioasq-adv-org-test.json"], 
]

batch_size = 4  
max_new_tokens = 150 

for model_id, data_key, output_path in metadata:
    print("Working on:", model_id)
    path = config.datasets_path[data_key]
    dataset = utils.read_json(path)
    model, tokenizer = llm_loader.load_tuned_model(model_id=model_id, token=config.huggingface_key)
    for i in tqdm(range(0, len(dataset), batch_size)):
        batch_samples = dataset[i:i+batch_size]
        outputs_texts = process_batch(model, tokenizer, batch_samples)
        evaluations = gpt4o_eval(outputs_texts)
        for j, evaluation in enumerate(evaluations):
            dataset[i + j]['synthesis_evaluation_rating'] = evaluation['rating']
            dataset[i + j]['synthesis_evaluation_rationale'] = evaluation['rationale']
    utils.save_json(data=dataset, file_path=output_path)
    
    
