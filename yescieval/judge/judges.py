from ..base import Judge, Rubric
from typing import Dict

from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel, PeftConfig
import torch
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


class GPTCustomAutoJudge(AutoJudge):

    def from_pretrained(self, model_id: str, api_key: str = None, base_url: str = None, **kwargs):

        self.model_name = model_id

        client_kwargs = {}
        if api_key:
            client_kwargs["api_key"] = api_key
        if base_url:
            client_kwargs["base_url"] = base_url
        client_kwargs.update(kwargs)

        self.client = OpenAI(**client_kwargs)
        return self  

    def _is_reasoning_model(self) -> bool:

        model_lower = self.model_name.lower()
        reasoning_prefixes = ("gpt-5", "o1", "o4" "o3", "o-1", "o-3")
        return any(model_lower.startswith(prefix) for prefix in reasoning_prefixes)

    def evaluate(
        self,
        rubric: Rubric,
        max_new_tokens: int = 300,
        temperature: float = 0.0,
        **kwargs
    ) -> str:
       
        if self.client is None:
            raise ValueError("Model not initialized. Call from_pretrained() first.")

        raw_messages = rubric.instruct()
        messages = self._format_messages(raw_messages)

        params = {
            "model": self.model_name,
            "messages": messages,
        }

        # Add model-specific parameters
        if self._is_reasoning_model():
            params["max_completion_tokens"] = max_new_tokens
        else:
            params["max_tokens"] = max_new_tokens
            params["temperature"] = temperature

        for key, value in kwargs.items():
            if key not in params:
                params[key] = value
        try:
            response = self.client.chat.completions.create(**params)
        except Exception as e:
            raise RuntimeError(f"OpenAI API call failed: {str(e)}")

        if response.choices and len(response.choices) > 0:
            content = response.choices[0].message.content
            return content if content else ""
        return ""

    def _format_messages(self, raw_messages) -> list:

        messages = []

        # Handle string input
        if isinstance(raw_messages, str):
            messages.append({"role": "user", "content": raw_messages})
        
        # Handle list input
        elif isinstance(raw_messages, list):
            for msg in raw_messages:
                if isinstance(msg, str):
                    messages.append({"role": "user", "content": msg})
                elif isinstance(msg, dict):
                    if "role" in msg and "content" in msg:
                        messages.append(msg)
                    else:
                        raise ValueError(f"Message dict missing 'role' or 'content': {msg}")
                else:
                    raise ValueError(f"Invalid message type in list: {type(msg)}")
        
        # Handle dict input (single message)
        elif isinstance(raw_messages, dict):
            if "role" in raw_messages and "content" in raw_messages:
                messages.append(raw_messages)
            else:
                raise ValueError(f"Message dict missing 'role' or 'content': {raw_messages}")
        
        else:
            raise ValueError(f"Unsupported rubric.instruct() output type: {type(raw_messages)}")

        return messages