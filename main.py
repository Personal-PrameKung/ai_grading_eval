"""Convert PDF files to Markdown with Mistral OCR."""

from __future__ import annotations

import argparse
import base64
import binascii
import os
import re
import sys
from pathlib import Path
from typing import Any, Iterable

from dotenv import load_dotenv

try:
    # mistralai 2.10 installs the generated client under this module.
    from mistralai.client import Mistral
except ImportError:  # pragma: no cover - compatibility with other SDK releases
    from mistralai import Mistral


PROJECT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT_DIR = PROJECT_DIR / "input_pdfs"
DEFAULT_OUTPUT_DIR = PROJECT_DIR / "output_markdown"
DEFAULT_MODEL = "mistral-ocr-latest"


def _safe_asset_name(image_id: str, page_index: int, image_index: int) -> str:
    """Return a filename that cannot escape the asset directory."""
    name = Path(image_id).name
    name = re.sub(r"[^A-Za-z0-9._-]", "_", name)
    if not name or name in {".", ".."}:
        name = f"page-{page_index + 1}-image-{image_index + 1}.png"
    return name


def _decode_image(data: str) -> bytes:
    """Decode either raw base64 or a base64 data URL returned by Mistral."""
    encoded = data.split(",", 1)[1] if data.startswith("data:") else data
    try:
        return base64.b64decode(encoded, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise ValueError("Mistral returned invalid base64 image data") from exc


def _save_page_images(
    page: Any, markdown: str, output_dir: Path, document_stem: str
) -> str:
    assets_name = f"{document_stem}_assets"
    assets_dir = output_dir / assets_name

    for image_index, image in enumerate(page.images):
        image_data = getattr(image, "image_base64", None)
        if not isinstance(image_data, str) or not image_data:
            continue

        filename = _safe_asset_name(image.id, page.index, image_index)
        assets_dir.mkdir(parents=True, exist_ok=True)
        (assets_dir / filename).write_bytes(_decode_image(image_data))

        old_reference = image.id
        new_reference = f"{assets_name}/{filename}"
        markdown = markdown.replace(f"]({old_reference})", f"]({new_reference})")
        markdown = markdown.replace(
            f'src="{old_reference}"', f'src="{new_reference}"'
        )
        markdown = markdown.replace(
            f"src='{old_reference}'", f"src='{new_reference}'"
        )

    return markdown


def convert_pdf(
    client: Any,
    pdf_path: Path,
    output_dir: Path,
    *,
    model: str = DEFAULT_MODEL,
    include_images: bool = True,
) -> Path:
    """Convert one PDF and return the generated Markdown path."""
    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError(f"Not a PDF file: {pdf_path}")
    if not pdf_path.is_file():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    output_dir.mkdir(parents=True, exist_ok=True)
    uploaded_file_id: str | None = None

    try:
        with pdf_path.open("rb") as pdf_file:
            uploaded = client.files.upload(
                file={
                    "file_name": pdf_path.name,
                    "content": pdf_file,
                    "content_type": "application/pdf",
                },
                purpose="ocr",
            )
        uploaded_file_id = uploaded.id

        result = client.ocr.process(
            model=model,
            document={"type": "file", "file_id": uploaded_file_id},
            include_image_base64=include_images,
            include_blocks=False,
            table_format="markdown",
        )

        pages: list[str] = []
        for page in sorted(result.pages, key=lambda item: item.index):
            markdown = page.markdown.strip()
            if include_images:
                markdown = _save_page_images(
                    page, markdown, output_dir, pdf_path.stem
                )
            pages.append(markdown)

        output_path = output_dir / f"{pdf_path.stem}.md"
        content = "\n\n---\n\n".join(pages).rstrip() + "\n"
        temporary_path = output_path.with_suffix(".md.tmp")
        temporary_path.write_text(content, encoding="utf-8")
        temporary_path.replace(output_path)
        return output_path
    finally:
        if uploaded_file_id is not None:
            try:
                client.files.delete(file_id=uploaded_file_id)
            except Exception as exc:  # Cleanup should not discard a good conversion.
                print(
                    f"Warning: could not delete temporary Mistral file "
                    f"{uploaded_file_id}: {exc}",
                    file=sys.stderr,
                )


def find_pdfs(paths: Iterable[Path], input_dir: Path) -> list[Path]:
    """Resolve explicit inputs, or discover PDFs in the input folder."""
    supplied = list(paths)
    if supplied:
        return supplied
    return sorted(
        (
            path
            for path in input_dir.iterdir()
            if path.is_file() and path.suffix.lower() == ".pdf"
        ),
        key=lambda path: path.name.lower(),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert PDFs to Markdown using Mistral OCR."
    )
    parser.add_argument(
        "pdfs",
        nargs="*",
        type=Path,
        help="PDF files to convert (default: every PDF in input_pdfs/)",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Markdown destination directory",
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=DEFAULT_INPUT_DIR,
        help="Folder scanned when no PDF paths are supplied",
    )
    parser.add_argument(
        "--model",
        default=os.getenv("MISTRAL_OCR_MODEL", DEFAULT_MODEL),
        help=f"Mistral OCR model (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--no-images",
        action="store_true",
        help="Do not download images embedded in PDFs",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    load_dotenv(PROJECT_DIR / ".env")
    args = build_parser().parse_args(argv)

    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        print(
            "Error: MISTRAL_API_KEY is not set. Copy .env.example to .env and add your key.",
            file=sys.stderr,
        )
        return 2

    args.input_dir.mkdir(parents=True, exist_ok=True)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pdfs = find_pdfs(args.pdfs, args.input_dir)
    if not pdfs:
        print(f"No PDF files found in {args.input_dir}")
        return 0

    client = Mistral(api_key=api_key)
    failures = 0
    for pdf_path in pdfs:
        try:
            output_path = convert_pdf(
                client,
                pdf_path,
                args.output_dir,
                model=args.model,
                include_images=not args.no_images,
            )
            print(f"Converted {pdf_path} -> {output_path}")
        except Exception as exc:
            failures += 1
            print(f"Failed to convert {pdf_path}: {exc}", file=sys.stderr)

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
