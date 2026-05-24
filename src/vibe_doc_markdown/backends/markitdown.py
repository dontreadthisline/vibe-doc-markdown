from __future__ import annotations

from ..types import Backend, ConvertInput, ConvertResult
from .base import AbstractBackend


class MarkItDownBackend(AbstractBackend):
    @property
    def name(self) -> Backend:
        return Backend.MARKITDOWN

    def convert(self, input: ConvertInput) -> ConvertResult:
        from markitdown import MarkItDown

        md = MarkItDown()
        if input.source_type == "bytes":
            path = input.resolve_local_path()
            result = md.convert(str(path))
        elif input.source_type == "url":
            import requests
            resp = requests.get(input._source, timeout=30)
            resp.raise_for_status()
            path = input.resolve_local_path()
            result = md.convert(str(path))
        else:
            result = md.convert(str(input._source))

        return ConvertResult(
            markdown=result.text_content,
            backend=self.name,
        )
