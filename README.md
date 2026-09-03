# AI Grading Evaluation

A small, reproducible pipeline for comparing an AI math grader with fixed human grading labels. The ground-truth dataset is never modified; each grader invocation writes a separate, versioned run result.

## Layout

- `data/evaluation_sample.jsonl`: eight validated examples across algebra, calculus, and probability, including full-credit, partial-credit, and incorrect responses.
- `src/ai_grading_eval/models.py`: Pydantic schemas for evaluation cases, grader-safe inputs, and run results.
- `src/ai_grading_eval/runner.py`: framework-independent grader execution and result persistence.
- `src/ai_grading_eval/metrics.py`: MAE and quadratic weighted kappa (QWK).
- `results/`: generated experiment outputs (ignored by Git).

`required_points` and `rubric` are JSON arrays. Each rubric is validated to ensure its criterion scores sum to `max_score`, and every `human_score` must be in range.

## Run the pipeline

The included exact-answer grader is only a deterministic smoke-test baseline. It proves that loading, label isolation, grading, result persistence, and metric calculation work before a model-backed grader is added.

```bash
uv run ai-grading-eval
```

Use a unique output file for each experiment:

```bash
uv run ai-grading-eval \
  --grader-version grader-v1 \
  --prompt-version prompt-v1 \
  --model model-name \
  --output results/grader-v1.jsonl
```

Each output row contains only experiment data: `run_id`, `response_id`, grader/prompt/model versions, `ai_score`, `ai_feedback`, latency in seconds, and a UTC timestamp. Human labels remain solely in the evaluation dataset.

## Connect a real grader

Implement the `Grader` protocol in `grader.py`:

```python
class MyGrader:
    def grade(self, grader_input: GraderInput) -> GraderOutput:
        # Call the model with grader_input; parse a structured response.
        return GraderOutput(score=score, feedback=feedback)
```

Then pass the instance to `run_evaluation`. `GraderInput` deliberately excludes `human_score` and `human_feedback`, preventing ground-truth leakage into the grader call.

Pydantic Evals can later wrap the same cases and task execution for experiment orchestration and reporting. The research metrics remain the independent implementations in `metrics.py`.

## Test

```bash
uv run python -m unittest discover -s tests -v
```
