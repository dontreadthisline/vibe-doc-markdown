## Context

vibe-doc-markdown 是一个 Python 库，提供统一接口将多种文档格式（PDF、DOCX 等）转换为 Markdown。当前已实现 5 个后端适配器：MarkItDown、Pandoc、pdfplumber、Docling、Marker。项目处于早期阶段，核心转换引擎已稳定，需要沉淀设计文档供后续维护参考。

**约束**：
- Python >= 3.12
- 后端是可选的（opt-in via import），不强制安装所有依赖
- 支持三种输入来源：本地路径、远程 URL、原始 bytes

## Goals / Non-Goals

**Goals:**
- 提供统一、类型安全的转换入口 `convert_document()`
- 后端可插拔，用户可按需安装依赖
- 输入来源透明：调用方无需关心文件来源，统一走 `ConvertInput` 抽象
- 后端实现最小化：每个 adapter 仅负责调用上游库，不做额外格式转换

**Non-Goals:**
- 不自行实现 PDF 解析或 OCR —— 全部委托给上游库
- 不做输出后处理或格式精修 —— 调用方自行处理
- 不支持流式转换
- 不做多页并行处理
- 不支持自定义管道编排

## Decisions

### 1. AbstractBackend 抽象基类 + ConvertInput 统一入口

**选型**：每个后端继承 `AbstractBackend`，实现 `convert(input: ConvertInput) -> ConvertResult`。

**为什么不用函数注册模式**：后端可能携带初始化逻辑（如 Docling 的 OCR 配置），类实例提供自然的作用域。

**为什么 ConvertInput 不支持子类化**：三种来源（path/url/bytes）已覆盖所有场景，子类化会增加不必要的复杂度。通过 `__init_subclass__` 显式禁止。

### 2. 后端懒加载 + 可选注册

**选型**：核心后端（markitdown/pandoc/pdfplumber/docling）在 `BACKENDS` 字典中直接注册，marker 后端通过 `_try_register()` 尝试导入。

**理由**：marker-pdf 依赖较重（GPU 推荐），安装失败率高，适合懒加载。核心后端依赖较轻或必须存在。

**代价**：`BACKENDS` 字典的状态依赖当前环境的已安装包，行为在不同环境下可能不同。

### 3. Pandoc 明确拒绝 PDF 输入

**选型**：检测文件后缀，对 `pdf/bin/odt` 抛出 `ValueError`。

**理由**：Pandoc 无法原生解析 PDF，试图转换会产生无意义输出。**快速失败优于静默错误**。

### 4. ConvertResult 携带 backend 标识

**选型**：`ConvertResult` 包含 `backend: Backend` 字段。

**理由**：调用方可能使用 `Backend.MARKITDOWN` 作为默认值但不显式指定，返回结果中携带实际使用的后端有利于审计和调试。

### 5. 数据模型使用 dataclass + Enum

**选型**：`Backend` 用 `str, Enum`（值可序列化），`ConvertResult` 用 `@dataclass`，`ConvertInput` 用经典类 + `__slots__`。

**理由**：`ConvertInput` 需要 `from_path/from_url/from_bytes` 多构造函数，dataclass 不适合这种模式。`__slots__` 减少内存开销。

## Risks / Trade-offs

| 风险 | 缓解 |
|------|------|
| 上游库 API 变更导致后端适配器失效 | 每个后端仅调用上游库的公开 API 的最小子集；测试覆盖所有后端的 convert 路径 |
| marker 后端在不同环境下注册状态不一致 | `_try_register` 吞掉 ImportError，`BACKENDS` 字典的 keys 是运行时真实状态 |
| `resolve_local_path` 将 URL/bytes 写入临时文件，未自动清理 | 临时文件由 OS 管理（`tempfile.NamedTemporaryFile`），接受短期磁盘占用 |
| Docling 首次运行下载模型（2.4GB），转换超时 | 首次调用文档中注明模型下载耗时 |
