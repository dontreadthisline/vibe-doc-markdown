## ADDED Requirements

### Requirement: AbstractBackend defines the backend contract
The system SHALL define an `AbstractBackend` abstract base class that all backends must implement.

#### Scenario: Backend implements convert method
- **WHEN** a backend class inherits from `AbstractBackend`
- **THEN** it MUST implement `convert(input: ConvertInput) -> ConvertResult`

#### Scenario: Backend exposes name property
- **WHEN** a backend class inherits from `AbstractBackend`
- **THEN** it MUST expose a `name` property returning the corresponding `Backend` enum member

### Requirement: BACKENDS registry maps backend names to classes
The system SHALL maintain a `BACKENDS` dictionary mapping backend name strings to their implementation classes.

#### Scenario: Core backends always registered
- **WHEN** the package is imported
- **THEN** `BACKENDS` SHALL contain entries for `"markitdown"`, `"pandoc"`, `"pdfplumber"`, and `"docling"`

#### Scenario: Marker backend conditionally registered
- **WHEN** the `marker` package is installed
- **THEN** `BACKENDS` SHALL contain an entry for `"marker"`
- **WHEN** the `marker` package is not installed
- **THEN** `BACKENDS` SHALL NOT contain an entry for `"marker"`

### Requirement: MarkItDown backend converts documents via the markitdown library
The system SHALL support conversion via the `markitdown` library.

#### Scenario: Convert PDF from local path
- **WHEN** user converts a valid PDF file using `Backend.MARKITDOWN`
- **THEN** the result SHALL contain non-empty markdown text

#### Scenario: Convert from raw bytes
- **WHEN** user converts valid PDF bytes using `Backend.MARKITDOWN`
- **THEN** the result SHALL contain non-empty markdown text

### Requirement: Pandoc backend converts non-PDF documents
The system SHALL support conversion of DOCX and other structured formats via `pypandoc`, but SHALL reject PDF input.

#### Scenario: Reject PDF input
- **WHEN** user attempts to convert a `.pdf` file using `Backend.PANDOC`
- **THEN** a `ValueError` is raised with message matching "Pandoc cannot parse"

#### Scenario: Reject binary format input
- **WHEN** user attempts to convert a `.bin` or `.odt` file using `Backend.PANDOC`
- **THEN** a `ValueError` is raised with message matching "Pandoc cannot parse"

### Requirement: pdfplumber backend extracts text and tables
The system SHALL support PDF conversion via `pdfplumber`, extracting page text and tables into markdown format.

#### Scenario: Convert PDF from local path
- **WHEN** user converts a valid PDF file using `Backend.PDFPLUMBER`
- **THEN** the result SHALL contain non-empty markdown text

#### Scenario: Convert PDF from raw bytes
- **WHEN** user converts valid PDF bytes using `Backend.PDFPLUMBER`
- **THEN** the result SHALL contain non-empty markdown text

#### Scenario: Tables rendered as markdown pipe tables
- **WHEN** a PDF page contains a table with headers and rows
- **THEN** the output SHALL contain a markdown table with `|` delimiters and a `---|---|` separator line

### Requirement: Docling backend converts with layout analysis
The system SHALL support conversion via the `docling` library, which provides structural layout analysis and OCR capability.

#### Scenario: Convert PDF from local path
- **WHEN** user converts a valid PDF file using `Backend.DOCLING`
- **THEN** the result SHALL contain non-empty markdown text

#### Scenario: Convert PDF from raw bytes
- **WHEN** user converts valid PDF bytes using `Backend.DOCLING`
- **THEN** the result SHALL contain non-empty markdown text

#### Scenario: RapidOCR models used when available
- **WHEN** RapidOCR models exist in `~/.cache/rapidocr/models/`
- **THEN** the Docling backend SHALL configure RapidOcrOptions for OCR processing

### Requirement: Marker backend converts PDF with formula preservation
The system SHALL support conversion via the `marker` library when the `marker-pdf` package is installed.

#### Scenario: Convert PDF from local path
- **WHEN** user converts a valid PDF file using `Backend.MARKER` and marker is installed
- **THEN** the result SHALL contain non-empty markdown text

#### Scenario: Convert PDF from raw bytes
- **WHEN** user converts valid PDF bytes using `Backend.MARKER` and marker is installed
- **THEN** the result SHALL contain non-empty markdown text

### Requirement: All backends produce non-empty output for valid PDF
The system SHALL produce non-empty markdown output from every available backend when given a valid PDF input.

#### Scenario: All backends produce output
- **WHEN** a valid PDF file is converted using each available backend in turn
- **THEN** every backend SHALL return a `ConvertResult` with `len(result.markdown) > 0`
