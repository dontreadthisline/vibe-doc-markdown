from __future__ import annotations

import pytest
from vibe_doc_markdown import (
    Backend,
    ConvertInput,
    ConvertResult,
    convert_document,
)
from vibe_doc_markdown.backends import BACKENDS

# ---------------------------------------------------------------------------
# ConvertInput
# ---------------------------------------------------------------------------


class TestConvertInput:
    def test_from_path_str(self) -> None:
        inp = ConvertInput.from_path("/tmp/test.pdf")
        assert inp.source_type == "path"
        assert inp.filename == "test.pdf"

    def test_from_path_pathlib(self) -> None:
        from pathlib import Path
        inp = ConvertInput.from_path(Path("/tmp/test.pdf"))
        assert inp.source_type == "path"
        assert inp.filename == "test.pdf"

    def test_from_url(self) -> None:
        inp = ConvertInput.from_url("https://example.com/doc.pdf")
        assert inp.source_type == "url"
        assert inp.filename == "doc.pdf"

    def test_from_url_invalid(self) -> None:
        with pytest.raises(ValueError, match="Invalid URL"):
            ConvertInput.from_url("not-a-url")

    def test_from_bytes(self) -> None:
        inp = ConvertInput.from_bytes(b"hello", filename="test.txt")
        assert inp.source_type == "bytes"
        assert inp.filename == "test.txt"
        assert inp.resolve_bytes() == b"hello"

    def test_from_bytes_default_filename(self) -> None:
        inp = ConvertInput.from_bytes(b"data")
        assert inp.filename == "document"

    def test_resolve_bytes_from_path(self, tmp_path: pytest.TempPathFactory) -> None:
        p = tmp_path / "test.txt"
        p.write_text("hello")
        inp = ConvertInput.from_path(str(p))
        assert inp.resolve_bytes() == b"hello"

    def test_cannot_subclass(self) -> None:
        with pytest.raises(TypeError):
            class MyInput(ConvertInput):
                pass


# ---------------------------------------------------------------------------
# Backend enum
# ---------------------------------------------------------------------------


class TestBackendEnum:
    def test_all_members(self) -> None:
        assert Backend.MARKITDOWN.value == "markitdown"
        assert Backend.PANDOC.value == "pandoc"
        assert Backend.PDFPLUMBER.value == "pdfplumber"
        assert Backend.DOCLING.value == "docling"
        assert Backend.MARKER.value == "marker"


# ---------------------------------------------------------------------------
# Real conversion tests
# ---------------------------------------------------------------------------


@pytest.mark.slow
class TestConversionWithPdf:
    """Test all available backends with the real PDF file."""

    @pytest.fixture(autouse=True)
    def _check_pdf(self, sample_pdf_path: str) -> None:
        from pathlib import Path
        if not Path(sample_pdf_path).exists():
            pytest.skip(f"PDF not found: {sample_pdf_path}")

    def _assert_valid_result(self, result: ConvertResult) -> None:
        assert isinstance(result, ConvertResult)
        assert isinstance(result.markdown, str)
        assert len(result.markdown) > 0
        assert isinstance(result.backend, Backend)

    def test_convert_markitdown_from_path(self, sample_pdf_path: str) -> None:
        if "markitdown" not in BACKENDS:
            pytest.skip("markitdown not available")
        inp = ConvertInput.from_path(sample_pdf_path)
        result = convert_document(inp, Backend.MARKITDOWN)
        self._assert_valid_result(result)

    def test_convert_markitdown_from_bytes(self, sample_pdf_bytes: bytes) -> None:
        if "markitdown" not in BACKENDS:
            pytest.skip("markitdown not available")
        inp = ConvertInput.from_bytes(sample_pdf_bytes, filename="2603.25551_zh_CN.pdf")
        result = convert_document(inp, Backend.MARKITDOWN)
        self._assert_valid_result(result)

    def test_convert_pandoc_rejects_pdf(self, sample_pdf_path: str) -> None:
        if "pandoc" not in BACKENDS:
            pytest.skip("pandoc not available")
        inp = ConvertInput.from_path(sample_pdf_path)
        with pytest.raises(ValueError, match="Pandoc cannot parse"):
            convert_document(inp, Backend.PANDOC)

    def test_convert_pdfplumber_from_path(self, sample_pdf_path: str) -> None:
        if "pdfplumber" not in BACKENDS:
            pytest.skip("pdfplumber not available")
        inp = ConvertInput.from_path(sample_pdf_path)
        result = convert_document(inp, Backend.PDFPLUMBER)
        self._assert_valid_result(result)

    def test_convert_pdfplumber_from_bytes(self, sample_pdf_bytes: bytes) -> None:
        if "pdfplumber" not in BACKENDS:
            pytest.skip("pdfplumber not available")
        inp = ConvertInput.from_bytes(sample_pdf_bytes, filename="2603.25551_zh_CN.pdf")
        result = convert_document(inp, Backend.PDFPLUMBER)
        self._assert_valid_result(result)

    def test_convert_docling_from_path(self, sample_pdf_path: str) -> None:
        if "docling" not in BACKENDS:
            pytest.skip("docling not available")
        inp = ConvertInput.from_path(sample_pdf_path)
        result = convert_document(inp, Backend.DOCLING)
        self._assert_valid_result(result)

    def test_convert_docling_from_bytes(self, sample_pdf_bytes: bytes) -> None:
        if "docling" not in BACKENDS:
            pytest.skip("docling not available")
        inp = ConvertInput.from_bytes(sample_pdf_bytes, filename="2603.25551_zh_CN.pdf")
        result = convert_document(inp, Backend.DOCLING)
        self._assert_valid_result(result)

    def test_convert_marker_from_path(self, sample_pdf_path: str) -> None:
        if "marker" not in BACKENDS:
            pytest.skip("marker not available")
        inp = ConvertInput.from_path(sample_pdf_path)
        result = convert_document(inp, Backend.MARKER)
        self._assert_valid_result(result)

    def test_convert_marker_from_bytes(self, sample_pdf_bytes: bytes) -> None:
        if "marker" not in BACKENDS:
            pytest.skip("marker not available")
        inp = ConvertInput.from_bytes(sample_pdf_bytes, filename="2603.25551_zh_CN.pdf")
        result = convert_document(inp, Backend.MARKER)
        self._assert_valid_result(result)

    def test_all_backends_produce_non_empty_output(self, sample_pdf_path: str) -> None:
        for backend in [Backend.MARKITDOWN, Backend.PDFPLUMBER, Backend.DOCLING, Backend.MARKER]:
            if backend.value not in BACKENDS:
                continue
            inp = ConvertInput.from_path(sample_pdf_path)
            result = convert_document(inp, backend)
            assert len(result.markdown) > 0, f"{backend} returned empty output"


# ---------------------------------------------------------------------------
# Error / edge cases
# ---------------------------------------------------------------------------


class TestErrorCases:
    def test_invalid_backend_raises(self) -> None:
        from vibe_doc_markdown.backends import BACKENDS
        inp = ConvertInput.from_bytes(b"fake pdf content", filename="test.pdf")
        # Must be a registered Backend enum member but not in BACKENDS dict.
        # Marker is now installed, so use a value we know can't be registered.
        fake = None
        for be in Backend:
            if be.value not in BACKENDS:
                fake = be
                break
        if fake is None:
            pytest.skip("all registered Backend members have available backends")
        with pytest.raises(ValueError, match="not available"):
            convert_document(inp, fake)

    def test_nonexistent_file(self) -> None:
        inp = ConvertInput.from_path("/nonexistent/path/file.pdf")
        with pytest.raises(FileNotFoundError):
            convert_document(inp, Backend.MARKITDOWN)
