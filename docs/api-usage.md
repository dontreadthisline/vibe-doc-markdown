# vibe-doc-markdown API 使用文档

## 概述

`vibe-doc-markdown` 是一个多后端文档转 Markdown 转换库，支持 PDF、Word、PPT 等多种文档格式。提供统一的 API 接口，可根据需求选择不同的转换后端。

## 安装

本项目未发布到 PyPI，需从 Git 仓库安装。

### 从 Git 仓库安装

**使用 uv：**

```bash
# 安装最新版本
uv add git+ssh://git@git.xiaojukeji.com/maps-global/doc-markdown.git


**在 pyproject.toml 中添加：**

```toml
[project]
dependencies = [
  "vibe-doc-markdown @ git+ssh://git@git.xiaojukeji.com/maps-global/doc-markdown.git@main",
]
```

### SSH 密钥配置

确保已配置 SSH 密钥可访问 Git 仓库：

```bash
ssh -T git@git.xiaojukeji.com
```

## 环境配置

### 安装 uv

**国内服务器安装（使用 GitHub 代理）：**

```bash
curl -LsSf https://gh-proxy.com/https://github.com/astral-sh/uv/releases/download/0.11.16/uv-x86_64-unknown-linux-gnu.tar.gz -o /tmp/uv.tar.gz
mkdir -p ~/.local/bin && tar -xzf /tmp/uv.tar.gz -C /tmp/ && cp /tmp/uv-x86_64-unknown-linux-gnu/{uv,uvx} ~/.local/bin/
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc
```

### 国内服务器依赖安装

```bash
cd doc-markdown

# 安装 Python（使用 gh-proxy 加速）
uv python install 3.12 --mirror "https://gh-proxy.com/https://github.com/astral-sh/python-build-standalone/releases/download"

# 同步依赖（使用清华 PyPI 镜像）
UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple uv sync
```

### 模型缓存

- `docling`: 模型缓存于 `~/.cache/huggingface/hub/`（约 500MB）
- `markitdown`: 无额外模型下载

## API 接口

### 核心函数

```python
def convert_document(
    input: ConvertInput,
    backend: Backend = Backend.ADAPTABLE,
) -> ConvertResult:
    """将文档转换为 Markdown 格式。"""
```

### 类型定义

#### Backend（后端枚举）

```python
class Backend(str, Enum):
    ADAPTABLE = "adaptable"    # 自动选择最佳后端（默认）
    MARKITDOWN = "markitdown"  # 通用文档转换，速度快
    PANDOC = "pandoc"          # 通用文档转换，不支持 PDF 解析
    PDFPLUMBER = "pdfplumber"  # PDF 专用，轻量级
    DOCLING = "docling"        # PDF 专用，高质量，需下载模型
    MARKER = "marker"          # PDF 专用，深度学习，需下载大型模型
```

#### ConvertInput（输入封装）

```python
class ConvertInput:
    @classmethod
    def from_path(cls, path: str | Path) -> ConvertInput:
        """从本地文件路径创建输入。"""

    @classmethod
    def from_url(cls, url: str) -> ConvertInput:
        """从远程 URL 创建输入（自动下载）。"""

    @classmethod
    def from_bytes(cls, data: bytes, filename: str = "document") -> ConvertInput:
        """从原始字节创建输入。"""

    @property
    def source_type(self) -> str:
        """返回输入类型: 'path' | 'url' | 'bytes'。"""

    @property
    def filename(self) -> str:
        """返回文件名。"""
```

#### ConvertResult（输出结果）

```python
@dataclass
class ConvertResult:
    markdown: str              # 转换后的 Markdown 文本
    backend: Backend           # 使用的后端
    metadata: dict[str, Any]   # 元数据（可选）
```

## 使用示例

### 基础用法（推荐）

```python
from vibe_doc_markdown import convert_document, ConvertInput

# 从本地文件转换，自动选择最佳后端
# PDF -> docling, DOCX -> markitdown
input_obj = ConvertInput.from_path("/path/to/document.pdf")
result = convert_document(input_obj)
print(result.markdown)
print(f"Used backend: {result.backend.value}")
```

### 手动指定后端

```python
from vibe_doc_markdown import convert_document, Backend, ConvertInput

input_obj = ConvertInput.from_path("/path/to/document.pdf")

# 使用 pdfplumber（轻量级，适合简单 PDF）
result = convert_document(input_obj, Backend.PDFPLUMBER)

# 使用 docling（高质量，需下载模型）
result = convert_document(input_obj, Backend.DOCLING)

# 使用 marker（深度学习，需下载大型模型）
result = convert_document(input_obj, Backend.MARKER)

# 默认使用 adaptable（自动选择最佳后端）
result = convert_document(input_obj)  # 等同于 Backend.ADAPTABLE
```

### 从 URL 转换

```python
from vibe_doc_markdown import convert_document, Backend, ConvertInput

input_obj = ConvertInput.from_url("https://example.com/document.pdf")
result = convert_document(input_obj, Backend.MARKITDOWN)
print(result.markdown)
```

### 从内存字节转换

```python
from vibe_doc_markdown import convert_document, Backend, ConvertInput

with open("/path/to/document.pdf", "rb") as f:
    data = f.read()

input_obj = ConvertInput.from_bytes(data, filename="document.pdf")
result = convert_document(input_obj, Backend.PDFPLUMBER)
print(result.markdown)
```

### 检测可用后端

```python
from vibe_doc_markdown.backends import BACKENDS

print("Available backends:", list(BACKENDS.keys()))
# 输出: ['adaptable', 'docling', 'markitdown', 'pandoc', 'pdfplumber', 'marker']
```

### 批量转换示例

```python
from pathlib import Path
from vibe_doc_markdown import convert_document, Backend, ConvertInput

def convert_directory(input_dir: Path, output_dir: Path, backend: Backend) -> None:
    """批量转换目录下的所有 PDF 文件。"""
    output_dir.mkdir(parents=True, exist_ok=True)

    for pdf_file in input_dir.glob("*.pdf"):
        input_obj = ConvertInput.from_path(pdf_file)
        result = convert_document(input_obj, backend)

        output_file = output_dir / f"{pdf_file.stem}.md"
        output_file.write_text(result.markdown, encoding="utf-8")
        print(f"Converted: {pdf_file.name} -> {output_file.name}")

# 使用示例
convert_directory(
    input_dir=Path("./documents"),
    output_dir=Path("./markdown"),
    backend=Backend.MARKITDOWN
)
```

## 后端选择指南

| 后端 | 适用场景 | 优点 | 缺点 |
|------|----------|------|------|
| **adaptable** | **通用（推荐）** | **自动选择最佳后端** | - |
| markitdown | DOCX/DOC | 速度快、无额外依赖 | PDF 效果一般 |
| pdfplumber | 简单 PDF | 轻量、快速 | 复杂排版支持差 |
| docling | 高质量 PDF | 格式保留好 | 需下载模型 (~500MB) |
| marker | 复杂 PDF | 深度学习、效果最佳 | 模型大 (~2GB)、速度慢 |
| pandoc | 非 PDF 文档 | 格式支持广 | 不支持 PDF 解析 |

### Adaptable 后端自动选择规则

| 文件类型 | 自动选择的后端 |
|----------|----------------|
| `.pdf` | docling |
| `.docx` | markitdown |
| `.doc` | markitdown |

## 异常处理

```python
from vibe_doc_markdown import convert_document, Backend, ConvertInput
from vibe_doc_markdown.backends import BACKENDS

input_obj = ConvertInput.from_path("/path/to/document.pdf")

# 检查后端是否可用
if Backend.DOCLING.value not in BACKENDS:
    print("docling backend not available, falling back to markitdown")
    result = convert_document(input_obj, Backend.MARKITDOWN)
else:
    result = convert_document(input_obj, Backend.DOCLING)

# 处理文件不存在
try:
    input_obj = ConvertInput.from_path("/nonexistent/file.pdf")
    result = convert_document(input_obj, Backend.MARKITDOWN)
except FileNotFoundError as e:
    print(f"File not found: {e}")
```

## 完整示例：带代理配置

```python
import os

# 在导入模块前设置代理（如需要）
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

from vibe_doc_markdown import convert_document, Backend, ConvertInput

def main():
    input_obj = ConvertInput.from_path("./example.pdf")

    # 尝试使用高质量后端，失败则回退
    try:
        result = convert_document(input_obj, Backend.DOCLING)
    except Exception as e:
        print(f"docling failed: {e}, using markitdown")
        result = convert_document(input_obj, Backend.MARKITDOWN)

    print(result.markdown)

if __name__ == "__main__":
    main()
```
