from ..base import Judge, Rubric
from typing import Dict

from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel, PeftConfig
import torch



class AutoJudge(Judge):

    def _from_pretrained(self, model_id:str, device:str="auto", token:str =""):
        config = PeftConfig.from_pretrained(model_id)
        base_model_name = config.base_model_name_or_path
        tokenizer = AutoTokenizer.from_pretrained(base_model_name,
                                                  padding_side="left",
                                                  token=token)
        tokenizer.pad_token = tokenizer.eos_token
        base_model = AutoModelForCausalLM.from_pretrained(
            base_model_name,
            torch_dtype=torch.float32,
            device_map=device,
            token=token
        )
        model = PeftModel.from_pretrained(base_model, model_id)
        return model, tokenizer

    def evaluate(self, rubric: Rubric, max_new_tokens: int=150) -> Dict[str, Dict[str, str]]:
        inputs = self.tokenizer.apply_chat_template(rubric.instruct(),
                                                    add_generation_prompt=True,
                                                    return_dict=True,
                                                    return_tensors="pt")
        inputs.to(self.model.device)
        outputs = self.model.generate(**inputs,
                                      max_new_tokens=max_new_tokens,
                                      pad_token_id=self.tokenizer.eos_token_id)
        evaluation = self.tokenizer.decode(outputs[0][len(inputs["input_ids"][0]):], skip_special_tokens=True)
        return evaluation


class AskAutoJudge(AutoJudge):
    def from_pretrained(self, model_id:str="SciKnowOrg/YESciEval-ASK-Llama-3.1-8B",
                         device:str="auto",
                         token:str =""):
        return super()._from_pretrained(model_id=model_id, device=device, token=token)

class BioASAutoJudge(AutoJudge):
    def from_pretrained(self, model_id: str = "SciKnowOrg/YESciEval-BioASQ-Llama-3.1-8B",
                         device: str = "auto",
                         token: str = ""):
        return super()._from_pretrained(model_id=model_id, device=device, token=token)
