# AP Calculus PDF downloader and OCR

## Download PDFs

```bash
uv run python pdf_downloader.py
```

PDF files are saved under `downloaded_pdfs/`.

## Convert PDFs to Markdown with Mistral OCR

The OCR script uses `mistral-ocr-4-1` by default.

Create an API key in Mistral AI Studio and put it in `.env.local`:

```dotenv
MISTRAL_API_KEY=your-api-key
```

Start with one PDF to verify the output and API usage:

```bash
uv run python ocr_to_markdown.py --limit 1
```

Then convert every PDF:

```bash
uv run python ocr_to_markdown.py
```

Markdown files are saved under `ocr_markdown/` with the same directory structure
as `downloaded_pdfs/`. Existing Markdown files are skipped. Pass `--overwrite`
to process them again.
