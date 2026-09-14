# PDF to Markdown

Convert PDF documents to Markdown with the Mistral OCR API. The converter keeps
page boundaries, Markdown tables, and (by default) extracted images.

## Setup

Dependencies are already declared in `pyproject.toml`. Install them with:

```bash
uv sync
```

Create your local environment file and add a Mistral API key:

```bash
cp .env.example .env
```

```dotenv
MISTRAL_API_KEY=your_actual_key
```

## Convert PDFs

Put one or more PDFs in `input_pdfs/`, then run:

```bash
uv run python main.py
```

Markdown files are written to `output_markdown/`. Images are stored beside them
in `<document-name>_assets/` folders, with working relative links in the Markdown.

You can also provide files explicitly:

```bash
uv run python main.py report.pdf invoice.pdf
```

Useful options:

```bash
uv run python main.py --help
uv run python main.py --no-images
uv run python main.py --output-dir converted report.pdf
```

The PDFs are uploaded temporarily for OCR and deleted from Mistral after each
conversion, including when conversion fails.
