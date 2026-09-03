"""Command-line entry point for a local baseline evaluation run."""

import argparse
from pathlib import Path

from .data import load_cases
from .grader import ExactAnswerBaseline
from .runner import make_run_id, run_evaluation


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate a math grader against human labels.")
    parser.add_argument("--dataset", type=Path, default=Path("data/evaluation_sample.jsonl"))
    parser.add_argument("--output", type=Path, help="Run output JSONL path")
    parser.add_argument("--grader-version", default="exact-answer-baseline-v1")
    parser.add_argument("--prompt-version", default="none")
    parser.add_argument("--model", default="deterministic-local")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    cases = load_cases(args.dataset)
    run_id = make_run_id()
    output = args.output or Path("results") / f"{run_id}.jsonl"
    results, metrics = run_evaluation(
        cases,
        ExactAnswerBaseline(),
        grader_version=args.grader_version,
        prompt_version=args.prompt_version,
        model=args.model,
        output_path=output,
        run_id=run_id,
    )
    print(f"Run ID: {results[0].run_id}")
    print(f"Cases:  {metrics.case_count}")
    print(f"MAE:    {metrics.mae:.4f}")
    print(f"QWK:    {metrics.qwk:.4f}")
    print(f"Results: {output}")


if __name__ == "__main__":
    main()
