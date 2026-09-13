"""Generate rubric JSON directly from local PDFs using graderai's existing agent."""

import argparse
import asyncio
import json
import os
from pathlib import Path
import sys
import tempfile

from dotenv import load_dotenv
import pymupdf

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")
backend = Path(os.getenv("GRADERAI_BACKEND_PATH", str(ROOT.parent / "graderai/backend")))
if not (backend / "app/agents/rubric.py").is_file():
    raise RuntimeError("Set GRADERAI_BACKEND_PATH in .env to graderai's backend directory")
sys.path.insert(0, str(backend.resolve()))

from app.agents.rubric import RubricGenerationAgent  # noqa: E402
from app.core.config import settings  # noqa: E402
from app.schemas.classroom import PreparedRubricSourcePage  # noqa: E402


def render_pdf(pdf_path: Path) -> list[bytes]:
    """Match graderai's 2x JPEG rendering without importing its service package."""
    with pymupdf.open(pdf_path) as document:
        if document.needs_pass:
            raise ValueError("Password-protected PDFs are not supported")
        if not document.page_count:
            raise ValueError("PDF has no pages")
        return [
            page.get_pixmap(matrix=pymupdf.Matrix(2, 2), colorspace=pymupdf.csRGB, alpha=False)
            .tobytes("jpeg", jpg_quality=80)
            for page in document
        ]


class LocalPDFRubricAgent(RubricGenerationAgent):
    """Replace remote source fetching with local PDF rendering only."""

    async def _prepare_source_pages(self, *, input_snapshot):
        pdf_path = Path(input_snapshot["local_pdf"])
        images = await asyncio.to_thread(render_pdf, pdf_path)
        return [
            PreparedRubricSourcePage(
                source_kind="teacher_solution",
                source_type="image",
                page_number=number,
                display_order=number,
                file_bytes=data,
                media_type="image/jpeg",
            )
            for number, data in enumerate(images, start=1)
        ]


async def generate_rubric(
    pdf_path: str | Path,
    *,
    language: str | None = None,
    subject: str | None = None,
    grade_level: str | None = None,
    scoring_policy: str | None = None,
) -> dict:
    """Generate one rubric. Repeat with await; raises on failure and never writes files."""
    pdf_path = Path(pdf_path).expanduser().resolve()
    if not pdf_path.is_file() or pdf_path.suffix.lower() != ".pdf":
        raise ValueError(f"Expected an existing PDF: {pdf_path}")
    if not settings.OPENAI_API_KEY.strip():
        raise ValueError("Set OPENAI_API_KEY in .env before generating rubrics")
    language = language or os.getenv("RUBRIC_LANGUAGE", "english")
    if language not in {"english", "thai"}:
        raise ValueError("language must be 'english' or 'thai'")
    metadata = {
        "rubric_language": language,
        "subject": subject if subject is not None else os.getenv("RUBRIC_SUBJECT", ""),
        "grade_level": grade_level if grade_level is not None else os.getenv("RUBRIC_GRADE_LEVEL", ""),
        "scoring_policy": scoring_policy if scoring_policy is not None else os.getenv("RUBRIC_SCORING_POLICY", ""),
    }
    draft = await LocalPDFRubricAgent().generate_rubric(
        input_snapshot={"local_pdf": str(pdf_path), "rubric_version": metadata}
    )
    return draft.model_dump(mode="json")


def save_json(path: Path, result: dict) -> None:
    """Use an atomic replacement so interrupted writes do not leave partial JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as file:
            temporary = Path(file.name)
            json.dump(result, file, ensure_ascii=False, indent=2)
            file.write("\n")
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


async def run_batch(args) -> int:
    source = args.input.expanduser().resolve()
    output = args.output.expanduser().resolve()
    if source.is_dir():
        files = sorted(p for p in source.rglob("*") if p.is_file() and p.suffix.lower() == ".pdf")
        base = source
    elif source.is_file() and source.suffix.lower() == ".pdf":
        files, base = [source], source.parent
    else:
        raise ValueError(f"Input must be a PDF or directory: {source}")
    if not files:
        raise ValueError(f"No PDFs found in {source}")
    failed = 0
    for index, pdf in enumerate(files, start=1):
        # Preserve subdirectories and the PDF extension to avoid filename collisions.
        destination = output / (str(pdf.relative_to(base)) + ".rubric.json")
        if destination.exists() and not args.overwrite:
            print(f"[{index}/{len(files)}] SKIP {pdf.name}", flush=True)
            continue
        print(f"[{index}/{len(files)}] GENERATE {pdf}", flush=True)
        try:
            result = await generate_rubric(pdf)
            save_json(destination, result)
            print(f"SAVED {destination}", flush=True)
        except Exception as exc:
            failed += 1
            print(f"FAILED {pdf}: {exc}", file=sys.stderr, flush=True)
    print(f"Finished: {len(files)} PDFs checked, {failed} failed.")
    return 1 if failed else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="One PDF or a directory searched recursively")
    parser.add_argument("--output", type=Path, default=ROOT / "output")
    parser.add_argument("--overwrite", action="store_true", help="Regenerate existing results (makes new AI calls)")
    args = parser.parse_args()
    try:
        return asyncio.run(run_batch(args))
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
