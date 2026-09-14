import base64
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from main import convert_pdf, find_pdfs


class FakeFiles:
    def __init__(self):
        self.deleted = []

    def upload(self, **kwargs):
        assert kwargs["purpose"] == "ocr"
        assert kwargs["file"]["content"].read() == b"pdf"
        return SimpleNamespace(id="uploaded-123")

    def delete(self, *, file_id):
        self.deleted.append(file_id)


class FakeOCR:
    def process(self, **kwargs):
        assert kwargs["document"] == {"type": "file", "file_id": "uploaded-123"}
        image = SimpleNamespace(
            id="figure.png", image_base64=base64.b64encode(b"image").decode()
        )
        return SimpleNamespace(
            pages=[
                SimpleNamespace(index=1, markdown="Second page", images=[]),
                SimpleNamespace(
                    index=0, markdown="First ![figure](figure.png)", images=[image]
                ),
            ]
        )


class ConverterTests(unittest.TestCase):
    def test_conversion_writes_markdown_images_and_cleans_up(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pdf = root / "sample.pdf"
            pdf.write_bytes(b"pdf")
            client = SimpleNamespace(files=FakeFiles(), ocr=FakeOCR())

            output = convert_pdf(client, pdf, root / "output")

            self.assertEqual(
                output.read_text(),
                "First ![figure](sample_assets/figure.png)\n\n---\n\nSecond page\n",
            )
            self.assertEqual(
                (root / "output/sample_assets/figure.png").read_bytes(), b"image"
            )
            self.assertEqual(client.files.deleted, ["uploaded-123"])

    def test_find_pdfs_ignores_other_files_and_sorts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "b.pdf").touch()
            (root / "A.PDF").touch()
            (root / "notes.txt").touch()
            self.assertEqual(
                [path.name for path in find_pdfs([], root)], ["A.PDF", "b.pdf"]
            )


if __name__ == "__main__":
    unittest.main()
