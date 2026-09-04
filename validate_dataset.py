"""Validate files produced by convert_dataset.py."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


FIELDS = [
    "question_id", "source", "subject", "topic", "question_type",
    "question_text", "reference_answer", "required_points", "rubric",
    "max_score", "response_id", "answer_text", "final_answer",
    "answer_image_path", "human_score", "human_feedback",
]


def load(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def validate(root: Path, output: Path) -> list[str]:
    errors: list[str] = []
    dataset = load(output / "dataset.csv")
    bank = load(output / "question_bank.csv")
    exceptions = load(output / "exceptions.csv")
    exception_records = {(row["code"], row["record"]) for row in exceptions}
    for name, rows in (("dataset.csv", dataset), ("question_bank.csv", bank)):
        if not rows:
            errors.append(f"{name}: no rows")
        if rows and list(rows[0]) != FIELDS:
            errors.append(f"{name}: schema mismatch")
    seen = set()
    for row in dataset:
        rid = row["response_id"]
        if not rid or rid in seen:
            errors.append(f"dataset: missing or duplicate response_id {rid!r}")
        seen.add(rid)
        if not row["question_text"]:
            errors.append(f"dataset: empty text {rid}")
        if not row["answer_text"] and ("EMPTY_ANSWER_TEXT", rid) not in exception_records:
            errors.append(f"dataset: empty answer without exception {rid}")
        if row["max_score"] and row["human_score"]:
            if int(row["human_score"]) < 0 or int(row["human_score"]) > int(row["max_score"]):
                errors.append(f"dataset: score out of range {rid}")
        for asset in filter(None, (x.strip() for x in row["answer_image_path"].split(";"))):
            if not (root / asset).is_file():
                errors.append(f"dataset: missing image {asset}")
    for row in bank:
        if row["response_id"] or row["answer_text"] or row["human_score"]:
            errors.append(f"question_bank: response fields not empty {row['question_id']}")
        if not row["question_id"].startswith("AP_CALCULUS_") or "_2026_" not in row["question_id"]:
            errors.append(f"question_bank: non-2026 row {row['question_id']}")
    if not (output / "metadata.json").is_file():
        errors.append("metadata.json missing")
    else:
        metadata = json.loads((output / "metadata.json").read_text(encoding="utf-8"))
        if metadata.get("rows") != len(dataset):
            errors.append("metadata rows count mismatch")
        if metadata.get("question_bank_rows") != len(bank):
            errors.append("metadata question_bank_rows count mismatch")
        if metadata.get("exceptions") != len(exceptions):
            errors.append("metadata exceptions count mismatch")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    output = args.output or args.root / "dataset_output"
    errors = validate(args.root.resolve(), output.resolve())
    if errors:
        print(f"FAILED: {len(errors)} validation errors")
        print("\n".join(errors[:100]))
        return 1
    print("PASSED: schema, ids, scores, question-bank scope, metadata, and image paths")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
