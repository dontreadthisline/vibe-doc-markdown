# 开源 Doc/PDF → Markdown 工具：安装到使用完整报告

> 调研日期：2026-05-22 | 覆盖工具：MarkItDown、Docling、Marker、MinerU、Pandoc、pdfplumber

---

## 目录

1. [MarkItDown（微软）](#1-markitdown微软)
2. [Docling（IBM）](#2-doclingibm)
3. [Marker（Datalab）](#3-markerdatalab)
4. [MinerU（上海AI实验室）](#4-minerushanghai-ai-实验室)
5. [Pandoc](#5-pandoc)
6. [pdfplumber](#6-pdfplumber)
7. [工具对比总结](#7-工具对比总结)

---

## 1. MarkItDown（微软）

**定位**：多格式、零模型依赖、开箱即用

### 安装

```bash
# 基础安装（仅 PDF/DOCX/PPTX/XLSX）
pip install markitdown

# 完整安装（含音频转录、YouTube 字幕等全部功能）
pip install 'markitdown[all]'
```

### 使用示例

```python
from markitdown import MarkItDown

md = MarkItDown()

# 转换 PDF
result = md.convert("document.pdf")
print(result.text_content)

# 转换 DOCX
result = md.convert("report.docx")
with open("report.md", "w") as f:
    f.write(result.text_content)

# 转换 PPTX
result = md.convert("slides.pptx")
print(result.text_content)

# 转换 Excel
result = md.convert("data.xlsx")
print(result.text_content)

# 转换 HTML
result = md.convert("page.html")
print(result.text_content)
```

### 命令行方式

```bash
# 单文件转换
python -m markitdown document.pdf -o output.md

# 批量转换
for f in *.pdf; do
    python -m markitdown "$f" -o "${f%.pdf}.md"
done
```

### 适用场景

纯数字 PDF、Office 文档（DOCX/PPTX/XLSX）的快速批量转换。扫描件请勿使用。

---

## 2. Docling（IBM）

**定位**：表格/结构精度最高，企业 RAG 首选

### 安装

```bash
pip install docling

# 如需 OCR 支持
pip install docling[ocr]
```

首次运行时自动下载模型（约 2.4GB），存放于 `~/.cache/docling/`。

### 使用示例

```python
from docling.document_converter import DocumentConverter

converter = DocumentConverter()

# 转换 PDF（自动识别扫描件并启用 OCR）
result = converter.convert("document.pdf")
markdown_text = result.document.export_to_markdown()

with open("output.md", "w") as f:
    f.write(markdown_text)

# 转换 DOCX
result = converter.convert("report.docx")
print(result.document.export_to_markdown())

# 导出为 JSON（保留结构化中间表示）
json_output = result.document.export_to_dict()

# 使用 VLM 增强（理解图表、生成图片描述）
from docling.datamodel.pipeline_options import PdfPipelineOptions

pipeline_options = PdfPipelineOptions()
pipeline_options.generate_picture_images = True  # 生成图表描述
pipeline_options.do_ocr = True                   # 启用 OCR

converter = DocumentConverter(
    pipeline_options=pipeline_options
)
result = converter.convert("scanned_doc.pdf")
print(result.document.export_to_markdown())
```

### 批量处理

```python
from pathlib import Path
from docling.document_converter import DocumentConverter

converter = DocumentConverter()
pdf_dir = Path("./pdfs")

for pdf_file in pdf_dir.glob("*.pdf"):
    result = converter.convert(pdf_file)
    md_path = pdf_file.with_suffix(".md")
    md_path.write_text(result.document.export_to_markdown())
    print(f"Done: {pdf_file.name} -> {md_path.name}")
```

### 适用场景

复杂 PDF、含表格/公式的文档、扫描件、需要结构化 JSON 输出的 RAG 系统。

---

## 3. Marker（Datalab）

**定位**：速度最快（0.86s/页），公式处理最佳

### 安装

```bash
pip install marker-pdf[all]

# 如果只用 CPU
pip install marker-pdf

# GPU 加速（CUDA）
pip install marker-pdf[all-cuda]
```

首次运行自动下载模型（layout 60MB + OCR 110MB），存放于 `~/.cache/marker/`。

### 使用示例

```python
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

# 创建模型字典
artifact_dict = create_model_dict()

# 创建转换器
converter = PdfConverter(artifact_dict=artifact_dict)

# 转换单个 PDF
rendered = converter("paper.pdf")

# 提取 markdown 文本和图片
markdown_text, metadata, images = text_from_rendered(rendered)

with open("paper.md", "w") as f:
    f.write(markdown_text)

# 保存提取的图片
for img_name, img_data in images.items():
    with open(f"images/{img_name}", "wb") as f:
        f.write(img_data)
```

### 命令行方式

```bash
# 单文件转换
marker single paper.pdf output_dir/

# 批量转换
marker batch ./pdfs/ ./output/ --workers 4

# 指定 GPU
marker single paper.pdf output/ --use_cuda

# 输出 JSON + Markdown
marker single paper.pdf output/ --output_format json,markdown
```

### 配置选项

```python
from marker.config.parser import ConfigParser

config = {
    "use_llm": False,           # 关闭 LLM 增强
    "force_ocr": False,         # 是否强制 OCR（扫描件设 True）
    "output_format": "markdown",
    "extract_images": True,     # 提取图片
}

converter = PdfConverter(
    artifact_dict=create_model_dict(),
    config=ConfigParser(config),
)
```

### 适用场景

学术论文批量处理、LaTeX 公式密集文档、需要 GPU 加速的高速流水线。

---

## 4. MinerU（上海AI 实验室）

**定位**：中文最强，VLM+OCR 双引擎

### 安装

```bash
# 方式一：pip 安装
pip install magic-pdf
pip install magic-pdf[all]  # 含 PaddleOCR

# 方式二：Docker（推荐，避免环境冲突）
docker pull opendatalab/mineru:latest
docker run -v /path/to/pdfs:/data opendatalab/mineru:latest
```

### 使用示例

```python
from magic_pdf.pipe.UNIPipe import UNIPipe
from magic_pdf.pipe.OCRPipe import OCRPipe
from magic_pdf.rw.DiskReaderWriter import DiskReaderWriter

# 纯数字 PDF（非扫描件）
pdf_path = "chinese_report.pdf"
output_dir = "./output/"

pipe = UNIPipe(
    pdf_bytes=open(pdf_path, "rb").read(),
    jso_useful_key={},
    image_writer=DiskReaderWriter(output_dir),
    is_debug=False,
    start_page=0,
    end_page=0,  # 0 表示全部页面
)
pipe.pipe_classify()
pipe.pipe_parse()
content_list = pipe.pipe_mk_uni_format("./output/images", drop_mode="none")
md_content = pipe.pipe_mk_markdown("./output/images", drop_mode="none")

# 保存结果
with open(f"{output_dir}/output.md", "w") as f:
    f.write(md_content)

# 扫描件 PDF（需要 OCR）
pipe = OCRPipe(
    pdf_bytes=open("scanned_doc.pdf", "rb").read(),
    image_writer=DiskReaderWriter(output_dir),
    is_debug=False,
)
pipe.pipe_classify()
pipe.pipe_parse()
pipe.pipe_mk_uni_format("./output/images")
md_content = pipe.pipe_mk_markdown("./output/images")

with open(f"{output_dir}/output.md", "w") as f:
    f.write(md_content)
```

### 命令行方式

```bash
# 快速转换
magic-pdf -p chinese_doc.pdf -o ./output/

# 指定 OCR 引擎
magic-pdf -p scanned.pdf -o ./output/ --method ocr

# 指定页面范围
magic-pdf -p book.pdf -o ./output/ --start-page 10 --end-page 50
```

### 适用场景

中文 PDF、中英混排文档、公章合同、古籍扫描件、竖排文字、跨页表格合并。

---

## 5. Pandoc

**定位**：格式互转瑞士军刀，非 PDF 解析器

### 安装

```bash
# Arch Linux
sudo pacman -S pandoc

# Ubuntu/Debian
sudo apt install pandoc

# macOS
brew install pandoc

# Windows
winget install --id JohnMacFarlane.Pandoc

# 安装 PDF 支持引擎（TeX Live）
sudo pacman -S texlive-core
```

### 使用示例

```bash
# DOCX → Markdown
pandoc report.docx -t markdown -o report.md

# DOCX → GitHub Flavored Markdown
pandoc report.docx -t gfm -o report.md

# DOCX → Markdown（包含图片）
pandoc report.docx -t markdown --extract-media=./images -o report.md

# LaTeX → Markdown
pandoc paper.tex -t markdown -o paper.md

# HTML → Markdown
pandoc page.html -t markdown -o page.md

# EPUB → Markdown
pandoc book.epub -t markdown -o book.md

# 自定义模板
pandoc input.docx -t markdown --template=custom.tpl -o output.md

# 使用 Lua 过滤器
pandoc input.docx --lua-filter=remove-header.lua -t markdown -o output.md
```

### Python 调用

```python
import subprocess

def pandoc_convert(input_path, output_path, fmt="gfm"):
    cmd = [
        "pandoc", input_path,
        "-t", fmt,
        "-o", output_path,
        "--extract-media=./images"
    ]
    subprocess.run(cmd, check=True)

pandoc_convert("report.docx", "report.md")
```

### 多步流水线（PDF 场景）

```bash
# PDF 不能直接进 Pandoc，需要先转中间格式

# 方案一：pdf2htmlEX → Pandoc
pdf2htmlEX document.pdf -o document.html
pandoc document.html -t markdown -o document.md

# 方案二：先用 Docling/Marker 解析 PDF，再用 Pandoc 做格式精修
# docling 导出 JSON → Pandoc 转 MD
```

### 适用场景

**不直接处理 PDF**。适合 DOCX/LaTeX/HTML/EPUB 等结构化格式转 Markdown。

---

## 6. pdfplumber

**定位**：传统坐标提取，轻量级 PDF 表格神器

### 安装

```bash
pip install pdfplumber
```

### 使用示例

```python
import pdfplumber

# 提取全部文本
with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)

# 提取表格（基于坐标线检测）
with pdfplumber.open("report.pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        tables = page.extract_tables()
        for j, table in enumerate(tables):
            print(f"--- Page {i+1}, Table {j+1} ---")
            for row in table:
                print(" | ".join([cell or "" for cell in row]))

# 转换为 Markdown
def pdf_to_markdown(pdf_path, output_path):
    md_lines = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # 提取文本
            text = page.extract_text()
            if text:
                md_lines.append(text)
                md_lines.append("")

            # 提取表格并转换
            tables = page.extract_tables()
            for table in tables:
                if table and len(table) > 0:
                    # 表头
                    header = table[0]
                    md_lines.append("| " + " | ".join([h or "" for h in header]) + " |")
                    md_lines.append("|" + "|".join(["---" for _ in header]) + "|")
                    # 数据行
                    for row in table[1:]:
                        md_lines.append("| " + " | ".join([c or "" for c in row]) + " |")
                    md_lines.append("")

    with open(output_path, "w") as f:
        f.write("\n".join(md_lines))

pdf_to_markdown("report.pdf", "report.md")
```

### 适用场景

数字原生 PDF 的表格提取、需要精细化坐标控制的场景、极轻量级（内存占用 < 50MB）。

---

## 7. 工具对比总结

### 性能对比

| 指标 | MarkItDown | Docling | Marker | MinerU | Pandoc |
|------|:---------:|:-------:|:------:|:------:|:------:|
| 安装体积 | 80MB | 2.4GB | 1.5GB | 2GB+ | 50MB |
| 速度（秒/页） | 0.04 | 4.1 | 0.86 | ~2.0 | N/A |
| GPU 需求 | 不需要 | 可选 | 推荐 | 可选 | 不需要 |
| CPU 可用 | ✅ | ✅ | ⚠️慢 | ✅ | ✅ |

### 能力对比

| 能力 | MarkItDown | Docling | Marker | MinerU | Pandoc |
|------|:---------:|:-------:|:------:|:------:|:------:|
| PDF 标题层级 | ❌ | ⚠️扁平化 | ❌ | ✅ | ❌ |
| 表格保留 | ❌ | ✅ 0.94 | ✅ 0.76 | ✅ | N/A |
| 扫描件 OCR | ❌ | ✅ | ✅ | ✅ | ❌ |
| LaTeX 公式 | ❌ | ⚠️图片 | ✅ 原生 | ✅ | ✅ |
| 中文支持 | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | N/A |
| DOCX 支持 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| 图表理解 | ❌ | ✅ | ❌ | ⭐⭐⭐ | ❌ |

### 选型速查

```
你的需求                            → 推荐工具
─────────────────────────────────────────────────
快速转 Office 文档                   → MarkItDown / Pandoc
复杂 PDF 含表格                      → Docling
学术论文 + LaTeX 公式                → Marker
中文文档 / 公章 / 古籍               → MinerU
RAG 管道 / 向量检索                  → Unstructured
极轻量表格提取                       → pdfplumber
```

---

## 附录：组合使用建议

```python
# 生产环境推荐的分层转换函数
from pathlib import Path

def convert_document(filepath: str) -> str:
    """智能选择转换引擎"""
    ext = Path(filepath).suffix.lower()

    if ext in (".docx", ".pptx", ".xlsx", ".html", ".epub"):
        # Office 文档：优先 Pandoc
        from markitdown import MarkItDown
        md = MarkItDown()
        return md.convert(filepath).text_content

    elif ext == ".pdf":
        # PDF：先用 MarkItDown 快速尝试
        from markitdown import MarkItDown
        md = MarkItDown()
        result = md.convert(filepath).text_content

        # 如果输出质量差（无标题、无表格），fallback 到 Docling
        if len(result) < 100 or "|" not in result:
            from docling.document_converter import DocumentConverter
            converter = DocumentConverter()
            doc = converter.convert(filepath)
            result = doc.document.export_to_markdown()

        return result

    else:
        raise ValueError(f"Unsupported format: {ext}")

# 使用
md_content = convert_document("report.pdf")
```
