"""Dataset loading and result persistence helpers."""

import csv

import json
from pathlib import Path
from typing import Iterable

from .models import EvaluationCase, RunResult


def load_cases(path: Path) -> list[EvaluationCase]:
    if path.suffix.lower() == ".csv":
        return _load_csv_cases(path)

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


def _load_csv_cases(path: Path) -> list[EvaluationCase]:
    """Load the converter's CSV and keep only rows usable for evaluation.

    The converter stores rubric text for human readability.  For the Pydantic
    schema, each required point becomes one unit-scored rubric criterion.  Rows
    without a human score, answer, reference answer, or usable rubric are
    intentionally skipped because they cannot participate in score metrics.
    """
    cases: list[EvaluationCase] = []
    skipped: dict[str, int] = {}
    seen_response_ids: set[str] = set()
    with path.open(encoding="utf-8-sig", newline="") as source:
        for line_number, row in enumerate(csv.DictReader(source), start=2):
            reason = ""
            points = [item.strip() for item in row.get("required_points", "").split(";") if item.strip()]
            if not row.get("response_id"):
                reason = "missing response_id"
            elif row["response_id"] in seen_response_ids:
                reason = "duplicate response_id"
            elif not row.get("human_score"):
                reason = "missing human_score"
            elif not row.get("answer_text"):
                reason = "missing answer_text"
            elif not row.get("reference_answer"):
                reason = "missing reference_answer"
            elif not row.get("rubric") or not points:
                reason = "missing rubric or required_points"
            if reason:
                skipped[reason] = skipped.get(reason, 0) + 1
                continue
            try:
                max_score = int(row["max_score"])
                human_score = int(row["human_score"])
                if len(points) != max_score:
                    raise ValueError("required_points count does not equal max_score")
                rubric_items = [{"criterion": f"{point}: See the scoring guideline below.", "score": 1} for point in points]
                rubric_items[0]["criterion"] += f"\nScoring guideline:\n{row['rubric']}"
                case = EvaluationCase.model_validate(
                    {
                        "question_id": row["question_id"],
                        "source": row["source"],
                        "subject": row["subject"],
                        "topic": row.get("topic") or "Unknown",
                        "question_type": row["question_type"],
                        "question_text": row["question_text"],
                        "reference_answer": row["reference_answer"],
                        "required_points": points,
                        "rubric": rubric_items,
                        "max_score": max_score,
                        "response_id": row["response_id"],
                        "answer_text": row["answer_text"],
                        "final_answer": row.get("final_answer") or None,
                        "answer_image_path": row.get("answer_image_path") or None,
                        "human_score": human_score,
                        "human_feedback": row.get("human_feedback") or "Imported from AP scoring commentary.",
                    }
                )
            except Exception as exc:
                reason = f"invalid row: {exc.__class__.__name__}"
                skipped[reason] = skipped.get(reason, 0) + 1
                continue
            seen_response_ids.add(case.response_id)
            cases.append(case)
    if not cases:
        raise ValueError(f"No valid evaluation rows found in {path}")
    if skipped:
        summary = ", ".join(f"{count} {reason}" for reason, count in sorted(skipped.items()))
        print(f"Skipped {sum(skipped.values())} CSV rows: {summary}")
    return cases


def write_results(path: Path, results: Iterable[RunResult]) -> None:
    """Write a complete run atomically so interrupted runs do not look valid."""

    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_suffix(path.suffix + ".tmp")
    with temporary_path.open("w", encoding="utf-8") as destination:
        for result in results:
            destination.write(result.model_dump_json() + "\n")
    temporary_path.replace(path)
