"""Schema generation, decoding and validation for structured evaluation results."""

import json
import logging
import time
from typing import Any, Callable, Dict, Optional, Type

from pydantic import BaseModel

logger = logging.getLogger(__name__)


def response_schema(response_model: Type[BaseModel], name: str, description: str) -> Dict[str, Any]:
    """
    Build an OpenAI function definition whose parameters are the JSON schema of `response_model`.

    Args:
        response_model: Pydantic model describing one structured evaluation result.
        name: Function name the model is asked to call.
        description: Function description shown to the model.

    Returns:
        Function definition for the chat completions `functions` parameter.
    """
    return {
        "name": name,
        "description": description,
        "parameters": response_model.model_json_schema(),
    }


def parse_response(raw_output: str,
                   response_model: Type[BaseModel],
                   wrapper_key: Optional[str] = None,
                   validator: Optional[Callable[[BaseModel], BaseModel]] = None) -> BaseModel:
    """
    Decode JSON text and validate it against `response_model`.

    Model output is only decoded as JSON, never executed.

    Args:
        raw_output: JSON text produced by the model.
        response_model: Pydantic model the decoded payload must satisfy.
        wrapper_key: Optional key, such as the rubric name, that may wrap the result
            (e.g. ``{"Correctness": {"rating": 4, ...}}``). The payload is unwrapped only when it
            consists of exactly this key and the key is not itself a field of `response_model`.
        validator: Optional rubric-specific check applied to the validated result,
            such as `Rubric.validate_result`.

    Returns:
        The validated `response_model` instance (as returned by `validator`, if given).

    Raises:
        json.JSONDecodeError: If `raw_output` is not valid JSON.
        pydantic.ValidationError: If the payload does not satisfy `response_model`.
        ValueError: If `validator` rejects the result.
    """
    payload = json.loads(raw_output)
    if (wrapper_key is not None and isinstance(payload, dict) and list(payload) == [wrapper_key]
            and wrapper_key not in response_model.model_fields):
        payload = payload[wrapper_key]
    result = response_model.model_validate(payload)
    if validator is not None:
        result = validator(result)
    return result


def call_with_retries(operation: Callable[[], Any], max_attempts: int, retry_delay: float) -> Any:
    """
    Call `operation` until it succeeds, at most `max_attempts` times.

    Any exception (API error, invalid JSON, failed validation) triggers another attempt after
    `retry_delay` seconds. The exception of the last attempt is re-raised. If `max_attempts`
    is below 1, no attempt is made and `RuntimeError` is raised.
    """
    for attempt in range(1, max_attempts + 1):
        try:
            return operation()
        except Exception as e:
            if attempt == max_attempts:
                logger.error(f"Structured response failed after {max_attempts} attempts: {e}")
                raise
            logger.warning(f"Attempt {attempt}/{max_attempts} failed, retrying in {retry_delay} seconds: {e}")
            time.sleep(retry_delay)
    raise RuntimeError(f"No attempt made: max_attempts must be at least 1 (got {max_attempts}).")
