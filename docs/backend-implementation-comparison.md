# 五个核心后端实现方案对比

> 分析 MarkItDown、Docling、Marker、Pandoc、pdfplumber 将 DOC/PDF 转为 Markdown 的技术路线差异。

---

## 总览

| 维度 | MarkItDown | Docling | Marker | Pandoc | pdfplumber |
|------|:---------:|:-------:|:------:|:------:|:----------:|
| 开发者 | 微软 | IBM | Datalab | John MacFarlane | jsvine |
| 语言 | Python | Python/C++ | Python | Haskell | Python |
| 方案类型 | 纯文档剖析 | ML 模型+OCR | ML 模型+OCR | 纯文档剖析 | 纯文档剖析 |
| AI/ML 依赖 | 无 | 布局+表格+OCR+VLM | 布局+检测+OCR+公式 | 无 | 无 |
| 安装体积 | ~80MB | ~2.4GB | ~1.5GB | ~50MB | ~10MB |
| 模型体积 | 0 | ~537MB | ~3.3GB | 0 | 0 |
| PDF 表格 | 不保留 | 精准(0.94) | 良好(0.76) | 不支持PDF | 坐标提取 |
| 扫描件 OCR | 不支持 | 支持 | 支持 | 不支持 | 不支持 |
| 公式还原 | 不支持 | 图片OCR | 原生LaTeX | 不支持PDF | 不支持 |
| DOCX 支持 | 好 | 优秀 | 不支持 | 优秀 | 不支持 |
| GPU 推理 | N/A | PyTorch CUDA | PyTorch CUDA | N/A | N/A |

---

## 1. MarkItDown — 薄封装层，零模型

### 技术路线：纯文档剖析

MarkItDown **本身不实现任何解析逻辑**，它是对现有成熟库的薄封装：

```
MarkItDown.convert()
    ├── PDF  → pdfminer.six 提取文本
    ├── DOCX → mammoth 提取文本
    ├── PPTX → python-pptx 提取文本
    ├── XLSX → pandas 读取表格
    └── HTML → beautifulsoup4 提取文本
```

- **pdfminer.six** 是纯 Python 的 PDF 文本提取库，按字符坐标逐字提取，不做布局分析
- **mammoth** 将 DOCX 内部 XML 结构转换为 HTML，再由 MarkItDown 转为 MD
- **不涉及任何神经网络、OCR、视觉模型**

### 转换流程

```
PDF 字节流 → pdfminer 按坐标提取字符 → 拼接为纯文本 → 输出 Markdown
                                        ↑ 表格/标题结构在此丢失
```

### 优缺点

- **优点**：极快（0.04s/页），零 GPU，零模型下载，部署最简单
- **缺点**：PDF 表格变成乱序段落、无标题层级、双栏文档文字交错、扫描件输出为空

### 依赖清单

| 依赖 | 用途 |
|------|------|
| `pdfminer.six` | PDF 文本提取 |
| `mammoth` | DOCX → HTML 转换 |
| `python-pptx` | PPTX 文本提取 |
| `pandas` | XLSX 表格读取 |
| `beautifulsoup4` | HTML 解析 |
| `magika` | 文件类型检测 |

---

## 2. Docling — 多层视觉理解管线

### 技术路线：ML 模型 + OCR

Docling 内部有 4 层处理管线，**部分模型走 GPU，OCR 走 CPU**：

```
Docling.convert()
    │
    ├── 第 1 层：格式路由
    │   根据文件类型选择解析器（PDF→视觉管线, DOCX→XML 解析, PPTX→python-pptx）
    │
    ├── 第 2 层：布局分析（Heron 模型, GPU 推理）
    │   PyTorch 模型扫描页面，识别标题/正文/页眉/页脚/表格/图片区域
    │
    ├── 第 3 层：OCR 引擎（自动检测是否需要, CPU 推理）
    │   数字原生 PDF → 直接提取文字
    │   扫描件 PDF   → RapidOCR（ONNX Runtime，CPU only）
    │
    ├── 第 4 层：VLM 增强（可选, GraniteDocling 258M 参数）
    │   图表理解：柱状图/饼图 → 表格数据 + 文字描述
    │
    └── 输出：DoclingDocument 统一中间表示 → export_to_markdown()
```

### 关键模型

| 模型 | 用途 | 大小 | 推理引擎 | GPU |
|------|------|------|---------|:--:|
| Heron | 页面布局分割 | ~164MB | PyTorch | ✅ CUDA |
| TableFormer | 表格结构识别 | ~342MB | PyTorch | ✅ CUDA |
| RapidOCR | 扫描件文字检测+识别 | ~31MB | ONNX Runtime | ❌ CPU |
| GraniteDocling VLM | 图表理解（可选） | 258M params | PyTorch | ✅ CUDA |

### 模型缓存位置

```
~/.cache/huggingface/hub/
├── models--docling-project--docling-layout-heron/   164MB
└── models--docling-project--docling-models/         342MB

~/.cache/rapidocr/models/                             31MB   (已从 venv 迁移)
```

### 优缺点

- **优点**：表格还原度 0.94（业界最高），扫描件 OCR，图表理解，支持 Apple Silicon MLX 加速
- **缺点**：慢（CPU 4.1s/页），安装体积大（2.4GB），RapidOCR 拖 GPU 后腿

### 依赖清单

| 依赖 | 用途 |
|------|------|
| `torch` + `torchvision` | 深度学习框架，GPU 推理 |
| `transformers` | HuggingFace 模型加载 |
| `onnxruntime` | RapidOCR ONNX 推理引擎 |
| `rapidocr` | OCR 文字检测与识别 |
| `opencv-python` | 图像预处理 |
| `scikit-learn` | 机器学习辅助 |
| `huggingface-hub` | 模型下载与管理 |
| `pydantic` | 配置与数据模型 |
| `docling-core` / `docling-ibm-models` / `docling-parse` | Docling 内部模块 |

---

## 3. Marker — 全 GPU 管线，公式之王

### 技术路线：ML 模型 + OCR（全 PyTorch）

Marker 采用 4 步流水线，**所有模型均走 PyTorch CUDA**，是唯一全 GPU 推理的方案：

```
Marker.convert()
    │
    ├── 第 1 步：文本抽取（pypdfium2）
    │   从 PDF 提取原始文字和坐标
    │
    ├── 第 2 步：布局分析（Surya Layout, GPU）
    │   检测页面区域：标题、正文、图片、表格、公式
    │
    ├── 第 3 步：文字检测与识别（Surya OCR, GPU）
    │   DetectionPredictor：定位文字框 → RecognitionPredictor：识别文字
    │   OCRErrorPredictor：修正 OCR 错字
    │
    ├── 第 4 步：后处理
    │   表格识别（TableRecPredictor, GPU）
    │   公式渲染（Texify, GPU）：行内/行间公式 → 原生 LaTeX
    │   阅读顺序重组、标题层级推断
    │
    └── 输出：Markdown + 提取的图片文件
```

### 关键模型

| 模型 | 用途 | 推理引擎 | GPU |
|------|------|---------|:--:|
| Surya Layout | 页面布局检测 | PyTorch | ✅ CUDA |
| Surya Detection | 文字框定位 | PyTorch | ✅ CUDA |
| Surya Recognition | 文字内容识别 | PyTorch | ✅ CUDA |
| Surya TableRec | 表格结构识别 | PyTorch | ✅ CUDA |
| Texify | LaTeX 公式识别 | PyTorch | ✅ CUDA |
| OCRErrorDetection | OCR 错字修正 | PyTorch | ✅ CUDA |

### 模型缓存位置

```
~/.cache/datalab/models/
├── layout/              布局检测模型
├── text_detection/      文字检测模型     (~73MB)
├── text_recognition/    文字识别模型
├── table_recognition/   表格识别模型
└── ocr_error_detection/ OCR 纠错模型     (~258MB)
```

### 优缺点

- **优点**：公式原生 LaTeX 保留（`$\hat{y} = \mathbf{W}x + b$`），全 GPU 推理，速度 0.86s/页，图片提取+标注
- **缺点**：模型体积大（3.3GB），需要 GPU 才能发挥性能，DOCX 不支持

### 依赖清单

| 依赖 | 用途 |
|------|------|
| `torch` + `torchvision` | 深度学习框架，GPU 推理 |
| `transformers` | HuggingFace 模型加载 |
| `surya-ocr` | 文字检测/识别/纠错模型 |
| `pypdfium2` | PDF 读取与渲染 |
| `opencv-python-headless` | 图像预处理 |
| `pillow` | 图像处理 |
| `huggingface-hub` | 模型下载与管理 |
| `pydantic` | 配置模型 |
| `scikit-learn` | 辅助算法 |
| `rapidfuzz` | 文本匹配 |

---

## 4. Pandoc — AST 转换引擎

### 技术路线：纯文档剖析（AST 重写）

Pandoc 的设计哲学与其他四者截然不同——它**不解析 PDF**，而是通过抽象语法树（AST）做格式间映射：

```
DOCX 文件 → Pandoc Reader（解析 XML → AST）
                      ↓
                Pandoc AST（统一的中间表示）
                - Header, Para, CodeBlock
                - Table, BulletList, Link
                - Image, Math, Cite...
                      ↓
                Pandoc Writer（AST → Markdown）
                      ↓
                  output.md
```

### 关键特性

- **30+ 输入格式**、**50+ 输出格式**，通过统一的 AST 连接
- **Lua 过滤器**：可在 AST 层做任意变换（如删除特定元素、重写链接）
- **模板系统**：输出格式可高度自定义
- **PDF 不能直接输入**：Pandoc 的 Reader 需要结构化输入（XML、JSON、TeX 语法树），PDF 是排版指令流，没有文档结构语义

### 优缺点

- **优点**：DOCX→MD 质量极高，格式互转最灵活，零模型依赖，极快
- **缺点**：不能直接处理 PDF，需配合其他工具做 `PDF → LaTeX/HTML → Pandoc → MD`

### 依赖清单

| 依赖 | 用途 |
|------|------|
| `pypandoc-binary` | Pandoc 二进制文件（~33MB），无需系统安装 pandoc |

---

## 5. pdfplumber — 坐标几何提取

### 技术路线：纯文档剖析（几何坐标计算）

pdfplumber 基于 **pdfminer.six** 的底层字符定位能力，在其上增加了表格识别逻辑：

```
PDF 页面
    │
    ├── pdfminer 底层：提取每个字符的 (x, y, 宽度, 高度)
    │
    ├── pdfplumber 表格检测：
    │   - 扫描页面上的水平和垂直线条（显式表格边框）
    │   - 分析字符间空白间距（隐式表格列边界）
    │   - 推断行结构（基于 y 坐标对齐）
    │
    ├── 文本提取：按阅读顺序拼接字符 → extract_text()
    │
    └── 表格提取：单元格坐标 → 二维数组 → extract_tables()
```

### 表格检测原理

```
检测到的线条：                  推断出的表格结构：
┌──┬──────┬────┐                [["名称", "数量", "单价"],
│名称│ 数量 │单价│                 ["苹果", "3", "5.00"],
├──┼──────┼────┤                 ["橘子", "5", "3.50"]]
│苹果│  3  │5.00│
│橘子│  5  │3.50│
└──┴──────┴────┘
```

- 显式边框：检测 PDF 绘图指令中的矩形/线段
- 隐式边界：字符间距超过阈值 → 判定为列边界

### 优缺点

- **优点**：数字原生 PDF 的表格提取最精准，极轻量（< 10MB），内存占用 < 50MB
- **缺点**：不输出规范 Markdown（需自行拼接），扫描件完全不可用，无标题层级检测

### 依赖清单

| 依赖 | 用途 |
|------|------|
| `pdfminer.six` | PDF 底层字符坐标提取 |
| `pillow` | 页面渲染为图像（可选） |

---

## 6. 核心技术路线对比

```
                    纯文档剖析                          AI/ML 驱动
                    ──────────                         ─────────
                    
MarkItDown:        薄封装，无自身逻辑                  无
                    pdfminer/mammoth/pandas 透传

Pandoc:            AST 重写引擎，格式间语义映射         无
                    结构化输入 → 统一 AST → 结构化输出

pdfplumber:        几何坐标计算                         无
                    字符坐标 + 线条检测 → 表格推断

Docling:           格式路由 + 管道调度                  布局模型 + OCR + VLM
                                                        混合 GPU/CPU

Marker:            文本抽取（pypdfium2）                布局+检测+识别+表格+公式+纠错
                                                        全 GPU 管线
```

### 核心差异一句话总结

| 后端 | 一句话 |
|------|--------|
| MarkItDown | 把 pdfminer/mammoth 的输出拼成 Markdown，**不关心结构和布局** |
| Docling | 视觉理解管线，**PyTorch 布局+表格 + ONNX OCR**，GPU/CPU 混合 |
| Marker | 全 PyTorch 管线，**6 个模型全部跑 GPU**，公式原生 LaTeX |
| Pandoc | 文档格式间的 AST 翻译器，**从根本设计上不处理 PDF** |
| pdfplumber | 基于坐标几何的表格检测器，**只看线条和间距，不看视觉语义** |

---

## 7. GPU 利用率对比

本机环境：2× NVIDIA GeForce RTX 5060 Ti（各 15GB），CUDA 可用。

| 后端 | GPU 使用 | 详情 |
|------|:--:|------|
| MarkItDown | ❌ | 无模型，无需 GPU |
| Pandoc | ❌ | 无模型，无需 GPU |
| pdfplumber | ❌ | 无模型，无需 GPU |
| Docling | ⚠️ 部分 | Heron + TableFormer 走 CUDA，RapidOCR 走 CPU |
| Marker | ✅ 全部 | 6 个模型全部 PyTorch CUDA，有 GPUManager 显存调度 |

---

## 8. 自定义模型目录（离线 / 企业内部部署）

Docling 和 Marker 默认从 HuggingFace Hub 下载模型。如果需要在**无外网环境**或**企业内部镜像**使用，两者都支持指定本地模型目录。

### 8.1 Docling — `artifacts_path`

`PdfPipelineOptions` 提供内置的 `artifacts_path` 参数：

```python
pipeline_options = PdfPipelineOptions(
    artifacts_path="/opt/models/docling",  # 本地预下载的模型目录
)
```

模型目录结构需遵循 Docling 内部约定，可用 `docling-tools models download` 预下载到指定路径。设置后完全跳过 HuggingFace 远程拉取。

### 8.2 Marker — 环境变量 + `~/.cache/datalab/models/`

Marker 底层 Surya 模型的 `from_pretrained` 使用 HuggingFace transformers 标准加载逻辑，支持以下方式指定本地模型：

**方式一：环境变量**

```bash
export HF_HUB_CACHE="/opt/models/huggingface"
```

HuggingFace transformers 会优先从该目录查找已缓存的模型。

**方式二：直接放缓存目录**

Surya 的 `settings.MODEL_CACHE_DIR` 默认为 `~/.cache/datalab/models/`，内部结构：

```
~/.cache/datalab/models/
├── layout/              # 布局检测模型 checkpoint
├── text_detection/      # 文字检测模型 checkpoint
├── text_recognition/    # 文字识别模型 checkpoint
├── table_recognition/   # 表格识别模型 checkpoint
└── ocr_error_detection/ # OCR 纠错模型 checkpoint
```

六类模型各自读取该目录下对应的 checkpoint 子目录。

**方式三：覆盖 surya settings（需改代码）**

```python
from surya.settings import settings as surya_settings

surya_settings.LAYOUT_MODEL_CHECKPOINT = "/opt/models/layout"
surya_settings.RECOGNITION_MODEL_CHECKPOINT = "/opt/models/recognition"
# ... 其余四类同理
```

**注意**：Marker 的 `create_model_dict()` 目前没有直接暴露 checkpoint 参数，最简便的方式是将内部镜像目录软链接到 `~/.cache/datalab/models/`，或设置 `HF_HUB_CACHE` 指向企业 HF 镜像。

---

## 9. Docling 与 Marker 的 Python 版本兼容性

本项目的实际验证结果：

| Python 版本 | docling + marker 共存 | 原因 |
|:--:|:--:|------|
| 3.12 | ✅ 可共存 | pillow 10.x 在 3.12 编译通过 |
| 3.14 | ❌ 冲突 | pillow 10.x C 扩展 API 不兼容 3.14，marker 锁死 `pillow<11` |

当前项目使用 **Python 3.12**，五个后端全部可用。

---

## 10. 选型建议

```
需求场景                                        推荐后端
─────────────────────────────────────────────────────────
快速转 DOCX/PPTX/XLSX（不涉及 PDF）           → Pandoc
快速转数字原生 PDF（不要求表格/标题质量）      → MarkItDown
精准提取 PDF 表格数据                          → pdfplumber
高质量 PDF→MD（表格/多栏/扫描件，有 GPU）      → Docling
学术论文 + LaTeX 公式 + GPU 加速               → Marker
生产环境 RAG 管道                              → Docling
需要自定义转换规则/格式互转                    → Pandoc + Lua过滤器
两种方案都觉得不够好                            → Docling + Marker 并行输出对比
```
