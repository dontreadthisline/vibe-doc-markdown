from .adaptable import AdaptableBackend
from .base import AbstractBackend
from .docling import DoclingBackend
from .markitdown import MarkItDownBackend
from .pandoc import PandocBackend
from .pdfplumber import PdfplumberBackend

BACKENDS = {
    "adaptable": AdaptableBackend,
    "docling": DoclingBackend,
    "markitdown": MarkItDownBackend,
    "pandoc": PandocBackend,
    "pdfplumber": PdfplumberBackend,
}


def _try_register(name: str, module: str, cls_name: str, pkg_check: str | None = None) -> None:
    try:
        if pkg_check:
            __import__(pkg_check)
        mod = __import__(module, fromlist=[cls_name])
        BACKENDS[name] = getattr(mod, cls_name)
    except ImportError:
        pass


_try_register("marker", "vibe_doc_markdown.backends.marker", "MarkerBackend", "marker")

__all__ = ["AbstractBackend", "BACKENDS"]
