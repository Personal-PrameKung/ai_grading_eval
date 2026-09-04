"""Command-line entry point for a local baseline evaluation run."""

import argparse
import os
from pathlib import Path

from dotenv import load_dotenv

from .data import load_cases
from .grader import ExactAnswerBaseline, GeminiGrader, OpenAIGrader
from .pydantic_runner import run_pydantic_evaluation
from .runner import make_run_id, run_evaluation


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate a math grader against human labels.")
    parser.add_argument("--dataset", type=Path, default=Path("data/evaluation_sample.jsonl"))
    parser.add_argument("--output", type=Path, help="Run output JSONL path")
    parser.add_argument("--grader-version", default="exact-answer-baseline-v1")
    parser.add_argument("--prompt-version", default="none")
    parser.add_argument("--model", default="deterministic-local")
    parser.add_argument("--runner", choices=("pydantic", "custom"), default="pydantic")
    parser.add_argument("--grader", choices=("auto", "exact", "gemini", "openai"), default="auto")
    parser.add_argument("--gemini-model", default="gemini-3.6-flash")
    parser.add_argument("--gemini-timeout", type=float, default=120.0)
    parser.add_argument("--openai-model", default=None)
    parser.add_argument("--openai-temperature", type=float, default=None)
    parser.add_argument("--openai-timeout", type=float, default=120.0)
    parser.add_argument("--limit", type=int, help="Evaluate only the first N cases (useful for API smoke tests).")
    return parser


def main() -> None:
    # Load local secrets/config before selecting the grader and model.
    load_dotenv()
    parser = build_parser()
    args = parser.parse_args()
    cases = load_cases(args.dataset)
    if args.limit is not None:
        if args.limit < 1:
            parser.error("--limit must be at least 1")
        cases = cases[: args.limit]
    run_id = make_run_id()
    output = args.output or Path("results") / f"{run_id}.jsonl"
    provider = args.grader
    if provider == "auto":
        provider = os.environ.get("LLM_PROVIDER", "exact").lower()
    if provider == "openai":
        grader = OpenAIGrader(
            model=args.openai_model or os.environ.get("AI_MODEL", "gpt-5.4-mini"),
            temperature=(args.openai_temperature if args.openai_temperature is not None else float(os.environ.get("AI_TEMPERATURE", "0.7"))),
            timeout=args.openai_timeout,
        )
    elif provider == "gemini":
        grader = GeminiGrader(model=args.gemini_model, timeout=args.gemini_timeout)
    elif provider == "exact":
        grader = ExactAnswerBaseline()
    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: {provider}")
    model_name = args.model
    if model_name == "deterministic-local":
        model_name = getattr(grader, "model", model_name)
    if args.runner == "pydantic":
        report, results, metrics = run_pydantic_evaluation(
            cases,
            grader,
            grader_version=args.grader_version,
            prompt_version=args.prompt_version,
            model=model_name,
            output_path=output,
            run_id=run_id,
        )
        report.print(include_input=False, include_output=True, include_durations=False)
    else:
        results, metrics = run_evaluation(
            cases,
            grader,
            grader_version=args.grader_version,
            prompt_version=args.prompt_version,
            model=model_name,
            output_path=output,
            run_id=run_id,
        )
    print(f"Run ID: {results[0].run_id}")
    print(f"Cases:  {metrics.case_count}")
    print(f"Accuracy: {metrics.accuracy:.4f}")
    print(f"MAE:    {metrics.mae:.4f}")
    print(f"QWK:    {metrics.qwk:.4f}")
    print(f"Results: {output}")


if __name__ == "__main__":
    main()
