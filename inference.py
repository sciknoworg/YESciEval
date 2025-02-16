from sciqaeval import config, utils, llm_loader
from sciqaeval.prompt import Prompts
from sciqaeval.dataset import SciQAEvalSFTDataset
from datetime import date
from tqdm import tqdm
from openai import OpenAI
import time

date_string: str = date.today().strftime("%d %b %Y")


prompts = Prompts()

dataset_sft_obj = SciQAEvalSFTDataset(prompts)

remove_columns = ['sample_id', 'eval_type', 'quality', 'synthesizer_model', 'evaluator_model', 
                  'research_question', 'synthesizer_synthesis', 'synthesis_evaluation_rating', 
                  'synthesis_evaluation_rationale', 'papers', 'original-synthesis', 'evaluation']




max_new_tokens = 150

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
    # ["assets/sft-orkg-synthesis-org",  "orkg-synthesis-test", "assets/sft-orkg-synthesis-org-test.json"],  
    # ["assets/sft-bioasq-org",  "bioasq-test", "assets/sft-bioasq-org-test.json"],
    
    # SFT (ORG) + RL (ADV)
    # ["assets/rlhf-orkg-synthesis-adv",  "orkg-synthesis-test", "assets/rlhf-orkg-synthesis-adv-test.json"],  
    # ["assets/rlhf-bioasq-adv",  "bioasq-test", "assets/rlhf-bioasq-adv-test.json"], 
    
    # SFT (ORG) + RL (ADV + ORG)
    ["assets/rlhf-orkg-synthesis-adv-org",  "orkg-synthesis-test", "assets/rlhf-orkg-synthesis-adv-org-test.json"],  
    # ["assets/rlhf-bioasq-adv-org",  "bioasq-test", "assets/rlhf-bioasq-adv-org-test.json"], 
]

for model_id, data_key, output_path in metadata:
    print("working on:", model_id)
    
    path = config.datasets_path[data_key]
    
    dataset = utils.read_json(path)
    
    model, tokenizer = llm_loader.load_tuned_model(model_id=model_id, token=config.huggingface_key)
    
    for index, sample in tqdm(enumerate(dataset)):
        while True:
            try:
                conversation  = dataset_sft_obj.preprocess_chat_data_inf(sample)
                inputs = tokenizer.apply_chat_template(
                            conversation,
                            add_generation_prompt=True,
                            return_dict=True,
                            return_tensors="pt",
                )
                inputs.to(model.device)
                outputs = model.generate(**inputs, max_new_tokens=max_new_tokens, pad_token_id=tokenizer.eos_token_id)
                outputs_text = tokenizer.decode(outputs[0][len(inputs["input_ids"][0]):], skip_special_tokens=True)

                completion = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": outputs_text}],
                    functions=functions
                )

                inference = eval(completion.choices[0].message.function_call.arguments)
                break
            except:
                time.sleep(3)
        dataset[index]['synthesis_evaluation_rating'] = inference['rating']
        dataset[index]['synthesis_evaluation_rationale'] = inference['rationale']
        
    utils.save_json(data=dataset, file_path=output_path)