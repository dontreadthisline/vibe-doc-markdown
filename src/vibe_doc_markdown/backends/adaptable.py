from __future__ import annotations

from pathlib import Path

from ..types import Backend, ConvertInput, ConvertResult
from .base import AbstractBackend

_PDF_BACKEND = Backend.DOCLING
_DOCX_BACKEND = Backend.MARKITDOWN

_BACKEND_MAP: dict[str, Backend] = {
    ".pdf": _PDF_BACKEND,
    ".docx": _DOCX_BACKEND,
    ".doc": _DOCX_BACKEND,
}


class AdaptableBackend(AbstractBackend):
    """Auto-select optimal backend based on file type."""

    @property
    def name(self) -> Backend:
        return Backend.ADAPTABLE

    def convert(self, input: ConvertInput) -> ConvertResult:
        from . import BACKENDS

        suffix = Path(input.filename).suffix.lower()
        backend_enum = _BACKEND_MAP.get(suffix)

        if backend_enum is None:
            supported = ", ".join(_BACKEND_MAP.keys())
            raise ValueError(
                f"Unsupported file type: {suffix}. Supported: {supported}"
            )

        backend_cls = BACKENDS.get(backend_enum.value)
        if backend_cls is None:
            raise ValueError(f"Backend '{backend_enum.value}' not available")

        return backend_cls().convert(input)
