from __future__ import annotations

from .backends import BACKENDS
from .types import Backend, ConvertInput, ConvertResult


def convert_document(
    input: ConvertInput,
    backend: Backend = Backend.ADAPTABLE,
) -> ConvertResult:
    backend_cls = BACKENDS.get(backend.value)
    if backend_cls is None:
        available = list(BACKENDS.keys())
        raise ValueError(
            f"Backend '{backend.value}' is not available. "
            f"Available backends: {available}"
        )
    instance = backend_cls()
    return instance.convert(input)
