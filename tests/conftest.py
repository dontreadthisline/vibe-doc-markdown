from __future__ import annotations

import pytest
from vibe_doc_markdown import Backend

PDF_PATH = "/home/zsl/Downloads/2603.25551_zh_CN.pdf"


@pytest.fixture(scope="session")
def sample_pdf_path() -> str:
    return PDF_PATH


@pytest.fixture(scope="session")
def sample_pdf_bytes() -> bytes:
    from pathlib import Path
    return Path(PDF_PATH).read_bytes()
