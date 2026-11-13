from ..base import Judge, Rubric
from ..base.response import call_with_retries, parse_response, response_schema
from .judges import AutoJudge

from typing import Dict, List, Type
from openai import OpenAI
from pydantic import BaseModel
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
    """
    Judge backed by an OpenAI chat model.

    The result format is the rubric's `response_model`; each result is validated against it and
    then checked by `rubric.validate_result()`. Failed API calls or invalid results are retried
    up to `max_attempts` times, waiting `retry_delay` seconds between attempts.
    """

    def __init__(self, max_attempts: int = 3, retry_delay: float = 5):
        self.max_attempts = max_attempts
        self.retry_delay = retry_delay
        self.client = None

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

    def _output_schema(self, response_model: Type[BaseModel]) -> List[Dict]:
        return [response_schema(response_model,
                                name="response_format",
                                description="Return the evaluation result only as a response.")]

    def judge(self, rubric: Rubric, max_new_tokens: int = 150) -> BaseModel:
        if not self.client:
            raise ValueError("Model not initialized.")
        response_model = rubric.response_model
        params = {
            "model": self.model_name,
            "messages": rubric.instruct()
        }
        use_function_calling = self._supports_function_calling()
        if use_function_calling:
            params["functions"] = self._output_schema(response_model)
            params["function_call"] = {"name": "response_format"}

        def evaluate() -> BaseModel:
            message = self.client.chat.completions.create(**params).choices[0].message
            raw_output = message.function_call.arguments if use_function_calling else message.content
            return parse_response(raw_output,
                                  response_model,
                                  wrapper_key=rubric.name,
                                  validator=rubric.validate_result)

        return call_with_retries(evaluate, max_attempts=self.max_attempts, retry_delay=self.retry_delay)
