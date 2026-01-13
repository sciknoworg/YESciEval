from ..base import Judge, Rubric
from typing import Dict

from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel, PeftConfig
import torch
import time
from openai import OpenAI
import logging

logger = logging.getLogger(__name__)


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

    def judge(self, rubric: Rubric, max_new_tokens: int=150) -> str:
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
        self.model, self.tokenizer = super()._from_pretrained(model_id=model_id, device=device, token=token)

class BioASQAutoJudge(AutoJudge):
    def from_pretrained(self, model_id: str = "SciKnowOrg/YESciEval-BioASQ-Llama-3.1-8B",
                         device: str = "auto",
                         token: str = ""):
        self.model, self.tokenizer = super()._from_pretrained(model_id=model_id, device=device, token=token)



class CustomAutoJudge(AutoJudge):

    def _from_pretrained(self, model_id:str, device:str="auto", token:str =""):
        tokenizer = AutoTokenizer.from_pretrained(model_id,
                                                  padding_side="left",
                                                  token=token)
        tokenizer.pad_token = tokenizer.eos_token
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.float32,
            device_map=device,
            token=token
        )
        return model, tokenizer


class GPTCustomAutoJudge(Judge):
    
    def from_pretrained(self, model_id:str, device: str="auto", token:str =""):
        if not token:
            raise ValueError(
                "OpenAI API token must be provided."
            )

        self.model_name = model_id
        self.client = OpenAI(api_key=token)


    def _is_reasoning_model(self) -> bool:
        model_lower = self.model_name.lower()
        reasoning_prefixes = ("gpt-5", "o1", "o4", "o3", "o-1", "o-3")
        return any(model_lower.startswith(prefix) for prefix in reasoning_prefixes)

    def _is_gpt4_family(self) -> bool:
        model_lower = self.model_name.lower()
        return model_lower.startswith(("gpt-4", "gpt-4o", "gpt-4.1"))
  
    def _build_rubric_evaluation_function_schema(self, rubric_id: str) -> dict:
        return {
            "name": "evaluate_rubric",
            "description": f"Return rating and rationale for rubric {rubric_id}",
            "parameters": {
                "type": "object",
                "properties": {
                    rubric_id: {
                        "type": "object",
                        "properties": {
                            "rating": {"type": "string", "description": "Score for this rubric"},
                            "rationale": {"type": "string", "description": "Explanation for the rating"}
                        },
                        "required": ["rating", "rationale"]
                    }
                },
                "required": [rubric_id]
            }
        }

    def judge(self, rubric: Rubric, max_new_tokens: int = 150) -> Dict[str, Dict[str, str]]:
        if not self.client:
            raise ValueError("Model not initialized.")

        messages = rubric.instruct()
        rubric_id = rubric.name

        params = {
            "model": self.model_name,
            "messages": messages,
            "max_completion_tokens" if self._is_reasoning_model() else "max_tokens": max_new_tokens
        }

        if self._is_gpt4_family():
            params["functions"] = [self._build_rubric_evaluation_function_schema(rubric_id)]
            params["function_call"] = {"name": "evaluate_rubric"}

        while True:
            try:
                response = self.client.chat.completions.create(**params)
                message = response.choices[0].message

                if self._is_gpt4_family():
                    if hasattr(message, 'function_call') and message.function_call:
                        raw_args = message.function_call.arguments.strip()
                        content = eval(raw_args) if raw_args else {}
                    else:
                        content = {rubric_id: {"rating": "N/A", "rationale": "No function call returned"}}
                else:
                    raw_text = getattr(message, 'content', '')
                    if raw_text:
                        try:
                            content = eval(raw_text)
                        except Exception:
                            content = {rubric_id: {"rating": "N/A", "rationale": raw_text}}
                    else:
                        if response.choices[0].finish_reason == 'length':
                            content = {rubric_id: {"rating": "N/A", "rationale": "Token limit reached. Increase max_new_tokens parameter."}}
                        else:
                            content = {rubric_id: {"rating": "N/A", "rationale": "Empty response"}}
                
                break

            except Exception as e:
                logger.warning(f"API call failed, retrying in 4 seconds: {e}")
                time.sleep(4) 

        return content
