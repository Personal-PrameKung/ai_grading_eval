"""Pydantic Evals runner for the human-scored math grading dataset."""

from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from time import perf_counter
from typing import Any

from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import Evaluator, EvaluatorContext

from .data import write_results
from .grader import Grader
from .metrics import EvaluationMetrics, calculate_metrics
from .models import EvaluationCase, GraderInput, GraderOutput, RunResult
from .runner import make_run_id


@dataclass
class ScoreAccuracyEvaluator(Evaluator[GraderOutput, int]):
    """Return 1 when the LLM score exactly matches the human score."""

    def evaluate(self, ctx: EvaluatorContext[GraderOutput, int]) -> float:
        return float(ctx.output.score == ctx.expected_output)


@dataclass
class AbsoluteScoreErrorEvaluator(Evaluator[GraderOutput, int]):
    """Return the absolute score error for a case."""

    def evaluate(self, ctx: EvaluatorContext[GraderOutput, int]) -> float:
        return float(abs(ctx.output.score - ctx.expected_output))


def run_pydantic_evaluation(
    cases: list[EvaluationCase],
    grader: Grader,
    *,
    grader_version: str,
    prompt_version: str,
    model: str,
    output_path: Path,
    run_id: str | None = None,
) -> tuple[Any, list[RunResult], EvaluationMetrics]:
    """Run the grader through Pydantic Evals and calculate dataset metrics."""

    if not cases:
        raise ValueError("at least one evaluation case is required")
    run_id = run_id or make_run_id()
    results_by_response_id: dict[str, RunResult] = {}

    def task(case: EvaluationCase) -> GraderOutput:
        started = perf_counter()
        output = grader.grade(GraderInput.from_case(case))
        if output.score > case.max_score:
            raise ValueError(f"Grader score exceeds max_score for response {case.response_id}")
        results_by_response_id[case.response_id] = RunResult(
                run_id=run_id,
                response_id=case.response_id,
                grader_version=grader_version,
                prompt_version=prompt_version,
                model=model,
                ai_score=output.score,
                ai_feedback=output.feedback,
                latency=perf_counter() - started,
                timestamp=datetime.now(UTC),
            )
        return output

    dataset = Dataset[EvaluationCase, GraderOutput, Any](
        name="ap_calculus_grading",
        cases=[
            Case(
                name=case.response_id,
                inputs=case,
                expected_output=case.human_score,
            )
            for case in cases
        ],
        evaluators=[ScoreAccuracyEvaluator(), AbsoluteScoreErrorEvaluator()],
    )
    report = dataset.evaluate_sync(task)
    # Pydantic Evals may complete cases concurrently. Re-align outputs with
    # the original case order before calculating pairwise metrics.
    results = [results_by_response_id[case.response_id] for case in cases]
    write_results(output_path, results)
    metrics = calculate_metrics(
        [case.human_score for case in cases],
        [result.ai_score for result in results],
        maximum=max(case.max_score for case in cases),
    )
    return report, results, metrics
