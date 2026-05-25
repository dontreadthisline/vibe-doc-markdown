"""Test all PDF to Markdown backends with a sample PDF file."""

from __future__ import annotations

from pathlib import Path

from vibe_doc_markdown import Backend, ConvertInput, convert_document
from vibe_doc_markdown.backends import BACKENDS

# Configuration
PDF_PATH = Path("/Users/didi/Downloads/end2endvad.pdf")
OUTPUT_DIR = Path(__file__).parent.parent / "outputs"

# All backends to test
BACKENDS_TO_TEST = [
    Backend.MARKITDOWN,
    Backend.PDFPLUMBER,
    Backend.DOCLING,
    Backend.MARKER,
    # Note: Pandoc cannot parse PDF files
]


def test_all_backends() -> None:
    """Test each available backend and save output to outputs directory."""
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"PDF not found: {PDF_PATH}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Clear existing outputs
    for f in OUTPUT_DIR.glob("*.md"):
        f.unlink()

    results: list[tuple[str, str, int]] = []  # (backend, status, size)

    for backend in BACKENDS_TO_TEST:
        backend_name = backend.value
        output_path = OUTPUT_DIR / f"{backend_name}.md"

        if backend_name not in BACKENDS:
            print(f"[SKIP] {backend_name}: not available")
            results.append((backend_name, "skipped", 0))
            continue

        try:
            print(f"[TEST] Converting with {backend_name}...")
            inp = ConvertInput.from_path(str(PDF_PATH))
            result = convert_document(inp, backend)

            # Save output
            output_path.write_text(result.markdown, encoding="utf-8")
            size = len(result.markdown)
            print(f"[OK] {backend_name}: {size} chars -> {output_path.name}")
            results.append((backend_name, "success", size))

        except Exception as e:
            print(f"[FAIL] {backend_name}: {e}")
            results.append((backend_name, f"error: {e}", 0))

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for name, status, size in results:
        print(f"  {name:12} | {status:20} | {size:8} chars")
    print("=" * 60)


if __name__ == "__main__":
    test_all_backends()
