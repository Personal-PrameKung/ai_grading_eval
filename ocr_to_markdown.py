import argparse
import base64
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from mistralai.client import Mistral


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT_DIR = SCRIPT_DIR / "downloaded_pdfs"
DEFAULT_OUTPUT_DIR = SCRIPT_DIR / "ocr_markdown"
DEFAULT_MODEL = "mistral-ocr-4-1"
ENV_FILE = SCRIPT_DIR / ".env.local"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert downloaded PDF files to Markdown with Mistral OCR."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument(
        "--limit",
        type=int,
        help="Process at most this many PDFs (useful for a low-cost test run).",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Run OCR again even when the destination Markdown already exists.",
    )
    return parser.parse_args()


def pdf_as_data_url(pdf_path: Path) -> str:
    encoded = base64.b64encode(pdf_path.read_bytes()).decode("ascii")
    return f"data:application/pdf;base64,{encoded}"


def save_page_images(page, markdown: str, asset_dir: Path) -> str:
    for image in page.images or []:
        image_data = image.image_base64
        if not isinstance(image_data, str) or not image_data:
            continue

        image_id = Path(image.id).name
        if not image_id:
            continue

        if image_data.startswith("data:"):
            _, image_data = image_data.split(",", maxsplit=1)

        output_name = f"page-{page.index + 1}-{image_id}"
        asset_dir.mkdir(parents=True, exist_ok=True)
        (asset_dir / output_name).write_bytes(base64.b64decode(image_data))

        relative_image_path = f"{asset_dir.name}/{output_name}"
        markdown = markdown.replace(f"]({image.id})", f"]({relative_image_path})")

    return markdown


def ocr_pdf(client: Mistral, pdf_path: Path, markdown_path: Path, model: str) -> None:
    response = client.ocr.process(
        model=model,
        document={
            "type": "document_url",
            "document_url": pdf_as_data_url(pdf_path),
        },
        include_image_base64=True,
    )

    asset_dir = markdown_path.parent / f"{markdown_path.stem}_assets"
    pages = []
    for page in response.pages:
        markdown = save_page_images(page, page.markdown, asset_dir)
        pages.append(f"<!-- Page {page.index + 1} -->\n\n{markdown.strip()}")

    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text("\n\n".join(pages) + "\n", encoding="utf-8")


def destination_for(pdf_path: Path, input_dir: Path, output_dir: Path) -> Path:
    return (output_dir / pdf_path.relative_to(input_dir)).with_suffix(".md")


def main() -> int:
    load_dotenv(ENV_FILE)
    args = parse_args()
    input_dir = args.input.resolve()
    output_dir = args.output.resolve()

    if args.limit is not None and args.limit < 1:
        print("Error: --limit must be at least 1.", file=sys.stderr)
        return 2
    if not input_dir.is_dir():
        print(f"Error: input folder does not exist: {input_dir}", file=sys.stderr)
        return 2

    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print(f"Error: set MISTRAL_API_KEY in {ENV_FILE}", file=sys.stderr)
        return 2

    pdf_paths = sorted(input_dir.rglob("*.pdf"))
    if args.limit is not None:
        pdf_paths = pdf_paths[: args.limit]
    if not pdf_paths:
        print(f"No PDF files found in {input_dir}")
        return 0

    client = Mistral(api_key=api_key)
    completed = skipped = failed = 0

    for position, pdf_path in enumerate(pdf_paths, start=1):
        markdown_path = destination_for(pdf_path, input_dir, output_dir)
        if markdown_path.exists() and not args.overwrite:
            print(f"[{position}/{len(pdf_paths)}] Skipped: {pdf_path.name}")
            skipped += 1
            continue

        print(f"[{position}/{len(pdf_paths)}] OCR: {pdf_path}")
        try:
            ocr_pdf(client, pdf_path, markdown_path, args.model)
        except Exception as error:
            print(f"  Failed: {error}", file=sys.stderr)
            failed += 1
        else:
            print(f"  Saved: {markdown_path}")
            completed += 1

    print(f"Done: {completed} converted, {skipped} skipped, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
