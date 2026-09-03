"""Execute one versioned grader run against a fixed evaluation dataset."""

from datetime import UTC, datetime
from pathlib import Path
from time import perf_counter
from uuid import uuid4

from .data import write_results
from .grader import Grader
from .metrics import EvaluationMetrics, calculate_metrics
from .models import EvaluationCase, GraderInput, RunResult


def run_evaluation(
    cases: list[EvaluationCase],
    grader: Grader,
    *,
    grader_version: str,
    prompt_version: str,
    model: str,
    output_path: Path,
    run_id: str | None = None,
) -> tuple[list[RunResult], EvaluationMetrics]:
    if not cases:
        raise ValueError("at least one evaluation case is required")

    run_id = run_id or make_run_id()
    results: list[RunResult] = []

    for case in cases:
        grader_input = GraderInput.from_case(case)
        started = perf_counter()
        output = grader.grade(grader_input)
        latency = perf_counter() - started
        if output.score > case.max_score:
            raise ValueError(
                f"Grader score {output.score} exceeds max_score {case.max_score} "
                f"for response {case.response_id}"
            )
        results.append(
            RunResult(
                run_id=run_id,
                response_id=case.response_id,
                grader_version=grader_version,
                prompt_version=prompt_version,
                model=model,
                ai_score=output.score,
                ai_feedback=output.feedback,
                latency=latency,
                timestamp=datetime.now(UTC),
            )
        )

    write_results(output_path, results)
    metrics = calculate_metrics(
        [case.human_score for case in cases],
        [result.ai_score for result in results],
        maximum=max(case.max_score for case in cases),
    )
    return results, metrics


def make_run_id() -> str:
    return f"run-{datetime.now(UTC):%Y%m%dT%H%M%SZ}-{uuid4().hex[:8]}"
