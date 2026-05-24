## 1. Spec compliance: convert-document

- [ ] 1.1 Verify ConvertInput.from_path accepts str and Path, sets correct source_type and filename
- [ ] 1.2 Verify ConvertInput.from_url accepts valid URL, rejects invalid URL with ValueError
- [ ] 1.3 Verify ConvertInput.from_bytes with and without explicit filename
- [ ] 1.4 Verify ConvertInput cannot be subclassed (TypeError)
- [ ] 1.5 Verify resolve_local_path works for path/url/bytes sources
- [ ] 1.6 Verify resolve_bytes works for path/bytes sources
- [ ] 1.7 Verify Backend enum contains all 5 members with correct string values
- [ ] 1.8 Verify ConvertResult dataclass has markdown, backend, metadata fields
- [ ] 1.9 Verify convert_document dispatches to correct backend
- [ ] 1.10 Verify convert_document defaults to Backend.MARKITDOWN when no backend specified
- [ ] 1.11 Verify convert_document raises ValueError with "not available" for unavailable backend

## 2. Spec compliance: multi-backend

- [ ] 2.1 Verify AbstractBackend enforces convert() and name property via ABC
- [ ] 2.2 Verify BACKENDS dict contains markitdown/pandoc/pdfplumber/docling on import
- [ ] 2.3 Verify marker backend registered when marker-pdf package is installed
- [ ] 2.4 Verify MarkItDown backend produces non-empty markdown for valid PDF
- [ ] 2.5 Verify Pandoc backend rejects .pdf/.bin/.odt inputs with ValueError
- [ ] 2.6 Verify pdfplumber backend extracts text and renders tables as markdown pipe tables
- [ ] 2.7 Verify Docling backend produces non-empty markdown for valid PDF
- [ ] 2.8 Verify Marker backend produces non-empty markdown for valid PDF (when installed)
- [ ] 2.9 Verify all available backends produce non-empty output for the same valid PDF

## 3. Run existing tests

- [ ] 3.1 Run `pytest tests/ -v` and verify all tests pass
- [ ] 3.2 Run `pytest tests/ -v -m "slow"` and verify slow tests pass with sample PDF
