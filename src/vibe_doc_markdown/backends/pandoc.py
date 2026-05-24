from __future__ import annotations

from pathlib import Path

import pypandoc

from ..types import Backend, ConvertInput, ConvertResult
from .base import AbstractBackend

_PANDOC_PDF_FORMATS = frozenset({"pdf", "bin", "odt"})


class PandocBackend(AbstractBackend):
    @property
    def name(self) -> Backend:
        return Backend.PANDOC

    def convert(self, input: ConvertInput) -> ConvertResult:
        path = str(input.resolve_local_path())
        suffix = Path(path).suffix.lstrip(".").lower()

        if suffix in _PANDOC_PDF_FORMATS:
            raise ValueError(
                f"Pandoc cannot parse .{suffix} files natively. "
                "Use a different backend (e.g. markitdown, docling, pdfplumber) for PDFs."
            )

        output = pypandoc.convert_file(path, "markdown", extra_args=["--wrap=none"])
        return ConvertResult(
            markdown=output,
            backend=self.name,
        )
