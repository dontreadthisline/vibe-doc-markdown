from __future__ import annotations

from ..types import Backend, ConvertInput, ConvertResult
from .base import AbstractBackend


class MarkerBackend(AbstractBackend):
    @property
    def name(self) -> Backend:
        return Backend.MARKER

    def convert(self, input: ConvertInput) -> ConvertResult:
        from marker.converters.pdf import PdfConverter
        from marker.models import create_model_dict
        from marker.output import text_from_rendered

        path = input.resolve_local_path()
        converter = PdfConverter(artifact_dict=create_model_dict())
        rendered = converter(str(path))
        md_text, _, _ = text_from_rendered(rendered)
        return ConvertResult(
            markdown=md_text,
            backend=self.name,
        )
