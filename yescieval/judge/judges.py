from ..base import Judge, Rubric
from typing import Dict

from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel, PeftConfig
import torch
import json
import ast
from openai import OpenAI



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

    def from_pretrained(self, model_id: str, token: str = ""):
        self.model_name = model_id

        if token:
            self.client = OpenAI(api_key=token)
        else:
            self.client = OpenAI()

    def _is_reasoning_model(self) -> bool:

        model_lower = self.model_name.lower()
        reasoning_prefixes = ("gpt-5", "o1", "o4", "o3", "o-1", "o-3")
        return any(model_lower.startswith(prefix) for prefix in reasoning_prefixes)

    def _is_gpt4_family(self) -> bool:
        model_lower = self.model_name.lower()
        return model_lower.startswith(("gpt-4", "gpt-4o", "gpt-4.1"))
    
    def _model_family(self) -> str:
        if self._is_gpt4_family():
            return "GPT-4 family"
        elif self._is_reasoning_model():
            return "GPT-5 / O-series"
        else:
            return "Other"

    
    def _judge_function_schema_single(self, rubric: Rubric) -> dict:
    
        rubric_id = rubric.__class__.__name__  
        return {
            "name": "submit_judgement",
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

    def _parse_json(self, text: str) -> dict:
            
            text = text.strip()
            
            if text.startswith("```"):
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
            
            text = text.strip()
            
            try:
                return json.loads(text)
            except json.JSONDecodeError:
                try:
                    return ast.literal_eval(text)
                except:
                    return None

    def judge(self, rubric: Rubric, max_new_tokens: int = 150) -> Dict[str, Dict[str, str]]:
        if not self.client:
            raise ValueError("Model not initialized. Call from_pretrained() first.")

        messages = self._format_messages(rubric.instruct())
        rubric_id = rubric.__class__.__name__

        if self._is_reasoning_model():
            actual_max_tokens = max_new_tokens * 10
        else:
            actual_max_tokens = max_new_tokens

        params = {
            "model": self.model_name,
            "messages": messages,
            "max_completion_tokens" if self._is_reasoning_model() else "max_tokens": actual_max_tokens
        }

        if self._is_gpt4_family():
            params["functions"] = [self._judge_function_schema_single(rubric)]
            params["function_call"] = {"name": "submit_judgement"}

        try:
            response = self.client.chat.completions.create(**params)
            message = response.choices[0].message
        except Exception as e:
            raise RuntimeError(f"OpenAI API call failed: {str(e)}")

        if self._is_gpt4_family():
            if hasattr(message, 'function_call') and message.function_call:
                raw_args = message.function_call.arguments.strip()
                content = self._parse_json(raw_args) or {}
            else:
                content = {rubric_id: {"rating": "N/A", "rationale": "No function call returned"}}
        else:
            raw_text = getattr(message, 'content', '')
            
            if raw_text:
                parsed = self._parse_json(raw_text)
                if parsed:
                    content = parsed
                else:
                    content = {rubric_id: {"rating": "N/A", "rationale": raw_text}}
            else:
                if response.choices[0].finish_reason == 'length':
                    content = {rubric_id: {"rating": "N/A", "rationale": "Token limit reached. Increase max_new_tokens parameter."}}
                else:
                    content = {rubric_id: {"rating": "N/A", "rationale": "Empty response"}}

        return content

    def _format_messages(self, raw_messages) -> list:
        """Convert rubric.instruct() output to OpenAI message format."""
        messages = []

        if isinstance(raw_messages, str):
            messages.append({"role": "user", "content": raw_messages})
        elif isinstance(raw_messages, list):
            for msg in raw_messages:
                if isinstance(msg, str):
                    messages.append({"role": "user", "content": msg})
                elif isinstance(msg, dict) and "role" in msg and "content" in msg:
                    messages.append(msg)
                else:
                    raise ValueError(f"Invalid message format: {msg}")
        elif isinstance(raw_messages, dict):
            if "role" in raw_messages and "content" in raw_messages:
                messages.append(raw_messages)
            else:
                raise ValueError(f"Message dict missing 'role' or 'content': {raw_messages}")
        else:
            raise ValueError(f"Unsupported rubric.instruct() type: {type(raw_messages)}")

        return messages