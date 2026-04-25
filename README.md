# multimodal-light-agent

（持续开发中，现已完成基础 DEMO）

本项目是一个基于 Python 的轻量级多模态 Agent 原型系统，面向视频、图像和文本等多模态输入场景。系统以自然语言问题为入口，通过任务路由、工具选择、工具执行和回答生成等模块，完成从用户问题到多模态信息处理结果的闭环调用。

项目当前以轻量级工程实现为核心，重点关注多模态任务路由、工具注册机制、模块化调用流程和大模型接口层设计。系统已支持 video / image / text 三类基础模态，并通过统一工具 schema 管理不同模态下的可用能力，为后续扩展更复杂的多模态理解、智能工具选择和 Agent 化任务规划提供基础。

## 项目定位

本项目不是单一的视频处理脚本，而是一个面向多模态智能交互场景的轻量 Agent 原型。其核心目标是构建一个可运行、可扩展、可逐步接入大模型能力的多模态任务处理系统。

系统当前主要包含以下能力：

- 自然语言问题输入
- 多模态任务识别
- video / image / text 模态路由
- 不同模态下的子任务路由
- 统一工具注册与工具 schema 管理
- 工具执行与异常兜底
- 基于 OpenCV 的视频与图像处理
- 基础文本统计处理
- LLM 接口层预留
- DeepSeek 回答重写能力接入
- 最终回答生成闭环

## 功能特性

### 1. 多模态任务路由

系统会根据用户输入的问题自动判断任务所属模态，目前支持：

- 视频任务：`video`
- 图像任务：`image`
- 文本任务：`text`

示例问题：

```text
这个视频有多长？
这个视频什么时候变化最明显？
这张图片的尺寸是多少？
这段文本有多少个字符？
```

### 2. 视频处理能力

当前视频模态是系统中完成度最高的部分，已支持：

- 获取视频总时长
- 获取视频总帧数
- 获取视频 FPS
- 检测视频中是否存在明显运动
- 定位视频中变化最明显的时间点
- 生成视频内容概括
- 分析视频主要内容

视频处理主要基于 OpenCV 实现，部分分析能力采用轻量规则方法完成，例如基于帧差的运动检测与变化时间定位。

### 3. 图像处理能力

当前图像模态已接入系统主流程，支持：

- 获取图片宽度和高度
- 图像路径合法性检查
- 图像工具注册与统一调用

图像模态目前处于基础能力阶段，后续可继续扩展目标检测、图像描述、图像内容理解等能力。

### 4. 文本处理能力

当前文本模态已支持：

- 文本字符长度统计
- 文本词数统计
- 文本句子数统计

文本工具已接入统一工具系统，可通过自然语言问题触发对应处理逻辑。

### 5. 统一工具系统

项目通过 `tools.py` 对不同模态下的工具进行统一注册和管理。

每个工具均包含统一字段：

- `name`
- `description`
- `modality`
- `input_type`
- `output_type`
- `keywords`
- `example_question`
- `func`

该设计使系统具备较好的可扩展性。新增工具时，只需要实现对应处理函数，并在工具库中注册，即可接入整体 Agent 调用流程。

当前工具系统支持：

- 按模态获取工具
- 生成工具 schema
- 获取指定模态工具 schema
- 获取全部工具 schema
- 校验工具 schema 完整性
- 展示当前可用工具
- 统一执行工具函数

### 6. LLM 接口层

项目已设计独立的 `llm_interface.py` 作为大模型接口层，用于隔离具体模型服务与主程序逻辑。

当前支持：

- `mock` 模式：不调用外部模型，保证项目默认可运行
- `deepseek` 模式：调用 DeepSeek API 对工具结果进行自然语言重写
- `openai` provider 入口预留
- 问题理解入口预留
- LLM 工具选择入口预留

当前系统主要使用规则路由完成任务识别与工具调用，LLM 主要用于回答重写。后续可进一步升级为由 LLM 根据工具 schema 自动选择工具。

## 项目结构

```text
multimodal-light-agent/
├── main.py                 # 主程序入口，负责整体交互流程与任务调度
├── router.py               # 路由模块，负责模态识别与子任务识别
├── tools.py                # 工具注册、工具 schema、工具展示与统一执行
├── video_processor.py      # 视频基础属性处理模块
├── analysis.py             # 视频规则分析模块
├── image_processor.py      # 图像处理模块
├── text_processor.py       # 文本处理模块
├── answer_generator.py     # 最终回答生成模块
├── llm_interface.py        # LLM 接口层，支持 mock / DeepSeek 等模式
├── utils.py                # 工具辅助模块
├── requirements.txt        # 项目依赖
├── .env.example            # 环境变量配置示例
├── .gitignore              # Git 忽略配置
├── LICENSE                 # 开源协议
└── README.md               # 项目说明文档
```

## 核心流程

系统整体运行流程如下：

```text
用户输入自然语言问题
        ↓
LLM 问题理解入口
        ↓
模态路由：video / image / text
        ↓
输入对应模态的数据
        ↓
子任务路由
        ↓
展示当前模态可用工具
        ↓
执行对应工具
        ↓
生成工具执行结果
        ↓
LLM 回答重写 / mock 回答返回
        ↓
输出最终回答
```

## 安装与运行

### 1. 克隆项目

```bash
git clone https://github.com/Xiawqq/multimodal-light-agent.git
cd multimodal-light-agent
```

### 2. 创建虚拟环境

Windows：

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS / Linux：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置环境变量

如果只想运行基础版本，可以不配置真实大模型 API，系统会默认使用 `mock` 模式。

如需启用 DeepSeek 回答重写能力，可参考 `.env.example` 新建 `.env` 文件：

```env
LLM_PROVIDER=deepseek
DEEPSEEK_API_KEY=your_api_key_here
DEEPSEEK_MODEL=your_model_name_here
```

如果不配置 `.env`，系统默认使用：

```env
LLM_PROVIDER=mock
```

### 5. 运行项目

```bash
python main.py
```

## 使用示例

### 视频任务示例

输入问题：

```text
这个视频有多长？
```

输入视频路径：

```text
C:\Users\xxx\Desktop\test.mp4
```

系统会自动识别为视频任务，并调用视频时长分析工具。

### 图像任务示例

输入问题：

```text
这张图片的尺寸是多少？
```

输入图片路径：

```text
C:\Users\xxx\Desktop\test.jpg
```

系统会自动识别为图像任务，并返回图片宽度和高度。

### 文本任务示例

输入问题：

```text
这段文本有多少个字符？
```

输入文本内容：

```text
This is a simple multimodal agent demo.
```

系统会自动识别为文本任务，并返回文本统计结果。

## 当前已支持工具

### Video Tools

| 工具 key | 工具名称 | 功能说明 |
|---|---|---|
| `duration` | `get_video_duration` | 获取视频总时长 |
| `frame_count` | `get_video_frame_count` | 获取视频总帧数 |
| `fps` | `get_video_fps` | 获取视频帧率 |
| `motion` | `analyze_motion` | 检测视频中是否存在明显运动 |
| `change_time` | `analyze_change_time` | 定位视频中变化最明显的时间点 |
| `summary` | `analyze_summary` | 生成视频内容概括 |
| `content` | `analyze_video_content` | 分析视频主要内容 |

### Image Tools

| 工具 key | 工具名称 | 功能说明 |
|---|---|---|
| `size` | `get_image_size` | 获取图片宽度和高度 |

### Text Tools

| 工具 key | 工具名称 | 功能说明 |
|---|---|---|
| `length` | `get_text_length` | 统计文本字符长度 |
| `word_count` | `get_text_word_count` | 统计文本词数 |
| `sentence_count` | `get_text_sentence_count` | 统计文本句子数 |

## 技术栈

- Python
- OpenCV
- OpenAI SDK
- python-dotenv
- DeepSeek API
- Rule-based Routing
- Tool Schema
- Lightweight Agent Workflow

## 设计特点

### 模块化架构

项目将主流程、任务路由、工具注册、视频处理、图像处理、文本处理和 LLM 接口进行拆分，避免所有逻辑集中在单个文件中，提高了系统的可维护性。

### 统一工具抽象

不同模态下的能力均被封装为工具，并通过统一 schema 管理。这种设计便于后续扩展更多工具，也便于将工具信息提供给大模型进行自动选择。

### 轻量级 Agent 闭环

系统已经形成了从用户问题到工具调用再到最终回答的完整链路，具备轻量级 Agent 的基本结构：

```text
Question → Routing → Tool Selection → Tool Execution → Answer Generation
```

### 可扩展 LLM 接口

项目没有将具体大模型调用逻辑直接写死在主程序中，而是通过独立接口层进行管理。当前可在 mock 模式下稳定运行，也可以通过配置 DeepSeek API 启用回答重写能力。

## 后续开发方向

后续计划继续完善以下方向：

- 接入真正的 LLM 工具选择能力
- 根据工具 schema 实现自动工具调用
- 增强图像内容理解能力
- 增强视频语义分析能力
- 增加多轮对话上下文管理
- 增加工具执行日志
- 优化命令行交互体验
- 支持更复杂的任务规划流程
- 逐步扩展为更完整的多模态轻量 Agent 系统

## 项目状态

当前项目处于持续开发阶段，已完成基础可运行 DEMO。现阶段重点是构建稳定的工程骨架和清晰的多模态 Agent 调用流程，后续将在此基础上继续增强智能决策、视觉理解和任务规划能力。

## License

This project is licensed under the MIT License.