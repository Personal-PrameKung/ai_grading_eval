"""Grader interface and a deterministic baseline for pipeline smoke tests."""

import re
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
