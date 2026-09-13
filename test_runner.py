import argparse
import asyncio
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import AsyncMock, patch

os.environ.setdefault("GRADERAI_BACKEND_PATH", "/home/pramekung/Documents/capstone/graderai/backend")

import fitz
import main


class RunnerTests(unittest.TestCase):
    def test_local_pdf_pages_and_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            pdf = Path(directory) / "input.pdf"
            with fitz.open() as document:
                document.new_page().insert_text((72, 72), "Question 1: 2 + 2?")
                document.new_page().insert_text((72, 72), "Answer: 4")
                document.save(pdf)
            pages = asyncio.run(main.LocalPDFRubricAgent()._prepare_source_pages(
                input_snapshot={"local_pdf": str(pdf)}
            ))
            self.assertEqual([p.page_number for p in pages], [1, 2])
            self.assertTrue(all(p.file_bytes.startswith(b"\xff\xd8") for p in pages))
            draft = main.generate_rubric.__globals__["LocalPDFRubricAgent"]
            result = unittest.mock.Mock()
            result.model_dump.return_value = {"questions": []}
            with patch.object(main.settings, "OPENAI_API_KEY", "test"), patch.object(
                draft, "generate_rubric", new_callable=AsyncMock, return_value=result
            ) as call:
                asyncio.run(main.generate_rubric(pdf, language="thai", subject="math"))
                snapshot = call.call_args.kwargs["input_snapshot"]
                self.assertEqual(snapshot["rubric_version"]["rubric_language"], "thai")
                self.assertEqual(snapshot["local_pdf"], str(pdf))

    def test_batch_continues_and_resumes(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "pdfs"
            source.mkdir()
            for name in ("a.pdf", "b.pdf", "c.PDF"):
                (source / name).touch()
            output = Path(directory) / "output"
            main.save_json(output / "a.pdf.rubric.json", {"existing": True})
            args = argparse.Namespace(input=source, output=output, overwrite=False)
            with patch.object(main, "generate_rubric", new_callable=AsyncMock,
                              side_effect=[RuntimeError("test failure"), {"questions": []}]) as call:
                self.assertEqual(asyncio.run(main.run_batch(args)), 1)
                self.assertEqual(call.await_count, 2)
            self.assertFalse((output / "b.pdf.rubric.json").exists())
            self.assertTrue((output / "c.PDF.rubric.json").exists())
            self.assertEqual((output / "a.pdf.rubric.json").read_text(), '{\n  "existing": true\n}\n')


if __name__ == "__main__":
    unittest.main()
