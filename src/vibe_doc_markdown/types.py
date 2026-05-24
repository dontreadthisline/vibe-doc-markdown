from __future__ import annotations

import tempfile
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


class Backend(str, Enum):
    MARKITDOWN = "markitdown"
    PANDOC = "pandoc"
    PDFPLUMBER = "pdfplumber"
    DOCLING = "docling"
    MARKER = "marker"


@dataclass
class ConvertResult:
    markdown: str
    backend: Backend
    metadata: dict[str, Any] = field(default_factory=dict)


class ConvertInput:
    """Unified input abstraction over local files, remote URLs, and raw bytes."""

    __slots__ = ("_source", "_source_type", "_filename")

    def __init_subclass__(cls, **kwargs: Any) -> None:
        raise TypeError(f"{cls.__name__} cannot be subclassed")

    def __init__(self, source: str | Path, source_type: str) -> None:
        self._source = Path(source) if isinstance(source, str) and source_type == "path" else source
        self._source_type: str = source_type
        self._filename: str = (
            self._source.name
            if source_type == "path"
            else source.rsplit("/", 1)[-1] if source_type == "url" else "document"
        )

    @classmethod
    def from_path(cls, path: str | Path) -> ConvertInput:
        return cls(path, "path")

    @classmethod
    def from_url(cls, url: str) -> ConvertInput:
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            raise ValueError(f"Invalid URL: {url}")
        return cls(url, "url")

    @classmethod
    def from_bytes(cls, data: bytes, filename: str = "document") -> ConvertInput:
        instance = cls.__new__(cls)
        instance._source = data
        instance._source_type = "bytes"
        instance._filename = filename
        return instance

    @property
    def source_type(self) -> str:
        return self._source_type

    @property
    def filename(self) -> str:
        return self._filename

    def resolve_local_path(self) -> Path:
        """Resolve input to a local file path (download URL / write bytes to temp)."""
        if self._source_type == "path":
            return Path(self._source)
        if self._source_type == "url":
            import requests
            resp = requests.get(self._source, timeout=30)
            resp.raise_for_status()
            suffix = Path(self._filename).suffix or ".tmp"
            tmp = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
            tmp.write(resp.content)
            return Path(tmp.name)
        if self._source_type == "bytes":
            suffix = Path(self._filename).suffix or ".tmp"
            tmp = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
            tmp.write(self._source)
            return Path(tmp.name)
        raise ValueError(f"Unknown source type: {self._source_type}")

    def resolve_bytes(self) -> bytes:
        """Resolve input to raw bytes."""
        if self._source_type == "bytes":
            return self._source
        if self._source_type == "path":
            return Path(self._source).read_bytes()
        if self._source_type == "url":
            import requests
            resp = requests.get(self._source, timeout=30)
            resp.raise_for_status()
            return resp.content
        raise ValueError(f"Unknown source type: {self._source_type}")
