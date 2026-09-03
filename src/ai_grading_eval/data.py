"""JSONL loading and persistence helpers."""

import json
from pathlib import Path
from typing import Iterable

from .models import EvaluationCase, RunResult


def load_cases(path: Path) -> list[EvaluationCase]:
    cases: list[EvaluationCase] = []
    seen_response_ids: set[str] = set()

    with path.open(encoding="utf-8") as source:
        for line_number, line in enumerate(source, start=1):
            if not line.strip():
                continue
            try:
                case = EvaluationCase.model_validate_json(line)
            except Exception as exc:
                raise ValueError(f"Invalid evaluation row at {path}:{line_number}: {exc}") from exc
            if case.response_id in seen_response_ids:
                raise ValueError(f"Duplicate response_id {case.response_id!r} at {path}:{line_number}")
            seen_response_ids.add(case.response_id)
            cases.append(case)

    if not cases:
        raise ValueError(f"Evaluation dataset is empty: {path}")
    return cases


def write_results(path: Path, results: Iterable[RunResult]) -> None:
    """Write a complete run atomically so interrupted runs do not look valid."""

    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_suffix(path.suffix + ".tmp")
    with temporary_path.open("w", encoding="utf-8") as destination:
        for result in results:
            destination.write(result.model_dump_json() + "\n")
    temporary_path.replace(path)
