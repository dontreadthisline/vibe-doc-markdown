from __future__ import annotations

import os
from pathlib import Path

from ..types import Backend, ConvertInput, ConvertResult
from .base import AbstractBackend

_RAPIDOCR_MODEL_DIR = Path.home() / ".cache" / "rapidocr" / "models"
_HF_CACHE_DIR = Path.home() / ".cache" / "huggingface"


def _setup_offline_mode() -> None:
    """Enable HuggingFace offline mode if local cache exists."""
    if _HF_CACHE_DIR.exists():
        os.environ.setdefault("HF_HUB_OFFLINE", "1")
        os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")


class DoclingBackend(AbstractBackend):
    @property
    def name(self) -> Backend:
        return Backend.DOCLING

    def convert(self, input: ConvertInput) -> ConvertResult:
        _setup_offline_mode()

        from docling.datamodel.base_models import InputFormat
        from docling.datamodel.pipeline_options import (
            PdfPipelineOptions,
            RapidOcrOptions,
        )
        from docling.document_converter import DocumentConverter, PdfFormatOption

        path = input.resolve_local_path()
        pipeline_options = PdfPipelineOptions()

        if _RAPIDOCR_MODEL_DIR.exists():
            pipeline_options.ocr_options = RapidOcrOptions(
                rapidocr_params={
                    "Global.model_root_dir": str(_RAPIDOCR_MODEL_DIR),
                }
            )

        converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
            }
        )
        result = converter.convert(str(path))
        return ConvertResult(
            markdown=result.document.export_to_markdown(),
            backend=self.name,
        )
