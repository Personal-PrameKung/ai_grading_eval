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

## Evaluate the converted AP Calculus dataset

The converter output at `../ai_grading_eval/dataset_output/dataset.csv` can be passed directly to the CLI. CSV rows that do not have enough ground-truth data for evaluation are skipped and reported. The CSV adapter converts each required point into a unit-scored Pydantic rubric criterion.

```bash
uv run ai-grading-eval \
  --dataset ../ai_grading_eval/dataset_output/dataset.csv \
  --grader-version exact-answer-baseline-v1 \
  --prompt-version none \
  --model deterministic-local \
  --output results/ap-calculus-baseline.jsonl
```

The CLI reports exact-score accuracy, MAE, and QWK. The current baseline is an exact string-match smoke test; it is not a production math grader. Because the converted rows are at sub-question level and have different `max_score` values, compare QWK by score scale or aggregate Parts A-D to a full-question score for a final experiment.

### OpenAI grader

Create a `.env` file in the `main` folder (do not commit the API key). The CLI loads it with `python-dotenv`:

```dotenv
OPENAI_API_KEY="ใส่ API key ของคุณตรงนี้"
AI_MODEL=gpt-5.4-mini
AI_TEMPERATURE=0.7
LLM_PROVIDER=openai
```

Install/sync the new dependency:

```powershell
uv sync
```

Run a small smoke test first:

```powershell
uv run ai-grading-eval --dataset "D:\Work\Chula\2026-1\Capstone\KruGrade\ai_grading_eval\dataset_output\dataset.csv" --grader auto --limit 5 --output results\openai-smoke.jsonl
```

Run the full evaluation:

```powershell
uv run ai-grading-eval --dataset "D:\Work\Chula\2026-1\Capstone\KruGrade\ai_grading_eval\dataset_output\dataset.csv" --grader auto --output results\openai-full.jsonl
```

The command prints Accuracy, MAE, and QWK and saves per-case predictions to the output JSONL.

The default runner is now `pydantic-evals`: it creates a typed `Dataset`/`Case`, runs the grader with `evaluate_sync()`, and reports the case-level `ScoreAccuracyEvaluator` and `AbsoluteScoreErrorEvaluator`. Accuracy, MAE, and QWK are calculated across the complete dataset after the Pydantic Evals report. Use `--runner custom` to run the previous runner.

### Gemini grader

Set the API key in the shell; never commit it to the repository:

```powershell
$env:GEMINI_API_KEY = "your-key"
uv run ai-grading-eval `
  --grader gemini `
  --dataset ..\ai_grading_eval\dataset_output\dataset.csv `
  --gemini-model gemini-3.6-flash `
  --grader-version gemini-v1 `
  --prompt-version rubric-prompt-v1 `
  --model gemini-3.6-flash `
  --output results/gemini-v1.jsonl
```

The first Gemini implementation is text-only and sends the OCR `answer_text`. It requires Gemini to return one 0/1 score for every required point, plus the total score and feedback; the response is validated with Pydantic before it is persisted.

For a small API smoke test, add `--limit 5`. Free-tier Gemini quotas may require running the full dataset in batches or waiting for the quota window to reset.

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
