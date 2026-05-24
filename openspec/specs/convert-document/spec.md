## ADDED Requirements

### Requirement: ConvertInput supports three source types
The system SHALL accept document input via local file path, remote URL, or raw bytes through the `ConvertInput` class.

#### Scenario: Create from local file path
- **WHEN** user calls `ConvertInput.from_path("/tmp/report.pdf")`
- **THEN** `source_type` returns `"path"` and `filename` returns `"report.pdf"`

#### Scenario: Create from pathlib.Path
- **WHEN** user calls `ConvertInput.from_path(Path("/tmp/report.pdf"))`
- **THEN** `source_type` returns `"path"` and `filename` returns `"report.pdf"`

#### Scenario: Create from remote URL
- **WHEN** user calls `ConvertInput.from_url("https://example.com/doc.pdf")`
- **THEN** `source_type` returns `"url"` and `filename` returns `"doc.pdf"`

#### Scenario: Reject invalid URL
- **WHEN** user calls `ConvertInput.from_url("not-a-url")`
- **THEN** a `ValueError` is raised with message matching "Invalid URL"

#### Scenario: Create from raw bytes with custom filename
- **WHEN** user calls `ConvertInput.from_bytes(b"pdf content", filename="custom.pdf")`
- **THEN** `source_type` returns `"bytes"` and `filename` returns `"custom.pdf"`

#### Scenario: Create from raw bytes with default filename
- **WHEN** user calls `ConvertInput.from_bytes(b"data")`
- **THEN** `filename` returns `"document"`

#### Scenario: Cannot subclass ConvertInput
- **WHEN** user attempts to subclass `ConvertInput`
- **THEN** a `TypeError` is raised

### Requirement: ConvertInput resolves to local path
The system SHALL resolve any input source to a local file path via `resolve_local_path()`.

#### Scenario: Path source returns itself
- **WHEN** input was created with `from_path("/tmp/test.pdf")`
- **THEN** `resolve_local_path()` returns `Path("/tmp/test.pdf")`

#### Scenario: URL source downloads to temp file
- **WHEN** input was created with `from_url("https://example.com/doc.pdf")` and the URL is reachable
- **THEN** `resolve_local_path()` returns a `Path` pointing to a temporary file containing the downloaded content

#### Scenario: Bytes source writes to temp file
- **WHEN** input was created with `from_bytes(b"hello", filename="test.txt")`
- **THEN** `resolve_local_path()` returns a `Path` pointing to a temporary file containing `b"hello"`

### Requirement: ConvertInput resolves to raw bytes
The system SHALL resolve any input source to raw bytes via `resolve_bytes()`.

#### Scenario: Bytes source returns itself
- **WHEN** input was created with `from_bytes(b"hello")`
- **THEN** `resolve_bytes()` returns `b"hello"`

#### Scenario: Path source reads file content
- **WHEN** input was created with `from_path("/tmp/test.txt")` and the file contains "hello"
- **THEN** `resolve_bytes()` returns `b"hello"`

### Requirement: Backend enum defines all supported backends
The system SHALL define a `Backend` enum with members for each supported converter.

#### Scenario: All backend enum values
- **WHEN** accessing `Backend` enum members
- **THEN** `Backend.MARKITDOWN.value` equals `"markitdown"`
- **AND** `Backend.PANDOC.value` equals `"pandoc"`
- **AND** `Backend.PDFPLUMBER.value` equals `"pdfplumber"`
- **AND** `Backend.DOCLING.value` equals `"docling"`
- **AND** `Backend.MARKER.value` equals `"marker"`

### Requirement: ConvertResult carries markdown and metadata
The system SHALL return conversion results as a `ConvertResult` dataclass containing the markdown text, the backend used, and optional metadata.

#### Scenario: Successful conversion returns markdown
- **WHEN** `convert_document` completes successfully
- **THEN** the returned `ConvertResult` has a non-empty `markdown` string and a `backend` field matching the requested backend

### Requirement: convert_document dispatches to backend
The system SHALL dispatch `convert_document(input, backend)` to the corresponding backend implementation.

#### Scenario: Explicit backend selection
- **WHEN** user calls `convert_document(input, Backend.MARKITDOWN)`
- **THEN** the MarkItDown backend's `convert` method is invoked

#### Scenario: Default backend
- **WHEN** user calls `convert_document(input)` without specifying a backend
- **THEN** `Backend.MARKITDOWN` is used as the default

#### Scenario: Unavailable backend raises error
- **WHEN** user requests a backend whose dependency is not installed
- **THEN** a `ValueError` is raised with message containing "not available" and a list of available backends
