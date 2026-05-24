from __future__ import annotations

from ..types import Backend, ConvertInput, ConvertResult
from .base import AbstractBackend


class PdfplumberBackend(AbstractBackend):
    @property
    def name(self) -> Backend:
        return Backend.PDFPLUMBER

    def convert(self, input: ConvertInput) -> ConvertResult:
        import pdfplumber

        path = input.resolve_local_path()
        md_lines: list[str] = []

        with pdfplumber.open(str(path)) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    md_lines.append(text)
                    md_lines.append("")

                tables = page.extract_tables()
                for table in tables:
                    if table and len(table) > 0:
                        header = table[0]
                        md_lines.append(
                            "| " + " | ".join([h or "" for h in header]) + " |"
                        )
                        md_lines.append(
                            "|" + "|".join(["---" for _ in header]) + "|"
                        )
                        for row in table[1:]:
                            md_lines.append(
                                "| " + " | ".join([c or "" for c in row]) + " |"
                            )
                        md_lines.append("")

        return ConvertResult(
            markdown="\n".join(md_lines),
            backend=self.name,
        )
