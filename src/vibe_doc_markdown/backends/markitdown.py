from __future__ import annotations

import re
import tempfile
import zipfile
from io import BytesIO
from pathlib import Path

from ..types import Backend, ConvertInput, ConvertResult
from .base import AbstractBackend


def _fix_docx_styles(docx_path: Path) -> Path:
    """Fix non-compliant docx files missing w:type attribute in styles.

    Some apps (e.g. Shimo Docs) export docx without the required w:type
    attribute on w:style elements. This function patches the styles.xml
    to add a default w:type="paragraph" where missing.
    """
    with zipfile.ZipFile(docx_path, "r") as zin:
        if "word/styles.xml" not in zin.namelist():
            return docx_path

        styles_content = zin.read("word/styles.xml").decode("utf-8")

        if 'w:type=' in styles_content:
            return docx_path

        fixed_content = re.sub(
            r'<w:style\s+w:styleId="',
            '<w:style w:type="paragraph" w:styleId="',
            styles_content,
        )

        if fixed_content == styles_content:
            return docx_path

        files = {name: zin.read(name) for name in zin.namelist()}

    output = BytesIO()
    with zipfile.ZipFile(output, "w") as zout:
        for name, content in files.items():
            if name == "word/styles.xml":
                zout.writestr(name, fixed_content.encode("utf-8"))
            else:
                zout.writestr(name, content)

    tmp = tempfile.NamedTemporaryFile(suffix=".docx", delete=False)
    tmp.write(output.getvalue())
    tmp.close()
    return Path(tmp.name)


class MarkItDownBackend(AbstractBackend):
    @property
    def name(self) -> Backend:
        return Backend.MARKITDOWN

    def convert(self, input: ConvertInput) -> ConvertResult:
        from markitdown import MarkItDown

        md = MarkItDown()
        path = input.resolve_local_path()

        if path.suffix.lower() == ".docx":
            path = _fix_docx_styles(path)

        result = md.convert(str(path))

        return ConvertResult(
            markdown=result.text_content,
            backend=self.name,
        )
