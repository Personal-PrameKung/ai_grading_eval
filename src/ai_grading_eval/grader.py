"""Grader interface and a deterministic baseline for pipeline smoke tests."""

import json
import os
import re
import urllib.error
import urllib.request
from typing import Protocol

from .models import GraderInput, GraderOutput


class Grader(Protocol):
    def grade(self, grader_input: GraderInput) -> GraderOutput: ...


class ExactAnswerBaseline:
    """Award full credit only when the submitted final answer matches the reference.

    This is deliberately simple and is not intended to be the research grader.
    """

    def grade(self, grader_input: GraderInput) -> GraderOutput:
        submitted = grader_input.final_answer or grader_input.answer_text
        if _normalize(submitted) == _normalize(grader_input.reference_answer):
            return GraderOutput(
                score=grader_input.max_score,
                feedback="Final answer matches the reference answer.",
            )
        return GraderOutput(
            score=0,
            feedback="Final answer does not exactly match the reference answer.",
        )


def _normalize(value: str) -> str:
    return re.sub(r"\s+", "", value).lower().rstrip(".")


class GeminiGrader:
    """Grade a response with Gemini using JSON output validated by Pydantic."""

    def __init__(self, *, model: str = "gemini-3.6-flash", timeout: float = 120.0) -> None:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required for GeminiGrader")
        self.api_key = api_key
        self.model = model
        self.timeout = timeout

    def grade(self, grader_input: GraderInput) -> GraderOutput:
        payload = {
            "contents": [{"parts": [{"text": _gemini_prompt(grader_input)}]}],
            "generationConfig": {
                "temperature": 0,
                "responseMimeType": "application/json",
                "responseSchema": {
                    "type": "OBJECT",
                    "properties": {
                        "score": {"type": "INTEGER"},
                        "point_scores": {"type": "OBJECT"},
                        "feedback": {"type": "STRING"},
                    },
                    "required": ["score", "feedback"],
                },
            },
        }
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent"
        request = urllib.request.Request(
            url,
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json", "x-goog-api-key": self.api_key},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                body = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:1000]
            raise RuntimeError(f"Gemini API request failed ({exc.code}): {detail}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"Gemini API connection failed: {exc.reason}") from exc
        try:
            text = body["candidates"][0]["content"]["parts"][0]["text"]
            result = json.loads(text)
        except (KeyError, IndexError, TypeError, json.JSONDecodeError) as exc:
            raise RuntimeError(f"Gemini returned an invalid structured response: {body}") from exc
        output = GraderOutput.model_validate(result)
        if output.point_scores:
            expected_points = set(grader_input.required_points)
            if set(output.point_scores) != expected_points:
                raise ValueError(
                    f"Gemini point_scores must contain exactly {sorted(expected_points)}; "
                    f"received {sorted(output.point_scores)}"
                )
            if any(value not in (0, 1) for value in output.point_scores.values()):
                raise ValueError("Gemini point_scores values must be 0 or 1")
            if sum(output.point_scores.values()) != output.score:
                raise ValueError("Gemini score must equal the sum of point_scores")
        if output.score > grader_input.max_score:
            raise ValueError("Gemini score exceeds max_score")
        return output


class OpenAIGrader:
    """Grade a response with OpenAI Responses API and validate the result with Pydantic."""

    def __init__(self, *, model: str = "gpt-5.4-mini", temperature: float = 0.7, timeout: float = 120.0) -> None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required for OpenAIGrader")
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.timeout = timeout

    def grade(self, grader_input: GraderInput) -> GraderOutput:
        point_properties = {point: {"type": "integer", "enum": [0, 1]} for point in grader_input.required_points}
        schema = {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "score": {"type": "integer", "minimum": 0, "maximum": grader_input.max_score},
                "point_scores": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": point_properties,
                    "required": list(point_properties),
                },
                "feedback": {"type": "string"},
            },
            "required": ["score", "point_scores", "feedback"],
        }
        payload = {
            "model": self.model,
            "input": _openai_prompt(grader_input),
            "temperature": self.temperature,
            "text": {"format": {"type": "json_schema", "name": "grader_output", "strict": True, "schema": schema}},
        }
        request = urllib.request.Request(
            "https://api.openai.com/v1/responses",
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.api_key}"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                body = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:1000]
            raise RuntimeError(f"OpenAI API request failed ({exc.code}): {detail}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"OpenAI API connection failed: {exc.reason}") from exc
        try:
            text = body["output_text"]
            result = json.loads(text)
        except (KeyError, TypeError, json.JSONDecodeError):
            try:
                text = next(
                    item["text"] for output in body["output"] for item in output.get("content", [])
                    if item.get("type") == "output_text"
                )
                result = json.loads(text)
            except (KeyError, TypeError, StopIteration, json.JSONDecodeError) as exc:
                raise RuntimeError(f"OpenAI returned an invalid structured response: {body}") from exc
        output = GraderOutput.model_validate(result)
        _validate_point_scores(output, grader_input, provider="OpenAI")
        return output


def _gemini_prompt(grader_input: GraderInput) -> str:
    rubric = [item.model_dump() for item in grader_input.rubric]
    return f"""You are a strict mathematics grading assistant. Grade the student's response using only the question, reference answer, and rubric.

Return JSON only: {{"score": integer, "point_scores": {{"P1": 0 or 1}}, "feedback": "brief explanation"}}.
Award each rubric point independently. Accept equivalent mathematically correct forms and unsimplified answers. Do not award credit when required work is missing. The total score must equal the sum of point_scores and be between 0 and {grader_input.max_score}.

Question:
{grader_input.question_text}

Reference answer:
{grader_input.reference_answer}

Rubric:
{json.dumps(rubric, ensure_ascii=False, indent=2)}

Student response:
{grader_input.answer_text}
"""


def _openai_prompt(grader_input: GraderInput) -> str:
    rubric = [item.model_dump() for item in grader_input.rubric]
    return f"""You are a strict mathematics grading assistant. Grade the student's response using only the question, reference answer, and rubric.

Award each rubric point independently. Accept equivalent mathematically correct forms and unsimplified answers. Do not award credit when required work is missing. The total score must equal the sum of point_scores and be between 0 and {grader_input.max_score}. Return only the requested structured JSON object.

Question:
{grader_input.question_text}

Reference answer:
{grader_input.reference_answer}

Rubric:
{json.dumps(rubric, ensure_ascii=False, indent=2)}

Student response:
{grader_input.answer_text}
"""


def _validate_point_scores(output: GraderOutput, grader_input: GraderInput, *, provider: str) -> None:
    expected_points = set(grader_input.required_points)
    if set(output.point_scores) != expected_points:
        raise ValueError(f"{provider} point_scores must contain exactly {sorted(expected_points)}; received {sorted(output.point_scores)}")
    if any(value not in (0, 1) for value in output.point_scores.values()):
        raise ValueError(f"{provider} point_scores values must be 0 or 1")
    if sum(output.point_scores.values()) != output.score:
        raise ValueError(f"{provider} score must equal the sum of point_scores")
    if output.score > grader_input.max_score:
        raise ValueError(f"{provider} score exceeds max_score")
