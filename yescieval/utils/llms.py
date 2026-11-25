"""LLM call utilities: retrying failed calls."""

import logging
import time
from typing import Any, Callable

logger = logging.getLogger(__name__)


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
