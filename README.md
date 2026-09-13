# PDF rubric generator

Calls graderai's existing `RubricGenerationAgent.generate_rubric()` directly.
Only source preparation is adapted: local PDFs become JPEG page images in memory.
The existing extractor, per-question generator, reviewer, and validation are reused.
Requires the sibling graderai checkout; no API server, database, Redis, or cloud file storage is required.
PDF images are sent to the configured OpenAI models, which incur API usage charges.

## Setup

```bash
uv sync
cp .env.example .env
```

Set `OPENAI_API_KEY` in `.env`. Adjust language (`english` or `thai`), subject,
grade level, scoring policy, or the backend path as needed. Environment variables
already exported in your shell take precedence over `.env`. Configure before importing `main`.

On this NixOS machine, PyMuPDF also needs the C++ runtime on the library path:

```bash
export LD_LIBRARY_PATH=/nix/store/0vqb1mcas5j8dv6bhbrshinlgsg6bvgi-gcc-15.3.0-lib/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
```

This store path is machine-specific and may change after a system update.

## Run

```bash
uv run python main.py /path/to/worksheet.pdf
uv run python main.py /path/to/pdfs --output ./output
```

Directory inputs are searched recursively. Each PDF is treated as a separate rubric.
Output mirrors the input subdirectories, e.g. `output/unit1/test.pdf.rubric.json`.
PDFs run sequentially; graderai processes questions within each PDF concurrently.
Existing results are skipped so rerunning a batch resumes missing results.
Use `--overwrite` to regenerate saved results, including after changing settings or inputs.
Run only one batch against a given output directory at a time.
Failures are printed, remaining PDFs continue, and the command exits with status 1 if any fail.

## Call the function repeatedly

```python
import asyncio
from main import generate_rubric, save_json
from pathlib import Path

async def run():
    for pdf in ["algebra.pdf", "geometry.pdf"]:
        rubric = await generate_rubric(pdf, language="english", subject="mathematics")
        save_json(Path("output") / f"{pdf}.rubric.json", rubric)

asyncio.run(run())
```

`generate_rubric()` returns a JSON-compatible dictionary with a `questions` list;
it does not write files. Scores are serialized as decimal strings by the existing schema.
AI reviewer rejections remain in the output with `needs_human_review` and feedback.
Review the rubric before using it for grading. This runner does not publish or save to graderai's database.
