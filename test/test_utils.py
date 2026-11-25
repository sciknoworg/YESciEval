import json
import unittest
from typing import Literal
from unittest.mock import MagicMock, patch
from pydantic import BaseModel, ValidationError
from yescieval.base import RubricLikertScale
from yescieval.utils import call_with_retries, parse_response, response_schema


class LabelResult(BaseModel):
    """Test result model with a categorical field, unrelated to any shipped rubric."""

    label: Literal["yes", "no", "unclear"]
    rationale: str


class RatedByName(BaseModel):
    """Test result model with a field called like a wrapper key."""

    Informativeness: int


class TestResponseSchema(unittest.TestCase):

    def test_function_definition_from_response_model(self):
        schema = response_schema(LabelResult, name="response_format", description="Return the result.")
        self.assertEqual(schema, {
            "name": "response_format",
            "description": "Return the result.",
            "parameters": LabelResult.model_json_schema(),
        })

    def test_likert_scale_schema(self):
        parameters = response_schema(RubricLikertScale, name="n", description="d")["parameters"]
        self.assertEqual(set(parameters["properties"]), {"rating", "rationale"})
        self.assertEqual(set(parameters["required"]), {"rating", "rationale"})
        self.assertEqual(parameters["properties"]["rating"]["minimum"], 1)
        self.assertEqual(parameters["properties"]["rating"]["maximum"], 5)


class TestParseResponse(unittest.TestCase):

    def setUp(self):
        self.likert = {"rating": 4, "rationale": "Informative synthesis."}

    def test_plain_payload(self):
        result = parse_response(json.dumps(self.likert), RubricLikertScale)
        self.assertEqual(result, RubricLikertScale(**self.likert))

    def test_payload_wrapped_by_wrapper_key_is_unwrapped(self):
        raw_output = json.dumps({"Informativeness": self.likert})
        result = parse_response(raw_output, RubricLikertScale, wrapper_key="Informativeness")
        self.assertEqual(result, RubricLikertScale(**self.likert))

    def test_unwrapped_payload_with_wrapper_key(self):
        result = parse_response(json.dumps(self.likert), RubricLikertScale, wrapper_key="Informativeness")
        self.assertEqual(result, RubricLikertScale(**self.likert))

    def test_wrapped_payload_without_wrapper_key_is_rejected(self):
        with self.assertRaises(ValidationError):
            parse_response(json.dumps({"Informativeness": self.likert}), RubricLikertScale)

    def test_payload_with_extra_keys_is_not_unwrapped(self):
        raw_output = json.dumps({"Informativeness": self.likert, "note": "extra"})
        with self.assertRaises(ValidationError):
            parse_response(raw_output, RubricLikertScale, wrapper_key="Informativeness")

    def test_wrapper_key_that_is_a_field_is_not_unwrapped(self):
        result = parse_response('{"Informativeness": 3}', RatedByName, wrapper_key="Informativeness")
        self.assertEqual(result, RatedByName(Informativeness=3))

    def test_validator_result_is_returned(self):
        replacement = LabelResult(label="no", rationale="Replaced by the validator.")
        validator = MagicMock(return_value=replacement)
        raw_output = json.dumps({"label": "yes", "rationale": "Stated."})
        result = parse_response(raw_output, LabelResult, validator=validator)
        validator.assert_called_once_with(LabelResult(label="yes", rationale="Stated."))
        self.assertIs(result, replacement)

    def test_validator_rejection_propagates(self):
        def reject(result):
            raise ValueError("label is not allowed")
        with self.assertRaisesRegex(ValueError, "not allowed"):
            parse_response(json.dumps({"label": "unclear", "rationale": "?"}), LabelResult, validator=reject)

    def test_invalid_json_raises_decode_error(self):
        with self.assertRaises(json.JSONDecodeError):
            parse_response("{not json", RubricLikertScale)

    def test_invalid_payload_raises_validation_error(self):
        for payload in ({"rating": 7, "rationale": "Out of range."},
                        {"rating": 4},
                        {"label": "maybe", "rationale": "Unknown label."}):
            with self.subTest(payload=payload):
                model = LabelResult if "label" in payload else RubricLikertScale
                with self.assertRaises(ValidationError):
                    parse_response(json.dumps(payload), model)

    def test_model_output_is_not_executed(self):
        with patch("builtins.eval", side_effect=AssertionError("eval must not be used")):
            self.assertEqual(parse_response(json.dumps(self.likert), RubricLikertScale),
                             RubricLikertScale(**self.likert))


@patch("yescieval.utils.llms.time.sleep")
class TestCallWithRetries(unittest.TestCase):

    def test_first_success_is_returned_without_sleep(self, sleep):
        operation = MagicMock(return_value="result")
        self.assertEqual(call_with_retries(operation, max_attempts=3, retry_delay=5), "result")
        operation.assert_called_once_with()
        sleep.assert_not_called()

    def test_failure_is_retried_after_delay(self, sleep):
        operation = MagicMock(side_effect=[ConnectionError("timeout"), ValueError("invalid"), "result"])
        with self.assertLogs("yescieval.utils.llms", level="WARNING") as logs:
            self.assertEqual(call_with_retries(operation, max_attempts=3, retry_delay=5), "result")
        self.assertEqual(operation.call_count, 3)
        self.assertEqual([c.args for c in sleep.call_args_list], [(5,), (5,)])
        self.assertEqual(len(logs.records), 2)

    def test_last_error_is_raised_after_max_attempts(self, sleep):
        operation = MagicMock(side_effect=[ValueError("first"), ValueError("second")])
        with self.assertLogs("yescieval.utils.llms", level="ERROR"):
            with self.assertRaisesRegex(ValueError, "second"):
                call_with_retries(operation, max_attempts=2, retry_delay=1)
        self.assertEqual(operation.call_count, 2)
        self.assertEqual(sleep.call_count, 1)

    def test_no_attempt_below_one(self, sleep):
        operation = MagicMock()
        for max_attempts in (0, -1):
            with self.subTest(max_attempts=max_attempts):
                with self.assertRaisesRegex(RuntimeError, "at least 1"):
                    call_with_retries(operation, max_attempts=max_attempts, retry_delay=1)
        operation.assert_not_called()
        sleep.assert_not_called()


if __name__ == "__main__":
    unittest.main()
