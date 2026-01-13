from ..base import Judge, Rubric, RubricLikertScale
from .judges import AutoJudge

import time
from typing import Dict, List
from openai import OpenAI
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import logging

logger = logging.getLogger(__name__)

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

    def from_pretrained(self, model_id: str, device: str = "auto", token: str = ""):
        if not token:
            raise ValueError("OpenAI API token must be provided.")
        self.model_name = model_id
        self.client = OpenAI(api_key=token)

    def _supports_function_calling(self) -> bool:
        gpt_4_prefixes = (
            "gpt-4", # gpt4 family including gpt-4o, gpt-4o-mini, gpt-4.1, ...
            "GPT-3.5", # gpt-3.5 family
        )
        return any(self.model_name.startswith(prefix) for prefix in gpt_4_prefixes)

    def _output_schema(self) -> List[Dict]:
        return [
            {
                "name": "response_format",
                "description": f"Return the `rating` and `rationale` only as a response.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        'rating': {
                                "type": "number",
                                "description": "A numerical rating assigned to the characteristic.",
                                "minimum": 1,
                                "maximum": 5
                        },
                        "rationale": {
                            "type": "string",
                            "description": "The explanation for the assigned rating."
                        },
                    },
                    "required": ["rating", "rationale"]
                }
            }
        ]

    def judge(self, rubric: Rubric, max_new_tokens: int = 150) -> RubricLikertScale:
        if not self.client:
            raise ValueError("Model not initialized.")
        messages = rubric.instruct()
        params = {
            "model": self.model_name,
            "messages": messages
        }
        if self._supports_function_calling():
            params["functions"] = self._output_schema()

        try_counter = 0
        while True:
            try:
                try_counter += 1
                response = self.client.chat.completions.create(**params)
                message = response.choices[0].message
                if self._supports_function_calling():
                    parsed_output = eval(message.function_call.arguments)
                else:
                    parsed_output = eval(message.content)[rubric.name]
                evaluation = RubricLikertScale(rating=parsed_output['rating'], rationale=parsed_output['rationale'])
                return evaluation

            except Exception as e:
                logger.error(f"{try_counter} times failed attempt!")
                logger.warning(f"API call failed, retrying in 4 seconds: {e}")
                time.sleep(5)


