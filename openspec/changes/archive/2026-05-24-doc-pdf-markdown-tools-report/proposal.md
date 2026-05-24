## Why

vibe-doc-markdown 是一个多后端通用文档转 Markdown 的 Python 库，已实现核心转换引擎和 5 个后端适配器（MarkItDown、Pandoc、pdfplumber、Docling、Marker），并有完整测试覆盖。目前项目缺少正式的规格说明文档（spec），导致后端行为契约、输入输出约束、错误处理策略等关键设计决策散落在代码中，不利于后续维护和扩展。

## What Changes

- 为 vibe-doc-markdown 项目的现有实现沉淀规格文档
- 新增 convert-document 能力 spec：定义统一转换入口的行为契约（输入类型、输出结构、错误语义）
- 新增 multi-backend 能力 spec：定义后端注册/发现/适配机制、每个后端的格式支持矩阵和已知限制
- 生成 tasks.md：列出可验证的规格合规性检查项

## Capabilities

### New Capabilities

- `convert-document`: 统一文档转换入口，定义 ConvertInput（path/url/bytes 三种来源）、ConvertResult、Backend 枚举的行为契约
- `multi-backend`: 后端抽象接口（AbstractBackend）、注册与发现（BACKENDS dict + 懒加载）、各后端适配器的格式支持与限制

### Modified Capabilities

<!-- None - this is initial spec documentation for existing code -->

## Impact

- 代码：无需变更，本次仅沉淀 spec 文档
- 测试：`tests/test_converter.py` 中的测试用例可作为 spec 合规性验证的基础
- 依赖：无变更
