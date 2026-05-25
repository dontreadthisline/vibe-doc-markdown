https://hjfy.top/arxiv/2512.13564
人工智能智能体时代的记忆：综述
形式、功能与动态
Yuyang Hu†, Shichun Liu†, Yanwei Yue†, Guibin Zhang†(cid:379), Boyang Liu, Fangyi Zhu,
Jiahang Lin, Honglin Guo, Shihan Dou, Zhiheng Xi, Senjie Jin, Jiejun Tan, Yanbin Yin,
Jiongnan Liu, Zeyu Zhang, Zhongxiang Sun, Yutao Zhu, Hao Sun, Boci Peng, Zhenrong
Cheng, Xuanbo Fan, Jiaxin Guo, Xinlei Yu, Zhenhong Zhou, Zewen Hu, Jiahao Huo,
Junhao Wang, Yuwei Niu, Yu Wang, Zhenfei Yin, Xiaobin Hu, Yue Liao, Qiankun Li, Kun
Wang, Wangchunshu Zhou, Yixin Liu, Dawei Cheng, Qi Zhang, Tao Gui‡, Shirui Pan, Yan
Zhang‡, Philip Torr, Zhicheng Dou‡, Ji-Rong Wen, Xuanjing Huang‡, Yu-Gang Jiang,
Shuicheng Yan‡
†Core Contributors with Names Listed Alphabetically. (cid:379)Project Organizer. ‡Core
Supervisors.
Aﬀiliations: National University of Singapore, Renmin University of China, Fudan
University, Peking University, Nanyang Technological University, Tongji
University, University of California San Diego, Hong Kong University of Science
and Technology (Guangzhou), Griffith University, Georgia Institute of
Technology, OPPO, Oxford University
记忆已浮现，并将持续成为基于基础模型的智能体的核心能力。它支撑着长时程推理、持续适应
以及与复杂环境的有效交互。随着关于智能体记忆的研究迅速扩展并吸引前所未有的关注，该
领域也日益呈现出碎片化趋势。现有属于智能体记忆范畴的工作在动机、实现方式、假设条件和
评估协议等方面往往存在显著差异，而大量松散定义的记忆术语进一步模糊了概念上的清晰性。
传统的分类体系如长/短期记忆已不足以捕捉当代智能体记忆系统的多样性与动态性。
本综述旨在提供当前智能体记忆研究的最新且全面的全景图。我们首先明确智能体记忆的范围，
并将其与相关概念（如大语言模型记忆、检索增强生成（RAG）以及上下文工程）区分开来。随
后，我们从形式、功能和动态三个统一视角审视智能体记忆。从形式角度，我们识别出三种主导
性的智能体记忆实现方式，即 token 级、参数化和潜在记忆。从功能角度，我们突破粗略的时间
划分，提出一种更细粒度的分类体系，区分事实性、经验性和工作记忆。从动态角度，我们分析
智能体在与环境交互过程中记忆如何形成、演化及被检索。
为支持实证研究与实际开发，我们整理了一份代表性基准测试与开源记忆框架的全面总结。除
整合之外，我们还提出了面向未来的前沿研究展望，包括以自动化为导向的记忆设计、强化学习
与记忆系统的深度融合、多模态记忆、多智能体系统中的共享记忆以及可信性问题。我们希望本
综述不仅可作为现有工作的参考，更能成为重新思考记忆作为未来代理智能设计中首要原语的
概念基础。
(cid:263) Main Contact: guibinz@u.nus.edu, yuyang.hu@ruc.edu.cn, liusc24@m.fudan.edu.cn,
ywyue25@stu.pku.edu.cn
2
Github: https://github.com/Shichun-Liu/Agent-Memory-Paper-List

Figure1 智能体记忆的概览，按照统一的分类体系组织，该体系涵盖形式（Section3）、功能（Section4）和动态（Section5）。
图示将记忆实体按其主导形式和主要功能进行定位。同时，还将代表性系统映射到这一分类体系中，以提供一个整合性
的全景视图。
1 引言
过去两年见证了日益强大的大语言模型（LLMs）向强大智能体的全面演化 (Matarazzo and Torlone,
2025; Minaee et al., 2025; Luo et al., 2025)。这些基于基础模型的智能体在深度研究 (Xu and Peng,
2025; Zhang et al., 2025o)、软件工程 (Wang et al., 2024i) 以及科学发现 (Wei et al., 2025c) 等多个领
域展现了显著进展，持续推动着迈向人工通用智能（AGI）的轨迹 (Fang et al., 2025a; Durante et al.,
2024)。尽管早期对“智能体”的概念极为多样化，但学界如今已逐渐形成共识：除了纯大模型核心外，
智能体通常还具备推理、规划、感知、记忆和工具使用等能力。其中一些能力，如推理和工具使用，已
通过强化学习在模型参数中实现高度内化 (Wang et al., 2025l; Qu et al., 2025b)，而另一些仍严重依赖
外部智能体支撑结构。这些组件共同作用，使大模型从静态的条件生成器转变为可学习的策略，能够与
多样化的外部环境交互，并随时间自适应演化 (Zhang et al., 2025f)。
在这些智能体能力中，记忆尤为突出，它明确地使静态的大模型——其参数无法快速更新——转变为能
够通过与环境交互实现持续适应的智能体 (Zhang et al., 2025r; Wu et al., 2025g)。从应用角度看，众多
领域需要具备主动记忆管理能力的智能体，而非短暂易忘的行为：个性化聊天机器人 (Chhikara et al.,
2025; Li et al., 2025b)、推荐系统 (Liu et al., 2025b)、社会仿真 (Park et al., 2023; Yang et al., 2025) 以
及金融调查 (Zhang et al., 2024) 均依赖于智能体处理、存储和管理历史信息的能力。从发展角度来看，
Note: If you identify your own or other papers relevant to this survey that have not been discussed (we apologize for any such
omissionsduetotherapidlyexpandingliterature),pleasefeelfreetocontactusviaemailorraiseanissueonGitHub.
3

AGI 研究的一个核心目标是赋予智能体通过环境交互实现持续演化的容量 (Hendrycks et al., 2025)，这
一能力从根本上依赖于智能体的记忆。
智能体记忆需要新的分类体系 随着智能体记忆系统日益重要的地位以及社区对其广泛关注，提供一个
关于当代智能体记忆研究的最新视角已成为及时且必要的任务。提出新分类体系与综述的动机有两方
面：❶ 现有分类体系的局限性：尽管近期已有若干综述对智能体记忆提供了宝贵且全面的概述 (Zhang
et al., 2025r; Wu et al., 2025g)，但其分类体系是在多项快速方法论进展之前构建的，因此未能充分反
映当前研究领域的广度与复杂性。例如，2025 年新兴的研究方向，如从过往经验中提炼可复用工具的
记忆框架 (Qiu et al., 2025a,c; Zhao et al., 2025c)，或增强记忆的测试时缩放方法 (Zhang et al., 2025g;
Suzgun et al., 2025)，仍未能在早期分类方案中得到充分体现。❷ 概念碎片化：随着与记忆相关研究的
爆炸式增长，该概念本身变得愈发广泛且碎片化。研究人员常常发现，声称研究“智能体记忆”的论文
在实现方式、目标及潜在假设上存在显著差异。多样化的术语（陈述性记忆、情景记忆、语义记忆、参
数化记忆等）的泛滥进一步模糊了概念的清晰性，凸显出建立一个能够整合这些新兴概念的统一分类体
系的紧迫需求。
因此，本文旨在建立一个系统性框架，以调和现有定义、连接新兴趋势，并阐明智能体系统中记忆的基
本原理。具体而言，本综述旨在解决以下关键问题：
Key Questions
❶ 智能体记忆是如何定义的，它与大语言模型记忆、检索增强生成（RAG）以及上下文工程等相关
概念有何关联？
❷ 形式：智能体记忆可以采取哪些架构或表示形式？
❸ 功能：为什么需要智能体记忆，它起到哪些作用或目的？
❹ 动态：智能体记忆如何随时间运作、适应与演化？
❺ 推进智能体记忆研究的有前景前沿领域有哪些？
为回答问题 ❶，我们首先在 Section 2 中对基于大语言模型的智能体及其记忆系统提供形式化定义，并
详细比较智能体记忆与相关概念（如大语言模型记忆、RAG 和上下文工程）之间的异同。遵循“形态
—功能—动态”三角框架，我们对智能体记忆进行了结构化概述。问题 ❷ 探讨记忆的架构形态，我们
在 Section 3 中进行讨论，重点介绍三种主流实现方式：token 级别记忆、参数化记忆和潜在记忆。问题
❸ 关注记忆的功能角色，相关内容在 Section 4 中阐述，我们区分了 事实记忆（记录智能体与用户及环
境交互所产生的知识）、经验记忆（通过任务执行逐步提升智能体的问题求解能力）以及 工作记忆（用
于管理单个任务实例中的工作空间信息）。问题 ❹ 聚焦于智能体记忆的生命周期与运行动态，我们按记
忆构建、检索和演化三个阶段依次展开论述。
在“形式–功能–动态”视角下审视现有研究后，我们进一步提出对智能体记忆研究的见解与思考。为促
进知识共享与未来发展，我们首先在 Section 6 中总结了关键基准与框架资源。在此基础上，我们接着
通过探讨 Section 7 中若干新兴但尚未充分发展的研究前沿来回应问题 ❺，包括面向自动化的记忆设计、
强化学习（RL）的融合、多模态记忆、多智能体系统的共享记忆以及可信性问题。
4

贡献 本综述的贡献可总结如下：(1) 我们从“形式–功能–动态”视角，提出了一种最新且多维度的智
能体记忆分类体系，为理解该领域的当前发展提供了结构化的分析视角。(2) 我们深入探讨了不同记忆
形式与功能目的的适用性及其相互作用，揭示了各类记忆类型如何有效匹配不同的 Agentic 目标。(3)
我们研究了智能体记忆领域中涌现的有前景的研究方向，从而明确了未来的发展机遇与推进路径。(4)
我们整理了一份全面的资源集合，包括基准测试和开源框架，以支持研究人员和实践者对智能体记忆系
统的进一步探索。
调查大纲 本文的其余部分组织如下。Section 2 对基于大语言模型的智能体及智能体记忆系统进行了
形式化定义，并阐明了它们与相关概念之间的关系。Section 3、Section 4 和 Section 5 分别探讨了智能
体记忆的形式、功能与动态特性。Section 6 总结了具有代表性的基准测试与框架资源。Section 7 讨论
了新兴的研究前沿与未来方向。最后，我们在 Section 8 中以总结关键见解的方式结束本综述。
2 预备知识：智能体与记忆的形式化
大型语言模型智能体越来越多地作为交互系统中的决策核心，这些系统能够随时间运行、操作外部工具，
并与人类或其他智能体进行协调。为了研究此类情景下的记忆机制，我们首先以一种涵盖单智能体和多
智能体配置的方式，形式化基于大型语言模型的智能体系统。随后，我们通过读/写交互形式化与智能
体决策过程耦合的记忆系统，从而统一处理在任务内部（试验内/短期记忆）和任务之间（试验间/长期
记忆）出现的记忆现象。
2.1 基于 LLM 的智能体系统
智能体与环境 设 I = {1,...,N} 表示智能体的索引集合，其中 N = 1 对应单智能体情形（例如
ReAct），而 N > 1 表示多智能体情景，如辩论 (Li et al., 2024c) 或规划者-执行者架构 (Wan et al.,
2025)。环境由状态空间 S 描述。在每个时间步 t ，环境根据受控的随机转移模型演化。
s ∼Ψ(s |s ,a ),
t+1 t+1 t t
其中 a 表示在时间 t 执行的动作。在多智能体系统中，这种抽象允许顺序决策（每次只有一个智能体
t
行动）或通过环境媒介效应实现隐式协调。每个智能体 i∈I 接收到一个观测
oi =O (s ,hi,Q),
t i t t
其中 hi 表示智能体 i 可见的交互历史部分。该历史可能包括之前的消息、中间工具输出、部分推理迹、
t
共享工作区状态或其他智能体的贡献，具体取决于系统设计。Q 表示任务规范，例如用户指令、目标描
述或外部约束，在任务中被视为固定不变，除非另有说明。
动作空间 基于大语言模型的智能体的一个显著特征是其动作空间的异质性。与仅限于纯文本生成的动
作不同，智能体可在多模态且语义结构化的动作空间中操作，包括：
• 自然语言生成，例如生成中间推理、解释、回复或指令 (Li et al., 2023b; Wu et al., 2024b; Hong
et al., 2024; Qian et al., 2024)。
5

• 工具调用动作，用于调用外部 API、搜索引擎、计算器、数据库、模拟器或代码执行环境 (Qin et al.,
2025; Li et al., 2025g; Zhou et al., 2023c, 2024c)。
• 规划动作，即明确输出任务分解、执行计划或子目标说明，以指导后续行为 (CAMEL-AI, 2025; Liu
et al., 2025f; Pan et al., 2024)。
• 环境控制动作，智能体直接操作外部环境（例如，在具身设置中导航 (Shridhar et al., 2021; Wang
et al., 2022a)、编辑软件仓库 (Jimenez et al., 2024; Aleithan et al., 2024)，或修改共享内存缓冲区）。
• 通信动作，通过结构化消息实现与其他智能体的协作或协商 (Marro et al., 2024)。
尽管这些动作在语义上各不相同，但它们的共同之处在于都是通过基于上下文输入的自回归大语言模型
主干生成的。形式上，每个智能体 i 都遵循一个策略
a =π (oi,mi,Q),
t i t t
其中 mi 是在 Section 2.2 中定义的由记忆生成的信号。策略在发出可执行动作之前，可能会内部生成
t
多步推理链、潜在的深思熟虑或草稿板计算；这些内部过程被抽象掉，并未被显式建模。
交互过程与轨迹 系统的完整执行会引发一条轨迹
τ =(s ,o ,a ,s ,o ,a ,...,s ),
0 0 0 1 1 1 T
其中 T 由任务终止条件或系统特定的停止标准决定。在每个步骤中，轨迹反映了（i）环境观测、（ii）可
选的记忆检索、（iii）基于大语言模型的计算以及（iv）驱动下一个状态转移的动作执行的交错过程。
该公式描述了一类广泛的 Agentic 系统，从单一智能体通过工具增强解决推理任务，到角色专业化的智
能体团队协作开发软件 (Qian et al., 2024; Wang et al., 2025k) 或开展科学探究 (Weng et al., 2025)。接
下来，我们将形式化整合进该智能体环中的记忆系统。
2.2 智能体记忆系统
当基于大语言模型的智能体与环境交互时，其瞬时观测 oi 通常不足以支持有效的决策。因此，智能体
t
需要依赖来自当前任务内部以及先前已完成任务中的额外信息。我们通过一个统一的 智能体记忆系统
来形式化这一能力，该系统表示为一个不断演化的记忆状态
M ∈M,
t
其中 M 表示可接受的记忆配置空间。对 M 未施加特定的内部结构；它可以表现为文本缓冲区、键值
t
存储、向量数据库、图结构或任何混合表示形式。在任务开始时，M 可能已包含从先前试验（跨试验
t
记忆）中提炼的信息。在任务执行过程中，新信息不断积累，并作为短期的、与任务相关的记忆。这两
种角色均在一个单一的记忆容器中得到支持，时间上的区分源于使用模式而非架构上的分离。
记忆生命周期：形成、演化与提取。 记忆系统的动态特性由三个概念性算子来描述。
记忆形成。在时间步 t ，智能体生成信息型产物 φ ，这些产物可能包括工具输出、推理迹、部分计划、
t
6

自我评估或环境反馈。一个形成算子
Mform =F(M ,φ )
t+1 t t
有选择地将这些人工制品转换为记忆候选，提取具有潜在未来用途的信息，而不是逐字存储整个交互历
史。
记忆演化。已形成的记忆候选通过一个演化算子被整合到现有的记忆库中
M =E(Mform),
t+1 t+1
这可能有助于整合冗余条目 (Zhao et al., 2024)，解决冲突 (Rasmussen et al., 2025; Li et al., 2025k)，
丢弃低效用信息 (Wang et al., 2025q)，或重新组织记忆以实现高效检索。由此产生的记忆状态将在后
续的决策步骤和任务中持续存在。
记忆检索。在选择动作时，智能体 i 检索一个与上下文相关的记忆信号
mi =R(M ,oi,Q),
t t t
其中 R 表示一个检索算子，用于构建任务感知的查询并返回相关的记忆内容。检索到的信号 mi 以适
t
合直接供大语言模型策略使用的形式进行格式化，例如文本片段序列或结构化摘要。
智能体环中的时间角色 尽管记忆被表示为统一的状态 M ，但三个生命周期算子（形成 F 、演化 E
t
和检索 R ）并不需要在每个时间步都被调用。相反，不同的记忆效应源于不同的时间调用模式。例如，
某些系统仅在任务初始化时执行一次检索，
R(M
0
,oi
0
,Q), t=0,
mi =
t 
⊥, t>0,


其中 ⊥ 表示空检索策略。其他策略可根据上下文触发条件间歇或连续地检索记忆。类似地，记忆的形
成可能从原始观测的最小积累到……
Mform =M ∪{oi},
t+1 t t
对可复用模式或抽象的复杂提取与精炼。因此，在一个任务内部，短期记忆效应可能源于轻量级日志记
录，如同Yaoetal.(2023b);Chenetal.(2023a)所示，或源于更复杂的迭代精炼过程(Huetal.,2025a)；
在任务之间，长期记忆可能在任务边界处以事件方式更新，或在整个运行过程中持续更新。因此，短期
记忆和长期记忆现象并非来自离散的架构模块，而是源自形成、演化和检索所涉及的时间模式。
记忆—智能体耦合。 记忆与智能体决策过程之间的交互同样具有灵活性。通常，智能体策略表示为
a =π (oi,mi,Q),
t i t t
其中，检索到的记忆信号 mi 可能存在也可能不存在，具体取决于检索调度。当在某个步骤中禁用检索
t
时，mi 可被视为一种特殊的空输入。
t
因此，整体智能体环包括观察环境、可选地检索记忆、计算动作、接收反馈，并可选地通过形成与演化
7

- Self-Evolving Memory
- Parametric Memory
e.g., Memento, H2R - Few-shot prompting
e.g., Retroformer, Early experience
- Multimodal Memory e.g., CoT, PALM
- RL-enabled Memory
e.g., Ella, ViloMem, M3-Agent - Self-Reflection
e.g., MemAgent, RMM, MemSearcher,
- Latent Memory e.g., Self-refine, CRITIC
MEM1, Mem-alpha, Memory-R1
e.g., MemoryLLM, M+, MemGen - KV compression/reuse
e.g., AutoCompressor, SnapKV
Agent - Attention KV management
- Memory graph Memory e.g., Mixture-of-Memory
e.g., Zep, AriGraph - Long context processing
- Agentic memory LLM e.g., Mamba, Memformer, MoA,
e.g., A-Mem, G-Memory Memory Sparseformer, NSA
- Working memory
e.g., HiAgent, ReSum,
- Tool-integrated reasoning
RAG
- Modular RAG Context e.g., ReTool, ToolLLM,
e.g., FlashRAG, ComposeRAG Toolformer, VTool-R1, ToRL
- Graph RAG Engineering - Tool selection
e.g., LightRAG, HippoRAG e.g., AutoTool, VisTA
- Agentic RAG - Communication protocol
e.g., PlanRAG, Self-RAG e.g., ANP, A2A, MCP, Agora
Figure2 智能体记忆与大语言模型记忆、检索增强生成和上下文工程的概念性对比。该图示展示了共享的技术实现（如
键值重用、图谱检索），同时突出了根本差异：与大语言模型记忆的架构优化、检索增强生成的静态知识访问以及上下文
工程的临时资源管理不同，智能体记忆的独特之处在于其对维持持久且自我演进的认知状态的关注，这种状态整合了事
实知识与经验。所列类别与示例仅为示意性而非严格对应，作为代表性的参考点，旨在阐明概念关系，而非定义僵化的
分类体系。
更新记忆。不同的智能体实现以不同时间频率实例化这些操作的不同子集，从而产生从被动缓冲区到主
动演化的知识库等各种记忆系统。
2.3 智能体记忆与其他关键概念的比较
尽管人们对具备记忆能力的智能体系统日益关注，但学术界对于什么是智能体记忆的理解仍然支离破
碎。在实践中，研究人员和从业者常常将智能体记忆与相关概念混淆，例如大语言模型记忆 (Wu et al.,
2025g)、检索增强生成（RAG） (Gao et al., 2024) 以及上下文工程 (Mei et al., 2025)。尽管这些概念
因涉及大语言模型驱动系统中信息的管理与利用而密切相关，但在范围、时间特性及功能角色上仍存在
差异。
这些重叠却又各不相同的概念已在文献和实践中引发了分歧。为了厘清这些差异，并将智能体记忆置于
更广泛的背景中，我们在随后的小节中探讨智能体记忆如何与大语言模型记忆、RAG 以及上下文工程
相关联，以及如何发散。Figure 2 通过一个维恩图直观展示了这些领域之间的共性和差异。
2.3.1 智能体记忆与大模型记忆
从高层次来看，智能体记忆几乎完全涵盖了传统上所指的 大语言模型记忆。自 2023 年以来，许多自称
“大语言模型记忆机制”的工作 (Zhong et al., 2024; Packer et al., 2023a; Wang et al., 2023b)，在当代
术语下更恰当的理解应为早期的智能体记忆实例。这一重新解读源于“大语言模型智能体”这一概念长
期以来存在的分歧。在 2023 至 2024 年间，该领域尚无稳定或一致的定义：某些情况下，仅通过提示大
语言模型调用计算器即可使其被视作智能体 (Wu et al., 2024c)；而在另一些情况下，代理能力则需要
8

更为丰富的功能，如显式的规划、工具使用、记忆以及反思性推理 (Ruan et al., 2023)。直到最近，才
开始出现更加统一和结构化的定义（例如，基于大语言模型的智能体 = 大语言模型 + 推理 + 规划 +
记忆 + 工具使用 + 自我改进 + 多轮交互 + 感知，如 Zhang et al. (2025f) 所述），尽管即便如此，该
定义也并非普遍适用。
在此历史背景下，早期系统如 MemoryBank (Zhong et al., 2024) 和 MemGPT (Packer et al., 2023a) 将
其贡献描述为提供 大语言模型记忆。然而，它们本质上解决的是经典的智能体问题，例如使基于大语
言模型的会话智能体能够追踪用户偏好、维持对话状态信息，并在多轮交互中积累经验。在现代且更为
成熟的代理理解下，这些系统自然应归类为 智能体记忆的实例。
尽管如此，这种涵盖关系并非绝对。有一条独立的研究路线真正关注的是大语言模型内部记忆：管理
Transformer 的键值（KV）缓存、设计长上下文处理机制，或修改模型架构（例如，RWKV (Peng et al.,
2023)、Mamba (Gu and Dao, 2024; Lieber et al., 2024)、基于扩散的语言模型 (Nie et al., 2025)），以
更好地在序列长度增长时保留信息。这些工作聚焦于模型的内在动态，通常处理不涉及智能体行为的任
务，因此应被视为智能体记忆范畴之外。
重叠。 在我们的分类体系中，历史上被称为“大语言模型记忆”的大部分内容都对应于智能体记忆的形
式。诸如 few-shot prompting (Prabhumoye et al., 2022; Ma et al., 2023a) 这类技术可被视为一种长期
记忆形式，其中过往的示例或提炼的任务摘要作为可通过检索或上下文注入方式复用的知识。自我反思
与迭代优化方法 (Madaan et al., 2023; Mousavi et al., 2023; Han et al., 2025c) 天然契合短期、任务内
的记忆，因为智能体在同一次任务中反复利用先前尝试所产生的中间推理迹或结果。即使 KV 压缩与
上下文窗口管理 (Yoon et al., 2024; Jiang et al., 2023)，当用于在单个任务过程中保留关键信息时，也
以智能体意义上的短期记忆机制发挥作用。这些技术均支持智能体在任务执行过程中积累、变换和复用
信息的能力。
区别。 相比之下，那些直接干预模型内部状态的内存机制——例如用于扩展有效上下文的架构修改、缓
存重写策略、循环状态持久化、注意力稀疏性机制或外部化的 KV 存储扩展——更适当地应被归类为
LLM 内存，而非智能体内存。它们的目标是扩展或重组潜在模型的表示容量，而不是为决策智能体提
供一个动态演化的外部记忆基础。这些机制通常不支持跨任务持久性、环境驱动的适应性或有意的记忆
操作（如形成、演化、检索），因此超出了本综述中定义的智能体内存的操作范围。
2.3.2 智能体记忆与 RAG
在概念层面，智能体记忆和 检索增强生成（RAG）表现出显著的重叠：这两个系统均构建、组织并利
用辅助信息存储，以扩展大型语言模型/智能体超出其原生参数化知识的能力。例如，结构化表示如知
识图谱和索引策略均出现在两个领域的方法中，而近期在 Agentic RAG 方面的发展表明，自主检索机
制能够以类似于智能体记忆架构的方式与动态数据库进行交互 (Singh et al., 2025)。实际上，许多 RAG
与智能体记忆系统的底层工程栈共享相同的构建模块，包括向量索引、语义搜索以及上下文扩展模块。
尽管存在这些技术收敛，但两种范式在历史上一直通过其应用背景加以区分。经典 RAG 技术主要通过
访问静态知识源来增强大语言模型（LLM），这些知识源包括扁平文档存储、结构化知识库或外部索引
的大规模语料库，以支持按需检索 (Zhang et al., 2025p; Han et al., 2025b)。这些系统旨在基于最新事
实生成内容，减轻幻觉现象，并提高知识密集型任务的准确率，但通常不会维护对过去交互的内部动态
9

记忆。相比之下，智能体记忆系统是在智能体与环境的持续交互中实现的，会不断将智能体自身动作
和环境反馈所产生的新信息整合到持久的记忆库中 (Wang et al., 2024l; Zhao et al., 2024; Sun et al.,
2025d)。
在早期的定义中，RAG 与智能体记忆之间的区别相对清晰：RAG 从外部维护的知识库中检索信息以
完成单次任务调用，而智能体记忆则在多轮、多任务交互过程中持续演化。然而，随着检索系统本身变
得愈发动态，这一界限逐渐模糊。例如，在某些检索任务中，相关上下文会随着迭代查询过程不断更新
（如多跳问答情景中，相关上下文逐步添加）。有趣的是，像 HippoRAG/HippoRAG2 (Gutierrez et al.,
2024; Gutiérrez et al., 2025) 这样的系统被 RAG 社区和记忆社区均视为解决大模型长期记忆挑战的方
法。因此，一个更实际（尽管并非完全可分离）的区分标准在于 任务领域。RAG 主要用于为大模型在
单个推理任务中补充大规模外部来源的上下文，典型例子包括经典的多跳和知识密集型基准测试，如
HotpotQA (Yang et al., 2018)、2WikiMQA (Ho et al., 2020) 和 MuSiQue (Trivedi et al., 2022)。相
比之下，智能体记忆系统通常在需要持续多轮交互、时间依赖性或环境驱动适应性的场景下进行评估。
代表性基准包括长上下文对话评估（如 LoCoMo (Maharana et al., 2024) 和 LongMemEval (Wu et al.,
2025a)）、复杂问题求解与深度研究基准（如 GAIA (Mialon et al., 2023)、XBench (Chen et al., 2025b)
和 BrowseComp (Wei et al., 2025b)）、以代码为中心的智能体任务（如 SWE-bench Verified (Jimenez
et al., 2024)），以及终身学习基准（如 StreamBench (Wu et al., 2024a)）。我们在 Section 6.1 中提供了
记忆相关基准的全面总结。
然而，即使这种基于领域的区分也存在大量模糊地带。许多自称为智能体记忆系统的研究在长文档问答
任务（如 HotpotQA (Wang et al., 2025g,o)）上进行评估，而众多被标榜为 RAG 系统的论文实际上实
现了某种形式的 Agentic 自我改进，能够随着时间不断提炼和优化知识或技能。因此，标题、方法论以
及实证评估常常模糊了这两种范式之间的概念边界。
为进一步厘清这些关系，以下三段内容借鉴了(Meietal.,2025)中已有的RAG分类体系：模块化RAG、
图 RAG 和 Agentic RAG，并考察每种谱系的核心技术如何在 RAG 与智能体记忆系统中体现。
模块化 RAG（Retrieval-Augmented Generation ） 模块化 RAG 指的是将检索流水线分解为明
确指定的组件（如索引、候选检索、重排序、过滤和上下文组装）的架构，这些组件以相对静态且流
水线化的方式运行 (Singh et al., 2025)。这类系统将检索视为一个经过精心设计的模块化子系统，该子
系统独立于大模型（LLM），主要在推理过程中向模型的上下文窗口注入相关知识。从智能体记忆的角
度来看，相应的技术通常出现在检索阶段，其中记忆访问通过向量搜索、语义相似度匹配或基于规则
的过滤实现，这在流行的智能体记忆框架如 Memary (Memary, 2025)、MemOS (Li et al., 2025k) 和
Mem0 (Chhikara et al., 2025) 中均有体现。
图 RAG 基于图形的 RAG 系统将知识库结构化为图，涵盖知识图谱、概念图或文档-实体关系等多
种形式，并利用图遍历或基于图形的排序算法来检索上下文 (Peng et al., 2024)。这种表示方式支持多
跳关系推理，已被证明在知识密集型任务中具有显著效果 (Edge et al., 2025; Han et al., 2025b; Dong
et al., 2025a)。在智能体记忆的背景下，当智能体随时间积累关系性洞察时，图结构记忆自然形成，例如
关联概念、追踪子任务间的依赖关系，或记录通过交互推断出的因果关系。一些成熟的做法包括 Mem0g
(Chhikaraetal.,2025)、A-MEM(Xuetal.,2025c)、Zep(Rasmussenetal.,2025)以及G-memory(Zhang
et al., 2025c)。值得注意的是，基于图形的智能体记忆系统可能在智能体运行过程中动态地“构建、扩
10

展或重组”其内部图。因此，基于图形的检索构成了两种范式中的结构核心，但只有智能体记忆将图视
为一种持续演化的经验表征。我们在Section 3.1.2中进一步分析了基于图形的记忆形式，并建议读者参
考相关综述 (Liu et al., 2025g)。
具身化 RAG Agentic RAG 将检索集成到自主决策环中，其中大语言模型智能体主动控制何时、如
何以及检索什么内容 (Singh et al., 2025; Sun et al., 2025d)。这些系统通常采用迭代查询、多步规划
或自我导向的搜索流程，使智能体能够通过有意识的推理来优化其信息需求，如 PlanRAG (Lee et al.,
2024b) 和 Self-RAG (Asai et al., 2023) 中所实现的那样。关于 Agentic RAG 的更深入理解，我们建议
读者参考 Singh et al. (2025)。从智能体记忆的角度来看，Agentic RAG 处于最接近的概念空间：两种
系统均涉及与外部信息存储的自主交互，均支持多步细化，并且均可将检索到的洞察融入后续推理中。
关键区别在于，传统的 Agentic RAG 通常作用于一个 * 外部 * 且常常是任务特定的数据库，而智能
体记忆则维护一个 * 内部、持久且自我演进 * 的记忆库，能够跨任务累积知识 (Yan et al., 2025a; Xu
et al., 2025c)。
2.3.3 智能体记忆与上下文工程
智能体记忆与上下文工程之间的关系最好理解为不同操作范式的交集，而非层级包含关系。上下文工程
是一种系统化的设计方法论，将上下文窗口视为一种受限的计算资源。它严格优化信息载荷，包括指令、
知识、状态和记忆，以缓解大规模输入容量与模型生成能力之间的不对称性 (Mei et al., 2025)。而智能
体记忆则聚焦于具有动态身份的持久实体的认知建模，上下文工程则在资源管理范式下运作。从上下文
工程的角度看，智能体记忆仅仅是上下文组装函数中的一个变量，需要高效调度以最大化推理效率。反
之，从智能体的角度看，上下文工程是确保认知连续性保持在潜在模型物理限制内的实现层。
重叠 在长时程交互中，这两个领域在工作记忆的技术实现上高度融合，并经常采用功能相同的机制来
应对有限上下文窗口 (Hu et al., 2025a; Zhang et al., 2025q; Kang et al., 2025c; Yu et al., 2025a) 所带
来的约束。两种范式均依赖于先进的信息压缩 (Zhou et al., 2025b; Wu et al., 2025f)、组织 (Xu et al.,
2025c; Zhang et al., 2025c; Anokhin et al., 2024) 和选择 (Zhang et al., 2025q) 技术，以在长时间交互序
列中保持操作的连续性。例如，作为上下文工程框架核心的 token 剪枝和基于重要性的选择方法 (Jiang
et al., 2023; Li et al., 2023c)，在智能体记忆系统中发挥着基础作用，能够过滤噪声并保留关键信息。
同样，滚动摘要技术作为一种共享的基础原语，同时充当缓冲区管理策略和临时情景记忆机制(Yuetal.,
2025a; Lu et al., 2025b)。实际上，在这些场景中，上下文工程与维护智能体短期记忆之间的界限实际
上已消失，因为两者都依赖于相同的潜在摘要、动态信息检索以及递归状态更新 (Tang et al., 2025b;
Yoon et al., 2024)。
区别 当从短期文本处理转向长期运行的智能体时，这种区别变得尤为明显。上下文工程主要解决大模
型与其运行环境之间交互接口的结构组织问题。这包括优化工具集成的推理与选择流水线 (Qin et al.,
2024a; Schick et al., 2023; Jia and Li, 2025)，以及标准化通信协议，如 MCP (Qiu et al., 2025c)。这些
方法侧重于确保指令、工具调用和中间状态在格式上正确、调度高效，并且能够在上下文窗口的约束下
被执行。因此，上下文工程作用于资源分配与接口正确性层面，强调语法有效性和执行效率。
相比之下，智能体记忆定义了一个显著更广阔的认知范围。除了短暂的上下文组装之外，它还涵盖了事
实性知识的持久存储 (Zhong et al., 2024)、经验迹的积累与演化 (Zhao et al., 2024; Tang et al., 2025d;
11

Zhang et al., 2025d)，以及在某些情况下将记忆内化为模型参数 (Wang et al., 2025n)。智能体记忆并
不关注推理时信息如何呈现给模型，而是决定智能体知道什么、经历过什么，以及这些要素如何随时
间演变。这包括将重复交互整合为知识 (Tan et al., 2025c)、从过往的成功与失败中抽象出程序性知
识 (Ouyang et al., 2025)，以及在不同任务和回合之间维持连贯的身份 (Wang et al., 2024f)。
从这一视角来看，上下文工程构建了在资源约束下实现感知与动作的外部支撑框架，而智能体记忆则构
成了支持学习、适应与自主性的内部基础。前者优化智能体与模型之间的即时交互界面，后者维持一种
超越单个上下文窗口的持久认知状态。
3 形式：什么承载记忆？
为了组织先验工作，我们首先考察构建智能体记忆所依赖的最基本表示单元。我们首先尝试回答：智能
体记忆可以采取哪些架构或表示形式？
在各种智能体系统中，记忆并非通过单一统一的结构实现。相反，不同的任务情景需要不同形式的存储，
每种形式都具有独特的结构特性。这些架构赋予记忆不同的能力，塑造智能体在交互过程中积累信息的
方式，并保持行为的一致性。它们最终使记忆能够在多样化的任务场景中发挥其预期作用。
根据记忆的存储位置及其表现形式，我们将这些记忆分为三类：
Three Major Memory Forms
1. Token 级内存 (Section 3.1)：以显式且离散的单元形式组织的内存，这些单元可以被单独访
问、修改和重构。这些单元保持外部可见性，并可长期以结构化形式存储。
2. 参数化记忆 (Section 3.2)：存储于模型参数中的记忆，其中信息通过参数空间的统计模式进行
编码，并在前向计算过程中隐式访问。
3. 潜在记忆 (Section 3.3)：以模型内部隐状态、连续表示或不断演化的潜在结构形式表示的记
忆。它可以在推理过程中或跨交互周期中持续存在并更新，捕捉上下文相关的内部状态。
上述三种记忆形式确立了理解“什么承载记忆”的核心结构框架。每种形式以自身的方式组织、存储和
更新信息，从而产生不同的表示模式和操作行为。在此结构分类的基础上，我们可以更系统地探讨智能
体为何需要记忆（Section 4），以及记忆如何在持续交互中演化、适应并塑造智能体行为（Section 5）。
这一分类为后续的讨论提供了概念基础。
3.1 Token 级记忆
Definition of Token-level Memory
Token 级记忆以持久的离散单元形式存储信息，这些单元外部可访问且可检查。此处的 token 是一
个广泛的表示概念：除了文本 token 外，还包括视觉 token、音频帧——任何可被写入、检索、重
新组织和修改的离散元素，且不依赖于模型参数。
由于这些单元是显式的，因此基于 token 的记忆通常具有透明性，易于编辑和解释，使其成为检索、路
由、冲突处理以及与参数化记忆和潜在记忆协调的自然层级。基于 token 的记忆也是最常见的记忆形
12

Experience Graph Memory graphs with Pyramid
... different node/edge types
image chat
e.g., ExpeL, AWM, ReasoningBank
Chunk
...
e.g., Nemori, Mem0, MemOS
e.g., G-Memory, CAM, others
e.g., A-Mem, Mem0^g,
Dialogue M3-Agent, D-SMART
Multi-Layer
...
Tree docs
e.g., MemGPT, MemoryBank
...
...
Summary
...
QAs
e.g., Think-in-Memory, RMM e.g., MemTree, TME, others HiAgent, HippoRAG, SGMem
(a) Flat Memory (1D) (b) Planar Memory (2D) (c) Hierarchical (3D)
Figure 3 按拓扑复杂度和维度对token级内存的分类：(a)平面内存（1D）以线性序列或独立簇的形式存储信息，不具
有显式的单元间拓扑关系，常用于 分块集合、对话日志和 经验池。(b) 平面内存（2D）引入单层结构化布局，通过 树
或图结构连接单元，以捕捉关系依赖，支持多种结点类型，如图像和聊天记录。(c)分层内存（3D）采用多层级形式，如
金字塔或 多层图，以促进不同数据粒度间的垂直抽象和跨层推理，例如原始文档与合成问答对之间。
式，且已有大量相关研究工作。
尽管所有基于 token 的记忆都具有以离散单元形式存储的特性，但这些单元的组织方式存在显著差异。
存储的 token 的结构组织在决定智能体搜索、更新或推理过往信息的效率方面起着核心作用。为了描述
这些差异，我们根据单元间的结构组织对基于 token 的记忆进行分类，从无显式拓扑结构到多层拓扑结
构：
Three Major Types of Token-level Memory
1. 平面内存（1D）：无显式的单元间拓扑结构。内存被累积为单元的序列或集合（例如，片段、
轨迹、块）
2. 平面记忆（2D）：在一个平面内的结构化但单层的组织形式：单元通过图、树、表等关系相互
关联，且不存在跨层关系。结构是显式的，但并非分层的。
3. 分层内存（3D）：跨多层结构化，具有层间连接，形成体积分层记忆
Figure 3 中清晰地展示了三种类型的 token 级别记忆。从无拓扑结构的扁平记忆，到具有单层结构组织
的平面记忆，再到具有多层互联结构的分层记忆，这种组织谱系不仅决定了 token 级别记忆如何支持搜
索、更新和推理，也决定了记忆本身的结构以及其所具备的能力。在接下来的小节中，我们将分别介绍
每种组织形式的优势与局限、典型应用场景以及代表性工作。代表性 token 级别记忆方法的总结与比较
如 Table 1 所示。
13

| Experience
...
e.g., ExpeL, AWM, ReasoningBank
Chunk
...
e.g., Nemori, Mem0, MemOS
Dialogue
...
e.g., MemGPT, MemoryBank
Summary
...
e.g., Think-in-Memory, RMM
(a) Flat Memory (1D) | Graph Memory graphs with
different node/edge types
image chat
e.g., A-Mem, Mem0^g,
M3-Agent, D-SMART
Tree
e.g., MemTree, TME, others
(b) Planar Memory (2D) | Pyramid
e.g., G-Memory, CAM, others
Multi-Layer
docs
...
...
QAs
HiAgent, HippoRAG, SGMem
(c) Hierarchical (3D) |
|---|---|---|

值得注意的是，遵循ReAct(Yaoetal.,2023b)提出的思想，一系列研究开始关注长时程交互任务(Song
et al., 2025a; Jin et al., 2025; Li et al., 2025g,e,i; Wu et al., 2025b)。这些任务中的许多都引入了显式
的记忆概念，由于记忆通常以明文形式存储，因此它们属于 token 级记忆的范畴。其中大多数研究强调
如何压缩或折叠累积的交互迹，以便智能体能够在不超出上下文限制的情况下处理长序列 (Zhou et al.,
2025b; Zhang et al., 2025q; Wu et al., 2025f; Sun et al., 2025a; Li et al., 2025h; Chen et al., 2025a)。关
于工作记忆的更详细讨论见Section 4.3。
3.1.1 平面内存（一维）
Definition of Flat (1D) Memory
扁平记忆将信息存储为离散单元的累积，未显式建模这些单元之间的语义或关系依赖。这些单元可
能包括文本片段、用户画像、经验轨迹、其对应的向量表示或多模态条目。这些单元之间的关系并
未直接编码在记忆中。
为了便于清晰连贯地呈现，我们根据平坦内存相关研究的主要设计目标和技术重点对其进行分类。这种
分类方式具有组织性目的，并不意味着由此产生的类别彼此严格平行或互不重叠。实际上，某些方法可
能适用于多个类别，而涉及多模态信息的一些方法在其他章节中讨论时，即使多模态并非其核心关注
点，也可能被提及。这种组织方式使我们能够系统性地回顾文献，同时保持解释上的灵活性。
Table 1 代表性token级记忆方法的比较。我们根据拓扑复杂度将现有工作分为三类：扁平记忆（1D）用于线性或独立
记录，平面记忆（2D）用于结构化单层图/树，以及分层记忆（3D）用于多层级架构。方法在四个维度上进行表征：(1)
多模态表示多模态能力，其中✔ 表示支持文本以外的模态（如视觉），✗ 表示仅支持文本；(2) 类型标识记忆的具体功能
类别（例如，Fact 表示事实记忆，Exp表示经验记忆，Work 表示工作记忆）；(3)记忆形式详细说明存储单元的内容；以
及 (4) 任务列出主要应用领域。
Method Multi Type MemoryForm Task
FlatMemoryModels
Reflexion(Shinnetal.,2023b) ✗ E&W Trajectory as short-term and feedback as QA,Reasoning,Coding
long-term
Memento(Zhouetal.,2025a) ✗ Exp Trajectorycase(success/failure). Reasoning
JARVIS-1(Wangetal.,2025p) ✔ Exp Plan-environmentpairs. Game
Expel(Zhaoetal.,2024) ✗ Exp Insightsandfew-shotexamples. Reasoning
BufferofThoughts(Yangetal.,2024b) ✗ Exp High-levelthought-templates. Game,Reasoning,Coding
SAGE(Liangetal.,2025) ✗ Exp Dual-storewithforgettingmechanism. Game,Reasoning,Coding
ChemAgent(Tangetal.,2025c) ✗ Exp Structuredsub-tasksandprinciples. Chemistry
AgentKB(Tangetal.,2025d) ✗ Exp 5-tupleexperiencenodes. Coding,Reasoning
H 2 R(Yeetal.,2025b) ✗ Exp PlanningandExecutionlayers. Game, Embodied Simula-
tion
AWM(Wangetal.,2024l) ✗ Exp Abstracteduniversalworkflows. Web
PRINCIPLES(Kimetal.,2025a) ✗ Exp Ruletemplatesfromself-play. EmotionalCompanion
ReasoningBank(Ouyangetal.,2025) ✗ Exp Transferablereasoningstrategyitems. Web
Voyager(Wangetal.,2024b) ✔ Exp Executableskillcodelibrary. Game
DGM(Zhangetal.,2025h) ✗ Exp Recursiveself-modifiablecodebase. Coding
Memp(Fangetal.,2025d) ✗ Exp Instructionsandabstractscripts. Embodied Simulation,
TravelPlanning
Continuedonnextpage
14

Table 1 代表性 token 级记忆方法的比较。我们根据拓扑复杂度将现有工作分为三类：扁平记忆（1D）用于线性或独
立记录，平面记忆（2D）用于结构化的单层图/树，以及层级记忆（3D）用于多层级架构。方法在四个维度上进行表征：
(1) 多模态表示多模态能力，其中✔ 表示支持文本以外的模态（如视觉），✗ 表示仅支持文本；(2) 类型识别记忆的具体
功能类别（例如，Fact 表示事实记忆，Exp 表示经验记忆，Work 表示工作记忆）；(3) 记忆结构详细说明存储单元的组
织机制；以及 (4) 任务列出主要应用领域。（续）
Method Multi Type MemoryStructure Task
UFO2(Zhangetal.,2025a) ✔ Exp Systemdocsandinteractionrecords. WindowsOS
LEGOMem(Hanetal.,2025a) ✗ Exp Vectorizedtasktrajectories. Oﬀice
ToolMem(Xiaoetal.,2025b) ✗ Exp Toolcapability. ToolCalling
SCM(Wangetal.,2025a) ✗ Fact Memorystreamandvectordatabase. Long-context
MemoryBank(Zhongetal.,2024) ✗ Fact Historyanduserprofile. EmotionalCompanion
MPC(Leeetal.,2023) ✗ Fact Personaandsummaryvectorpool. QA
RecMind(Wangetal.,2024h) ✗ Fact Usermetadataandexternalknowledge. Recommendation
InteRecAgent(Huangetal.,2025d) ✗ Fact Userprofilesandcandidateitem. Recommendation
Ego-LLaVA(Shenetal.,2024) ✔ Fact Language-encodedchunkembeddings. MultimodalQA
ChatHaruhi(Lietal.,2023a) ✗ Fact Dialoguedatabasefrommedia. Role-Playing
Memochat(Luetal.,2023) ✗ Fact Memosandcategorizeddialoguehistory. Long-convQA
RecursiveSum(Wangetal.,2025h) ✗ Fact Recursivesummariesofshortdialogues. Long-convQA
MemGPT(Packeretal.,2023a) ✗ Fact Virtualmemory(Main/Externalcontexts). Long-convQA,DocQA
RoleLLM(Wangetal.,2024d) ✗ Fact Role-specificQApairs. Role-Playing
Think-in-memory(Liuetal.,2023a) ✗ Fact Hashtableofinductivethoughts. Long-convQA
PLA(Yuanetal.,2025b) ✗ Fact Evolvingrecordsofhistoryandsummaries. QA,HumanFeedback
COMEDY(Chenetal.,2025c) ✗ Fact Single-modelcompressedmemoryformat. Summary, Compression,
QA
Memoro(Zulfikaretal.,2024) ✔ Fact Speech-to-textvectorembeddings. UserStudy
MemorySharing(GaoandZhang,2024a) ✗ Fact Query-Responsepairretrieval. Literary Creation, Logic,
PlanGeneration
ConvAgent(Alonsoetal.,2024) ✗ Fact Chain-of-tablesandvectorentries. QA
EM-LLM(Fountasetal.,2025) ✗ Fact EpisodiceventswithBayesianboundaries. Long-context
Memocrs(Xietal.,2024a) ✗ Fact Usermetadataandknowledge. Recommendation
SECOM(Panetal.,2025) ✗ Fact Paragraph-levelsegmentedblocks. Long-convQA
Mem0(Chhikaraetal.,2025) ✗ Fact Summaryandoriginaldialogue. Long-convQA
RMM(Tanetal.,2025c) ✗ Fact Reflection-organizedflatentries. Personalization
MEMENTO(Kwonetal.,2025) ✔ Fact Interactionhistoryentries. Personalization
MemGuide(Duetal.,2025b) ✗ Fact Dialogue-derivedQApairs. Long-convQA
MIRIX(WangandChen,2025) ✔ Fact Sixoptimizedflatmemorytypes. Long-convQA
SemanticAnchor (Chatterjee and Agar- ✗ Fact Syntactic5-tuplestructure. Long-convQA
wal,2025)
MMS(Zhangetal.,2025b) ✗ Fact DualRetrievalandContextunits. Long-convQA
Memory-R1(Yanetal.,2025b) ✗ Fact RL-managedmem0architecture. Long-convQA
ComoRAG(Wangetal.,2025f) ✗ Fact Fact/Semantic/Plotunitswithprobes. NarrativeQA
Nemori(Nanetal.,2025) ✗ Fact Predictivecalibrationstore. Long-convQA
Livia(XiandWang,2025) ✔ Fact Prunedinteractionhistory. EmotionalCompanion
MOOM(Chenetal.,2025d) ✗ Fact Decoupledplotandcharacterstores. Role-Playing
Mem-α(Wangetal.,2025o) ✗ Fact Core,Semantic,andEpisodicMem. MemoryManagement
Personalized Long term Interac- ✗ Fact Hierarchicalhistoryandsummaries. Personalization
tion(Westhäußeretal.,2025)
LightMem(Fangetal.,2025b) ✗ Fact OptimizedLong/Short-termstore. Long-convQA
MEXTRA(Wangetal.,2025b) ✗ Fact Extractedrawdialoguedata. PrivacyAttack
Continuedonnextpage
15

Table 1 代表性 token 级记忆方法的比较。我们根据拓扑复杂度将现有工作分为三类：扁平记忆（1D）用于线性或独
立记录，平面记忆（2D）用于结构化的单层图/树，以及层级记忆（3D）用于多层级架构。方法在四个维度上进行表征：
(1) 多模态表示多模态能力，其中✔ 表示支持文本以外的模态（如视觉），✗ 表示仅支持文本；(2) 类型识别记忆的具体
功能类别（例如，Fact 表示事实记忆，Exp 表示经验记忆，Work 表示工作记忆）；(3) 记忆结构详细说明存储单元的组
织机制；以及 (4) 任务列出主要应用领域。（续）
Method Multi Type MemoryStructure Task
MovieChat(Songetal.,2024) ✔ Fact Short-term features and long-term persis- VideoUnderstanding
tence.
MA-LMM(Heetal.,2024) ✔ Fact VisualandQuerymemorybanks. VideoUnderstanding
VideoAgent(Wangetal.,2024g) ✔ Fact Temporaltextdescriptionsandobjecttrack- VideoUnderstanding
ing.
KARMA(Wangetal.,2025q) ✔ Fact 3Dscenegraphanddynamicobjectstates. EmbodiedTask
EmbodiedVideoAgent(Fanetal.,2025) ✔ Fact Persistentobjectandsensorstore. MultiModal
Mem2Ego(Zhangetal.,2025l) ✔ Fact Map,landmark,andvisitedlocationstores. EmbodiedNavigation
Context-as-Memory(Yuetal.,2025b) ✔ Fact Generatedcontextframes. VideoGeneration
RCR-Router(Liuetal.,2025c) ✗ Fact Budget-awaresemanticsubsets. QA
PlanarMemoryModels
D-SMART(Leietal.,2025) ✗ Fact Structuredmemorywithreasoningtrees. Long-convQA
Reflexion(Shinnetal.,2023b) ✗ Work Reflectivetextbufferfromexperiences. QA,Reasoning,Coding
PREMem(Kimetal.,2025b) ✗ Fact Dynamiccross-sessionlinkedtriples. Long-convQA
QueryReconstruct(Xuetal.,2025b) ✗ Exp Logicgraphsbuiltfromknowledgebases. KnowledgeGraphQA
KGT(Sunetal.,2024) ✗ Fact KGnodefromqueryandfeedback. QA
Optimus-1(Lietal.,2024d) ✔ F&E Knowledgegraphandexperiencepool. Game
SALI(Panetal.,2024) ✔ Exp Topologicalgraphwithspatialnodes Navigation
HAT(Aetal.,2024) ✗ Fact Hierarchicalaggregatetree. Long-convQA
MemTree(Rezazadehetal.,2025c) ✗ Fact Dynamichierarchicalconversationtree. Long-convQA
TeaFarm(iunnOngetal.,2025) ✗ Fact Causaledgesconnectingmemories. Long-convQA
COMET(Kimetal.,2024b) ✗ Fact Context-awarememorythroughgraph. Long-convQA
IntrinsicMemory(Yuenetal.,2025) ✗ Fact Privateinternalandsharedexternalmem. Planning
A-MEM(Xuetal.,2025c) ✗ Fact Card-basedconnectedmem. Long-convQA
Ret-LLM(Modarressietal.,2023) ✗ Fact TriplettableandLSHvectors. QA
HuaTuo(Wangetal.,2023a) ✗ Fact MedicalKnowledgeGraph. MedicalQA
M3-Agent(Longetal.,2025) ✔ Fact Multimodalnodesingraphstructure. EmbodiedQA
HierarchicalMemoryModels
GraphRAG(Edgeetal.,2025) ✗ Fact Multi-levelcommunitygraphindices. QA,Summarization
H-Mem(SunandZeng,2025) ✗ Fact Decoupledindexlayersandcontentlayers. Long-convQA
EMG-RAG(Wangetal.,2024k) ✗ Fact Three-tieredmemorygraph. QA
G-Memory(Zhangetal.,2025c) ✗ Exp Query-centricthree-layergraphstructure. QA, Game, Embodied
Task
Zep(Rasmussenetal.,2025) ✗ Fact TemporalKnowledgeGraphs. Long-convQA
SGMem(Wuetal.,2025h) ✗ Fact ChunkGraphandSentenceGraph. Long-convQA
HippoRAG(Gutierrezetal.,2024) ✗ Fact Knowledgewithquerynodes. QA
HippoRAG2(Gutiérrezetal.,2025) ✗ Fact KGwithphraseandpassage. QA
AriGraph(Anokhinetal.,2024) ✗ Fact SemanticandEpisodicmemorygraph. Game
LyfeAgents(Kaiyaetal.,2023) ✗ Fact Working,Short&Long-termlayers. SocialSimulation
CAM(Lietal.,2025f) ✗ Fact Multilayergraphwithtopic. DocQA
HiAgent(Huetal.,2025a) ✗ E&W Goalgraphswithrecursivecluster. AgenticTasks
Continuedonnextpage
16

Table 1 代表性 token 级记忆方法的比较。我们根据拓扑复杂度将现有工作分为三类：扁平记忆（1D）用于线性或独
立记录，平面记忆（2D）用于结构化的单层图/树，以及层级记忆（3D）用于多层级架构。方法在四个维度上进行表征：
(1) 多模态表示多模态能力，其中✔ 表示支持文本以外的模态（如视觉），✗ 表示仅支持文本；(2) 类型识别记忆的具体
功能类别（例如，Fact 表示事实记忆，Exp 表示经验记忆，Work 表示工作记忆）；(3) 记忆结构详细说明存储单元的组
织机制；以及 (4) 任务列出主要应用领域。（续）
Method Multi Type MemoryStructure Task
ILM-TR(Tangetal.,2024) ✗ Fact HierarchicalMemorytree. Long-context
对话 一些平面内存工作专注于存储和管理对话内容。早期的方法主要通过存储原始对话历史或生成递
归摘要来扩展上下文窗口，以防止遗忘 (Wang et al., 2025a; Lu et al., 2023; Wang et al., 2025h; Yuan
et al., 2025b)。MemGPT (Packer et al., 2023a) 引入了操作系统隐喻和分层管理，启发了后续工作 (Li
et al., 2025k; Kang et al., 2025a) 将活跃上下文与外部存储解耦，实现无限上下文管理。
为提高检索准确率，记忆单元的粒度和结构变得日益多样化，并与认知过程更加契合。一些工作，如
COMEDY (Chen et al., 2025c)、Memory Sharing (Gao and Zhang, 2024a) 和 MemGuide (Du et al.,
2025b) 将信息压缩为紧凑的语义表示或查询-响应对，以促进直接查找，而另一些工作，如 Alonso et al.
(2024) 和 MIRIX (Wang and Chen, 2025) 则采用从向量-表格组合到多功能记忆类型的混合结构。此
外，研究开始基于认知心理学定义记忆边界，通过句法元组 (Chatterjee and Agarwal, 2025) 组织信息，
或根据贝叶斯意外性与段落结构对事件进行分割 (Fountas et al., 2025; Pan et al., 2025)，从而实现类
似人类的认知分段。
随着对话深度的增加，记忆逐渐演化为存储高层次认知过程与叙事复杂性的能力。不同于简单的事实
记录，像 Think-in-Memory (Liu et al., 2023a) 和 RMM (Tan et al., 2025c) 这类系统会存储归纳性思
维与回溯性反思，以指导未来的推理。在角色扮演或长篇叙事等复杂场景中，ComoRAG (Wang et al.,
2025f) 与 MOOM (Chen et al., 2025d) 等方法将记忆分解为事实、情节层级与角色层级组件，确保智能
体在长时间交互中保持连贯的人物形象与理解。
记忆已从静态存储过渡到自主与自适应最优化。Mem0(Chhikara et al., 2025) 建立了记忆维护的标准化
操作，为智能控制奠定了基础。近期进展将强化学习引入记忆构建的最优化 (Yan et al., 2025b; Wang
et al., 2025o)，同时其他机制聚焦于动态校准与效率提升，例如预测缺失信息 (Nan et al., 2025)、在多
智能体系统中管理 token 预算 (Liu et al., 2025c)，以及减少长期存储中的冗余 (Fang et al., 2025b)。
偏好 一些记忆系统专注于建模用户不断演变的偏好、兴趣和决策模式，尤其是在以理解偏好为核心推
荐场景中。与侧重于保持对话连贯性的对话中心记忆不同，偏好记忆更关注识别用户的具体品味和倾
向。早期的工作如 RecMind (Wang et al., 2024h) 通过分别存储用户的事实性属性和物品元数据，将用
户特定信息与外部领域知识相分离。InteRecAgent (Huang et al., 2025d) 将记忆融入推荐工作流，但
更侧重于当前候选物品集合，保留用户画像和活跃物品池以支持上下文感知的推荐。MR.Rec (Huang
et al., 2025b) 构建了一个记忆索引，用于归档完整的交互过程，存储原始物品信息以及按类别汇总的偏
好摘要。在对话场景中，Memocrs (Xi et al., 2024a) 提出了更为结构化的设计，包含一个针对用户的
记忆来追踪实体和用户态度，以及一个通用记忆来聚合跨用户的知识。
17

简介 一类扁平记忆系统专注于存储和维护稳定的用户资料、角色属性或长期身份信息，使智能体在多
轮对话和不同任务中能够保持行为一致性。MemoryBank (Zhong et al., 2024) 是该方向最早的框架之
一：它按时间戳组织对话历史和事件摘要，逐步构建用户资料，以支持对与身份相关的信息进行准确检
索。AI Persona (Wang et al., 2024f) 使记忆系统不仅处理对话上下文中的信息，还整合来自多维度人
机交互的信息。MPC (Lee et al., 2023) 通过将实时角色信息和对话摘要存储在记忆池中，扩展了这一
思路，确保长时间交互中对话行为与一致的角色保持一致。Westhäußer et al. (2025) 提出了一种更全面
的资料维护机制，结合长期记忆与短期记忆，并在每轮对话后自动生成摘要，形成中期上下文，使用户
资料能够通过交互持续演化。
在虚拟角色扮演情景中，ChatHaruhi (Li et al., 2023a) 从小说和电视剧剧本中提取对话，通过检索记忆
使模型能够保持角色一致的行为。RoleLLM (Wang et al., 2024d) 采用更结构化的方法，构建问答对以
捕捉角色特有的知识。
经验 与静态的通用知识不同，经验记忆源于智能体在实际交互任务中的动态积累，包括具体的观察、
思维链、动作轨迹以及环境反馈。需要指出的是，本节仅从 token 级存储的角度对经验记忆进行了简要
概述；关于该领域的更全面分析和详细讨论将在Section 4.2中呈现。
经验记忆最基础的形式涉及对历史行为轨迹的直接存档。该范式使智能体能够通过检索和重用过去的经
验实例来影响当前的决策，涵盖成功与失败的案例 (Zhou et al., 2025a; Wang et al., 2025p)。
为了应对原始轨迹固有的泛化能力有限的问题，大量研究聚焦于将特定交互抽象为更高级别的、可泛
化的经验。作为最早且最具影响力的方法之一，Reflexion (Shinn et al., 2023b) 将短期记忆定义为轨迹
历史，长期记忆则定义为自我反思模型产生的反馈。某些研究通过将复杂的交互历史压缩为通用的工
作流、规则模板或高层级的“思维模板”，以促进跨问题的迁移和复用 (Wang et al., 2024l; Kim et al.,
2025a; Yang et al., 2024b)。其他工作则强调记忆的结构化组织与动态维护。这些方法确保存储的洞察
能够适应新任务，并通过构建领域特定的结构化知识库、采用分层规划-执行记忆架构，或引入类人遗
忘与反思机制来高效更新 (Tang et al., 2025c,d; Ouyang et al., 2025; Ye et al., 2025b; Zhao et al., 2024;
Liang et al., 2025)。
在涉及编程或特定工具使用的场景中，经验记忆演化为可执行的技能。在此范式下，智能体将探索经验
整合为代码仓库、过程脚本或工具使用条目。借助环境反馈，这些系统能够迭代优化代码质量，甚至动
态修改其潜在逻辑以实现自我演化 (Wang et al., 2024a; Yin et al., 2025; Fang et al., 2025d; Xiao et al.,
2025b)。此外，针对操作系统等复杂环境，一些研究将成功的执行记录提炼为可复用的范例或向量化表
示，从而实现从离线构建到在线分配的高效流水线 (Zhang et al., 2025a; Han et al., 2025a)。
多模态 多模态记忆系统将信息以从原始多模态数据（如图像、视频帧、音频片段和文本）中提取的离
散 token 级单元形式存储，使智能体能够跨通道并跨越长时间经验捕获、压缩和检索知识。在可穿戴和
第一人称情景中，早期工作如 Ego-LLaVA (Shen et al., 2024) 会捕捉第一人称视频并将其转换为轻量
级语言描述。Memoro (Zulfikar et al., 2024) 遵循类似理念，但采用语音转文本生成基于嵌入的记忆单
元。在此方向基础上，Livia (Xi and Wang, 2025) 将长期用户记忆融入具有情感感知能力的 AR 系统
中，应用遗忘曲线和剪枝策略。
对于视频理解，重点转向将瞬时视觉线索与持久的上下文信息分离开来。MovieChat (Song et al., 2024)
采用短期/长期分离策略，存储最近帧的特征。MA-LMM (He et al., 2024) 进一步推进这一思路，采用
18

双存储库设计——一个存储原始视觉特征，另一个保留查询嵌入。VideoAgent (Wang et al., 2024g) 采
取更为语义化的组织方式，同时维护文本片段描述的时间记忆以及跟踪跨帧实体的物体级记忆。在交互
式视频生成中，Context-as-Memory (Yu et al., 2025b) 表明，仅将先前生成的帧作为记忆存储同样具有
很高的有效性。
在具身场景中，记忆与空间结构及持续的交互行为密不可分。KARMA (Wang et al., 2025q) 引入了两
级记忆系统：长期记忆将静态物体存储在三维场景图中，而短期记忆则跟踪物体的位置和状态变化。具
身视频智能体 Embodied VideoAgent (Fan et al., 2025) 也构建了持久的物体记忆，但将其与第一人称
视频及其他具身传感器信息融合。Mem2Ego (Zhang et al., 2025l) 将这一思想扩展至导航任务，通过将
全局地图、地标描述和访问历史分离为三个独立的记忆存储来实现。此外，MEMENTO (Kwon et al.,
2025) 提供了一个评估框架，将多模态交互历史视为智能体的记忆，从而能够系统性地评估具身系统如
何利用累积的感知经验。
讨论 扁平记忆的主要优势在于其简单性和可扩展性：内存可以以极低的成本进行追加或修剪，而相似
度搜索等检索方法能够实现灵活访问，无需预先定义结构。这使其适用于广泛的召回、情景式累积以及
快速变化的交互历史。然而，由于缺乏显式的关联组织，连贯性和相关性高度依赖于检索质量。随着记
忆规模的增长，冗余和噪声会不断积累，模型可能检索到相关单元却无法理解它们之间的关系，从而限
制了组合推理、长时程规划和抽象能力的形成。因此，无拓扑结构的记忆集合在覆盖范围广和轻量级更
新方面表现优异，但在需要结构化推理或稳定知识组织的任务中受到限制。
3.1.2 平面存储（2D）
Definition of Planar (2D) Memory
平面存储引入了存储单元之间的显式组织拓扑，但仅限于单一结构层内，简称 2D。该拓扑可以是
图、树、表格、隐式连接结构等，其中诸如邻接关系、父子顺序或语义分组等关系被编码在单一平
面内，不包含层级结构或跨层引用。
平面内存架构的核心在于通过建立明确的关联机制，突破单一存储池的限制，实现从单纯的“存储”到
“组织”的跃迁。
树 树形结构以层次化方式组织信息，能够处理不同抽象层次的内容。HAT (A et al., 2024) 通过分割
长序列交互并逐步聚合，构建了层次化聚合树。这种多层级结构支持粗粒度到细粒度的检索，在长上下
文问答系统中表现优于扁平向量索引。为减少对话碎片化，MemTree (Rezazadeh et al., 2025c) 引入了
一种动态表示方法，从孤立的对话日志中推断出层次化结构。它将具体的事件逐步归纳为更高层次的概
念，使智能体能够同时利用详细记忆和抽象知识。
图表 图结构在二维记忆领域占据主导地位，因其能够捕捉复杂的关联性、因果关系和时间动态。奠基
性工作如 Ret-LLM (Modarressi et al., 2023) 将外部存储抽象为可寻址的三元组单元，使大语言模型
能够与以关系为中心的表格进行交互，该表格功能类似于轻量级知识图谱。在医疗领域，华佗 (Wang
et al., 2023a) 引入专业知识，通过整合结构化的中文医学知识图谱与临床文本语料库来微调基础模型。
KGT (Sun et al., 2024) 提出一种实时个性化机制，将用户偏好与反馈编码为用户特定知识图谱中的结
19

点与边。针对推理密集型任务，PREMem (Kim et al., 2025b) 将部分推理负担转移至记忆构建阶段，从
原始对话中推导出结构化记忆项及其演化关系。类似地，增强型查询重构 (Xu et al., 2025b) 维护一个
专用的查询记忆，记录过往的知识图谱查询与推理步骤，利用检索到的记录重构更准确的查询。基于时
间线视角，TeaFarm (iunn Ong et al., 2025) 沿分段时间线组织对话历史，并应用结构化压缩以管理终
身上下文。COMET (Kim et al., 2024b) 进一步通过使用外部常识资源解析对话，并动态更新包含推断
隐藏属性的上下文感知人格图谱，从而优化对话记忆。A-Mem (Xu et al., 2025c) 将知识标准化为类卡
片单元，按相关性组织，并将相关记忆置于同一盒子中，构建完整的记忆网络。内在记忆智能体 (Yuen
et al., 2025) 采用划分式架构，其中子智能体各自维护角色特异的私有记忆，同时协同读写共享记忆。
扩展至多模态智能体，M3-Agent (Long et al., 2025) 将图像、音频与文本统一为以实体为中心的记忆图
谱。SALI (Pan et al., 2024) 构建现实—想象混合记忆，将真实观测与设想的未来场景统一为一致的导
航图谱。
混合动力 复杂任务通常需要混合架构，将不同的认知功能分离，同时共享一个共同的内存基础。Optimus-
1 (Li et al., 2024d) 显式地将静态知识分离到用于规划的分层有向知识图谱中，将动态交互分离到用于
反思和自我改进的抽象多模态经验池中。D-SMART (Lei et al., 2025) 将结构化的事实记忆（以持续更
新的知识图谱形式实现）与基于遍历的推理树相结合。
讨论 平面记忆通过有效建立结点之间的连接，使记忆能够发挥集体协同效应，从而编码更全面的上下
文知识。此外，它支持超越简单迭代的检索机制，包括结构化的键值查找以及沿图边的关系遍历。这些
能力使其在存储、组织和管理记忆方面表现出色。然而，它也面临一个关键局限：由于缺乏分层存储机
制，所有记忆必须整合为单一的、整体的模块。随着任务场景变得日益复杂和多样化，这种冗余且扁平
化的设计越来越难以维持稳健性能。更重要的是，其高昂的构建与搜索成本显著阻碍了实际部署。
3.1.3 分层内存（3D）
Definition of Hierarchical (3D) Memory
分层记忆通过多层组织信息，并利用层间连接将记忆构建成一个立体的结构化空间。
这种层次结构支持从原始观测到紧凑的事件摘要，再到更高级的主题模式等不同抽象程度的表示。跨层
连接进一步通过一个三维记忆空间使系统不仅能横向在单元间导航，还能纵向跨越抽象层级进行导航。
层次化记忆超越了简单的分层结构，旨在构建具备深层抽象能力和动态演化机制的复杂系统。这些研究
通常采用多层级图结构或受神经科学启发的机制，构建更接近人类的立体化记忆空间，使信息更加丰
富，记忆单元之间的联系也更加清晰和明确。
金字塔 该类别将记忆构建为多层金字塔结构，信息逐级抽象化组织，并以粗粒度到细粒度的方式进行
查询。HiAgent (Hu et al., 2025a) 通过以子目标为中心的分层工作记忆管理长时程任务，保留当前活
跃子目标的详细轨迹，同时将已完成的子目标压缩为高层级摘要，按需选择性检索。GraphRAG (Edge
etal.,2025)通过社区发现构建多层图索引，递归地将实体级子图聚合为社区级摘要。在聚类记忆结点思
想的基础上，Zep (Rasmussen et al., 2025) 将智能体记忆形式化为时间知识图谱，并同样执行社区划分。
ILM-TR(Tangetal.,2024)采用树状金字塔索引结合内部环机制，反复在不同抽象层级查询摘要并更新
20

短期记忆缓冲区，直至检索到的证据与生成的答案趋于稳定。为确保可控的个性化，EMG-RAG (Wang
et al., 2024k) 将可编辑记忆图划分为三个层级，其中树状类型与子类型索引（L1、L2）位于实体级记忆
图（L3）之上。在多智能体系统中，G-Memory (Zhang et al., 2025c) 使用三层图层次结构组织共享经
验，包括洞察图、查询图和交互图。该设计支持以查询为中心的遍历，可在高层级跨试验洞察与具体协
作的紧凑轨迹之间垂直移动。
多层 这些形式则更强调分层特化，将记忆组织为不同的模块或层级，专注于特定类型的信息或功能。
Lyfe Agents (Kaiya et al., 2023) 将显著的长期记录与低价值的瞬时细节分离，使系统能够维持一个紧
凑且行为重要的记忆层。H-Mem (Sun and Zeng, 2025) 显式地将长期对话记忆组织为按语义抽象程度
排序的多层级层次结构，底层存储细粒度的交互片段，高层则存储逐渐压缩的摘要。受生物启发的架构
如 HippoRAG (Gutierrez et al., 2024) 将记忆分解为一个关联索引组件（以开放知识图谱实现）和一个
潜在的段落存储，利用图层对存储内容进行多跳检索调度。其后续版本 HippoRAG 2 (Gutiérrez et al.,
2025) 将此设计扩展至非参数持续学习情景，通过更深层次的段落整合和在线大语言模型过滤丰富索引
层。AriGraph (Anokhin et al., 2024) 在统一图中按信息类型分离记忆，结合一个编码环境结构的语义
知识图谱世界模型与一个事件级组件，将具体观察结果链接回语义主干。类似地，SGMem (Wu et al.,
2025h) 在原始对话之上增加了一个句子图记忆层级，将历史表示为分块单元内的句子级图。CAM (Li
et al., 2025f) 通过逐步聚类重叠的语义图，将阅读过程本身分层，形成层次化的框架结构。
讨论 通过在层次维度与关系维度的交点处设置记忆结点，分层记忆结构使不同记忆能够相互作用并形
成多维度协同效应。这种设计有助于系统编码更加整体化且上下文更深入的知识。该结构还支持强大的
检索功能：能够实现复杂的多路径查询，这些查询可在每一层的关系网络中流动，并跨越层间抽象层级
进行传递。这种能力使系统能够以高准确率检索与任务相关的记忆，从而实现出色的任务表现。
然而，该结构的复杂性及其稠密的信息组织方式给检索效率和整体有效性带来了挑战。特别是，如何确
保所有存储的记忆始终保持语义上的意义，以及如何设计系统最优的三维布局，仍然是困难且关键的问
题。
3.2 参数化记忆
与以可见且可编辑的离散单元形式存储信息的令牌级记忆不同，参数化记忆直接将信息存储在模型的参
数中。在本节中，我们探讨将记忆嵌入可学习参数空间的方法，使模型能够在不依赖外部存储的情况下
内化并召回信息。
根据内存相对于核心模型参数的存储位置，我们区分出两种主要的参数化内存形式：
Two Major Types of Parametric Memory
1. 内部参数化记忆：编码在模型原始参数（例如，权重、偏置）中的记忆。这些方法直接调整基
础模型以融入新知识或行为。
2. 外部参数化记忆：存储在额外或辅助参数集中的记忆，例如适配器、LoRA 模块或轻量级代理
模型。这些方法通过引入新参数来承载记忆，而无需修改原始模型权重。
这一区分反映了关键的设计选择：记忆是否完全融入基础模型，还是以模块化的方式附加在模型旁边。
21

Table 2 参数记忆方法的分类体系。我们根据参数存储位置相对于核心模型的位置对现有工作进行分类：内部参数记忆
将知识直接嵌入到原始权重中，而外部参数记忆则将信息隔离在辅助参数集合中。基于训练的阶段，我们对文章进行了
二次分类。方法在三个技术维度上进行比较：(1) 类型定义了记忆的本质，(2) 任务指定了目标下游应用，以及 (3) 最优
化表示优化策略，例如 SFT、FT（微调）和 PE（提示工程）。
Method Type Task Optimization
I. Internal Parametric Memory
(a) Pre-Train Phase
TNL (Qin et al., 2024b) Working QA, Reasoning SFT
StreamingLLM (Xiao et al., 2024) Working QA, Reasoning SFT
LMLM (Zhao et al., 2025b) Factual QA, Factual Gen SFT
HierMemLM(Pouransarietal.,2025) Factual QA, Language Modeling SFT
FunctionToken(Zhangetal.,2025n) Factual Language Modeling Pretrain
(b) Mid-Train Phase
Agent-Founder (Su et al., 2025) Experiential Tool Calling, Deep Research SFT
Early Experience (Zhang et al., Experiential Tool Calling, Embodied Simulation, SFT
2025j) Reasoning, Web
(c) Post-Train Phase
Character-LM (Shao et al., 2023) Factual Role Playing SFT
CharacterGLM (Zhou et al., 2024a) Factual Role Playing SFT
SELF-PARAM (Wang et al., 2025n) Factual QA, Recommendation KL Tuning
Room (Kim et al., 2023b) Experiential Embodied Task RL
KnowledgeEditor (Cao et al., 2021) Factual QA, Fact Checking FT
Mend (Mitchell et al., 2022) Factual QA, Fact Checking, Model Editing FT
PersonalityEdit Mao et al. (2024) Factual QA, Model Editing FT, PE
APP (Ma et al., 2024) Factual QA FT
DINM (Wang et al., 2024c) Experiential QA, Detoxification FT
AlphaEdit (Fang et al., 2025c) Factual QA FT
II. External Parametric Memory
(a) Adapter-based Modules
MLP-Memory (Wei et al., 2025d) Factual QA, Classification, Textual Entail- SFT
ment
K-Adapter (Wang et al., 2021) Factual QA, Entity Typing, Classification SFT
WISE (Wang et al., 2024e) Factual QA, Hallucination Detection SFT
ELDER (Li et al., 2025d) Factual Model Editing SFT
T-Patcher (Huang et al., 2023) Factual QA FT
Lin et al. (2025) Factual QA SFT
(b) Auxiliary LM-based Modules
MAC (Tack et al., 2024) Factual QA SFT
Retroformer (Yao et al., 2024a) Experiential QA, Web Navigation RL
在接下来的各小节中，我们将针对每种形式，概述其实现方法，分析其优势与局限性，并列出代表性系
统或研究工作。Table 2 对代表性参数化记忆方法进行了综述。
22

3.2.1 内部参数记忆
内部参数记忆将下游任务所需的领域知识、个性化知识或先验信息注入模型。我们也将增强模型的长上
下文能力视为一种先验注入。记忆注入的时间点可以是预训练阶段、持续预训练阶段、训练中期或后训
练阶段。存储在内部参数中的记忆不会增加额外的参数或附加模块。
预训练 一些工作在预训练阶段引入了记忆机制，旨在解决长尾世界知识难以压缩到有限模型参数中的
问题。LMLM (Zhao et al., 2025b) 和 HierMemLM (Pouransari et al., 2025) 在预训练阶段将用于知识
检索的记忆存储于模型中，而将知识本身存储在外部知识库中。还有一些工作通过优化注意力的计算效
率，以增强长窗口记忆能力 (Xiao et al., 2024; Qin et al., 2024b,c; Dao, 2024; Shah et al., 2024)。
列车中部 在持续预训练阶段，一些工作引入了来自下游任务的可泛化经验。例如，Su et al. (2025) 和
Zhang et al. (2025j) 集成了智能体经验。一些工作在训练中期提升了大模型的长窗口性能或效率，使模
型能够在记忆增强型任务中保持更长时间的短期记忆 (Zaheer et al., 2020; Chen et al., 2024a)。
训练后 其他工作在后训练阶段引入记忆以适应下游任务。一些工作使大模型能够记住个性化的用户历
史或风格。一些工作允许大模型从过去类似任务执行的成功或失败中学习。Character-LM (Shao et al.,
2023) 和 CharacterGLM (Zhou et al., 2024a) 通过微调大模型使其具备不同的特征。在后训练阶段，
SELF-PARAM (Wang et al., 2025n) 通过 KL 散度蒸馏注入额外知识，且无需额外参数。Room (Kim
et al., 2023b) 将知识外部存储，同时内部保存经验。KnowledgeEditor (Cao et al., 2021) 修改内部参数，
旨在仅改变需要编辑的知识。MEND (Mitchell et al., 2022) 通过使用小型网络修改大模型的梯度，实
现快速知识编辑。PersonalityEdit (Mao et al., 2024) 基于心理学中的人格理论提出了一个大模型人格
编辑数据集。APP (Ma et al., 2024) 采用多种训练目标，确保知识编辑过程中相邻知识受到最小干扰。
DINM (Wang et al., 2024c) 提出了一种模型编辑方法，使模型学会拒绝此类危险请求，同时不影响其
正常功能。
讨论 内部参数的优势在于其结构简单，不会给原始模型增加额外的推理开销或部署成本。其缺点是更
新内部参数较为困难：存储新记忆需要重新训练，成本高且容易遗忘旧记忆。因此，内部参数记忆更适
用于大规模领域知识或任务先验的存储，而非短期个性化的记忆或工作记忆。
3.2.2 外部参数记忆
将记忆以 token 形式存储在大模型之外，会导致模型在输入窗口中对 token 形式记忆内容的理解不足。
同时，将记忆存储在大模型的参数中也存在一些问题，例如难以更新，并且与预训练知识产生冲突。一
些研究采用折衷方案，通过外部参数引入记忆，而不改变大模型原有的参数。
适配器 一种常见的外部参数化记忆方法依赖于附加在冻结的基模型上的模块。MLP-Memory (Wei
etal.,2025d)通过多层感知机（MLP）将RAG知识与Transformer解码器进行整合。K-Adapter(Wang
et al., 2021) 通过训练特定任务的适配器模块注入新知识，同时保持原始骨干网络不变，从而在不干扰
预训练表示的情况下实现持续的知识扩展。WISE (Wang et al., 2024e) 进一步引入了双参数记忆设置
——将预训练知识与编辑后的知识分离，并采用路由机制，在推理时动态选择使用哪个参数记忆，从
而缓解终身编辑过程中的冲突问题。ELDER (Li et al., 2025d) 在此方向上进一步推进，通过维护多个
23

Input
Query LLM Layer-wise
Forward transformer
forward
Inspection
Closer
(a) Generate
Latent Emb.
Auxiliary Models
SLM, LoRA,
Decoder heads
LLM Internal Interfere /
Calculation augment
Output
KV cache/
Intermediate ment
Embeddings aug
Token Token Token
Selection MergeProjection
(b) Resue (c) Transform
Figure 4 大型语言模型智能体中潜在记忆的整合概述。与显式文本存储不同，潜在记忆在模型内部表示空间中运行。该
框架根据潜在状态的来源进行分类：(a) 生成，其中辅助模型合成嵌入以干扰或增强大语言模型的前向传播；(b) 重用，
直接传播先前的计算状态，如键值缓存或中间嵌入；(c)变换，通过token选择、合并或投影压缩内部状态，以保持高效
的上下文。
LoRA 模块并学习一个路由函数，根据输入语义自适应地选择或融合这些模块，提升了长期编辑场景下
的鲁棒性与可扩展性。总体而言，这些方法利用额外的参数子空间以模块化且可逆的方式存储和检索记
忆，避免了直接修改核心模型权重所带来的灾难性干扰风险。
辅助语言模型 除了基于适配器的存储之外，另一类工作采用了一种更具架构解耦的外部参数化记忆形
式，其中记忆存储在独立的模型或外部知识模块中。MAC (Tack et al., 2024) 通过一个摊销网络将新文
档的信息压缩为一种紧凑的调制，并将其存储在内存库中。Retroformer (Yao et al., 2024a) 提出了一个
用于记忆过去任务执行中成功或失败经验的学习范式。
讨论 这种外部参数化记忆方法在模型的适应性与稳定性之间取得了平衡。由于记忆被编码到额外的参
数模块中，因此可以在不干扰基础模型预训练表示空间的情况下，进行添加、移除或替换。这支持模块
化更新、任务特定的个性化以及可控回滚，同时避免了全模型微调可能引发的灾难性遗忘或全局权重失
真问题。
然而，这种方法也存在局限性。外部参数模块仍需与模型内部的表示流程进行整合，这意味着它们的影
响是间接的，并通过模型的注意力和计算路径来传递。因此，记忆注入的效果取决于外部参数与内部参
数化知识接口的兼容程度。
24

3.3 潜在记忆
Definition of Latent Memory
潜在记忆指的是模型内部表示（例如，键值缓存、活性值、隐状态、潜在嵌入）中隐式携带的记忆，
而不是以显式的、人类可读的 token 或专用参数集的形式存储。
潜在表示避免以明文形式暴露内存，引入的实际推理延迟较低，同时通过在模型自身的表示空间中保留
细粒度的上下文信号，可能带来更好的性能提升。
如图Figure 4所示，我们根据潜在记忆的来源对先验工作进行组织，这意味着潜在状态是如何形成并引
入智能体的。本部分的工作总结如Table 3所示。
Three Major Types of Latent Memory
1. 生成: 潜在记忆由独立的模型或模块生成，随后作为可重用的内部表示提供给智能体。
2. 复用: 潜在记忆直接从先前的计算中继承，最显著的是键值缓存复用（在回合内或跨回合之
间），以及传播隐状态的循环或有状态控制器。
3. 变换: 现有的潜在状态被变换为新的表示（例如，蒸馏、池化或压缩），以便智能体能够在降
低延迟和上下文占用的同时保留关键信息。
3.3.1 生成
一种主要的研究方向通过生成新的潜在表示来构建记忆，而非复用或变换现有的活性值。在此范式中，
模型或辅助编码器创建紧凑的连续状态。这些状态可能以序列中的特殊 token 形式出现，或作为独立
向量存在。它们总结了长上下文、任务轨迹或多模态输入中的关键信息。生成的潜在摘要随后被存储、
插入，或用作后续推理或决策的条件。这使得系统能够突破其原生上下文长度限制，保持与任务相关的
中间状态，并在不重新访问原始输入的情况下跨回合保留知识。尽管不同研究中的具体形式各异，但其
潜在思想保持一致：记忆是通过学成的编码或压缩显式生成的，所产生的潜在状态作为可重用的记忆单
元，支持未来的推断。
这种设计选择也可能与参数化记忆产生潜在分歧，特别是因为许多方法依赖于独立训练的模型来生成潜
在表示。然而，在本章中，我们的分类是基于记忆的形式，而非学习机制。关键在于，尽管这些方法通
过学成编码生成记忆，但所产生的潜在表示被显式实例化并作为独立的记忆单元重复使用，而不是直接
嵌入到模型的参数或前向传播活性值中。在详细讨论具体方法时，我们将再次回到这一区别。
单模态 在单模态情景下，一大类方法聚焦于长上下文处理和语言模型化，其中模型生成一组少量的内
部表示来替代长原始输入 (Mu et al., 2023; Luo et al., 2024; Xu et al., 2025d; Chevalier et al., 2023;
Qian et al., 2025; Wang et al., 2024j, 2025m)。一种典型策略是将长序列压缩为少量内部 token 或连续
向量，这些表示可在后续推理过程中重复使用。例如，Gist (Mu et al., 2023) 训练语言模型在处理长提
示后生成一组概要 token。Luo et al. (2024) 在每个块边界引入一个特殊的哨兵 token，并鼓励模型将局
部语义聚合到该 token 中。SoftCoT (Xu et al., 2025d) 采用类似方向，从最后一个隐状态生成特定实
例的软 token。CARE (Choi et al., 2025) 进一步扩展了潜在 token，通过训练一个上下文评估器，将检
25

Table 3 潜在记忆方法的分类体系。我们根据潜在状态的 origin 对现有工作进行分类：Generate 通过辅助模块生成记
忆，Reuse 传播内部计算状态，Transform 对现有的潜在状态进行压缩、修改或重构。方法在三个技术维度上进行比较：
(1) Form 指定潜在记忆的具体数据类型，(2) Type 定义记录内容的性质（例如，工作型、事实型和经验型），(3) Task
表示目标下游应用。
Method Form Type Task
I.Generate
(a)SingleModal
Gist(Muetal.,2023) GistTokens Working Long-contextCompression
TakingaDeepBreath(Luoetal.,2024) SentinelTokens Working Long-contextQA
SoftCoT(Xuetal.,2025d) SoftTokens Working Reasoning
CARE(Choietal.,2025) MemoryTokens Working QA,FactChecking
AutoCompressor(Chevalieretal.,2023) SummaryVectors Working QA,Compression
MemoRAG(Qianetal.,2025) GlobalSemanticStates Working QA,Summary
MemoryLLM(Wangetal.,2024j) PersistentTokens Factual Long-convQA,ModelEditing
M+(Wangetal.,2025m) Cross-layerTokenPools Factual QA
LM2(Kangetal.,2025b) MatrixSlots Working QA,Reasoning
Titans(Behrouzetal.,2025b) NeuralWeights(MLP) Working QA,LanguageModeling
MemGen(Zhangetal.,2025d) LoRAFragments Working,Exp. QA,Math,Code,EmbodiedTask,Reasoning
EMU(Naetal.,2024) Embeddingsw/Returns Factual Game
TokMem(Wuetal.,2025j) MemoryTokens Exp. Funcationcalling
NestedLearning(Behrouzetal.,2025a) NestedOptimization Factual LanguageModeling
(b)Multi-Modal
CoMem(Wuetal.,2025d) MultimodalEmbeddings Factual MultimodalQA
ACM(Wuetal.,2025e) TrajectoryEmbeddings Working Web
Time-VLM(Zhongetal.,2025) PatchEmbeddings Working VideoUnderstanding
MemAugmentedRL (Mezghanietal.,2022) NoveltyStateEncoder Working VisualNavigation
MemoryVLA(Shietal.,2025a) PerceptualStates Factual,Working EmbodiedTask
XMem(ChengandSchwing,2022) Key-ValueEmbeddings Working VideoSegmentation
II.Reuse
MemorizingTransformers(Wuetal.,2022) ExternalKVCache Working LanguageModeling
SirLLM(Yaoetal.,2024b) Entropy-selectedKV Factual Long-convQA
Memory3(Yangetal.,2024a) CriticalKVPairs Factual QA
FOT(Tworkowskietal.,2023) Memory-AttentionKV Working QA,Few-shotlearning,LanguageModeling
LONGMEM(Wangetal.,2023b) ResidualSideNetKV Working LanguageModelingandUnderstanding
III.Transform
Scissorhands(Liuetal.,2023b) PrunedKV Working Imageclassification&generation
SnapKV(Lietal.,2024b) AggregatedPrefixKV Working LanguageModeling
PyramidKV(Caietal.,2024) Layer-wiseBudget Working LanguageModeling
RazorAttention(Tangetal.,2025a) CompensatedWindow Working LanguageModeling
H2O(Zhangetal.,2023) HeavyHitterTokens Working QA,LanguageModeling
索到的 RAG 文档压缩为紧凑的记忆 token。
诸如 AutoCompressor (Chevalier et al., 2023) 和 MemoRAG (Qian et al., 2025) 的工作强调向量化或独
立的潜在表示。AutoCompressor (Chevalier et al., 2023) 将整个长文档编码为少量摘要向量，作为软提
示，而 MemoRAG (Qian et al., 2025) 则利用大语言模型生成紧凑的隐藏状态记忆，以捕捉全局语义结
构。这些方法不仅抽象出原始文本，还将检索到或上下文化的信息变换为新的潜在记忆单元，优化其复
用性。为了支持更持久的记忆，MemoryLLM (Wang et al., 2024j) 在模型的潜在空间中嵌入一组专用
的记忆 token。M+ (Wang et al., 2025m) 将这一思想扩展为跨层的长期记忆架构。LM2 (Kang et al.,
2025b) 则沿着相关但结构不同的方向，将矩阵形状的潜在记忆槽引入每一层。
另一类工作将潜在记忆的生成内化到模型的参数动态中。尽管这些工作依赖于参数化模块，其操作记忆
单元仍为潜在表示，因此明确归属于此类。Titans (Behrouz et al., 2025b) 将长程信息压缩为在线更新
的 MLP 权重，在推理过程中生成潜在向量。MemGen (Zhang et al., 2025d) 在解码过程中动态生成潜
在记忆：两个 LoRA 适配器决定插入记忆片段的位置以及插入的潜在内容。EMU (Na et al., 2024) 训
练一个状态编码器以生成带有总回报和可取性的潜在嵌入。
26

多模态 在多模态情景下，生成式潜在记忆扩展至图像、音频和视频，将其编码为紧凑的潜在表示。
CoMem (Wu et al., 2025d) 使用视觉语言模型（VLM）将多模态知识压缩为一组嵌入，作为即插即用
的记忆。类似地，Wu et al. (2025e) 将整个 GUI 交互轨迹压缩为固定长度的嵌入，并将其注入到 VLM
的输入空间中。对于时序建模，Time-VLM (Zhong et al., 2025) 将视频或交互流划分为多个块，为每个
块生成一个潜在嵌入。
在基于视觉的导航中，Mezghani et al. (2022) 学习一个状态编码器，将视觉观测映射到潜在空间，并构
建仅包含新观测的场景记忆。MemoryVLA (Shi et al., 2025a) 维护一个感知-认知记忆库，存储感知细
节和高层语义作为 Transformer 隐状态。在长视频目标分割中，XMem(Cheng and Schwing, 2022) 将
每一帧编码为键-值潜在嵌入，并将其组织成包含感知、工作和长期组件的多级记忆。
讨论 这些单模态和多模态方法共享相同的基本原理：首先生成紧凑的潜在表示，然后将其作为记忆条
目进行维护和检索。该模型能够主动构建针对任务的高度信息密集型表示，以极低的存储成本捕捉关键
动态、长距离依赖关系或跨模态关系。同时，它避免了反复处理完整上下文，从而在长时间交互中实现
更高效的推理。
然而，其缺点同样明显。生成过程本身可能会引入信息损失或偏差，状态在多次读写周期中可能发生漂
移或累积误差。此外，训练一个专用模块来生成潜在表示会带来额外的计算开销、数据需求以及工程复
杂性。
3.3.2 重复使用
与生成新潜在表示的方法不同，另一类工作直接复用模型内部的激活值，主要是键-值（KV）缓存，作
为潜在记忆。这些方法不转换（修改、压缩）存储的 KV 对，而是将前向传播中的原始激活值视为可重
用的记忆条目。主要挑战在于确定保留哪些 KV 对，如何对其进行索引，以及在长上下文或持续处理需
求下如何高效地检索它们。
从认知视角来看，Gershman et al. (2025) 通过将生物记忆框架为键–值系统，提供了概念基础，其
中键作为检索地址，值编码存储内容——这一抽象与现代大模型中的基于键值的记忆机制高度一致。
Memorizing Transformers (Wu et al., 2022) 在推理过程中显式存储过去的键值对，并通过最近邻搜索
（KNN）进行检索。FOT (Tworkowski et al., 2023) 在此基础上进一步拓展，引入了记忆注意力层，在
推理期间对额外的键值记忆执行基于 KNN 的检索。LONGMEM (Wang et al., 2023b) 也以类似方式
增强长程检索能力，采用轻量级残差侧网（SideNet），将历史键值嵌入视为持久的记忆存储。这些系统
展示了如何通过有检索意识的方式组织潜在的键值状态，从而显著提升对远距离信息的访问能力。
讨论 重用型潜在记忆方法突显了直接利用模型自身内部活性值作为记忆的有效性，表明经过精心整理
的键值（KV）表示可作为长程检索与推理的强大且高效的基底。
它们最大的优势在于能够保持模型内部激活值的完整保真度，确保在剪枝或压缩过程中不会丢失任何信
息。这使得它们在概念上简单明了，易于集成到现有架构中，并且对模型的原始计算具有高度忠实性。
然而，原始的键值缓存会随着上下文长度的增加而迅速增长，导致内存消耗上升，可能使检索效率降低。
因此，重用的有效性在很大程度上取决于索引策略。
27

3.3.3 变换
变换型潜在记忆方法专注于修改、压缩或重构现有的潜在状态，而非生成全新的潜在状态或直接重用原
始的 KV 缓存。这些方法将 KV 缓存和隐藏激活值视为可塑的记忆单元，通过选择、聚合或结构变换
对其进行重塑。由此，它们在生成型与重用型记忆之间占据了一个概念上的中间位置：模型并未创建全
新的潜在表示，但其行为也远不止于简单地重放存储的 KV 对。
一项主要的研究方向专注于在保持语义重要性的同时压缩 KV 缓存。一些方法通过仅保留最具影响
力的 token 来降低内存使用量。Scissorhands (Liu et al., 2023b) 在缓存容量超出时根据注意力得分
剪枝 token，而 SnapKV (Li et al., 2024b) 则通过头级别的投票机制聚合高重要性前缀的 KV 表示。
PyramidKV (Cai et al., 2024) 在各层之间重新分配 KV 预算。SirLLM (Yao et al., 2024b) 在此基础上
进一步提出，利用基于 token 熵的准则估计 token 重要性，并仅选择性地保留具有信息量的 KV 条目。
3
Memory (Yang et al., 2024a) 仅存储最关键的注意力键值对，显著缩小了存储需求。RazorAttention
(Tang et al., 2025a) 引入了更明确的压缩方案：它计算每个头的有效注意力跨度，仅保留有限的局部窗
口，并使用补偿 token 来保留被丢弃条目的信息。从更注重效率的角度出发，H2O (Zhang et al., 2023)
采用更简单的淘汰策略，仅保留最近的 token 以及特殊的 H2 token 以减少内存占用。
讨论 这些方法展示了潜在记忆如何通过选择、检索增强或压缩重编码，变换为更有效的记忆表示，从
而使大模型能够在不依赖原始缓存重用的情况下，扩展可用上下文长度并提升推理性能。
其主要优势在于生成更紧凑且信息稠密的内存表示，从而降低存储成本，并实现对长上下文的高效检
索。通过重塑潜在状态，这些方法使模型能够访问经过提炼的语义信号，这些信号可能比原始活性值更
有用。然而，变换过程会带来信息丢失的风险，且压缩后的状态相较于直接复用的键值缓存，更难解释
或验证。此外，剪枝、聚合或重新编码所需的额外计算也增加了系统的复杂性。
3.4 适应
如上所示，如此大量的研究聚焦于智能体记忆，清楚地表明记忆机制对智能体系统至关重要 (Zhang
et al., 2025r)。智能体系统中记忆类型的选取反映了设计者期望智能体在特定任务中如何表现。设计者
不仅仅要求智能体记住某些信息，还隐含地表达了希望这些信息如何塑造智能体的行为。因此，为特定
任务选择合适类型的记忆远非简单的组合选择。
在本节中，我们从每种记忆类型的特征出发，讨论在理想情景下它们最适合的任务和应用场景，如 Fig-
ure 5 所示。我们希望这一讨论能为实际选择提供有益的思路和指导。这些例子仅展示了在这些理想化
情景中记忆的一种可能形式，并不意味着其他记忆类型在相同情景下缺乏独特优势。
Token 级记忆 token 级别的记忆保持符号性、可寻址性和透明性，使其特别适合需要明确推理、可控
性和可问责性的场景。这种记忆在实时、高频更新的设置中表现优异，其中智能体必须持续跟踪并修正
信息，且知识本身具有清晰的结构，能够被显式建模。其外部化特性使得记忆可以轻松地被检查、审计、
转移或修改，因此特别适用于需要精确添加、删除或更新操作的领域。高度的可解释性进一步确保了智
能体的决策过程可以追溯到具体的记忆单元，这是高风险应用中的关键属性。此外，token 级别的记忆
提供了长期稳定性，避免了灾难性遗忘，使智能体能够在较长的时间范围内积累可靠的知識。另一个实
际优势是，token 级别的记忆通常以即插即用模块的形式实现，能够方便地集成到最新的闭源或开源基
础模型中，而无需修改其内部参数。
28

Token-level Parametric Latent
Memory Memory Memory
Features: Features:
Features:
- Implicit, abstract, and generalizable - Implicit, human-unreadable
- Symbolic, addressable, transparent
- Swift adding/deleting/updating - Slower memory update - Trade-off between efficiency/flexibility
- (Typically) better performance gain - Convenient modality fusion
- More severe catastrophic forgetting - Machine-native and token-efficient
Suitable Applications:
Suitable Applications: Suitable Applications:
Multi-turn chatbot
Role-playing Multimodal memory
Personalized agents
Reasoning-intensive task
On-device or edge delopy
Recommender system
Tasks that require
High-stake domains Low-resource or small-data
fundamentally new
(law, finance, medical) setting
capabilities
Figure5 大语言模型智能体的三种互补记忆范式概述。在表示形式、更新动态、可解释性和效率方面，token级记忆、参
数化记忆和潜在记忆存在差异，从而在长周期和交互式智能体系统中展现出不同的优势、局限性及应用领域。
可能的情况：
• 聊天机器人与多轮对话系统。 (Zhong et al., 2024; Lu et al., 2023; Chhikara et al., 2025)
• 长时程或终身智能体需要稳定的记忆。 (Wang et al., 2024f; Westhäußer et al., 2025)
• 用户特定的个性化配置文件。 (Wang et al., 2024f; Lee et al., 2023)
• 推荐系统。 (Wang et al., 2024h; Huang et al., 2025d; Xi et al., 2024a)
• 企业或组织的知识库。
• 法律、合规及其他需要可验证来源的高风险领域。
参数化记忆 与符号记忆相比，参数化记忆具有隐式性、抽象性和泛化能力，使其天然适用于需要概念
理解与广泛模式归纳的任务。当智能体必须依赖跨多样化情境的通用知识或规则时，其效果尤为显著，
因为这类规律可被内化为分布式表示，而无需显式地进行外部查找。这种内化支持流畅推理与端到端处
理，使模型能够系统性地泛化至未见过的任务或问题变体。因此，参数化记忆更契合那些要求结构洞察
力、强抽象能力以及深层内化的行为或风格模式的任务。
可能的情况：
• 角色扮演或与人物设定一致的行为。 (Shao et al., 2023; Zhou et al., 2024a)
• 数学推理、编码、游戏和结构化问题解决。
• 人类对齐与规范行为先验。
• 风格化、专业或领域专家级的回应。
29

潜在记忆 与基于 token 或参数的记忆不同，潜在记忆介于显式数据与固定模型权重之间，实现了灵活
性与效率的独特平衡。其低可读性提供了内在的隐私保护，使潜在表示适用于敏感信息处理。同时，其
高表达能力允许以最小的信息损失实现丰富的语义编码，使智能体能够捕捉跨模态或跨任务的细微相关
性。潜在记忆还支持高效的推理阶段检索与整合，使智能体能够注入大量紧凑的知识。因此，这种记忆
类型更注重性能与可扩展性而非可解释性，实现了高知识密度和理想的压缩效果，特别适用于资源受限
或高度动态的环境。
可能的情况：
• 多模态或完全集成的智能体架构。(Shi et al., 2025a; Cheng and Schwing, 2022; Wu et al., 2025d)
• 设备端或边缘部署环境以及云服务环境。
• 加密或隐私敏感的应用领域。
4 功能：为什么智能体需要记忆？
从大型语言模型作为通用的、无状态的文本处理工具，向自主的、目标导向的智能体转变，不仅仅是一
个渐进的步骤，而是一次根本性的范式转移。这一转变揭示了无状态性的关键局限性。根据定义，智能
体必须能够持续存在、适应变化，并在时间上保持连贯的交互。实现这一点不仅依赖于大的上下文窗口，
更根本地依赖于记忆的能力。本节探讨智能体记忆的功能，或基本目的，优先关注为何其至关重要的问
题，而非如何实现。我们认为，智能体记忆并非一个单一的整体组件，而是由一系列不同的功能能力构
成，每一项功能都服务于特定的目标，以实现持久且智能的行为。
为了进行系统性分析，本节围绕记忆的“为何”问题构建了一个功能分类体系，该体系直接映射到智能
体的核心需求。在最高层级上，我们区分了两种时间类别：长期记忆，作为跨会话的持久存储，用于积
累的知识；以及 短期记忆，作为会话内的瞬时工作空间，用于活跃推理。这一高层的时间划分进一步细
化为三个主要的功能支柱，构成了我们分析的结构。该分类体系的概览见 Figure 6。
Three Primary Memory Functions
1. 事实记忆 (Section 4.1)：智能体的陈述性知识库，通过回忆明确的事实、用户偏好和环境状态，
以确保一致性、连贯性和适应性。该系统回答的问题是：“智能体知道什么？”
2. 经验记忆 (Section 4.2)：智能体通过抽象过往轨迹、失败与成功而积累的程序性与策略性知
识，旨在实现持续学习与自我演化。该系统回答的问题是：“智能体如何改进？”
3. 工作记忆 (Section 4.3)：智能体在单个任务或会话期间用于主动上下文管理的容量有限、动态
控制的临时工作区。该系统回答的问题是：“智能体现在正在思考什么？”
这三种记忆系统并非孤立存在，而是构成一个动态、相互关联的架构，定义了智能体的认知环。该循环
始于编码，在此过程中，智能体交互的结果（如新获取的事实或计划失败的后果）通过总结、反思或抽
象被整合进长期记忆。随后在工作记忆中发生处理，工作记忆作为即时推理的主动工作区。为支持这一
推理过程，系统依赖检索，从持久的事实与经验记忆存储中提取相关上下文和技能以填充工作区。这一
编码-处理-检索序列构成了核心的架构模式，使智能体能够同时从过去的学习中获益并在当下进行推理。
30

(a) Long-term Memory
User
Dialogue Coherence Goal Consistency
factual memory
Factual MemoryBank, Livia, TiM, RMM, RecurrentGPT, A-Mem,
Section 4.1.1 Comedy, mem0, MemOS, etc. H-Mem, M3-agent, etc.
Memory
Environment
Knowledge Persistence Share Memory Access
factual memory
Section 4.1 HippoRAG, MemTree, LMLM MetaGPT, Memory Sharing,
Section 4.1.2 MemoryLLM, M+, WISE, etc. GameGPT, G-Memory, etc.
Case-based Solutions Trajectories
Section 4.2.1 MapCoder, Synapse, Expel, Momento, MemGen
Fincon, etc. JARVIAS-1, Early Experience, etc.
Experiential
Memory Strategy-based Insights Workflows Patterns
H2R, Reasoning
Section 4.2.2 -Bank, ACE etc. AgentKB, AWM, etc. RecMind, BoT, etc.
Section 4.2
Skill-based Functions Codebase MCP/API
Section 4.2.3 LEGOMem, Memp, DGM, HGM, Voyager, Alita, Alita-G,Gorilla
SkillWeaver, etc. Live-SWE-Agent, etc. COLT, ToolGen, etc.
(b) Short-term Memory
Single Input Condensation Observation Abstraction
turn LongLLMLingua, ICAE, HyCo2 Synapse, Context-as-memory,
Working Sec 4.3.1 AutoCompressots, etc. VideoAgent, M3-Agent, MA-LLM, etc.
Memory
State Hierachical Cognitive
Multi Consolidation Folding Planning
Section 4.3 turn Mem1, IterResearch, Context-folding, Agent- PRIME, Agent-S,
Sec 4.3.2 MemSearcher, ReSum,etc. Fold, DeepAgent, etc. KARMA, SayPlan, etc.
Figure 6 智能体记忆的功能分类。我们根据记忆能力的功能（目的）将其组织为跨越两个时间域的三大支柱：(1) 事实
记忆作为持久的陈述性知识库，以确保交互的一致性、连贯性和适应性；(2)经验记忆包含程序性知识，以实现跨回合的
持续学习和自我演化；以及 (3) 工作记忆提供对瞬时上下文进行主动管理的机制。
4.1 事实记忆
事实记忆指的是智能体存储和检索关于过去事件、用户特定信息以及外部环境状态的显式、声明性事实
的能力。这些信息涵盖广泛的内容，包括对话历史、用户偏好以及外部世界的相关属性。通过使智能体
在解释当前输入时能够利用历史信息，事实记忆成为上下文感知、个性化响应和扩展任务规划的基础。
为了理解智能体记忆的结构组成，我们借鉴了认知科学中的陈述性记忆 (Riedel and Blokland, 2015) 框
架。在神经科学中，陈述性记忆指可被有意识访问的长期信息存储，通常被分析为两个主要组成部分：
情景记忆和语义记忆 (Squire, 2004)。情景记忆存储与特定时间与空间背景相关联的个人经历事件——
即事件的什么、哪里和何时 (Tulving, 1972, 2002)。其核心特征是能够心理上重新体验过去的事件。语
义记忆则保留独立于获取具体情境的一般事实知识、概念及词汇含义 (Squire, 2004)。尽管人类大脑中
的这两种成分由统一的陈述性系统支持，但它们代表了不同抽象层次的信息。
在智能体系统中，这种生物上的区分并非被操作化为一个僵化的二元对立，而是作为一个处理的连续
统。系统通常通过将具体的交互历史记录为情景迹（episodic traces），例如对话回合、用户动作和环境
31

| (a) Long-term Memory
User
Dialogue Coherence Goal Consistency
factual memory
Factual MemoryBank, Livia, TiM, RMM, RecurrentGPT, A-Mem,
Section 4.1.1 Comedy, mem0, MemOS, etc. H-Mem, M3-agent, etc.
Memory
Environment
Knowledge Persistence Share Memory Access
factual memory
Section 4.1 HippoRAG, MemTree, LMLM MetaGPT, Memory Sharing,
Section 4.1.2 MemoryLLM, M+, WISE, etc. GameGPT, G-Memory, etc.
Case-based Solutions Trajectories
Section 4.2.1 MapCoder, Synapse, Expel, Momento, MemGen
Fincon, etc. JARVIAS-1, Early Experience, etc.
Experiential
Memory Strategy-based Insights Workflows Patterns
H2R, Reasoning
Section 4.2.2 -Bank, ACE etc. AgentKB, AWM, etc. RecMind, BoT, etc.
Section 4.2
Skill-based Functions Codebase MCP/API
Section 4.2.3 LEGOMem, Memp, DGM, HGM, Voyager, Alita, Alita-G,Gorilla
SkillWeaver, etc. Live-SWE-Agent, etc. COLT, ToolGen, etc. |
|---|
| (b) Short-term Memory
Single Input Condensation Observation Abstraction
turn LongLLMLingua, ICAE, HyCo2 Synapse, Context-as-memory,
Working Sec 4.3.1 AutoCompressots, etc. VideoAgent, M3-Agent, MA-LLM, etc.
Memory
State Hierachical Cognitive
Multi Consolidation Folding Planning
Section 4.3 turn Mem1, IterResearch, Context-folding, Agent- PRIME, Agent-S,
Sec 4.3.2 MemSearcher, ReSum,etc. Fold, DeepAgent, etc. KARMA, SayPlan, etc. |

状态 (Zhong et al., 2024; Wang et al., 2024h; Chhikara et al., 2025)，来启动这一过程。后续的处理阶段
会应用摘要 (Wang et al., 2025h; Chen et al., 2025c)、反思 (Tan et al., 2025c; Park et al., 2023; Wang
et al., 2025h)、实体抽取 (Gutierrez et al., 2024) 以及事实归纳 (Rasmussen et al., 2025)。生成的抽象
内容被存储在向量数据库 (Zhong et al., 2024)、键-值数据库或知识图谱 (Rasmussen et al., 2025; Sun
et al., 2024) 等结构中，并由去重与一致性检查的规程进行管理。通过这一序列，原始事件流逐渐转化
为可复用的语义事实库。
从功能上讲，该架构确保智能体在交互过程中表现出三个基本特性：一致性、连贯性和 适应性。
• 连贯性体现在强大的上下文感知能力上。智能体能够回忆并整合相关的交互历史，参考用户之前
的输入，并保持主题的连续性，确保回复形成逻辑连贯的对话，而非孤立的语句。
• 一致性指的是在时间上保持行为和自我呈现的稳定性。通过维持关于用户特定事实及其自身承诺
的持续内部状态，智能体能够避免矛盾和立场的任意变化。
• 适应性体现了根据存储的用户档案和历史反馈个性化行为的能力。因此，响应风格和决策过程会
逐步与用户的具体需求和特征相吻合。
为了便于阐述，我们进一步根据事实记忆所指的主要实体对其进行组织。这种以实体为中心的分类体
系，连同代表性方法及其技术设计选择，系统地总结在 Table 4 中。这一视角突出了两个核心应用领域：
Two Types of Factual Memory
• 用户事实记忆 (Section 4.1.1) 指维持人类与智能体之间交互一致性的事实，包括身份、稳定
偏好、任务约束和历史承诺。
• 环境事实记忆 (Section 4.1.2) 指的是与外部世界保持一致的事实，例如文档状态、资源可用
性以及其它智能体的能力。
4.1.1 用户事实记忆
用户事实记忆是指在不同会话和任务之间持续保留关于特定用户的可验证事实，包括身份、偏好、日常
习惯、历史承诺以及重要事件。
其主要功能是防止无状态交互中的典型失效模式，例如指代漂移、重复引出和矛盾回应，从而减少对长
时程目标的干扰 (Tan et al., 2025c; Zhong et al., 2024)。工程实践通常包括选择与压缩、结构化组织、
检索与复用以及一致性治理，旨在以有限的访问成本维持长程对话与行为连贯性。
对话连贯性 对话连贯性要求智能体在长时间内保持对话上下文、用户特定信息以及稳定的个人特征。
这确保了后续发言能够对早期披露的信息和情感线索保持敏感，而非退化为重复的澄清或不一致的回
复。为实现这一目标，现代系统通过两种互补策略来实现用户的事实记忆：启发式选择和 语义抽象。
为了高效地处理有限的上下文窗口，一种主要策略是有选择性地保留并排序交互历史。与其保留所有原
始日志，系统 (Xi and Wang, 2025; Zhong et al., 2024; Park et al., 2023; Lei et al., 2025) 会维护过去
交互的结构化存储，并根据诸如相关性、近期性、重要性或独特性等指标对条目进行排序。通过基于这
些得分进行过滤检索，高价值条目得以保留，并周期性地浓缩为更高层次的摘要，从而在不使智能体的
工作记忆过载的情况下，确保后续响应的连贯性。
32

除了简单的选择之外，高级框架还强调将原始对话片段转化为更高级语义表示的变换与抽象。Think in
Memory (Liu et al., 2023a) 和 Reflective Memory Management (Tan et al., 2025c) 等方法通过迭代更
新操作，将原始交互迹线转换为思维表示或反思。这使得智能体能够查询一个稳定的语义记忆，从而保
持后续回复在主题上的一致性，并减少重复。类似地，COMEDY (Chen et al., 2025c) 使用单一语言模
型生成、压缩并重用记忆，同时更新紧凑的用户画像。这些方法通过将记忆存储与原始 token 表面形式
解耦，有效稳定了长对话历史中人格和偏好的表达。
目标一致性 目标一致性要求智能体在时间推移过程中持续维护并优化明确的任务表示。这确保了澄清
性提问、信息请求和动作始终严格与主要目标保持一致，从而最大限度地减少意图漂移。
为了缓解这种漂移，系统利用事实记忆来动态跟踪并更新任务状态。像 RecurrentGPT (Zhou et al.,
2023b)、Memolet (Yen and Zhao, 2024) 和 MemGuide (Du et al., 2025b) 这类方法会保留已确认的信
息，同时突出未解决的元素。通过根据任务意图引导检索，这些方法有助于智能体满足缺失的约束，并
在会话间保持专注。
对于复杂的、长时程的任务，记忆形式通常为结构化，以促进围绕当前目标的局部检索 (Wu et al.,
2025h)。例如，A-Mem (Xu et al., 2025c) 将记忆组织为相互连接的笔记图谱，而 H-Mem (Limbacher
and Legenstein, 2020) 则采用关联机制，在后续步骤依赖于先验观察时，回忆相关的前置事实。
在具身场景中，事实记忆将智能体的行为建立在用户特定习惯和环境上下文的基础上。如M3-Agent(Long
etal.,2025)和MEMENTO(Kwonetal.,2025)等系统会持久化保存家庭成员信息、物品位置以及日常
惯例，复用这些信息以减少冗余的探索和重复指令。类似地，Encode-Store-Retrieve (Shen et al., 2024)
将自我中心视觉流处理为可文本访问的条目，使智能体能够基于过去的视觉经验回答问题，而无需用户
重复说明。
概要 这些机制共同将短暂的交互迹线转化为持久的认知基础。通过结合基于检索的排序与生成式抽
象，用户事实记忆使系统从简单的相似度匹配升级为对明确目标和约束的主动维护。这一基础带来了双
重效益：一方面，通过长期行为的一致性增强了熟悉感与信任感；另一方面，通过提高任务成功率、减
少冗余并降低错误恢复开销，显著提升了操作效率。
4.1.2 环境事实记忆
环境事实记忆涉及用户外部的实体和状态，包括长文档、代码库、工具和交互迹。
该记忆范式解决了事实召回不完整和来源不可验证的问题，减少了多智能体协作中的矛盾与冗余，并在
异构环境中稳定了长时程任务。核心目标是提供一个可更新、可检索且可管控的外部事实层，为跨会话
和阶段提供稳定的参考依据。具体而言，我们从两个互补的维度对现有实现进行分类：知识持久性和 多
智能体共享访问。
知识持久性 知识记忆指的是支持长文档分析、事实问答、多跳推理以及可靠检索代码和数据资源的持
久性世界知识和领域特定知识表示。
在知识组织方面，现有研究集中于结构化外部数据以增强推理能力。例如，HippoRAG(Gutierrezetal.,
2024) 利用知识图谱来促进证据传播，而 MemTree (Rezazadeh et al., 2025c) 则采用动态层次结构，在
不断增长的语料库中优化聚合与目标访问。关于存储形式，LMLM (Zhao et al., 2025b) 通过将事实性
33

Case-based Memory Strategy-based Memory
Store previous trajectories, solutions Transform previous experience into
strategies, templates or workflows
e.g., Momento, Agent KB, JARVIS-1,
ExpeL, MemGen, ... e.g., AWM, H2R, BrowserAgent, ACE,
Experiential SE-Agents, ReasoningBank, ...
Memory
Skill-based Memory
Hybrid Memory
Distill previous trajectories into
functions/APIs/MCPs/toolbox... Hybrid experiential memory
e.g., ExpeL, G-Memory, Memp,
e.g., SkillWeaver, Voyager, Alita,
MemEvolve, Agent KB ...
Memp, Dynamic Cheatsheet, ...
Figure 7 经验记忆范式的分类。我们根据存储知识的抽象层次对方法进行分类：(1) 基于案例的记忆保留原始轨迹和解
决方案作为具体实例；(2) 基于策略的记忆将经验抽象为高层次的策略、模板或工作流；(3) 基于技能的记忆将程序性知
识提炼为可执行函数和 API；(4) 混合记忆集成多种表示方式。这些系统共同模拟人类的程序性记忆，以实现持续学习
与自我演化。本图灵感来源于Gao et al. (2025)。
知识显式地从模型权重中解耦并外置于数据库，实现了知识的直接编辑和溯源验证，而无需重新训练。
在叙事领域，CALYPSO (Zhu et al., 2023) 将冗长的游戏上下文提炼为简洁的散文，保持了关键故事状
态的可访问性。
在需要持续知识更新的场景中，以参数为中心的方法将持久性直接集成到模型架构中。MEMORYLLM(Wang
et al., 2024j)、M+ (Wang et al., 2025m) 和 WISE (Wang et al., 2024e) 等方法引入可训练的记忆池或
侧网络，以吸收新信息。与仅依赖静态外部检索不同，这些设计聚焦于模型编辑的挑战，使智能体能够
适应动态环境，在纠正过时事实的同时保持预训练主干的稳定性。
共享访问 共享内存为多智能体协作建立了一个可见且可管理的共同事实基础，用于对齐目标、传递中
间成果，并消除重复工作。通过维护一个集中式的过去查询与响应的存储库，诸如MemorySharing(Gao
and Zhang, 2024b) 这样的框架使智能体能够异步访问并基于同伴积累的洞见进行构建。该机制确保了
个体智能体能直接从集体知识中获益，从而抑制矛盾结论的产生，并提升整体系统效率。
在复杂的项目协调中，MetaGPT (Hong et al., 2024) 和 GameGPT (Chen et al., 2023b) 等系统利用共
享消息池作为中央工作区，用于发布计划和部分结果。类似地，G-Memory (Zhang et al., 2025e) 采用
分层记忆图作为统一的协调媒介。这些架构有助于围绕当前项目状态保持一致性，从而降低通信开销，
并能够从历史协作中提取可复用的工作流。
在社会仿真领域，像 Generative Agents (Park et al., 2023) 和 S3 (Gao et al., 2023a) 这样的平台，以
及 OASIS (Yang et al., 2025) 和 AgentSociety (Piao et al., 2025) 等大规模仿真器，将全局环境和公共
交互日志建模为共享的内存基础。该基础由群体逐步更新并观察，使信息能够在智能体之间自然传播，
并支持大规模、具有历史感知能力的社会动态。
概要 环境事实记忆提供了一个可持续更新、可审计且可重复使用的外部事实层。在知识维度上，通过
结构化组织和长期记忆模块，提升了事实召回的完整性、可解释性和可编辑性。在协作维度上，通过共
享与治理机制，保持了跨智能体和跨阶段的一致性，从而在长周期、多演员及多源信息环境下实现稳健
的决策与执行。
34

4.2 体验记忆
经验记忆封装了智能体将历史轨迹、提炼出的策略以及交互结果编码为持久且可检索表示的机制。与管
理临时上下文的工作记忆不同，经验记忆专注于在不同回合之间长期积累和传递知识。
基于认知科学的理论基础，这一范式与人类的非陈述性记忆（nondeclarative memory）相呼应，特别是
程序性（procedural）和习惯（habit）系统 (Squire, 2004; Seger and Spiering, 2011)。生物系统依赖于
分布式神经回路来实现隐式技能习得 (Reber, 2013)。相比之下，智能体的经验记忆通常采用显式的数
据结构，例如向量数据库或符号日志。这种实现上的差异赋予了智能体一种生物对应物所不具备的独特
能力：能够对自己的程序性知识进行内省、编辑和推理。
关键的是，经验记忆为 持续学习和 自我演化奠定了基础，在 经验时代 (Sutton, 2025; Gao et al., 2025)。
通过维护结构化经验的存储库，智能体实现了一条非参数化的适应路径，并避免了频繁参数更新的高昂
成本。这一机制通过将交互反馈转化为可重用的知识，有效闭合了学习环。通过这一过程，智能体纠正
过去的错误，抽象出可泛化的启发式方法，并整理常规行为。因此，这种适应随着时间的推移最小化了
冗余计算并优化了决策 (Zhao et al., 2024; Shinn et al., 2023b)。
为了系统地分析现有文献，我们根据存储信息的抽象层次对经验记忆进行分类。基于抽象层次的分类体
系及代表性范式如Figure 7所示。该抽象层次分类体系下的代表性方法，以及它们的存储载体、表示形
式和最优化策略，总结于Table 5。
Three Types of Experiential Memory
• 基于案例的记忆 (Section 4.2.1) 存储经过最少处理的历史回合记录，优先保证高信息保真度，
以支持直接重放和模仿。通过保留情境与结果之间的原始对应关系，它作为具体且可验证的
证据库，为证据驱动的学习提供上下文中的范例。
• 基于策略的记忆 (Section 4.2.2) 从过往轨迹中提炼可迁移的推理模式、工作流和高层次洞察，
以指导在多样化场景中的规划。作为认知支架，它将决策逻辑与具体上下文解耦，从而提升跨
任务泛化能力，并约束复杂推理的搜索空间。
• 基于技能的记忆 (Section 4.2.3) 封装了可执行的过程性能力，从原子代码片段到标准化 API
协议不等，能够将抽象策略转化为可验证的动作。此类记忆作为智能体的主动执行基础，支持
能力的模块化扩展以及对工具使用环境的高效处理。
Table 5 经验记忆方法的分类体系。我们根据存储知识的抽象层次对现有工作进行分类：基于案例的记忆保留原始记
录以实现直接回放，基于策略的记忆提炼出用于规划的抽象启发式规则，基于技能的记忆整合可执行的能力以支持动作。
这些方法在三个技术维度上进行比较：(1) 载体 (Section 3) 确定存储介质，(2) 形式指明经验的表示格式，以及 (3) 最
优化表示集成策略，其中 PE 包含提示工程和推理时技术而无需参数更新，与基于梯度的方法如 SFT 和 RL 相区别。
Method Carrier Form Task Optimization
I.Case-basedMemory
Expel(Zhaoetal.,2024) Token-level Solution Reasoning PE
Synapse(Zhengetal.,2024a) Token-level Solution WebInteraction,Instruction-guidedWeb PE
Task
Continuedonnextpage
35

Table 5 经验记忆方法的分类。我们根据存储知识的抽象层次对现有工作进行分类：基于案例的记忆保留原始记录以实
现直接重放，基于策略的记忆提炼出用于规划的抽象启发式规则，基于技能的记忆整合可执行的能力以实现动作。(续)
Method Carrier Form Task Optimization
Fincon(Yuetal.,2024) Token-level Solution Financial PE
MapCoder(Islametal.,2024) Token-level Solution Coding PE
Memento(Zhouetal.,2025a) Token-level Trajectory Reasoning RL
COLA(Zhaoetal.,2025a) Token-level Trajectory GUI,WebNavigation,Reasoning PE
Continuous Memory (Wu et al., Latent Trajectory GUI SFT
2025e)
JARVIS-1(Wangetal.,2025p) Token-level Trajectory Game,GUIInteraction PE
MemGen(Zhangetal.,2025d) Latent Trajectory WebSearch,EmbodiedSimulation,Rea- RL,SFT
soning,Math,Code
Early Experience (Zhang et al., Parametric Trajectory Embodied Simulation, Reasoning, Web SFT
2025j) Navigation
DreamGym(Chenetal.,2025e) Token-level Trajectory Web Interaction, Embodied Simulation, RL
Shopping
II.Strategy-basedMemory
Reflexion(Shinnetal.,2023a) Token-level Insight Embodied Simulation, Reasoning, Cod- PE
ing
Buffer of Thoughts (Yang et al., Token-level Pattern Game,Reasoning,Coding PE
2024b)
AWM(Wangetal.,2024l) Token-level Workflow WebInteraction,Instruction-guidedWeb PE
Task
RecMind(Wangetal.,2024h) Token-level Pattern Recommendation PE
2
H R(Yeetal.,2025b) Token-level Insight Game,EmbodiedSimulation PE
ReasoningBank (Ouyang et al., Token-level Insight WebInteraction,Instruction-guidedWeb PE
2025) Task
R2D2(Huangetal.,2025c) Token-level Insight WebInteraction PE
BrowserAgent(Yuetal.,2025d) Token-level Insight GeneralQA,Websearch RL,SFT
AgentKB(Tangetal.,2025d) Token-level Workflow Code,Reasoning PE
ToolMem(Xiaoetal.,2025b) Token-level Insight Reasoning,ImageGeneration PE
PRINCIPLES(Kimetal.,2025a) Token-level Pattern EmotionalCompanion PE
SE-Agent(Sunetal.,2025b) Token-level Insight Coding PE
ACE(Zhangetal.,2025m) Token-level Insight Coding,Toolcalling,Financial PE
Flex(Caietal.,2025b) Token-level Insight Math,Chemistry,Biology PE
AgentEvolver(Zhaietal.,2025) Parametric Pattern Tool-augmentedTask RL
Dynamic Cheatsheet (Suzgun et al., Token-level Insight Math,Reasoning,Game PE
2025)
Training-Free GRPO (Cai et al., Token-level Insight Math,Reasoning,WebSearch PE
2025a)
III.Skill-basedMemory
CREATOR(Qianetal.,2023) Token-level FunctionandScript Reasoning,Math PE
Gorilla(Patiletal.,2024) Token-level API Toolcalling SFT
ToolRerank(Zhengetal.,2024b) Token-level API Toolcalling PE
Voyager(Wangetal.,2024b) Token-level CodeSnippet Game PE
RepairAgent(Bouzeniaetal.,2024) Token-level FunctionandScript Coding PE
COLT(Quetal.,2024) Token-level API Toolcalling SFT
ToolLLM(Qinetal.,2024a) Token-level API ToolCalling SFT
Continuedonnextpage
36

Table 5 经验记忆方法的分类。我们根据存储知识的抽象层次对现有工作进行分类：基于案例的记忆保留原始记录以实
现直接重放，基于策略的记忆提炼出用于规划的抽象启发式规则，基于技能的记忆整合可执行的能力以实现动作。(续)
Method Carrier Form Task Optimization
LEGOMem(Hanetal.,2025a) Token-level FunctionandScript Oﬀice PE
DarwinGödelMachine(Zhangetal., Token-level CodeSnippet Code PE
2025h)
Huxley-GödelMachine(Wangetal., Token-level CodeSnippet Code PE
2025j)
p
Memp (Fangetal.,2025d) Token-level FunctionandScript EmbodiedSimulation,TravelPlanning PE
SkillWeaver(Zhengetal.,2025a) Token-level FunctionandScript WebInteraction,Instruction-guidedWeb PE
Task
Alita(Qiuetal.,2025c) Token-level MCP Math,Reasoning,VQA PE
Alita-G(Qiuetal.,2025b) Token-level MCP Math,Reasoning,VQA PE
LearnAct(Liuetal.,2025a) Token-level FunctionandScript MobileGUI PE
ToolGen(Wangetal.,2025i) Parametric API Toolcalling SFT
MemTool(Lumeretal.,2025) Token-level MCP Toolcalling SFT
ToolRet(Shietal.,2025c) Token-level API Web,Code,ToolRetrieval SFT
DRAFT(Quetal.,2025a) Token-level API Toolcalling PE
ASI(Wangetal.,2025r) Token-level FunctionsandScripts WebInteraction PE
4.2.1 基于案例的记忆
基于案例的记忆存储了对历史事件的最小化处理记录，优先保证保真度，以确保回合可以作为上下文中
的范例进行重放或复用。与策略模板或技能模块不同，案例避免了过度抽象，从而保留了情境与解决方
案之间的原始对应关系。
轨迹 此类别保留交互迹以支持重放和证据驱动的学习。为优化文本环境中的检索，Memento (Zhou
et al., 2025a) 采用软 Q 学习动态调整选择高价值历史迹的概率。在多模态情景中，JARVIS-1 (Wang
et al., 2025p)、EvoVLA(Liu et al., 2025h) 和自动缩放连续记忆 (Wuet al., 2025e) 保留视觉上下文，前
者在 Minecraft 中存储生存经验，后者将 GUI 历史压缩为连续嵌入。此外，早期经验范式 (Zhang et al.,
2025j) 构建无奖励的、智能体生成的交互迹，并通过训练中期集成到模型参数中，以增强泛化能力。
解决方案 此类方法将记忆视为经过验证解决方案的存储库。ExpeL(Zhaoetal.,2024)通过试错自主收
集经验，将成功的轨迹存储为范例，并提取文本洞察以指导未来的动作。Synapse(Zhengetal.,2024a)同
样将抽象的状态-动作回合作为上下文示例注入，以对齐问题求解模式。在程序合成领域，MapCoder(Is-
lam et al., 2024) 将相关示例代码作为类似战术手册的案例保存，多智能体流水线可检索并适配这些案
例以提升复杂任务上的可靠性。在金融领域，FinCon (Yu et al., 2024) 维护过去动作、盈亏轨迹及信念
更新的回合记忆，以促进跨回合的稳健决策。
概要 基于案例的记忆具有高信息保真度，并为模仿提供了可验证的证据。然而，依赖原始数据在检索
效率和上下文窗口占用方面带来了挑战。与可执行技能或抽象策略不同，案例不包含编排逻辑或功能接
口。相反，它们作为高级推理所依托的事实基础。
37

4.2.2 基于策略的记忆
与仅保留发生了什么的案例库不同，基于策略的记忆提取了可迁移的如何行动的知识，涵盖可复用的推
理模式、任务分解、洞察、抽象以及跨情境的工作流。它将经验提升为可编辑、可审计和可组合的高层
知识，从而减少对冗长轨迹回放的依赖，并提升跨任务的泛化能力和效率。本节重点关注非代码或弱代
码基础的模板和工作流，而可执行函数、API、MCP 协议和代码片段则归类于Section 4.2.3。根据所保
留知识的粒度和结构复杂性，我们将基于策略的记忆分为三种不同类型：原子级的洞察、顺序性的工作
流以及图式化的模式。
洞察力 这类方法专注于从过往轨迹中提炼离散的知识片段，例如细粒度的决策规则和反思性启发式。
H2 R (Ye et al., 2025b) 显式地将规划层与执行层的记忆分离，使得高层规划洞见与低层操作规则能够
分别被检索，从而在多任务场景中实现细粒度迁移。R2D2 (Huang et al., 2025c) 集成记忆、反思与动
态决策以实现网页导航，通过失败与成功案例共同推导出修正性洞察，以指导后续回合。对于长时程网
页自动化，BrowserAgent (Yu et al., 2025d) 将关键结论作为显式记忆持久保存，以稳定长期推理链条
并缓解上下文漂移问题。
工作流 与原子的、静态的洞察不同，工作流将策略封装为结构化的 动作序列——从先验轨迹中抽象
出的可执行例程，用于在推理时指导多步执行。智能体工作流记忆（AWM） (Wang et al., 2024l) 在
Mind2Web (Deng et al., 2023) 和 WebArena (Zhou et al., 2023a) 上诱导出可复用的工作流，并将其
作为高层框架来引导后续生成，从而在不更新基础模型权重的情况下提升成功率并减少步骤。这表明策
略模板可作为顶层控制器，补充案例级证据。智能体知识库（Agent KB） (Tang et al., 2025d) 建立了
一个统一的知识库，将工作流视为可迁移的过程知识。它采用分层检索机制，优先访问工作流以构建战
略方法，实现跨多种智能体架构的问题求解逻辑复用。
模式 在更高层次的抽象下，推理模式作为认知模板，封装了问题求解的结构，使智能体能够通过实
例化这些可泛化的骨架来应对复杂的推理任务。Thoughts (Yang et al., 2024b) 的思维缓存维护了一个
思维模板的元缓存，这些模板被检索并实例化以解决新问题。类似地，ReasoningBank (Ouyang et al.,
2025) 将成功与失败抽象为可复用的推理单元，促进了测试时的扩展和鲁棒学习。RecMind 的自激励规
划算法 (Wang et al., 2024h) 生成中间自我引导，以构建后续规划和工具使用的结构。在对话智能体领
域，PRINCIPLES (Kim et al., 2025a) 通过离线自对弈构建合成策略记忆，以指导推理时的策略规划，
从而无需额外训练。
这些进展表明，推理范式正从描述性规则转向可移植的推理结构。
概要 基于策略的记忆，包括洞察、工作流和模式，作为高层级的框架来指导生成式推理。与依赖检索
具体、原始轨迹（可能含有噪声或受上下文影响）的案例记忆不同，这种记忆形式提炼出可泛化的模式，
有效约束搜索空间，并提升在未见任务上的鲁棒性。然而，一个关键区别在于，这些策略仅作为结构化
指导原则，而非可执行的动作；它们引导规划过程，但不直接与环境交互。这一局限性要求引入下一节
将讨论的能力型记忆，其存储可调用的能力和工具。最终，鲁棒智能体通常会协同运用这些组件：策略
提供抽象的规划逻辑，而能力则负责具体的执行。
38

4.2.3 基于技能的记忆
技能记忆捕捉了智能体的程序化能力，将抽象策略具体化为可验证的动作。它编码了智能体能够执行的
内容，补充了智能体所知的陈述性知识，并通过提供可调用、可测试和可组合的可执行指令，锚定感知
—推理—动作环。近期证据表明，语言模型能够学习何时以及如何调用工具，并在拥有大量工具库时实
现可靠扩展，这确立了技能记忆作为现代智能体执行基础的地位。
技能记忆涵盖从内部细粒度代码到外部标准化接口的连续谱。统一的标准很简单：技能必须能被智能体
调用，其结果必须可验证以支持学习，并且能够与其他技能组合形成更大的流程。
代码片段 可执行代码以可复用片段的形式存储，能够从经验快速转化为能力。在开放性任务中，智能
体将成功的子轨迹提炼为可解释的程序，并在不同环境中复用。Voyager (Wang et al., 2024b) 体现了
这一模式，其技能库持续增长；Darwin Gödel Machine (Zhang et al., 2025h) 更进一步，能够在经验验
证下安全地重写自身代码，从而生成自指且逐步更强大的技能集。
功能和脚本 将复杂行为抽象为模块化函数或脚本能够提升其可重用性和泛化能力。近期进展使得智能
体能够自主创建专用工具以解决各类问题 (Qian et al., 2023; Yuan et al., 2024a)，且通过演示和环境反
馈在移动 GUI、网页导航以及软件工程等不同领域中不断优化工具使用能力 (Fang et al., 2025d; Zheng
et al., 2025a; Bouzenia et al., 2024)。此外，涌现的程序化记忆机制使智能体能够将执行轨迹提炼为可
检索的脚本，从而高效地泛化到新场景 (Liu et al., 2025a; Han et al., 2025a)。
应用程序编程接口 API作为封装技能的通用接口。早期工作侧重于通过微调模型来正确调用工具(Schick
et al., 2023; Patil et al., 2024)，然而 API 库的指数级增长已使主要瓶颈转向信息检索。标准的信息检
索方法往往无法捕捉工具的功能语义 (Shi et al., 2025c)。因此，近期的方法转向基于学习的检索与重排
序策略，这些策略考虑了工具文档质量、层级关系以及协作使用模式，以弥合用户意图与可执行函数之
间的差距 (Zheng et al., 2024b; Gao and Zhang, 2024c; Qu et al., 2024, 2025a)。
MCPs 为减少基于 API 生态中的协议碎片化，模型上下文协议提供了一个开放标准，统一了智能体
发现和使用工具与数据的方式，包括按需加载工具的代码执行模式，从而降低上下文开销 (Qiu et al.,
2025c,b)。广泛的平台支持表明正朝着统一的接口层收敛。
除了标准可执行文件外，研究还探索了可学习的工具能力记忆以应对不确定的神经工具，参数化集成将
工具符号嵌入以统一检索与调用，以及架构即技能的观点，其中专用智能体是模块化设计空间内的可调
用模块 (Xiao et al., 2025b; Wang et al., 2025i; Zhao et al., 2025a)。这些研究方向共同将技能记忆重新
构架为一种可学习、可演化且可编排的能力层。
概要 总之，基于技能的记忆构成了智能体主动执行的基础，从静态的代码片段和模块化脚本演化为标
准化的 API 和可学习的架构。它通过将基于案例和策略的记忆中的洞察转化为可验证的程序，弥合了
抽象规划与环境交互之间的鸿沟。随着工具创建、检索和互操作性（如 MCP）等机制的成熟，技能记
忆已超越简单的存储功能，实现了能力合成、优化与执行的持续环路，推动智能体的开放性演化。
39

4.2.4 混合内存
先进的智能体架构越来越多地采用一种混合设计，将多种经验记忆形式整合在一起，以平衡具体证据与
可泛化的逻辑。通过保持从原始回合到提炼规则，再到可执行技能的知识谱系，这些系统能够动态选择
最合适的记忆格式，从而确保在各种上下文中的检索准确率和广泛泛化能力。
一个突出的研究方向是将基于案例的记忆与基于策略的记忆相结合，以促进互补性推理。例如，Ex-
peL (Zhao et al., 2024) 将具体的轨迹与抽象的文本洞察相结合，使智能体在回忆具体解决方案的同时
能够应用通用启发式方法。AgentKB(Tangetal.,2025d)采用分层结构，其中高层工作流指导规划，而
具体的解决方案路径则提供执行细节。类似地，R2D2 (Huang et al., 2025c) 将历史迹的经验池与反思机
制相结合，从过往错误中优化决策策略，有效连接了案例检索与策略抽象。与此相辅相成的是，Dynamic
Cheatsheet (Suzgun et al., 2025) 通过存储累积的策略和问题求解洞察，防止冗余计算，实现推理时的
即时复用。
此外，近期的框架致力于统一记忆的生命周期，融入基于技能的组件或构建全面的认知架构。在科学
推理中，ChemAgent (Tang et al., 2025c) 构建了一个自我更新的库，将执行案例与可分解的技能模块
相匹配，使模型能够通过积累的经验不断优化其化学推理能力。采取整体性方法，LARP (Yan et al.,
2023) 建立了面向开放世界游戏的认知架构，协调语义记忆（用于世界知识）、情景记忆（用于交互案
例）以及程序性记忆（用于可学习技能），从而确保一致的角色扮演和稳健的决策能力。最后，演化系
统如 G-Memory (Zhang et al., 2025c) 和 Memp (Fang et al., 2025d) 实现了动态转移，将重复成功的
案例逐步编译为高效技能，自动完成从高开销检索到快速执行的转变。最近的一项工作 MemVerse (Liu
et al., 2025d) 则结合了参数化记忆与 token 级别的程序性记忆。
4.3 工作记忆
在认知科学中，工作记忆被定义为一种容量有限、动态调控的机制，通过即时选择、保持和变换与任务
相关的信息来支持高级认知功能 (Baddeley, 2012)。这不仅仅是临时存储，更意味着在资源约束下的主
动控制。
这一观点建立在多重成分模型和嵌入式过程解释等框架之上，两者均强调注意力聚焦、干扰控制以及容
量的有限性 (Cowan, 2014)。
当转置到大模型时，标准上下文窗口主要作为被动的只读缓冲区。尽管模型在推理过程中可以读取窗口
内容，但缺乏明确的机制来动态选择、维持或变换当前工作空间。近期的行为证据表明，当前模型并不
表现出类人的工作记忆特征，这凸显了显式设计可操作工作记忆机制的必要性 (Huang et al., 2025a)。
在本节中，我们将工作记忆定义为对单个回合内上下文进行主动管理与操作的一系列机制(Zhangetal.,
2025q)。目标是将上下文窗口从一个被动的缓冲区转变为可控制、可更新且抗干扰的工作空间。这一转
移带来了即时收益：在固定的注意力预算下提升了任务相关信息的密度，抑制了冗余和噪声，并支持表
示的重写或压缩，以保持思维链条的连贯性。我们根据交互动态对这些机制进行分类。基于这种交互式
分类法的代表性工作记忆方法，以及它们的存储载体、任务领域和最优化策略，系统地总结于Table 6。
40

Two Types of Working Memory
• 单轮工作记忆 (Section 4.3.1) 侧重于 输入压缩与抽象。在此情景下，系统必须在单次前向传
播中处理大量即时输入，如长文档或高维多模态流。目标是动态地过滤和重写证据，以构建一
个有限的计算临时空间，从而最大化每个 token 的有效信息量。
• 多轮工作记忆 (Section 4.3.2) 解决了 时序状态维持问题。在序列交互中，挑战在于防止历史
信息的累积淹没注意力机制。这涉及通过持续的读取、执行和更新环，维持任务状态、目标和
约束，确保中间产物在各轮次间被折叠和整合。
总而言之，大模型的工作记忆代表了一种朝着回合内主动上下文管理的范式转变。通过契合主动操作的
认知需求，它抑制了干扰，并为长上下文推理的工程约束提供了切实可行的解决方案。
4.3.1 单轮工作记忆
单轮工作记忆解决了在单次前向传播中处理大量即时输入的挑战，包括长文档 (Chevalier et al., 2023)
和高维多模态流(Wangetal.,2024g)。与其被动地接收整个上下文，不如主动构建一个可写的工作空间。
这涉及对原始信息进行过滤和变换，以在固定的注意力和记忆预算下提高信息密度与可操作性 (Jiang
et al., 2023, 2024)。我们将这些机制分为 输入压缩，即减少物理 token 数量，以及 观测抽象，即把数
据转换为结构化的语义表示。
输入冷凝 输入压缩技术旨在预处理上下文，以最小化 token 使用量，同时保留关键信息 (Jiang et al.,
2023)。这些方法通常可分为三种范式：硬压缩、软压缩和混合压缩 (Liao et al., 2025a)。
硬压缩根据重要性度量离散地选择 token。例如，LLMLingua (Jiang et al., 2023) 和 LongLLMLin-
gua (Jiang et al., 2024) 通过估计 token 困惑度来丢弃可预测或与任务无关的内容，而 CompAct (Yoon
et al., 2024) 采用迭代策略保留能够最大化信息增益的片段。尽管高效，但硬选择可能破坏语法或语义
依赖关系。
软压缩将可变长度的上下文编码为稠密的潜在向量（记忆槽）。诸如 Gist (Mu et al., 2023)、上下文自
编码器（ICAE）(Ge et al., 2024) 以及 AutoCompressors (Chevalier et al., 2023) 等方法训练模型将提
示压缩为有效摘要 token 或独特的记忆嵌入。这种方法实现了较高的压缩比，但需要额外的训练，且可
能掩盖细粒度细节。
混合方法如 HyCo2 (Liao et al., 2025a) 试图通过结合全局语义适配器（软）与逐 token 保留概率（硬）
来调和这些 权衡。
观察抽象 虽然凝结关注的是简化，观测抽象则旨在将原始观测转换为有助于推理的结构化格式。该机
制将动态的、高维度的观测空间映射到固定大小的记忆状态，防止智能体被原始数据所淹没。
在复杂的交互环境中，抽象将冗长的输入转化为简洁的状态描述。Synapse (Zheng et al., 2024a) 将非
结构化的 HTML DOM 树重写为与任务相关状态摘要，以指导 GUI 自动化。类似地，在多模态情景中，
处理视频流的每一帧在计算上是不可行的。工作记忆机制通过提取语义结构来解决这一问题：Context
as Memory (Yu et al., 2025b) 根据视场重叠过滤帧，VideoAgent (Wang et al., 2024g) 将流转换为时间
41

事件描述，MA-LMM (He et al., 2024) 维护一个视觉特征库。这些方法有效地将高维度、冗余的流重写
为低维度、语义丰富的表示，可在有限的上下文窗口内进行高效处理。
概要 单轮工作记忆充当一个主动压缩层，旨在最大化上下文窗口在即时推理中的效用。通过采用输入
压缩和观察抽象，这些机制有效提升了操作工作区的信息密度，确保在容量受限的情况下仍能保留关键
证据。然而，这种最优化严格局限于单轮内；它解决的是静态输入的广度与复杂性，而非动态交互的时
间连续性。
4.3.2 多轮工作记忆
多轮工作记忆解决的问题空间与单轮情景截然不同。在长时程交互中，主要瓶颈从即时上下文容量转变
为对任务状态和历史相关性的持续维护。即使拥有扩展的上下文窗口，历史信息的累积仍不可避免地导
致注意力预算饱和、延迟增加，并引发目标漂移 (Lu et al., 2025b)。为缓解此问题，多轮设置中的工作
记忆充当外部化的状态载体，形成读取、评估与写入的连续环。其目标是在有限资源预算内，保持关键
状态信息的可访问性与一致性。我们根据其状态管理策略，将这些机制分为：状态整合、分层折叠以及
认知规划。
状态整合 在连续交互流中，状态整合通过动态更新将不断增长的轨迹映射到固定大小的状态空间。将
交互视为流式环境，MemAgent (Yu et al., 2025a) 和 MemSearcher (Yuan et al., 2025a) 采用循环机制
更新固定预算的记忆并丢弃冗余信息，从一个紧凑且不断演化的状态中回答查询。ReSum (Wu et al.,
2025f) 进一步通过周期性地将历史信息提炼为推理状态，利用强化学习优化摘要条件下的行为，以实现
无限期的探索。
除了启发式总结之外，ACON (Kang et al., 2025c) 将帧状态整合建模为一个最优化问题，联合压缩环境
观测与交互历史至一个有界浓缩状态，并从失败案例中迭代优化压缩准则。IterResearch (Chen et al.,
2025a) 进一步采用受马尔可夫决策过程（MDP）启发的公式化方法，结合迭代的工作区重构，其中不
断演化的报告充当持久记忆，周期性合成有效缓解了长时程研究中的上下文窒息与噪声污染问题。
关于状态表示，不同方法旨在确保恒定大小的足迹。MEM1 (Zhou et al., 2025b) 维护一个共享的内部状
态，将新观测与先验记忆合并。与显式文本不同，MemGen (Zhang et al., 2025d) 直接将潜在记忆 token
注入推理流中。
分层折叠 对于复杂且长期的任务，状态维护需要超越线性总结的结构。层次折叠基于子目标对任务轨
迹进行分解，在子任务活跃时仅保持细粒度的迹，而在子轨迹完成时将其折叠为简洁的摘要。
这种分解-再整合策略使得工作记忆能够动态地扩展和收缩。HiAgent(Huetal.,2025a)通过将子目标作
为记忆单元来实现这一策略，仅保留活跃的动作-观测对，并在子目标完成之后写回一个摘要。Context-
Folding (Zhang et al., 2025q) 和 AgentFold (Ye et al., 2025a) 通过将折叠操作变为可学习的策略，进
一步扩展了该方法，训练智能体自主决定何时分支进入子轨迹以及如何将它们抽象为高层状态。Deep-
Agent (Li et al., 2025h) 将此方法进一步应用于工具使用推理，将交互压缩为结构化的情景记忆和工作
记忆，以支持细粒度的信用分配。通过用稳定的高层抽象替换已完成的子轨迹，这些方法在保持关键上
下文的同时，使活跃窗口保持较小。
42

认知规划 在最高层次的抽象中，工作记忆创建并维持一个外化的计划或世界模型。状态不仅作为过去
经历的总结，更作为一种面向未来的结构，指导未来动作。
PRIME (Tran et al., 2025) 将检索直接集成到规划环中，确保记忆更新能够主动支持复杂的推理步骤。
在具身化和智能体环境中，将语言模型视为高层规划器，使计划成为工作记忆的核心。类似 SayPlan 的
方法利用可查询的三维场景图作为环境记忆，以实现大规模空间上的规划扩展 (Rana et al., 2023)。在
图形用户界面和家庭任务中，Agent-S (Agashe et al., 2025) 和 KARMA (Wang et al., 2025q) 等系统通
过将推理锚定在分层计划上，稳定了长时程性能，并利用增强记忆的检索来连接长期知识与短期执行。
通过将计划和结构化的环境表示作为工作记忆中可读写的核心，智能体可以在感知失败的情况下稳健地
保持目标一致性并修订策略 (Song et al., 2023)。
概要 多轮工作记忆依赖于可操作的状态载体的构建，而非原始历史的保留。通过整合状态固化以压缩
连续流、层级折叠以结构化子轨迹，以及认知规划以锚定未来动作，这些机制有效解耦了推理性能与交
互长度的关系。该范式使智能体能够在无限时域内保持时间连贯性和目标一致性，同时遵守严格的计算
和内存约束。
5 动态学：记忆如何运作与演变？
前文介绍了记忆的结构形式（Section 3）与功能角色（Section 4），构建了一个相对静态的智能体记忆
概念框架。然而，这种静态视角忽视了本质上构成智能体记忆的内在动态性。与静态编码于模型参数或
固定数据库中的知识不同，智能体记忆系统能够动态构建和更新其记忆存储，并根据不同的查询执行定
制化的检索。这种适应能力对于使智能体实现自我演化并开展终身学习至关重要。
相应地，本节研究从静态存储到动态内存管理与利用的范式转变。这一范式转变体现了智能体记忆相较
于静态数据库方法的基础性操作优势。在实践中，一个智能体记忆系统能够基于推理迹和环境反馈自主
提取出精炼且可泛化的知识。通过将新提取的知识动态融合并更新至现有的记忆库中，系统确保了对不
断演化的环境的持续适应，并缓解认知冲突。基于构建的记忆库，系统可在精确时刻从指定的记忆模块
中执行目标检索，从而有效增强推理能力。为系统地分析“如何”实现记忆系统的运作与演化，我们通
过将记忆生命周期分解为三个基本过程来进行考察。Figure 8 对这一动态记忆生命周期提供了整体性图
示，突出了记忆形成、演化与检索之间的相互作用，以支持适应性强且自我演化的智能体行为。
43

Task description Environment Obs
Env.
Task
Solution Action
Task
Iterative Retrieved Status
tasks
Agent Memory
(a) Raw information M
Backbone em
Looku o
p
ry
3. Memory Retrieval
1. Memory
Self-evolving (d)
Formulation Memory Retrieval
Query
raw Mem
data Unit When&Where What to
to retrieve retrieve
Semantic Knowledge
Summarize Distillation Memory
Structured Latent Base
(e)
Construction Representation
(g) Info
How to How to
Parametric Update retrieved
Internalization ... ... Memory retrieve consolidate
System (f) (c)
(b)
2. Memory Evolution Existing Query
New
Memory Integrate the newly extracted memories Similar Related
with the existing memory repository Memories Memories
Units
Consolidate Update Forget
Operations inside Operations between agents
Notations
memory systems and memory systems
Figure 8 智能体记忆的运行机制。我们将完整的记忆生命周期解耦为三个基本过程，这些过程驱动系统的适应性与自我
演化：(1) 记忆形成通过有选择地识别具有长期效用的模式，将原始交互经验转化为信息密集的知识单元；(2) 记忆演化
通过巩固、更新和遗忘机制，动态地将新记忆整合到现有知识库中，以确保知识库保持连贯性和高效性；以及 (3) 记忆
检索执行上下文感知查询以访问特定记忆模块，从而在精确信息支持下优化推理性能。字母顺序表示记忆系统内操作的
顺序。
Three Fundamental Process in Memory Systems
1. 记忆形成 (Section 5.1)：此过程专注于将原始经验转化为信息稠密的知识。记忆系统并非被动
记录所有交互历史，而是有选择性地识别具有长期效用的信息，例如成功的推理模式或环境
约束。此部分回答的问题是：“如何提取记忆？”
2. 记忆演化 (Section 5.2)：此过程代表了记忆系统的动态演化。它专注于将新形成的记忆与现有
的记忆基础进行整合。通过相关条目的巩固、冲突消解以及自适应剪枝等机制，系统确保记忆
在不断变化的环境中保持泛化性、一致性与高效性。此部分回答的问题是：“如何优化记忆？”
3. 记忆检索 (Section 5.3)：此过程决定了所检索记忆的质量。在上下文条件的约束下，系统构建
一个任务感知的查询，并采用精心设计的检索策略来访问相应的记忆库。因此，所检索的记忆
不仅在语义上相关，而且在推理过程中具有功能上的关键作用。这一部分回答的问题是：“如
何利用记忆？”。
44

这三个过程并非相互独立，而是形成一个相互关联的循环，推动记忆系统的动态演化与运行。在记忆形
成阶段提取的记忆，在记忆演化阶段被整合并更新至现有的记忆基础中。借助前两个阶段构建的记忆基
础，记忆检索阶段能够实现目标性访问，以优化推理。反过来，推理结果和环境反馈又回流至记忆形成
阶段，以提取新的洞察，并进入记忆演化阶段以完善记忆基础。总体而言，这些组件使大模型能够从静
态的条件生成器转变为能够持续从变化环境中学习并作出响应的动态系统。
5.1 记忆形成
我们定义记忆形成为将原始上下文（如对话或图像）编码为紧凑知识的过程。由于处理长篇、嘈杂且高
度冗余的原始上下文存在固有的缩放限制，记忆形成变得必要。全上下文提示通常会遇到计算开销大、
内存占用过高以及在分布外输入长度下的推理性能下降等问题。为缓解这些问题，近期的记忆系统将关
键信息提炼为高效存储且精确可检索的表示，从而实现更高效、更有效的推理。
记忆形成并非独立于先前各部分。根据任务类型，记忆形成过程会从 Section 3 中描述的不同架构化记
忆中选择性地提取信息，以实现 Section 4 中概述的相应功能。基于信息压缩的粒度和编码逻辑，我们
将记忆形成过程分为五种不同类型。Table 7 总结了每类中的代表性方法，对比了它们的子类型、表示
形式及关键机制。
Five Categories of Memory Formation Operations
• 语义摘要 (Section 5.1.1) 将冗长的原始数据变换为紧凑的摘要，过滤掉冗余信息的同时保留
全局性的高层次语义信息，以降低上下文开销。
• 知识蒸馏 (Section 5.1.2) 提取特定的认知资产，涵盖从事实细节到经验性规划策略的各个方
面。
• 结构化构建 (Section 5.1.3) 将无定形的源数据组织为显式的拓扑表示，例如知识图谱或层次
树，以增强记忆的可解释性并支持多跳推理。
• 潜在表示 (Section 5.1.4) 将原始经验直接编码为机器原生格式（例如，向量嵌入或 KV 状态），
位于一个连续的潜在空间中。
• 参数化内化 (Section 5.1.5) 通过参数更新将外部记忆直接整合到模型的权重空间中，有效地
将可检索的信息转化为智能体的内在能力与直觉。
尽管我们将这些方法分为五类，但我们认为这些记忆形成策略并非相互排斥。单一算法可以整合多种记
忆形成策略，并在不同表示之间进行知识迁移 (Li et al., 2025k)。
5.1.1 语义摘要
语义摘要将原始观测数据转换为紧凑且语义丰富的摘要。生成的摘要捕捉了原始数据的全局性、高层次
信息，而非具体的事实或经验细节 (Zhao et al., 2024; Anokhin et al., 2024)。这类摘要的典型例子包
括文档的总体叙事 (Kim and Kim, 2025; Yu et al., 2025a)、任务的流程步骤 (Ye et al., 2025a; Zhang
et al., 2025q)，或用户的历史画像 (Zhang, 2024; Westhäußer et al., 2025)。通过过滤冗余内容的同时保
留与任务相关的全局语义，语义摘要为后续推理提供了高层次的指导蓝图，而不会引入过多的上下文开
销。为了实现这些效果，压缩过程可以采用两种主要方式：增量式和划分式语义摘要。
45

增量语义摘要 该范式采用一种时间整合机制，持续将新观测到的信息与现有摘要融合，生成全局语义
的动态表示。这种逐块处理的范式支持增量学习 (McCloskey and Cohen, 1989)，避免了完整序列处理
带来的 O(n2) 计算负担 (Yu et al., 2025a)，并促进了向全局语义的渐进收敛 (Chen et al., 2024b)。早
期实现如 MemGPT (Packer et al., 2023a) 和 Mem0 (Chhikara et al., 2025) 在适当时刻直接将新块与
现有摘要合并，仅依赖大语言模型（LLM）固有的摘要能力。然而，这种方法受限于模型容量，常导致
不一致或语义漂移。为缓解这些问题，Chen et al. (2024b) 和Wu et al. (2025i) 引入外部评估器以过滤
冗余或不连贯内容，分别使用基于卷积的判别器进行一致性验证，以及使用 DeBERTa (He et al., 2020)
过滤无关内容。与依赖辅助网络不同，后续方法如 Mem1 (Zhou et al., 2025b) 和 MemAgent (Yu et al.,
2025a) 通过强化学习结合 PPO (Schulman et al., 2017) 和 GRPO (Shao et al., 2024)，增强了 LLM 自
身的摘要能力。
随着增量摘要技术从启发式融合发展到过滤集成，最终迈向基于学习的最优化，摘要能力逐渐内化于模
型之中，从而减少了迭代过程中的累积误差。然而，串行更新的特性仍然带来了计算瓶颈 (Fang et al.,
2025b) 和潜在的信息遗忘问题，这推动了划分式语义摘要方法的发展。
划分语义摘要 该范式采用空间分解机制，将信息划分为不同的语义分区，并为每个分区生成独立的摘
要。早期研究通常采用启发式划分策略来处理长上下文。MemoryBank (Zhong et al., 2024) 和 COM-
EDY(Chenetal.,2025c)通过将每一天或每个会话视为基本单元，对长期对话进行摘要和聚合。在结构
维度上，Wu et al. (2021) 和 Bailly et al. (2025) 通过将长文档划分为章节或段落，生成摘要的摘要。虽
然直观，但此类方法常常在分区之间产生语义不连续性。为解决此问题，ReadAgent (Lee et al., 2024a)
和 LightMem (Fang et al., 2025b) 在摘要生成前引入语义或主题聚类，从而提升块间连贯性。超越文本
压缩范畴，DeepSeek-OCR(Weietal.,2025a)首次提出通过光学二维映射压缩长上下文的思想，在多模
态场景中实现了更高的压缩比。在视频记忆领域，FDVS (You et al., 2024) 和 LangRepo (Kahatapitiya
et al., 2025) 将长视频划分为片段，通过整合字幕、目标检测和场景描述等多源信号生成文本摘要，并
将其分层聚合为全局视频故事。
与增量摘要相比，划分方法具有更高的效率并能捕捉更细粒度的语义。然而，其对每个子块独立处理的
方式可能导致跨分区语义依赖关系的丢失。
概要 语义摘要作为一种有损压缩机制，旨在从冗长的交互日志中提炼核心内容。与逐字存储不同，它
更注重全局语义连贯性而非局部事实准确率，将线性流变换为紧凑的叙事块。语义摘要的主要优势在于
效率：它大幅缩短上下文长度，特别适用于长期对话。然而，其代价是细节损失：具体信息或细微线索
可能被模糊处理，从而限制了其在证据关键任务中的应用。
5.1.2 知识蒸馏
尽管语义摘要在宏观层面捕捉了原始数据的全局语义，知识蒸馏则在更细粒度的层次上运作，从交互轨
迹或文档中提取可复用的知识。广义而言，知识指的是Section 4中所描述的各种事实性与经验性记忆，
具体取决于任务的潜在功能。
提炼事实性记忆 该过程专注于将原始交互和文档转化为关于用户和环境状态的显式、声明性知识。
通过保留可验证的事实而非瞬时上下文，此过程确保智能体保持一致性和适应性。在用户建模领域，
TiM (Liu et al., 2023a) 和 RMM (Tan et al., 2025c) 等系统采用抽象机制，将对话轮次转换为高层级思
46

维或基于主题的记忆，从而维持长期人格一致性。在用户目标建模方面，MemGuide (Du et al., 2025b)
等方法从对话中提取用户意图描述。在推理过程中，系统会捕获并更新目标状态，将已确认的约束与未
解决的意图分离开来，以缓解目标漂移问题。此外，这种蒸馏方法还扩展至多模态环境，例如ESR(Shen
et al., 2024) 和 M3-Agent (Long et al., 2025) 等智能体将自我中心视觉观察压缩为可文本访问的对象位
置和用户习惯的相关事实。
提炼经验记忆 该过程专注于从历史轨迹中提取任务执行的潜在策略。通过从成功尝试中提炼规划原
则，并从失败中获取纠正信号，这一范式提升了智能体在特定任务上的问题解决能力。通过抽象与泛化，
它进一步支持跨任务的知识迁移。因此，经验泛化使智能体能够持续精进其能力，逐步迈向终身学习。
该研究方向旨在从成功与失败的轨迹中提炼高层次的规划策略和关键洞察。一些方法聚焦于基于成功的
蒸馏，例如AgentRR(Fengetal.,2025)和AWM(Wangetal.,2024l)从成功案例中总结整体任务计划。
Memp (Fang et al., 2025d) 分析并总结训练集中的黄金轨迹，将其提炼为抽象的过程性知识。另一些
方法则采用基于失败的反思，以 Matrix (Liu et al., 2024)、SAGE (Liang et al., 2025) 和 R2D2 (Huang
et al., 2025c) 为代表，通过将推理迹线与真实答案进行对比，识别错误来源并提取反思性洞见。结合两
者，ExpeL (Zhao et al., 2024) 与 From Experience to Strategy (Xia et al., 2025) 对比成功与失败的经
验，以揭示全面的规划洞察。
然而，先前的工作主要集中在总结任务级别的规划知识上，缺乏细粒度的、步骤级别的洞察。为弥补这
一不足，H2 R (Ye et al., 2025b) 提出了一种两层反思机制：它遵循 ExpeL 构建高层次规划洞察的池，
同时通过子目标序列对轨迹进行细分，以获得步骤级的执行洞察。
早期的方法依赖于固定的提示进行洞察提取，使其性能对提示设计和潜在大语言模型（LLM）的容量敏
感。最近，可训练蒸馏方法变得普遍。Learn-to-Memorize (Zhang et al., 2025t) 为不同智能体优化特定
任务的提示。另一方面，Memory-R1 (Yan et al., 2025b) 使用一个 LLMExtract 模块获取经验性和事实
性知识，而仅训练后续融合组件将这些输出整合到记忆库中。尽管这些方法采用端到端框架，但仍未能
有效提升 LLM 内在的洞察蒸馏能力。为克服这一局限，Mem-α (Wang et al., 2025o) 显式地训练 LLM
以确定应提取哪些洞察以及如何保存它们。
概要 本部分重点从原始上下文中提取特定功能的知识，而不涉及记忆存储的结构。每一条知识可被视
为一个扁平的记忆单元。若仅将多个单元无序地存入表格，将忽略它们之间的语义和层级关系。为解决
此问题，记忆形成过程可应用结构化规则，以推导出洞察，并将其存储于分层架构中。本文提出的单一
知识蒸馏方法虽简单但至关重要，可作为更复杂、更结构化记忆形成机制的基础组件。
5.1.3 结构化构建
尽管语义摘要（Section 5.1.1）和知识蒸馏（Section 5.1.2）在不同粒度层次上有效地压缩了摘要和知识，
但它们通常将记忆视为孤立的单元。相比之下，结构化构建将无定形的数据转化为有组织的拓扑表示。
这一过程不仅仅是存储格式的改变，更是一种主动的结构操作，决定了信息如何被关联和分层。与非结
构化的纯文本摘要不同，结构化提取显著提升了可解释性和检索效率。至关重要的是，这种结构先验在
捕捉多跳推理任务中的复杂逻辑和依赖关系方面表现出色，相较于传统的检索增强方法具有显著优势。
根据潜在结构生成的操作粒度，我们将现有方法分为两种范式：实体级构建，通过将文本分解为实体和
关系来构建潜在拓扑；片段级构建，通过组织完整的文本片段或记忆项来构建结构。
47

实体层面的构建 该范式的基础结构源自关系三元组的提取，其将原始上下文分解为其最细粒度的语
义原子实体与关系。传统方法将记忆建模为平面知识图谱。例如，KGT (Sun et al., 2024) 引入了一种
实时个性化机制，将用户偏好和反馈直接编码为特定于用户的知识图谱中的结点和边。类似地，Mem0g
(Chhikara et al., 2025) 利用大模型在提取阶段直接将对话消息转换为实体与关系三元组。
然而，这些直接提取方法通常受限于大语言模型（LLM）的固有能力，可能导致噪声或结构错误。为了
提升构建图谱的质量，D-SMART (Lei et al., 2025) 采用了一种优化的方法：首先利用大语言模型将核
心语义内容提炼为简洁、断言式的自然语言声明，随后通过神经符号流水线提取符合 OWL 标准的知识
图谱片段。此外，Ret-LLM (Modarressi et al., 2023) 对大语言模型应用监督微调，使其能够与关系图
谱进行更稳健的读写交互。
尽管上述方法专注于平面结构，但最近的进展已转向构建分层记忆以捕捉高层次抽象。例如，GraphRAG(Edge
et al., 2025) 从源文档中推导出实体知识图谱，并应用社区发现算法来迭代地提取图簇并生成簇摘要。
这种分层方法识别实体之间的更高级别簇关联，从而实现泛化洞察的提取，并支持在不同粒度下的灵活
检索。
为了更好地反映原始数据的内部一致性与时间信息，一些工作通过引入情景图来扩展语义知识图谱。
AriGraph (Anokhin et al., 2024) 和 HippoRAG (Gutierrez et al., 2024) 建立了包含语义图和情景图的
双层结构。它们从对话中提取语义三元组，同时连接同时发生的结点或建立结点–段落索引。Zep (Ras-
mussen et al., 2025) 进一步将其形式化为三层时间图架构：情景子图 (G )，通过双时间模型记录原始消
e
息的出现与处理时间；语义子图 (G )，用于实体和时间限定的事实；以及社区子图 (G )，用于实体的高
s c
层聚类与摘要。
块级构建 该范式将连续文本片段或离散记忆项视为结点，在保持局部语义完整性的同时，将其组织成
拓扑结构。该领域的发展经历了从固定语料库中静态的平面（2 维）提取，到对输入轨迹的动态适应，
最终演变为分层（3 维）架构的过程。
早期的方法侧重于将固定的文本库组织成静态的平面结构。HAT (A et al., 2024) 通过分段长文本并逐
步聚合摘要来构建层次树。类似地，RAPTOR (Sarthi et al., 2024) 使用 UMAP 进行降维，并利用高
斯混合模型进行软聚类，递归地对文本块进行聚类，迭代地总结这些簇以形成树状结构。然而，这些静
态方法在处理流数据时缺乏灵活性，且需要昂贵的重构过程。
为解决此问题，动态平面方法随着新轨迹的到来逐步构建记忆结构，其差异性取决于其基础元素。基于
原始文本的方法包括 MemTree (Rezazadeh et al., 2025c) 和 H-MEM (Sun and Zeng, 2025)。MemTree
采用自下而上的方法，新文本片段会检索最相似的结点，并作为子结点插入或迭代进入子树，从而触
发所有父结点的自下而上摘要更新。相反，H-MEM 采用自顶向下的策略，促使大语言模型将数据组
织成包含领域、类别、记忆迹和回合层的四层 JSON 层次结构。另外，A-MEM (Xu et al., 2025c) 和
PREMem (Kim et al., 2025b) 专注于重新组织提取的记忆项。A-MEM 将知识总结为离散笔记，并将
相关笔记链接以构建网络化记忆。PREMem 将提取的事实性、经验性和主观性记忆进行聚类，以识别
并存储跨会话的高维推理模式。
最近的进展已超越平面布局，构建出层次化结构，提供更丰富的语义深度。SGMem (Wu et al., 2025h)
通过使用 NLTK 将文本拆分为句子，形成所有句子结点之间的 KNN 图，并随后调用大语言模型提取
与每段对话对应的摘要、事实和洞察。为支持流式数据到达时层次结构的增量构建，CAM (Li et al.,
48

2025f) 根据语义相关性和叙事连贯性在文本块之间建立边。它通过显式解耦重叠簇（通过结点复制）来
迭代总结自指图并处理新记忆的插入。在多智能体场景中，G-memory (Zhang et al., 2025c) 通过维护
三个不同的图扩展了这一动态 3D 方法：一个用于原始聊天历史的交互图，一个用于特定任务的查询图，
以及一个用于洞察的图。该结构使每个智能体能够以不同粒度接收定制化的记忆。
概要 结构化构建的主要优势在于可解释性以及处理复杂关系查询的能力。这类方法能够捕捉记忆元素
之间的复杂语义和层次关系，支持多步依赖关系的推理，并有助于与符号或基于图形的推理框架集成。
然而其缺点是模式僵化：预先定义的结构可能无法有效表示细微或模糊的信息，且提取和维护成本通常
较高。
5.1.4 潜在表示
前几章聚焦于如何构建基于 token 的记忆；本部分则关注将记忆编码为机器原生的潜在表示。潜在表示
将原始经验编码为存在于潜在空间中的嵌入。与在嵌入向量之前对经验进行语义压缩和结构化提取不
同，潜在编码本质上将经验直接存储在潜在空间中，从而减少了在摘要和文本嵌入过程中产生的信息损
失。此外，潜在编码更有利于机器认知，能够实现跨模态的统一表示，并确保记忆表示具有高密度和丰
富的语义内涵。
文本潜在表示 尽管最初设计用于加速推理，KV 缓存也可被视为上下文中的潜在表示形式 (Li et al.,
2025c;Jiangetal.,2025b)。它利用额外的内存存储过去的信息，从而避免冗余计算。MEMORYLLM(Wang
et al., 2024j) 和 M+ (Wang et al., 2025m) 将记忆表示为可自我更新的潜在嵌入，在推理过程中注入
Transformer 层。此外，MemGen (Zhang et al., 2025d) 引入了记忆触发机制以监控智能体的推理状态，
并决定何时显式调用记忆，以及一种记忆豁免机制，该机制利用智能体的当前状态构建潜在 token 序
列。该序列作为机器原生记忆，增强了智能体的推理能力。
多模态潜在表示 在多模态记忆研究中，CoMEM (Wu et al., 2025d) 通过 Q-Former 将视觉-语言输入
压缩为固定长度的 token，实现了稠密的连续记忆，并支持无限上下文长度的即插即用使用。Encode-
Store-Retrieve (Shen et al., 2024) 使用 Ego-LLaVA 将第一人称视频帧转换为语言编码，随后通过嵌入
模型将其变换为向量表示。尽管嵌入模型被用于确保语义对齐，但这些方法在处理长上下文序列时，通
常面临压缩损失与计算开销之间的权衡，尤其是在梯度流方面。
当与具身人工智能结合时，多模态潜在记忆能够融合来自多个传感器的数据。例如，Mem2Ego (Zhang
et al., 2025l) 动态地将全局上下文信息与局部感知对齐，将地标语义嵌入为潜在记忆，以增强长时程任
务中的空间推理和决策能力。KARMA (Wang et al., 2025q) 采用混合的长短期记忆形式，将物体信息
编码为多模态嵌入，实现了即时响应性与一致表示之间的平衡。这些探索突显了潜在编码在跨模态提供
统一且语义丰富的表示方面的优势。
概要 潜在表示绕过了人类可读的格式，将经验直接编码为机器原生的向量或键值缓存。这种高密度格
式保留了丰富的语义信号，这些信号在文本解码过程中可能会丢失，从而实现与模型内部计算更流畅的
集成，并支持多模态对齐的无缝进行。然而，它存在不透明性问题。潜在记忆是一个黑盒子，使得人类
难以对其存储的知识进行调试、编辑或验证。
49

5.1.5 参数内化
随着大模型越来越多地引入记忆系统以支持长期适应，一个核心的研究问题是这些外部记忆应如何被
整合为参数化形式。尽管上述潜在表示方法将记忆参数化置于模型外部，而参数化内部化则直接调整模
型的内部参数。它利用模型通过学成参数空间编码和泛化信息的能力。这一范式从根本上增强了模型的
内在能力，在消除外部存储与检索开销的同时，无缝支持持续更新。正如我们在 Section 4中讨论的，不
是所有记忆内容都具有相同功能：某些条目提供陈述性知识，而其他条目则编码了塑造智能体推理与行
为的过程性策略。这一区分促使我们对记忆内部化采取更细致的视角，将其分为知识内部化与能力内部
化。
知识内化 该策略涉及将外部存储的事实记忆（如概念定义或领域知识）转换到模型的参数空间中。
通过这一过程，模型能够直接回忆并利用这些事实，而无需依赖显式的检索或外部记忆模块。在实际
应用中，知识内化通常通过模型编辑实现 (Sinitsin et al., 2020; De Cao et al., 2021)。早期工作，如
MEND(Mitchelletal.,2022)，引入了一个辅助网络，通过分解微调梯度，实现快速、单步编辑，从而最大
限度减少对无关知识的干扰。在此基础上，ROME (Meng et al., 2022) 利用因果追踪精确定位存储特定
事实的MLP层，并采用秩一更新注入新信息，实现了更高精度和更好泛化能力的编辑。MEMIT(Meng
et al., 2023) 进一步推进了这一方向，支持批量编辑，通过多层残差分布和批量公式，实现数千条事实
的同时更新，显著提升了可扩展性。随着像 LoRA (Hu et al., 2022) 这类参数高效范式的发展，知识
内化可通过轻量级适配器而非直接修改参数来完成。例如，CoLoR (Wistuba et al., 2023) 冻结预训练
Transformer 的参数，仅训练小型 LoRA 适配器以内化新知识，避免了全参数微调的高昂成本。尽管取
得这些进展，这些方法仍可能引发非目标效应 (De Cao et al., 2021)，且在持续学习场景下仍易受到灾
难性遗忘的影响。
能力内化 该策略旨在将经验知识（如程序性专长或战略启发式）嵌入模型的参数空间中。这一范式在
广义上代表了一种记忆形成操作，其重点从事实知识的获取转向经验能力的内化。具体而言，这些能力
包括领域特定的求解模式、战略规划以及智能体技能的有效部署等。从技术层面来看，能力内化是通过
从推理迹中学习实现的，例如采用监督微调 (Wei et al., 2022; Zelikman et al., 2022; Schick et al., 2023;
Mukherjee et al., 2023)，或基于偏好引导的最优化方法，如 DPO (Rafailov et al., 2023; Tunstall et al.,
2023; Yuan et al., 2024c; Grattafiori et al., 2024) 和 GRPO (Shao et al., 2024; DeepSeek-AI et al.,
2025)。由于此方面不属于典型智能体记忆研究的范畴，因此本节将不作详细讨论。
概要 参数化内化代表记忆的最终固化，即通过梯度将外部知识融合到模型的权重中。这一过程改变了
信息检索的范式，转而强调能力的拥有，模拟生物体的长期增强作用。当知识变得如同本能般自然时，
访问延迟为零，模型无需查询外部记忆即可立即响应。然而，这种方法面临诸多挑战，包括灾难性遗忘
和高昂的更新成本。与外部记忆不同，参数化内化难以在不产生意外副作用的情况下精确修改或删除，
从而限制了灵活性和适应性。
5.2 记忆演化
记忆形成在 Section 5.1 中从原始数据中提取记忆。接下来的重要步骤是将新提取的记忆与现有的记忆
库进行整合，从而实现记忆系统的动态演化。一种简单的策略是直接将新条目追加到现有记忆库中。然
而，这种方法忽略了记忆条目之间的语义依赖关系和潜在矛盾，也忽视了信息的时间有效性。为解决这
50

些局限性，我们引入了记忆演化机制。该机制将新旧记忆进行整合，以提炼高层次的洞察，解决逻辑冲
突，并删除过时的数据。通过确保长期知识的紧凑性、一致性和相关性，这一方法使记忆系统能够随着
环境和任务的变化，动态调整其认知过程和上下文理解能力。
基于记忆演化的目标，我们将其分为以下机制：
Three Mechanisms of Memory Evolution
• 记忆巩固 (Section 5.2.1) 将新旧记忆合并并进行反思性整合，形成更具泛化的洞察。这确保
了学习是累积性的而非孤立的。
• 记忆更新 (Section 5.2.2) 解决新旧记忆之间的冲突，对知识库进行修正和补充，以保持准确
性和相关性。它使智能体能够适应环境或任务需求的变化。
• 记忆遗忘 (Section 5.2.3) 会移除过时或冗余的信息，释放容量并提高效率。这可以防止因知
识过载导致的性能下降，并确保记忆库始终聚焦于可执行和当前的知识。
这些机制共同维护了记忆库的泛化能力、准确率和时效性。通过主动管理记忆演化，这些机制凸显了记
忆系统的智能体能力，促进了持续学习和自主自我提升。Figure 9 提供了这些记忆演化机制的统一视图，
展示了它们在共享记忆数据库中的操作角色和代表性框架。
5.2.1 巩固
记忆巩固旨在将新获取的短期痕迹转化为结构化且可泛化的长期知识。其核心机制是识别新旧记忆之间
的语义关系，并将其整合到更高层次的抽象或洞察中。该过程主要服务于两个目的：首先，它将零散的
信息片段重组为连贯的结构，防止在短期保留过程中丢失关键细节，从而促进稳定知识架构的形成；其
次，通过抽象、压缩和泛化经验数据，巩固过程从具体事件中提取出可重复使用的模式，生成支持跨任
务泛化的洞见。
一个核心挑战是确定新记忆应以何种粒度与现有记忆进行匹配和合并。先前的研究涵盖了从局部内容合
并到簇级融合再到全局整合的多种整合策略。
本地整合 该操作专注于涉及高度相似记忆片段的细粒度更新。在 RMM (Tan et al., 2025c) 中，每个
新的主题记忆会检索其最相似的前 K 个候选项，由大语言模型决定是否适合合并，从而降低错误泛化
的风险。在多模态情景下，当容量饱和时，VLN (Song et al., 2025b) 触发池化机制。它识别出最相似或
冗余的记忆对，并将其压缩为更高级别的抽象。这些方法在保持记忆存储全局结构的同时，细化了细节
知识，提升了准确率和存储效率。然而，它们无法完全捕捉簇级关系，以及语义相关记忆之间产生的高
阶依赖关系。
簇级融合 采用簇级融合对于在记忆增长过程中捕捉跨实例规律至关重要。在不同簇之间，PREMem(Kim
et al., 2025b) 将新的记忆簇与相似的现有簇对齐，并应用泛化和精炼等融合模式，形成更高阶的推理单
元，显著提升可解释性和推理深度。在簇内部，TiM (Liu et al., 2023a) 定期调用大语言模型来检查具
有相同哈希桶的记忆，并合并语义冗余的条目。CAM (Li et al., 2025f) 将目标簇内的所有结点合并为一
个代表性摘要，生成更高级且一致的跨样本表示。这些方法在更广泛的尺度上重新组织记忆结构，标志
着迈向结构化知识的重要一步。
51

Constructive
Agentic Memory MOOM
Think-in- PREMem MATRIX AgentFold
Memory
ReSum
VLN a. Consolidation Context
Memory Folding
Memory-
RMM
as-Acion
Raw
Local Cluster Global
Materials
Consolidation Fusion Integration
MemGPT MemGPT
(for external
MAICC Time database) Mem0
Memory Expired Update Memo^g
Bank
Memory Zep AI
Low Access Database
Frequency Re C so o l n u f t li i c o t n LightMem
Mem-alpha
XMem Low Value D-SMART
v
MemOS Parameter
update
c. Forgetting b. Updating
KARMA
ChemAgent
VLN
Memory
Livia
MemoryLLM
MemTool M+
WISE
MOOM AlphaEdit
Figure 9 记忆演化机制的全景图。我们将演化过程分为三个不同的分支，这些分支均维护着核心的记忆数据库：(a) 巩
固通过局部巩固、簇融合和全局整合对原始材料进行处理，以合成洞察；(b)更新通过对外部数据库执行冲突消解，并对
内部模型应用参数更新，确保准确性和一致性；以及 (c) 遗忘通过基于特定标准（时间过期、低访问频率、低信息价值）
的数据剪枝来优化效率。外环展示了与每种演化机制相关的代表性框架和智能体。
全球一体化 该操作执行整体整合，以保持全局一致性，并从积累的经验中提炼系统级洞察。与 Sec-
tion 5.1.1 相比，语义摘要侧重于从现有上下文中推导出全局总结，可视为摘要的初始构建。相比之
下，本段强调随着新信息的到来，如何将新信息整合到已有摘要中。对于用户事实记忆，MOOM (Chen
et al., 2025d) 通过基于规则的处理、嵌入方法以及大模型驱动的抽象，将临时角色快照与历史迹线相结
合，构建稳定的角色档案。对于经验记忆，Matrix (Liu et al., 2024) 执行迭代优化，将执行轨迹与反思
洞见同全局记忆融合，提炼出不依赖特定任务的原则，支持跨场景复用。随着单步推理上下文和环境反
馈长度增加，如 AgentFold (Ye et al., 2025a) 和 Context Folding (Zhang et al., 2025q) 等方法内化了
压缩工作记忆的能力。在多步交互（包括网页导航）中，这些方法在每一步后自动总结并浓缩全局上下
文，支持高效且有效的推理。全局整合从完整经验历史中凝聚高层次、结构化的知识，提供可靠的上下
文基础，同时提升泛化能力、推理准确率及个性化决策水平。
概要 整合是将零散的短期记忆痕迹重组为连贯的长期认知模式的认知过程。它超越了简单的存储，通
过建立孤立信息之间的联系，形成结构化的世界观，从而提升泛化能力并减少存储冗余。然而，这一过
52

程存在信息平滑的风险，即在抽象过程中，异常事件或特殊例外可能被忽略，从而降低智能体对异常情
况和特定事件的敏感性。
5.2.2 更新
记忆更新指的是当出现冲突或获取新信息时，智能体对其现有记忆进行修订或替换的过程。其目标是在
不进行完整模型重训练的情况下，保持事实的一致性并实现持续适应。与 Section 5.2.1 中描述的记忆
固化不同，后者侧重于抽象和泛化，记忆更新则强调局部修正和同步，使智能体能够与不断演化的环境
保持一致。
通过持续更新，智能体记忆系统能够保持知识的准确性和时效性，防止过时信息对推理造成偏差。因此，
它是实现终身学习和自我演化的核心机制。根据记忆所处的位置，更新可分为两类：（1）外部记忆更新：
对外部记忆存储的更新；（2）模型编辑：在参数空间内的模型内部编辑。
外部记忆更新 向量数据库或知识图谱中的条目会在出现矛盾或新事实时进行更新。这种方法通过对外
部存储的动态修改来保持事实一致性，而非改变模型权重。静态记忆不可避免地会积累过时或冲突的条
目，导致逻辑不一致和推理错误。更新外部记忆可以在避免完整重训练或重新索引成本的前提下实现轻
量级修正。
外部记忆更新机制的发展沿着一条轨迹演进，从基于规则的修正，发展到具有时间感知的软删除，再
到延迟一致性策略，最终实现了完全学成的更新策略。早期系统如 MemGPT (Packer et al., 2023a)、
D-SMART (Lei et al., 2025) 和 Mem0g (Chhikara et al., 2025) 采用了一种直接的流水线方式，其中大
语言模型检测新信息与现有记忆之间的冲突后，调用替换或删除操作来更新记忆。尽管在基础事实修复
方面有效，但这些系统依赖于破坏性替换，抹除了宝贵的上下文历史，破坏了时间连续性。为解决此问
题，Zep (Rasmussen et al., 2025) 引入了时间标注，将冲突的事实标记为无效时间戳而非直接删除，从
而同时保留语义一致性和时间完整性。这标志着从硬性替换转向软性、时间感知的更新。然而，实时更
新在高频交互下带来了巨大的计算和I/O开销。因此，MOOM(Chenetal.,2025d)和LightMem(Fang
et al., 2025b) 提出了双阶段更新：先进行软性在线更新以保证实时响应，随后通过离线反思整合阶段，
利用大语言模型推理合并相似条目并解决冲突。这种最终一致性范式在延迟与连贯性之间取得了平衡。
随着智能体强化学习的成熟，通过强化学习增强大语言模型内在的记忆更新决策能力成为可能。Mem-α
(Wang et al., 2025o) 将记忆更新建模为策略学习问题，使大语言模型能够自主学习何时、如何以及是
否更新，从而在稳定性与新鲜度之间实现动态权衡。
总体而言，外部记忆的更新已从手动触发的修正，转变为由大语言模型驱动的、具有时间感知能力的自
我调节学习过程，通过检索、冲突检测和修订，保持事实一致性和结构稳定性。
模型编辑 模型编辑在模型的参数空间内进行直接修改，以纠正错误或注入知识，而无需完全重新训练，
从而实现隐式知识更新。重新训练成本高昂且容易引发灾难性遗忘。模型编辑能够实现精确、低成本的
修正，提升模型的适应性与内部知识保留能力。
模型编辑方法主要分为两大类。(1) 显式定位与修改：ROME (Tan et al., 2025b) 通过梯度追踪识别编
码特定知识的参数区域，并执行针对性的权重更新；Model Editor Networks (Tang et al., 2025c) 训练一
个辅助的元编辑网络，以预测最优的参数调整。(2) 潜在空间自更新：MEMORYLLM (Xu et al., 2025c)
53

在 Transformer 层中嵌入记忆池，周期性地替换记忆 token 以融入新知识；M+ (Wang et al., 2025m)
维持双层记忆结构，丢弃过时的短期条目，并将关键信息压缩至长期存储。
混合方法如 ChemAgent (Tang et al., 2025c) 进一步将外部记忆更新与内部模型编辑相结合，同步事实
和表示的变化，实现快速的跨领域自适应。
概要 从实现角度来看，记忆更新侧重于解决新记忆到来时触发的冲突并修正知识，而记忆巩固则强调
对新旧知识的整合与抽象。上述两种记忆更新策略建立了一种双路径机制，涉及外部数据库中的冲突消
解以及模型内部参数的编辑，使智能体能够实现持续的自我修正，并支持长期演化。其核心挑战在于稳
定性与可塑性之间的矛盾：如何判断何时应覆盖现有知识，何时应将新信息视为噪声。错误的更新可能
覆盖关键信息，导致知识退化和推理错误。
5.2.3 遗忘
记忆遗忘指的是有意识地删除过时、冗余或低价值的信息，以释放容量并保持对重要知识的专注。与解
决记忆冲突的更新机制不同，遗忘更侧重于消除过时信息，以确保效率和相关性。随着时间推移，无限
制的记忆积累会导致噪声增加、检索延迟以及过时知识的干扰。可控的遗忘有助于缓解认知负荷并维持
认知聚焦。然而，过度激进的剪枝可能误删稀有但关键的知识，损害长期上下文中的推理连贯性。
遗忘机制可分为基于时间的遗忘、基于频率的遗忘和基于重要性的遗忘，分别对应创作时间、检索活动
以及综合语义评估。
基于时间的遗忘 时间驱动遗忘仅考虑记忆的创建时间，随时间逐渐衰减其强度以模拟人类记忆的消
退。MemGPT (Packer et al., 2023a) 在上下文上溢时剔除最早的消息。Xu et al. (2025c) 和 Wang et al.
(2025m) 采用随机 token 替换，替换比例为 K/N，以模拟人类认知中的指数遗忘，在内存池超过容量
时丢弃最旧的条目。与显式删除旧记忆不同，MAICC (Jiang et al., 2025c) 通过随时间逐渐衰减记忆的
权重来实现软遗忘。这一过程模拟了自然遗忘，确保持续适应而不会因历史数据过载。
基于频率的遗忘 频率驱动的遗忘根据检索行为对记忆进行优先级划分，保留频繁访问的条目，同时丢
弃不活跃的条目。XMem (Cheng and Schwing, 2022) 采用 LFU 策略移除低频条目；KARMA (Wang
et al., 2025q) 使用计数布隆过滤器来追踪访问频率；MemOS (Li et al., 2025k) 应用 LRU 策略，移除
长时间未使用的项目，同时归档高活跃度的条目。这确保了高效检索与存储之间的平衡。
通过区分创建时间与检索频率，这两个维度形成了一种更正交的分类体系：基于时间的衰减捕捉自然的
时间老化，而基于频率的遗忘则反映使用动态，二者共同维持系统的效率与时效性。
基于重要性的遗忘 基于重要性的遗忘机制整合了时间、频率和语义信号，在剪枝冗余信息的同时保留
高价值知识。早期工作如 Zhong et al. (2024) 和 Chen et al. (2025d) 通过结合时间衰减与访问频率的综
合得分来量化重要性，实现了基于数值的选择性遗忘。后续方法逐步发展为语义层面的评估：VLN(Song
et al., 2025b) 利用相似度聚类对语义冗余的记忆进行聚合，而 Livia (Xi and Wang, 2025) 则引入情感
显著性和上下文相关性，以建模情感驱动的选择性遗忘。随着大模型判断能力的不断增强，TiM (Liu
et al., 2023a) 和 MemTool (Lumer et al., 2025) 利用大模型评估记忆的重要性，并显式地剪枝或遗忘低
重要性记忆。这一转变反映了从静态数值评分向语义智能的转移。智能体现在能够进行有意识的遗忘，
并选择性保留最符合任务上下文、语义及情感线索的记忆。
54

概要 基于时间的衰减反映了记忆随时间自然消退的特性，基于频率的遗忘确保了对频繁使用记忆的高
效访问，而基于重要性的遗忘则引入了语义上的辨别能力。这三种遗忘机制共同决定了智能体记忆的时
效性、高效可访问性以及语义相关性。然而，像 LRU 这样的启发式遗忘机制可能会剔除那些很少被访
问但对正确决策至关重要的长尾知识。因此，当存储成本不是关键约束时，许多记忆系统会避免直接删
除某些记忆。
5.3 记忆检索
在Section 5.1和Section 5.2建立的内存库基础上，下一步的关键步骤是如何在推理过程中检索并利用记
忆。我们将记忆检索定义为从特定内存存储中适时地提取相关且简洁的知识片段，以支持当前的推理任
务。其核心挑战在于如何在大规模内存存储中高效且准确地定位所需的知识片段。为解决这一问题，许
多算法采用启发式策略或可学习模型来优化检索过程的各个阶段。根据检索执行顺序，该过程可分解为
四个方面。Figure 10对这一检索流水线提供了结构化的概述，按照现有方法在检索各阶段中的角色进行
组织。
Four Steps of Memory Retrieval
• 检索时机与意图 (Section 5.3.1) 决定了记忆检索的具体时刻和目标，从被动的、由指令驱动
的触发机制转变为自主的、自我调节的决策。
• 查询构建 (Section 5.3.2) 通过将查询分解或重写为有效的检索信号，弥合了用户原始输入与
存储的记忆索引之间的语义鸿沟。
• 检索策略 (Section 5.3.3) 在记忆存储库上执行搜索，采用从稀疏词法匹配到稠密语义嵌入以
及结构感知的图遍历等多种范式。
• 后检索处理 (Section 5.3.4) 通过重新排序、过滤和聚合，对检索到的原始片段进行精炼，确保
提供给模型的最终上下文简洁且连贯。
这些机制共同将记忆检索从静态的搜索操作转变为动态的认知过程。检索时机与意图决定了何时何地进
行检索；接下来，查询构建确定需要检索的内容，而检索策略则关注如何执行检索。最后，检索后处理
决定如何整合与利用所获取的信息。一个稳健的智能体系统通常在统一的流水线中协调这些组件，使智
能体能够近似人类联想记忆的激活，从而实现高效的知识访问。
5.3.1 检索时间与意图
检索意图和时机决定了何时触发检索机制以及查询哪个记忆存储。现有的记忆系统在这一方面采用了不
同的设计选择，从始终开启的检索到由显式指令或内部信号触发的检索 (Zhao et al., 2024; Wang et al.,
2025o; Fang et al., 2025b)。例如，MIRIX (Wang and Chen, 2025) 对每个查询都从六个记忆数据库中
进行检索，并将检索到的内容连结起来，体现了优先保证全面记忆访问的设计理念。而其他方法则旨在
更选择性地触发检索，使模型能够自主决定记忆访问的时机和范围，从而实现对记忆资源更精准、高效
的利用。在本小节中，我们从两个互补的角度回顾相关文献：自动化检索时机和自动化检索意图。
自动检索时间 该术语指模型在推理过程中自主决定何时触发记忆检索操作的能力。最简单的策略
是将决策权交由大语言模型（LLM）或外部控制器，使其仅根据查询判断是否需要进行检索。例如，
55

MemGPT(Packeretal.,2023a),MemTool(Lumeretal.,2025)
AutomatedTiming ComoRAG(Wangetal.,2025f),PRIME(Tranetal.,2025)
Timing&Intent MemGen(Zhangetal.,2025d)
(Section5.3.1)
AgentRR(Fengetal.,2025),MemOS(Lietal.,2025k)
AutomatedIntent
H-MEM(SunandZeng,2025)
Visconde(Pereiraetal.,2023),ChemAgent(Tangetal.,2025c)
Decomposition PRIME(Tranetal.,2025),MA-RAG(Nguyenetal.,2025)
AgentKB(Tangetal.,2025d),Auto-RAG(Kimetal.,2024a)
QueryConstruction
(Section5.3.2)
HyDE(Gaoetal.,2023b),MemoRAG(Qianetal.,2025)
MemGuide(Duetal.,2025b),ToC(Kimetal.,2023a)
Rewriting
Rewrite-Retrieve-Read(Maetal.,2023b)
Auto-RAG(Kimetal.,2024a)
AgentKB(Tangetal.,2025d),MemAlpha(Wangetal.,2025o)
LexicalRetrieval
SeCom(Panetal.,2025)
MemGPT(Packeretal.,2023b),MemoryBank(Zhongetal.,2024)
Voyager(Wangetal.,2024b),Memory3(Yangetal.,2024a)
Memory Retrieval SemanticRetrieval A-MEM(Xuetal.,2025c),RMM(Tanetal.,2025c)
(Section 5.3) TIM(Duetal.,2025a),MA-RAG(Nguyenetal.,2025)
MemoRAG(Qianetal.,2025),R2D2(Huangetal.,2025c)
RetrievalStrategies
(Section5.3.3) AriGraph(Anokhinetal.,2024),EMG-RAG(Wangetal.,2024k)
Mem0g(Chhikaraetal.,2025),SGMem(Wuetal.,2025h)
GraphRetrieval HippoRAG(Gutierrezetal.,2024),CAM(Lietal.,2025f)
D-SMART(Leietal.,2025),Zep(Rasmussenetal.,2025)
MemoTime(Tanetal.,2025b)
AgentKB(Tangetal.,2025d),MIRIX(WangandChen,2025)
SemanticAnchoring(ChatterjeeandAgarwal,2025)
HybridRetrieval
GenerativeAgents(Kaiyaetal.,2023),MAICC(Jiangetal.,2025c)
MemoriesDB(Ward,2025)
SemanticAnchoring(ChatterjeeandAgarwal,2025)
RCR-Router(Liuetal.,2025c),MemoTime(Tanetal.,2025b)
Re-ranking& Zep(Rasmussenetal.,2025),learn-to-memorize(Zhangetal.,2025t)
Filtering Memory-R1(Yanetal.,2025b)
Post-Retrieval PersonalizedLongtermInteraction(Westhäußeretal.,2025)
RMM(Tanetal.,2025c),Memento(Zhouetal.,2025a)
(Section5.3.4)
Aggregation& ComoRAG(Wangetal.,2025f),MA-RAG(Nguyenetal.,2025)
Compression G-Memory(Zhangetal.,2025c)
Figure10 智能体系统中记忆检索方法的分类。思维导图将现有文献组织为检索流水线的四个不同阶段：时机与意图，决
定流程的启动；查询构建，涵盖查询分解与重写技术；检索策略，将搜索范式分为词汇、语义、基于图形和混合方法；以
及 检索后处理，专注于通过重新排序、过滤和聚合来优化输出。
MemGPT (Packer et al., 2023a) 和 MemTool (Lumer et al., 2025) 允许大语言模型自身调用检索函数，
从而在类操作系统框架内高效访问外部记忆。然而，这些方法仅依赖查询的静态判断，忽略了模型在推
理过程中动态演化的认知状态。
为解决这一局限性，近期工作将快慢思考机制融入检索时机控制中。例如，ComoRAG (Wang et al.,
2025f) 和 PRIME (Tran et al., 2025) 首先生成快速响应，然后让智能体评估其充分性。若初始推理被
认为不足，系统将根据失败反馈触发更深层次的检索与推理。MemGen (Zhang et al., 2025d) 进一步优
化了触发机制，将显式的智能体层级决策转化为潜在的可训练过程。它引入了记忆触发器，从潜在的演
进状态中检测关键的检索时刻，从而在保持端到端可微分性的前提下提升了检索时机的准确率。
自动检索意图 这一方面关注模型在分层存储结构中自主决定访问哪个记忆源的能力。例如，Agen-
tRR (Feng et al., 2025) 会根据环境反馈动态在低层次的程序模板与高层次的经验抽象之间切换。然而，
其对显式反馈的依赖限制了其在开放性推理情景中的适用性。
为了克服这一约束，MemOS (Li et al., 2025k) 采用了一种 MemScheduler，根据用户、任务或组织层面
的上下文动态选择参数化内存、活性值内存或明文内存。然而，这种扁平的选择机制忽略了内存系统的
56

层次结构。H-MEM (Sun and Zeng, 2025) 通过引入基于索引的路由机制来解决这一问题，该机制执行
从粗到细的检索，从领域层逐步移动到回合层，逐渐缩小搜索范围，以定位最相关的子内存。这种层次
化路由不仅提升了检索准确率，还缓解了信息过载问题。
概要 自主的时间安排与意图判断有助于降低计算开销并抑制不必要的噪声，但也可能带来潜在漏洞。
当智能体过度高估其内部知识，在需要时未能启动检索，系统可能会进入一种静默故障模式，导致知识
缺口引发幻觉输出。因此，必须实现平衡：在恰当的时机为智能体提供必要信息，同时避免过度检索引
入噪声。
5.3.2 查询构造
在启动检索流程后，下一个挑战在于将原始查询变换为与记忆索引相匹配的有效检索信号。查询构建充
当用户表面表述与记忆潜在存储之间的翻译层。传统方法通常直接基于用户查询进行检索，虽然简单，
但无法使查询语义与记忆索引的语义对齐。为弥合这一差距，智能体记忆系统主动执行查询分解或查询
重写，生成更符合记忆潜在结构的中间检索信号。
查询分解 该方法将复杂的查询分解为更简单的子查询，使系统能够检索到更加细粒度且相关的信
息。这种分解通过实现模块化检索和对中间结果的推理，缓解了 single-shot 检索的瓶颈。例如，Vis-
conde (Pereira et al., 2023) 和 ChemAgent (Tang et al., 2025c) 使用大模型将原始问题分解为子问题，
从记忆中检索每个子问题的候选结果，并最终将它们整合为连贯的答案。然而，这些方法缺乏全局规
划。为解决此问题，PRIME (Tran et al., 2025) 和 MA-RAG (Nguyen et al., 2025) 引入了 Planner 智能
体，受到 ReAct (Yao et al., 2023b) 范式的启发，在分解为子查询之前先制定全局检索计划。但这些方
法主要依赖于问题驱动的分解，因此无法明确识别模型所缺失的具体知识。为了使子查询更具针对性，
Agent KB (Tang et al., 2025d) 采用两阶段检索过程，其中教师模型观察学生模型的失败情况，并据此
生成细粒度的子查询。这种有针对性的分解提高了检索准确率，减少了无关结果，尤其在知识密集型任
务中表现显著。
查询重写 与其进行分解，该策略会重写原始查询或生成一个假设文档，在检索之前细化其语义。这
种重写有助于缓解用户意图与记忆索引之间的不匹配。例如，HyDE (Gao et al., 2023b) 指示语言模型
以 zero-shot 方式生成一个假设文档，并使用其语义嵌入进行检索。生成的文档封装了期望的语义，有
效弥合了用户查询与目标记忆之间的差距。MemoRAG (Qian et al., 2025) 通过将全局记忆引入假设
文档生成过程，扩展了这一思路。它首先压缩全局记忆，然后基于查询和压缩后的记忆生成一个草稿
回答；该草稿随后被用作重写后的查询。由于草稿能够访问全局记忆上下文，因此能更准确地捕捉用
户意图并揭示隐含的信息需求。类似地，MemGuide (Du et al., 2025b) 利用对话上下文，提示语言模
型生成一个简洁的、类似命令的短语，作为检索的高层次意图描述。除了直接提示语言模型重写查询
外，Rewrite-Retrieve-Read(Maetal.,2023b)通过强化学习训练一个小型语言模型作为专用重写器，而
ToC (Kim et al., 2023a) 则采用澄清树（Tree of Clarifications）逐步细化和明确用户的检索目标。
概要 这两种范式——分解与重写——并非相互排斥。Auto-RAG (Kim et al., 2024a) 通过在相同的检
索条件下评估 HyDE 与 Visconde，然后选择在给定任务上表现更优的策略，实现了两者的融合。本研
究的发现表明，记忆检索查询的质量对推理性能具有显著影响。与早期研究主要关注设计复杂的记忆架
57

构不同，近期的研究 (Yan et al., 2025a) 越来越强调检索构建过程，使记忆的角色逐渐转向服务于检索。
而决定检索什么内容，显然正是这一过程中的关键组成部分。
5.3.3 检索策略
在明确检索目标后，我们获得一个意图清晰的查询。接下来的核心挑战在于，如何利用该查询从大规模
且复杂的记忆库中高效、准确地检索出真正相关知识。检索策略充当查询与记忆库之间的桥梁，其设计
直接决定了检索效率和结果质量。本节系统回顾了各种检索范式，并分析它们的优势、局限性及应用场
景——从基于关键词匹配的传统稀疏检索，到使用语义嵌入的现代稠密检索，再到面向结构化知识的基
于图形检索，以及新兴的生成式检索方法，最后是融合多种范式的混合检索技术。
词汇检索 该策略依赖于关键词匹配来定位相关文档，代表性方法包括 TF-IDF (SPARCK JONES,
1972) 和 BM25 (Robertson and Zaragoza, 2009)。TF-IDF 根据词频和逆文档频率衡量关键词的重要
性，实现快速且可解释的检索。BM25 进一步通过引入词频饱和度和文档长度规范化来优化该方法。此
类方法常用于注重准确率的检索情景中，此时结果的准确率与相关性优先于召回率 (Tang et al., 2025d;
Wang et al., 2025o; Pan et al., 2025)。然而，纯粹的词汇匹配难以捕捉语义差异和上下文关系，对语言
表达差异高度敏感，因此在开放领域知识或多模态记忆设置下效果较差。
语义检索 该策略将查询和记忆条目编码到共享的嵌入空间中，并基于语义相似度而非词法重叠进行匹
配。代表性方法采用语义编码器，包括Sentence-BERT(ReimersandGurevych,2019)和CLIP(Radford
et al., 2021)。在记忆系统中，该方法能更好地捕捉任务上下文，支持语义泛化和模糊匹配，因此成为
大多数智能体记忆框架中的默认选择 (Lewis et al., 2020; Wang et al., 2024b; Yang et al., 2024a; Xu
et al., 2025c; Tan et al., 2025c; Nguyen et al., 2025; Qian et al., 2025; Hassell et al., 2025; Huang et al.,
2025c)。然而，语义漂移和强制的 top-K 检索常常引入检索噪声和虚假召回。为解决这些问题，近期系
统引入了动态检索策略、重排序模块和混合检索方案。
图表检索 该策略不仅利用语义信号，还显式地利用图的拓扑结构，从而实现本质上更精确且具有结构
感知能力的检索。通过直接访问结构路径，这些方法展现出更强的多跳推理能力，并能更有效地探索长
程依赖关系。此外，将关系结构视为对推理路径的约束，自然支持由确切规则和符号约束所驱动的检索。
代表性方法如 AriGraph (Anokhin et al., 2024)、EMG-RAG (Wang et al., 2024k)、Mem0g (Chhikara
et al., 2025) 和 SGMem (Wu et al., 2025h) 首先识别最相关的结点或三元组，然后扩展至其语义相关的
K 跳邻居，构建一个自中心图（ego-graph）。HippoRAG (Gutierrez et al., 2024) 在检索到的结点上执
行个性化 PageRank (Page et al., 1999)，并根据与其他种子结点的接近程度对图中其余部分进行排序，
从而实现有效的多跳检索。超越固定扩展规则，CAM (Li et al., 2025f) 和 D-SMART (Lei et al., 2025)
利用大模型引导子图探索：CAM 使用大模型选择中心结点的有信息量邻居及其子结点以进行关联探索；
而 D-SMART 将大模型视为规划器，在知识图谱记忆中执行束搜索，以检索目标实体的一跳邻居以及
连接给定实体对的关系。对于时序图，Zep (Rasmussen et al., 2025) 与 MemoTime (Tan et al., 2025b)
进一步在显式的时间约束下实现实体-子图构建和关系检索，确保返回结果满足所需的时间规则。
生成式检索 该策略将词汇或语义检索替换为一个直接生成相关文档标识符的模型 (Tay et al., 2022;
Wang et al., 2022b)。通过将检索任务视为条件生成任务，模型在其参数中隐式存储候选文档，并在解
58

码过程中实现深度的查询-文档交互 (Li et al., 2025j)。利用预训练语言模型的语义能力，这一范式通常
优于传统检索方法，尤其是在小规模设置下 (Zeng et al., 2024)。
然而，生成式检索需要额外的训练以内化所有候选文档的语义，导致在语料库演化时扩展性受限 (Yuan
et al., 2024b)。出于这些原因，尽管生成与检索的紧密集成暗示了未开发的潜力，但智能体记忆系统对
此范式的关注相对较少。
混合检索 该策略整合了多种检索范式的优点。例如，Agent KB (Tang et al., 2025d) 和 MIRIX (Wang
and Chen, 2025) 将词汇检索与语义检索相结合，以在精确的术语或工具匹配与更广泛的语义对齐之
间取得平衡。类似地，Semantic Anchoring (Chatterjee and Agarwal, 2025) 在语义嵌入和符号求逆索
引上并行搜索，以实现互补的覆盖。其他一些方法则结合多种评估信号来引导检索。例如，Generative
Agents (Kaiya et al., 2023) 通过一个评分机制展示了这种多因子方法，该机制累积了时效性、重要性
和相关性。MAICC (Jiang et al., 2025c) 采用混合效用评分函数，将相似度与全局及预测的个体总回报
相结合。在基于图形的情景中，检索通常分为两个阶段：首先通过语义检索识别相关结点或三元组，随
后利用图拓扑结构扩展搜索空间 (Anokhin et al., 2024; Wang et al., 2024k; Gutierrez et al., 2024; Li
et al., 2025f)。
在数据库基础设施层面，MemoriesDB (Ward, 2025) 提出了一种面向长期智能体记忆的时序-语义-关系
型数据库，提供一种混合检索架构，将这些维度整合到统一的存储与访问框架中。
通过融合异构检索信号，混合方法在保持关键词匹配准确率的同时，融入了语义方法的上下文理解能
力，最终生成更加全面且相关的结果。
5.3.4 检索后处理
初始检索常常返回冗余、含噪声或语义不一致的片段。直接将这些结果注入提示词会导致上下文过长、
信息冲突，以及因无关内容而分散推理注意力。因此，检索后的处理变得至关重要，以确保提示词的质
量。其目标是将检索到的结果提炼为简洁、准确且语义连贯的上下文。实践中，有两个核心组件：(1)
重排序与过滤：进行细粒度的相关性评估，以移除无关或过时的记忆，并对剩余片段重新排序，从而减
少噪声和冗余。(2) 聚合与压缩：将检索到的记忆与原查询整合，消除重复内容，合并语义相似的信息，
并重构出紧凑且连贯的最终上下文。
重排序与过滤 为保持上下文的简洁性和连贯性，初始检索结果会重新排序并过滤，以去除低相关性
项。早期方法依赖启发式准则来评估语义一致性。例如，Semantic Anchoring (Chatterjee and Agarwal,
2025) 将向量相似度与实体级和话语级对齐相结合，而 RCR-Router (Liu et al., 2025c) 则整合了多种手
工设计信号，包括角色相关性、任务阶段优先级和时效性。然而，这些方法通常需要大量超参数调参以
平衡异构的重要性得分。为减轻这一负担，learn-to-memorize (Zhang et al., 2025t) 将得分聚合建模为
强化学习问题，使模型能够学习检索信号的最优权重。尽管这些技术主要优化语义连贯性，但在需要严
格时间推理的场景中，还需引入额外约束：Rasmussen et al. (2025) 和 Tan et al. (2025b) 根据记忆的
时间戳和有效窗口进行过滤，以满足复杂的时间依赖关系。
随着大模型能力的不断提升，近期方法利用其内在的语言理解能力直接评估记忆质量。Memory-R1(Yan
et al., 2025b) 和 Westhäußer et al. (2025) 均引入基于大模型的评估器（回答智能体或自验证智能体），
在生成最终响应前对检索内容进行过滤。然而，基于提示的过滤仍受限于大模型的潜在容量，以及提示
59

语义与下游应用之间的不匹配。因此，许多系统训练辅助模型以更稳健地估计记忆的重要性 (Tan et al.,
2025c)。Memento (Zhou et al., 2025a) 使用 Q 学习 (Watkins and Dayan, 1992) 预测检索项对正确答
案贡献的概率，而 MemGuide (Du et al., 2025b) 则微调 LLaMA-8B (Grattafiori et al., 2024)，利用边
际槽位补全增益对候选内容进行重排序。这些重排序和过滤策略共同优化了检索结果，且无需修改底层
检索器，从而兼容任何预训练的检索模型，同时支持任务特定的最优化。
聚集与压缩 通过后检索处理改进下游推理的质量和效率的另一种方法是聚合与压缩。该过程将检索到
的证据与查询整合，形成连贯且紧凑的上下文。与主要解决噪声和优先级问题的过滤与重排序不同，此
阶段专注于将多个碎片化的记忆项合并为更高级别的、提炼后的知识表征，并在需要任务特定适配时对
这些表征进行优化。ComoRAG (Wang et al., 2025f) 通过其集成智能体（Integration Agent）展示了这
一思想，该智能体识别与查询语义对齐的历史信号，并将其合并为一个抽象的全局摘要，以提供广泛的
上下文基础。MA-RAG (Nguyen et al., 2025) 中的提取智能体（Extractor Agent）对检索到的文档执行
细粒度的内容选择，仅保留与当前子查询强相关的关键信息，生成针对局部推理需求量身定制的简洁片
段。
此外，G-Memory (Zhang et al., 2025c) 将聚合与压缩扩展至多智能体系统的个性化中。它整合检索到
的高层见解和稀疏化轨迹，并利用大语言模型根据智能体的角色定制这些压缩后的经验。这一过程将通
用知识转化为针对特定角色的提示，填充到智能体的个性化记忆中。
概要 总之，检索后处理作为关键的中间步骤，能够将嘈杂且零散的检索结果转化为精确且连贯的推理
上下文。通过上述机制，检索后处理不仅提升了提供给模型的记忆密度和保真度，还使信息与任务需求
及智能体特性相匹配。
6 资源与框架
6.1 基准和数据集
在本节中，我们综述了被用于（或可被用于）评估基于大语言模型的智能体在记忆、长期学习、持续学习
或长上下文方面能力的代表性基准和数据集。我们将这些基准分为两大类：（1）专为记忆/终身学习/自
我演进智能体设计的基准；（2）最初为其他目的（如工具使用能力、网络搜索、具身动作）开发的基准，
但由于其具有长时程、多任务或序列性特征，同样适用于记忆能力的评估。
6.1.1 记忆 / 持续学习 / 自我演化智能体的基准
以记忆为导向的基准主要关注智能体构建、维护和利用过去交互或世界事实显式记忆的能力。这些任务
通常考察在多轮对话、用户特定会话或长篇合成叙事中信息的保留与检索能力，有时还包含多模态信
号。
这些基准的综合概览，包括其内存关注点、环境类型、模态以及评估尺度，如Table 8所示，为比较其设
计目标和评估情景提供了结构化参考。代表性示例如 MemBench (Tan et al., 2025a)，LoCoMo (Maha-
rana et al., 2024)，WebChoreArena (Miyai et al., 2025)，MT-Mind2Web (Deng et al., 2024)，Person-
aMem (Jiang et al., 2025a)，PerLTQA (Du et al., 2024)，MPR (Zhang et al., 2025u)，PrefEval (Zhao
et al., 2025d)，LOCCO (Jia et al., 2025)，StoryBench (Wan and Ma, 2025)，Madial-Bench (He et al.,
60

2025)，DialSim (Zheng et al., 2025b)，LongBench (Bai et al., 2024)，LongBench v2 (Bai et al., 2025)，
RULER (Hsieh et al., 2024)，BALILong (Kuratov et al., 2024)，MM-Needle (Wang et al., 2025e)，以
及 HaluMem (Packer et al., 2023a)，强调用户建模、偏好追踪和对话级一致性，通常在可精确控制真实
记忆的模拟情景下进行。
终身学习基准不仅局限于孤立的记忆检索，还考察智能体如何在长时间跨度和不断演变的任务分布下持
续获取、巩固和更新知识。诸如 LongMemEval (Wu et al., 2025a)、MemoryBank (Zhong et al., 2024)、
MemoryBench (Ai et al., 2025)、LifelongAgentBench (Zheng et al., 2025b) 和 StreamBench (Wu et al.,
2024a) 等基准，均围绕一系列任务或回合设计，其中新信息逐步到来，而早期信息可能变得过时或产生
冲突。这些设置强调灾难性遗忘、前向与后向迁移以及测试时适应等现象，使其适用于研究记忆机制如
何与持续学习目标相互作用。在许多情况下，性能不仅在当前任务上进行跟踪，还在先前见过的任务或
对话上进行评估，从而量化智能体在适应新用户、领域或交互模式的同时，保留有用知识的能力。
自演化智能体基准更进一步，将智能体视为一个开放的系统，能够通过交互不断迭代地优化自身的记
忆、技能和策略。在此情景下，关注点不仅在于信息的存储与召回，还涉及元层次的行为，如自我反思、
记忆编辑、工具增强的存储以及在多个回合或游戏中的策略改进。像 MemoryAgentBench (Hu et al.,
2025c)、Evo-Memory (Wei et al., 2025e) 以及其他多回合或任务型环境，都可以通过允许智能体积累轨
迹、构建更高层次的抽象，并根据自身过往表现调整未来运行行为，从而实例化为自演化设置。从这一
视角来看，这些基准提供了一个测试平台，用于评估智能体是否能够自主地逐步提升更强大的行为——
将静态任务转变为长期适应、策略优化和真正自改善记忆使用的场景。
6.1.2 其他相关基准
除了专门针对记忆或终身学习设计的基准测试外，还有大量面向智能体且具有长时程特性的评估套件也
与研究基于大语言模型的智能体的记忆能力密切相关。尽管这些基准测试最初旨在评估工具使用、具身
交互或知识密集型推理等其他方面，但其顺序性、多步骤和多任务的特性，隐含地对长期信息保持、上
下文管理和状态追踪提出了较高要求。
具身化和交互式环境构成此类基准的主要类别。像 ALFWorld (Shridhar et al., 2021) 和 Science-
World (Wang et al., 2022a) 这样的框架在模拟的基于文本或部分具身的环境中评估智能体，成功需
要记住过去的观察结果、中间目标以及跨长时间动作序列的环境动态。类似地，BabyAI (Chevalier-
Boisvert et al., 2019) 专注于在时间上延展的回合中对语言条件指令的遵循，隐式测试智能体在整个交
互过程中保持任务相关状态的能力。尽管这些基准并未显式建模外部记忆模块，但有效表现通常依赖于
智能体在长时程中保留并重用信息的能力。
另一个显著类别包括基于网络和工具增强的交互基准。WebShop (Yao et al., 2023a)、WebArena (Zhou
et al., 2024b) 和 MMInA (Tian et al., 2025) 评估智能体在真实或半真实网络环境中的表现，这些环境
涉及多步骤导航、信息获取和决策制定。这些情景自然会产生长上下文轨迹，要求在后续阶段回忆并整
合早期动作、检索到的信息或用户约束。ToolBench (Qin et al., 2024a) 进一步扩展了这一范式，通过
评估智能体在复杂工作流中选择并调用 API 的能力，其中对先前工具输出及工具使用经验的记忆对于
连贯执行至关重要。
多任务与通用智能体评估平台也提供了关于内存使用情况的间接但有价值的信息。AgentGym(Xietal.,
2024b) 和 AgentBoard (Xi et al., 2024b) 将多种环境或任务整合为统一的评估套件，要求智能体在跨任
61

务适应的同时保留特定任务的知识和策略。基于 PDDL 的规划环境在智能体基准中被广泛使用，用于
评估在结构化动作空间中的战略推理能力，其中智能体可通过在多个回合中积累并复用经验来提升长周
期规划性能。
最后，多个近期基准针对具有挑战性的现实世界或准现实世界推理场景，这些场景本质上对长上下文和
跨步骤一致性提出了高要求。SWE-Bench Verified (Jimenez et al., 2024) 在真实的软件仓库上评估代码
修复任务，要求智能体能够对长文件和不断演化的代码状态进行推理。GAIA (Mialon et al., 2023) 和
xBench (Chen et al., 2025b) 评估深度研究与搜索密集型任务，这些任务需要在多步和多源信息中进行
综合。GenAI-Bench (Li et al., 2024a) 虽然侧重于多模态生成质量，但也涉及复杂的任务工作流，其中
先验提示、中间输出或视觉约束的记忆起着非平凡的作用。
综上所述，这些基准通过将基于大语言模型的智能体置于丰富、交互性强且具有长期目标的情景中，补
充了以记忆为导向的评估。尽管记忆并非总是明确的测量目标，但在这些环境中持续表现出色，隐含地
依赖于智能体管理长上下文、保留相关信息以及将过往经验融入当前决策的能力，使其成为研究实际记
忆相关行为的宝贵试验平台。
6.2 开源框架
一个快速发展的开源记忆框架生态系统旨在为构建增强记忆的大型语言模型智能体提供可复用的基础
架构。表 Table 9 总结了代表性开源记忆框架的结构化对比，包括其支持的记忆类型、架构抽象以及
评估覆盖范围。这些框架大多通过向量或结构化存储支持事实性记忆，越来越多的框架也开始建模经
验性迹线，例如对话历史、用户动作和情景摘要，而多模态记忆则近期才开始出现。面向大型语言模
型智能体的开源记忆框架涵盖从以智能体为中心、具有丰富层次化记忆抽象的系统，到更通用的检索
或记忆即服务后端，例如 MemGPT (Packer et al., 2023b), Mem0 (Chhikara et al., 2025), Memobase,
MemoryOS (Kang et al., 2025a), MemOS (Li et al., 2025k), Zep (Rasmussen et al., 2025), Lang-
Mem(LangChain,2025),SuperMemory(Supermemory,2025),Cognee(Cognee,2025),Memary(Memary,
2025), Pinecone, Chroma, Weaviate, Second Me, MemU, MemEngine (Zhang et al., 2025s), Memori,
ReMe (AgentScope, 2025), AgentMemory，以及 MineContext (MineContext, 2025)。其中许多框架明
确分离短期与长期存储，并提供基于图形、基于档案或模块化的记忆空间，部分框架已开始报告在基于
记忆的基准测试上的结果。其余框架通常提供可扩展的向量或图数据库、API 以及语义或流式实体层，
有助于组织上下文，但通常将智能体行为和评估协议留给应用层处理。总体而言，这些框架在表示灵活
性和系统设计方面正迅速成熟。
7 位置与前沿
本节阐述了基于大语言模型智能体的记忆系统设计中的关键观点与新兴前沿。超越对现有方法的描述性
综述，我们聚焦于范式层面的转变，重新定义了在长时程智能体场景中记忆的构建、管理与优化方式。
具体而言，我们探讨了从以检索为中心的记忆向生成式记忆的转移，从人工设计的记忆系统向自主管理
的记忆系统的演进，以及从启发式流水线向强化学习驱动的记忆控制的转型。此外，我们还讨论了这些
转变如何与多模态推理、多智能体协作及可信性相互交织，指出了可能塑造下一代智能体记忆架构的开
放性挑战与研究方向。
62

7.1 记忆检索与记忆生成
7.1.1 回望：从记忆检索到记忆生成
历史上，智能体记忆研究的主导范式集中于记忆检索。在这一范式下，主要目标是在当前上下文给定的
情况下，从现有的记忆存储中识别、过滤并选择最相关的记忆条目。大量前期工作致力于通过更优的索
引策略、相似度度量、重排序模型或结构化表示（如知识图谱）来提升检索准确率 (Tan et al., 2025c;
Memobase, 2025)。实际上，这包括使用稠密嵌入的向量相似度搜索、结合词汇与语义信号的混合检索、
层次化过滤以及基于图形的遍历等技术。这些方法强调访问存储信息时的准确率与召回率，隐含假设记
忆库本身已经构建良好。
然而，最近越来越多的注意力转向了记忆生成。与将记忆视为可查询的静态存储库不同，记忆生成强调
智能体根据需要主动合成新的记忆表示的能力。其目标不仅仅是检索并连结现有的片段，而是以一种针
对当前上下文和未来效用的方式，对信息进行整合、压缩和重组。这一转变反映了人们日益认识到，有
效的记忆使用通常需要抽象和重新组合，尤其是在原始存储信息存在噪声、冗余或与当前任务不一致的
情况下。
现有的记忆生成方法大致可分为两个方向。其中一个方向采用 检索然后生成的策略，其中检索到的记
忆项作为重构的原始材料。在这种情景下，智能体首先访问一组相关记忆，然后生成一个更简洁、连贯
且上下文特定的精炼记忆表示，如 ComoRAG (Wang et al., 2025f)、G-Memory (Zhang et al., 2025c)
和 CoMEM (Wu et al., 2025d) 所实现的那样。该方法在保持历史信息基础性的同时，实现了自适应
的摘要和重构。另一个方向探索 直接记忆生成，即在没有显式检索步骤的情况下生成记忆。相反，智
能体直接从当前上下文、交互历史或潜在内部状态生成记忆表示。MemGen (Zhang et al., 2025d) 和
VisMem (Yu et al., 2025e) 等系统体现了这一方向，通过构建针对特定任务定制的潜在记忆 token，完
全绕过了显式的记忆查找过程。
7.1.2 未来展望
展望未来，我们预计生成方法将在智能体记忆系统中发挥越来越核心的作用。我们强调了未来生成式记
忆机制应具备的三个理想特性。
首先，生成式记忆应当具有上下文自适应性。与其存储通用的摘要，不如让记忆系统生成明确针对智能
体预期未来需求而优化的表示。这包括根据不同的任务、问题求解阶段或交互模式，调整记忆的粒度、
抽象层次和语义焦点。
其次，生成式记忆应支持跨异构信号的集成。智能体越来越多地处理多种模态和信息来源，包括文本、
代码、工具输出以及环境反馈。记忆生成为融合这些碎片化信号提供了自然机制，能够生成比简单拼接
或单独检索更有用的统一表示。我们假设，潜在记忆（如Section 3.3中讨论的）可能是实现这一目标的
一个有前景的技术路径。
第三，生成式记忆应当是学成且自我最优化的。与其依赖人工设定的生成规则，未来的系统应通过优化
信号（如强化学习或长时程任务表现）来学习何时以及如何生成记忆。在此视角下，记忆生成成为智能
体策略的内在组成部分，与推理和决策共同演化。
63

7.2 自动内存管理
7.2.1 回望：从手工设计到自动构建的内存系统。
现有的智能体记忆系统(Xuetal.,2025c;Packeretal.,2023a)通常依赖于手动设计的策略来决定存储哪
些信息、何时使用以及如何更新或检索。通过用详细的指令 (Chhikara et al., 2025)、预设的阈值 (Kang
et al., 2025a)，或由人类专家明确编写的规则 (Xu et al., 2025c) 引导固定的大型语言模型（LLMs），系
统设计者可以以相对较低的计算和工程成本将记忆模块集成到当前的智能体框架中，从而实现快速原型
设计与部署。此外，这些方法还提供了可解释性、可复现性和可控性，使开发者能够精确指定记忆的状
态与行为。然而，与其它领域的专家系统类似，这类人工精心设计的方法存在显著局限：它们本质上缺
乏灵活性，往往难以在多样且动态的环境中泛化。因此，这些系统在长期或开放式的交互中表现往往不
佳。
近期的智能体记忆研究进展开始着手解决这些局限性，通过使智能体自身能够自主管理记忆的演化与检
索。例如，CAM (Li et al., 2025f) 使大语言模型智能体能够自动将细粒度的记忆条目聚类为高层抽象
单元。Memory-R1 (Yan et al., 2025b) 引入了一个配备专用“记忆管理”工具的辅助智能体来处理记
忆更新。尽管取得了这些进展，当前的解决方案仍存在局限：许多仍然依赖于手动设计的规则，或针对
特定任务的学习目标进行优化，难以泛化到开放式的设置中。
7.2.2 未来展望
为了支持真正自动化的内存管理，一个有前景的方向是通过显式的工具调用，将内存构建、演化和检索
直接整合到智能体的决策环中，使智能体自身能够推理内存操作，而不是依赖外部模块或手工设计的工
作流。与现有将智能体内部推理过程与其内存管理动作分离的设计相比，在这种基于工具的策略下，大
型语言模型智能体可以精确地知晓自己执行了哪些内存操作（例如，添加/更新/删除/检索），从而实现
更加连贯、透明且上下文相关的内存行为。
另一个关键前沿在于开发采用分层和自适应架构的自优化记忆结构，这些架构受到认知系统的启发。首
先，分层记忆结构已被证明能够提升效率和性能 (Kang et al., 2025a)。除了分层之外，能够动态链接、
索引和重构记忆条目的自演化记忆系统，使记忆存储本身能够随时间自我组织，从而支持更丰富的推
理，并减少对人工设计规则的依赖。最终，这种自适应、自我组织的记忆架构为实现具备稳健、可扩展
且真正自主的记忆管理能力的智能体铺平了道路。
7.3 强化学习邂逅智能体记忆
7.3.1 回溯：强化学习正在让智能体内化记忆管理能力。
强化学习正在迅速重塑基于现代大语言模型的智能体的发展范式。在广泛的智能体能力领域，包括规
划、推理、工具使用，以及在数学推理、深度研究和软件工程等多样任务领域中，强化学习已经开始在
推动智能体性能方面发挥核心作用 (Zhang et al., 2025f,k)。记忆作为智能体能力的基础组件之一，其
发展也呈现出从流水线式到模型原生范式的类似趋势 (Sang et al., 2025)。智能体记忆研究社区正集体
地从早期的启发式与手动设计，转向强化学习越来越多地主导关键决策的方法。展望未来，可以合理预
期，完全基于强化学习的记忆系统最终可能成为主流方向。在详细讨论这一轨迹之前，我们先简要概述
发展的第一阶段。这一转变过程——即通过强化学习逐步内化并优化记忆管理——在Figure 11中以示
64

e.g., A-Mem, No human
T H h u r e e r s i h s o ti l c d Reas E on xp in e g L B , ank G P e b n ro a e m s ra e p d ti t o - n RL-based e.g., RMM R M L- e t m ra o in ry ed m p s r y e i s o m t r e o m o r n y
Reranker Writer
Fully
e.g., MemGPT agentic
e.g., Mem-alpha control
Semantic
Search RL-free RL Partially Fully RL-
Memory Involved driven
e.g., MemOS, RL-trained
Mem0 Memory
C C o h n u c n a k t e.g., MemoryBank Manager R W L- o tr r a k i i n n e g d e M .g e ., m C o o r n y t - e a x s t - A fo c l t d io in n g , , d M es S e i m e g l n f o - i r n y g
e.g., Memory-R1 Memory ACON, MemGen Arch.
Figure 11 强化学习赋能的智能体记忆系统的发展演化。从基于启发式或提示驱动流水线的无强化学习记忆系统，到部
分引入强化学习的设计，其中强化学习控制特定的记忆操作，最终发展为完全由强化学习驱动的记忆系统，其记忆架构
与控制策略均实现端到端学成。这一演化过程反映了更广泛范式的转变：从人工设计的记忆流水线，转向基于大语言模
型智能体的模型原生、自我优化的记忆管理。
意图形式展示。
无 RL 的存储系统 在之前综述的智能体记忆文献中，相当大一部分可以归类为无强化学习（RL-free）
的记忆系统。这些方法通常依赖于启发式或手动指定的机制，例如受遗忘曲线启发的固定阈值规则、在
MemOS (Li et al., 2025k)、Mem0 (Chhikara et al., 2025) 和 MemoBase (Memobase, 2025) 等框架中
发现的僵化语义搜索流水线，或基于简单拼接策略来存储记忆块。在某些系统中，大语言模型（LLM）
以看似具有 Agentic 特征的方式参与记忆管理，但其潜在行为完全由提示驱动。LLM 被要求生成记忆
条目，但并未接受任何专门针对有效记忆控制的训练，这一点在 Dynamic Cheatsheet (Suzgun et al.,
2025)、ExpeL (Zhao et al., 2024)、EvolveR (Wu et al., 2025c) 和 G-Memory (Zhang et al., 2025c) 等
系统中可见。这类方法在该领域的早期工作中占据主导地位，并由于其简洁性和实际可访问性，预计在
未来一段时间内仍将持续产生影响。
基于强化学习的内存系统 随着该领域的发展，许多工作开始将基于强化学习（RL）的方法融入记忆
流水线的特定组件中。这一方向的早期尝试是 RMM (Tan et al., 2025c)，它在初始检索阶段之后，利用
一个轻量级的策略梯度学习器，根据 BM25 或其他语义相似度度量对记忆块进行排序。后续系统探索
了更为雄心勃勃的设计。例如，Mem-α (Wang et al., 2025o) 将整个记忆构建过程交由通过强化学习训
练的智能体完成，而 Memory-R1 (Yan et al., 2025b) 采用了类似的思路。一条迅速扩展的研究路线正
在探讨智能体如何自主地折叠、压缩并管理超长多轮任务中的上下文。这种情景对应于工作记忆 (Kang
et al., 2025c; Ye et al., 2025a) 的管理。该领域中的许多领先系统均采用强化学习进行训练，包括但不限
于 Context Folding (Sun et al., 2025a)、Memory-as-Action (Zhang et al., 2025q)、MemSearcher (Yuan
et al., 2025a) 和 IterResearch (Chen et al., 2025a)。这些基于强化学习的辅助方法已展现出强大的能力，
并预示着强化学习在未来记忆系统设计中将扮演越来越重要的角色。
7.3.2 未来展望
展望未来，我们预计完全由强化学习驱动的记忆系统将构成智能体记忆演化中的下一个重要阶段。我们
强调这类系统应理想具备的两个特性。
65

• 首先，由智能体管理的内存架构应尽量减少对人工设计先验的依赖。许多现有的框架继承了受人
类认知启发的设计模式，例如皮层或海马体类比 (Gutierrez et al., 2024)，或预先定义的层次化分
类体系，将内存划分为情景、语义和核心等类别 (Wang and Chen, 2025)。尽管这些抽象在早期研
究中具有一定的指导意义，但在复杂环境中运行的人工智能体可能并不需要最有效或最自然的结
构。一种完全由强化学习驱动的情景为智能体提供了发明新颖且可能更合适的内存组织方式的可
能性，这些组织方式直接源于最优化动态而非人类直觉。在这种视角下，智能体被鼓励通过强化
学习激励来设计新的内存格式、存储模式或更新规则，从而实现适应性强且富有创造性的内存架
构，而非手工打造。
• 其次，未来的记忆系统应当赋予智能体对记忆管理所有阶段的完全控制权。当前基于强化学习
（RL）辅助的方法通常仅干预记忆生命周期中的部分环节。例如，Mem-α 自动化了记忆写入的某
些方面，但仍依赖于手动定义的检索流水线；而 MemSearcher (Yuan et al., 2025a) 等系统则主要
关注短期工作记忆，未涉及长期记忆的巩固或演化。一个完全具备 Agentic 特性的记忆系统要求
智能体以一体化方式自主处理多粒度记忆形成、记忆演化以及记忆检索。要实现这一级别的控制，
几乎必然需要端到端的强化学习训练，因为启发式方法或基于提示的方法无法充分协调这些组件
在长时间跨度下的复杂交互。
这两个方向共同预示着一个未来：记忆不再仅仅是附加在大语言模型智能体上的辅助机制，而将演变为
一个可完全学习且自我组织的子系统，与智能体通过强化学习共同进化。这类系统有望实现真正意义上
的持续学习和长期能力。
7.4 多模态记忆
7.4.1 回顾
随着基于文本的记忆研究日益成熟并得到广泛探索，多模态大语言模型以及能够联合支持多模态理解和
生成的统一模型持续发展，注意力自然扩展至多模态记忆。这一转变反映了更广泛的认识：许多现实世
界的智能体情景本质上是多模态的，而仅限于文本的记忆系统不足以支持在复杂环境中的长时程推理与
交互。
现有的多模态记忆研究大致可归为两个互补方向。第一个方向致力于使多模态智能体能够存储、检索并
利用来自多种感官输入的记忆 (Long et al., 2025; Zuo et al., 2025)。这一方向是智能体记忆的自然延
伸，因为运行在真实环境中的智能体不可避免地会遇到异构数据源，包括图像、音频、视频以及其他非
文本信号 (Xie et al., 2024)。多模态记忆的发展程度与相应模态的成熟度密切相关。视觉模态（如图像
和视频）受到了最多关注，从而催生了大量关于视觉和视频记忆机制的研究工作，这些机制支持视觉定
位、时间追踪以及长期场景一致性等任务 (Long et al., 2025; Wang et al., 2024g; Gurukar and Kadav,
2025; Yu et al., 2025e; Bo et al., 2025; Wang et al., 2025p; Li et al., 2024d)。相比之下，针对音频及其
他模态的记忆系统仍相对缺乏探索 (Li et al., 2025a)。
第二个方向将记忆视为统一模型的赋能组件。在此情景下，记忆并非主要用于支持智能体决策，而是用
于增强多模态生成和一致性。例如，在图像与视频生成系统中，记忆机制常被用来保持实体一致性、在
帧间维持世界状态，或确保长生成周期内的连贯性 (Yu et al., 2025b)。在此情境中，记忆充当一种稳定
结构，将生成内容锚定在先前生成的内容上，而非单纯作为智能体经验的记录。
66

7.4.2 未来展望
展望未来，多模态记忆很可能会成为智能体系统中不可或缺的组成部分。随着智能体越来越多地进入具
身化和交互式情景，其信息来源将天然具有多模态特性，涵盖感知、动作和环境反馈。因此，有效的记
忆系统必须能够以统一的方式支持异构信号的存储、整合与检索。
尽管近期取得了进展，目前尚无任何记忆系统能够提供真正的多模态支持。大多数现有方法仍局限于单
一模态，或在不同模态间松散耦合。未来的关键挑战在于设计能够灵活适应多种模态的记忆表示与操作，
同时保持语义对齐和时间连贯性。此外，多模态记忆必须超越被动存储，支持抽象、跨模态推理以及长
期适应能力。解决这些挑战对于实现能够在丰富、多模态环境中稳健且连贯运行的智能体至关重要。
7.5 多智能体系统中的共享内存
7.5.1 回望：从孤立的记忆到共享的认知基质
随着基于大语言模型的多智能体系统（MAS）日益重要，共享内存已成为实现协调、一致性以及集体
智能的关键机制。早期的多智能体框架主要依赖于隔离的本地内存与显式的消息传递，其中智能体通过
对话历史或特定任务的通信协议交换信息 (Qian et al., 2024; Wu et al., 2024b; Hu et al., 2025b; Zhang
et al., 2025i)。尽管这种设计避免了智能体之间的直接干扰，但在团队规模和任务时长增加时，往往面
临冗余、上下文碎片化以及高通信开销等问题。
后续工作引入了集中式共享内存结构，例如全局向量存储、黑板系统或共享文档 (Hong et al., 2024)，所
有智能体均可访问。这些设计实现了一种团队级别的记忆形式，支持注意力协同、减少重复，并促进长
周期协调。代表性系统表明，共享内存可作为规划、角色交接和共识构建的持久共同基础 (Rezazadeh
et al., 2025b; Xu et al., 2025a)。然而，简单的全局共享也带来了新的挑战，包括内存杂乱、写入竞争以
及缺乏角色或权限感知的访问控制。
7.5.2 未来展望
展望未来，共享内存可能会从一个被动的存储库演变为一种主动管理且具有自适应性的集体表示。一个
重要方向是开发智能体感知的共享内存，其中读写行为基于智能体的角色、专长和信任度进行条件控
制，从而实现更结构化和可靠的知识聚合。
另一个有前景的方向在于学习驱动的共享内存管理。与其依赖手工设计的同步、摘要或冲突消解策略，
未来系统可能训练智能体根据长期团队性能，自主决定何时、以何种方式以及贡献什么内容到共享内
存。最后，随着多智能体系统越来越多地运行在开放且多模态的环境中，共享内存必须支持跨异构信号
的抽象，同时保持时间与语义的一致性，而我们认为潜在记忆为此提供了一条有前景的路径 (Wu et al.,
2025d)。在这些方向上的进展，对于将共享内存从一种协调辅助工具提升为稳健集体智能的基础至关重
要。
7.6 世界模型的内存
7.6.1 回顾
世界模型的核心目标是构建一个能够高保真仿真物理世界的内部环境。这类系统是下一代人工智能的关
键基础设施。世界模型的核心属性在于生成内容，这些内容既具有无限可扩展性，又能在实时交互中运
67

行。与传统视频生成固定长度片段不同，世界模型采用迭代方式，在每个时间步接收动作并预测下一状
态，从而提供持续反馈。
在这一迭代框架中，记忆机制成为系统的基石。记忆存储并维护前一时间步的空间信息、语义信息或隐
状态，确保下一阶段生成内容在场景布局、物体属性和运动逻辑方面与先前上下文保持长期一致性。本
质上，记忆机制使世界模型能够处理长期的时间依赖关系，并实现可信的仿真交互。
此前，记忆建模依赖于简单的缓冲方法。帧采样（Frame Sampling）使生成过程基于少量历史帧 (Bruce
et al., 2024)。虽然直观，但导致了上下文碎片化和感知漂移，早期细节逐渐丢失。滑动窗口（Sliding
Window）方法借鉴了如注意力下沉和局部键值缓存等大语言模型技术 (Liu et al., 2025e)。尽管这解决
了计算瓶颈问题，却将记忆限制在固定窗口内。一旦物体离开该视图，模型便等效地将其遗忘，难以完
成环闭合等复杂任务。
到 2025 年底，该领域从有限的上下文窗口转向结构化的状态表示。当前架构主要沿着三条路径发展：
• 状态空间模型（SSMs）架构，如长上下文 SSMs，采用类似 Mamba 的骨干网络 (Po et al., 2025;
Yu et al., 2025f)。这些模型将无限历史压缩为固定大小的递归状态，从而在推理成本恒定的情况
下实现理论上无限的记忆容量。
• 显式记忆库。与压缩状态不同，这些系统维护一个外部的历史表示存储，以支持精确召回。其结
构逻辑各不相同：UniWM 采用分层设计，通过基于特征的相似度门控将短期感知与长期历史分
离 (Dong et al., 2025b)。相反，基于检索的方法（如 WorldMem 和 Context-as-Memory，CaM）
则保持一个扁平的记忆库来存储过去的上下文，利用几何检索（例如视场重叠）动态选择相关帧，
以维持三维场景的一致性 (Xiao et al., 2025c; Yu et al., 2025c)。
• 稀疏记忆与检索为了在长期一致性与效率之间取得平衡，Genie Envisioner 和 Ctrl-World 采用稀
疏记忆机制 (Liao et al., 2025b; Guo et al., 2025)。这些模型通过注入稀疏采样的历史帧或检索姿
态条件的上下文，增强当前观测，以锚定预测并防止操作任务中的漂移。
7.6.2 未来展望
从架构角度看，该领域正经历一场根本性转变，即从关注被动保留的数据缓存，转向关注主动维护的状
态仿真。这一演化目前正凝练为两种截然不同的范式，旨在解决实时响应性与长期逻辑一致性之间的冲
突。
• 双系统架构。受认知科学启发，世界模型可被划分为快速和慢速两个部分。系统 1 代表快速且直
觉性的层，利用如 SSM 等高效骨干网络处理即时物理和流体交互。系统 2 代表缓慢且深思熟虑
的层，通过大规模视觉语言模型或显式数据库处理复杂推理、规划及世界一致性问题。
• 主动内存管理。被动机制正被主动内存策略所取代。新模型不再将内存视为一个固定的缓冲区，盲
目存储近期历史，而是设计为认知工作空间，根据任务的相关性主动整理、总结并丢弃信息。最近
的实证研究显示，这种主动内存管理在处理功能性的无限上下文时，显著优于静态检索方法。这
一转变标志着从单纯记忆前 N 个 token，转向维护一个连贯且可查询的世界状态。
68

7.7 可信内存
7.7.1 回溯：从可信的 RAG 到可信的记忆
正如本综述中所示，记忆在实现智能体行为方面起着基础性作用，支持持久性、个性化和持续学习。然
而，随着记忆系统越来越深入地嵌入基于大语言模型的智能体中，可信性问题变得至关重要。
早期关于检索增强生成（RAG）系统中幻觉和事实性的问题 (Niu et al., 2024; Sun et al., 2025e; Lu
et al., 2025c)，现已演变为对记忆增强智能体更广泛的信任讨论。与 RAG 类似，使用外部或长期记忆
的主要动机之一是通过将模型输出基于可检索的事实内容，来减少幻觉 (Ru et al., 2024; Wang et al.,
2025c)。然而，与 RAG 不同的是，智能体记忆通常存储用户特定的、持久的且可能敏感的内容，涵盖
从事实知识到过往交互、偏好或行为迹线等各种信息。这在隐私、可解释性和安全性方面引入了额外挑
战。
最近的研究 Wang et al. (2025b) 表明，记忆模块可能通过间接的基于提示的攻击泄露私有数据，凸显
了记忆化和过度保留的风险。与此同时， Wu et al. (2025g) 认为，智能体记忆系统必须支持显式的 访
问控制、可验证遗忘和 可审计更新机制，才能保持可信性。值得注意的是，在记忆持续时间较长的智能
体场景中，此类风险被进一步放大。
可解释性仍然是一个关键瓶颈。尽管显式记忆（如文本日志或键-值数据库）提供了一定程度的透明
性，但用户和开发者仍然缺乏工具来追踪哪些记忆项被检索、它们如何影响生成过程，或者是否存在
滥用情况。在这方面，诊断工具如 RAGChecker (Ru et al., 2024) 以及冲突解决框架如 RAMDocs 与
MADAM-RAG (Wang et al., 2025d) 为在不确定性下的记忆使用追踪和推理提供了启发。
此外，除了个体记忆之外，Shi et al. (2025d) 和 Rezazadeh et al. (2025a) 强调了在共享或联邦记忆系
统中，集体隐私正日益重要，这类系统可能跨越多智能体部署或组织运行。所有这些发展共同表明，有
必要将信任提升为记忆设计中的首要原则。
7.7.2 未来展望
展望未来，我们认为可信记忆必须建立在三个相互关联的支柱之上：隐私保护、可解释性和 幻觉鲁棒
性——每一项都要求在架构和算法上进行创新。
为了保护隐私，未来的系统应支持细粒度的授权内存、由用户控制的保留策略、加密或设备本地存储，
以及在需要时的联邦访问 (Wu et al., 2025g; Shi et al., 2025d; Rezazadeh et al., 2025a)。差分隐私、记
忆删减和自适应遗忘（例如基于衰减的模型或用户擦除界面）等技术可作为防止记忆和泄露的保障措
施 (Chhikara et al., 2025)。
可解释性要求超越可见内容，包含可追溯的访问路径、自我合理化的检索，以及可能的反事实推理（例
如，如果没有这条记忆会有什么不同？） (OpenAI, 2024; Zhang et al., 2025u)。记忆注意力的可视化、
记忆影响的因果图以及面向用户的调试工具可能会成为标准组成部分。
幻觉缓解将受益于冲突检测、多文档推理以及不确定性感知生成等方面的持续进展。诸如在低置信度检
索下选择不回答、回退到模型先验 (Wang et al., 2025c)，或采用多智能体交叉验证 (Hu et al., 2024) 等
策略颇具前景。除了行为层面的防护措施外，新兴的机制可解释性技术提供了一条互补路径，通过分析
内部表示和推理电路如何导致幻觉输出来实现深入理解。诸如表示层探测和推理路径分解等方法能够实
69

现对幻觉起源位置的更细粒度诊断，并提供有原则的干预与控制工具 (Sun et al., 2025e,c)。
从长远来看，我们设想由类似操作系统（OS）的抽象所支配的记忆系统：分段式、版本控制、可审计，
并由智能体与用户共同管理 (Packer et al., 2023b)。构建此类系统将需要在表示学习、系统设计和策略
控制等多个领域开展协同努力。随着大语言模型智能体开始在持久且开放的环境中运行，可信记忆不仅
是一种理想特性，更将成为现实世界部署的基础性要求。
7.8 人脑认知连接
7.8.1 回望
当代智能体记忆系统的架构已与过去一个世纪建立的人类认知基础模型趋于一致。当前主流的设计将
容量受限的上下文窗口与大规模外部向量数据库相结合，这与 Atkinson-Shiffrin 多存储模型 (Atkinson
and Shiffrin, 1968) 相似，有效地实现了工作记忆与长期记忆之间区别的仿生对应 (Baddeley, 2012)。此
外，智能体记忆划分为交互日志、世界知识和基于代码的技能，其结构与 Tulving 对情景、语义和程序
记忆的分类呈现出显著的结构一致性 (Tulving, 1972; Squire, 2004)。当前的框架 (Zhong et al., 2024;
Park et al., 2023; Gutierrez et al., 2024; Li et al., 2025k) 将这些生物类别转化为工程化实体，其中情景
记忆提供自传式连续性，语义记忆则提供泛化的世界知识。
尽管存在这些结构上的相似性，检索与维持的动态仍存在根本性差异。人类记忆运作是一种建构性过
程，大脑根据当前认知状态主动重构过去的事件，而非重放确切的记录 (Schacter and Addis, 2007)。相
比之下，大多数现有的智能体记忆系统依赖于逐字检索机制（如 RAG），将记忆视为通过语义相似度查
询的不可变 token 的存储库 (Packer et al., 2023b; Chhikara et al., 2025)。因此，尽管智能体拥有对过
去的准确记录，却缺乏生物体所具备的记忆扭曲、抽象以及历史动态重塑的能力，而这些正是人类智能
的特征。
7.8.2 未来展望
为了弥合静态存储与动态认知之间的鸿沟，下一代智能体必须超越单一的在线更新，通过引入类似生
物睡眠的离线巩固机制实现进化。借鉴互补学习系统（CLS）理论 (Kumaran et al., 2016; McClelland
et al., 1995)，未来的架构很可能会引入专门的巩固时段，在此期间智能体脱离环境交互，进行记忆重组
和生成式回放 (Mattar and Daw, 2018)。在这些离线阶段，智能体可自主地从原始的情景迹中提炼出可
泛化的模式，执行主动遗忘以剔除冗余噪声 (Anderson and Hulbert, 2021)，并在无实时处理延迟约束
的情况下优化其内部索引。
最终，这种演化暗示了记忆形式与功能的范式转变：从显式的文本检索转向生成式重构。未来的系统可
能利用生成式记忆 (Zhang et al., 2025d)，使智能体按需合成潜在的记忆 token，模仿大脑的重构特性。
通过整合类睡眠的巩固周期，智能体将从仅存档数据的实体演变为内化经验的实体，通过周期性地将庞
大的情景流压缩为高效、参数化的直觉，解决可塑性-稳定性窘境。
8 结论
本综述考察了智能体记忆作为现代基于大语言模型的 Agentic 系统中的一项基础组件。通过将现有研
究置于形式、功能与动态这一统一视角下，我们厘清了智能体记忆的概念图景，并将其置于 Agentic 智
70

能演化的更广阔背景之中。在形式层面，我们识别出三种主要实现方式：token 级、参数化和潜在记忆，
每种形式近年来均经历了显著且迅速的发展，反映出其在表示、适应性以及与智能体策略集成方面根本
不同的权衡。在功能层面，我们超越了以往综述中普遍存在的长期记忆与短期记忆的粗略二分法，提出
了一种更为精细且全面的分类体系，根据其在知识保留、能力积累和任务级推理中的作用，区分了事实
性、经验性和工作记忆。这些视角共同表明，记忆并非仅仅是辅助性的存储机制，而是智能体实现时间
连贯性、持续适应性以及长周期能力的关键基础。
除了梳理已有研究，我们还识别出若干关键挑战和新兴方向，这些指向智能体记忆研究的下一阶段。特
别是强化学习的日益融合、多模态与多智能体情景的兴起，以及从以检索为中心转向生成式记忆范式的
转变，预示着未来记忆系统将实现完全可学习、自适应且自我组织。此类系统有望将大型语言模型从强
大但静态的生成器转变为能够持续交互、自我改进并随时间进行有原则推理的智能体。
我们希望本次调查能为未来的研究提供一个连贯的基础，并成为研究人员和实践者的重要参考。随着智
能体系统不断成熟，记忆设计将持续成为一个核心且开放的问题，这一问题很可能在构建稳健、通用且
持久的人工智能方面发挥决定性作用。
References
AadharshAadhithyaA,SachinKumarS,andSomanK.P.Enhancinglong-termmemoryusinghierarchicalaggregate
tree for retrieval augmented generation, 2024. https://arxiv.org/abs/2406.06124.
Saaket Agashe, Jiuzhou Han, Shuyu Gan, Jiachen Yang, Ang Li, and Xin Eric Wang. Agent S: An Open Agen-
tic Framework that Uses Computers Like a Human. In The Thirteenth International Conference on Learning
Representations, ICLR 2025, Singapore, April 24-28, 2025. OpenReview.net, 2025.
AgentScope. GitHub - agentscope-ai/ReMe: ReMe: Memory Management Kit for Agents - Remember Me, Refine
Me. — github.com. https://github.com/agentscope-ai/ReMe, 2025. [Accessed 14-12-2025].
Qingyao Ai, Yichen Tang, Changyue Wang, Jianming Long, Weihang Su, and Yiqun Liu. Memorybench: A bench-
mark for memory and continual learning in llm systems. arXiv preprint arXiv:2510.17281, 2025.
ReemAleithan,HaoranXue,MohammadMahdiMohajer,ElijahNnorom,GiasUddin,andSongWang.Swe-bench+:
Enhanced coding benchmark for llms, 2024. https://arxiv.org/abs/2410.06992.
Nick Alonso, Tomas Figliolia, Anthony Ndirango, and Beren Millidge. Toward conversational agents with context
and time sensitive long-term memory. CoRR, abs/2406.00057, 2024. doi: 10.48550/ARXIV.2406.00057. https:
//doi.org/10.48550/arXiv.2406.00057.
MichaelC.AndersonandJustinC.Hulbert. Activeforgetting: Adaptationofmemorybyprefrontalcontrol. Annual
Review of Psychology, 72:1–36, January 2021. ISSN 1545-2085. doi: 10.1146/annurev-psych-072720-094140.
Petr Anokhin, Nikita Semenov, Artyom Sorokin, Dmitry Evseev, Andrey Kravchenko, Mikhail Burtsev, and Evgeny
Burnaev. Arigraph: Learningknowledgegraphworldmodelswithepisodicmemoryforllmagents. arXiv preprint
arXiv:2407.04363, 2024.
AkariAsai,ZeqiuWu,YizhongWang,AvirupSil,andHannanehHajishirzi. Self-rag: Learningtoretrieve,generate,
and critique through self-reflection, 2023. https://arxiv.org/abs/2310.11511.
R.C.AtkinsonandR.M.Shiffrin. Humanmemory: Aproposedsystemanditscontrolprocesses. InThePsychology
of Learning and Motivation: II, pages xi, 249–xi, 249. Academic Press, Oxford, England, 1968. doi: 10.1016/
S0079-7421(08)60422-3.
71

Alan Baddeley. Working Memory: Theories, Models, and Controversies. Annual Review of Psychology, 63(Volume
63, 2012):1–29, January 2012. ISSN 0066-4308, 1545-2085. doi: 10.1146/annurev-psych-120710-100422.
YushiBai,XinLv,JiajieZhang,HongchangLyu,JiankaiTang,ZhidianHuang,ZhengxiaoDu,XiaoLiu,AohanZeng,
Lei Hou, Yuxiao Dong, Jie Tang, and Juanzi Li. LongBench: A bilingual, multitask benchmark for long context
understanding.InProceedingsofthe62ndAnnualMeetingoftheAssociationforComputationalLinguistics(Volume
1: Long Papers), pages 3119–3137, Bangkok, Thailand, August 2024. Association for Computational Linguistics.
doi: 10.18653/v1/2024.acl-long.172. https://aclanthology.org/2024.acl-long.172/.
YushiBai,ShangqingTu,JiajieZhang,HaoPeng,XiaozhiWang,XinLv,ShulinCao,JiazhengXu,LeiHou,Yuxiao
Dong, et al. Longbench v2: Towards deeper understanding and reasoning on realistic long-context multitasks. In
Proceedingsofthe63rdAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1: LongPapers),
pages 3639–3664, 2025.
Alexandre Bailly, Antoine Saubin, Gabriel Kocevar, and Jonathan Bodin. Divide and summarize: improve slm text
summarization. Frontiers in Artificial Intelligence, 8:1604034, 2025.
AliBehrouz, Meisam Razaviyayn, PeilinZhong, and VahabMirrokni. Nested learning: The illusion of deep learning
architectures. In The Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025a. https:
//openreview.net/forum?id=nbMeRvNb7A.
AliBehrouz,PeilinZhong,andVahabMirrokni. Titans: Learningtomemorizeattesttime. CoRR,abs/2501.00663,
2025b. doi: 10.48550/ARXIV.2501.00663. https://doi.org/10.48550/arXiv.2501.00663.
Weihao Bo, Shan Zhang, Yanpeng Sun, Jingjing Wu, Qunyi Xie, Xiao Tan, Kunbin Chen, Wei He, Xiaofan Li,
Na Zhao, Jingdong Wang, and Zechao Li. Agentic learner with grow-and-refine multimodal semantic memory,
2025. https://arxiv.org/abs/2511.21678.
Islem Bouzenia, Premkumar Devanbu, and Michael Pradel. RepairAgent: An Autonomous, LLM-Based Agent for
Program Repair, October 2024. http://arxiv.org/abs/2403.17134. arXiv:2403.17134 [cs].
JakeBruce,MichaelDDennis,AshleyEdwards,JackParker-Holder,YugeShi,EdwardHughes,MatthewLai,Aditi
Mavalankar, Richie Steigerwald, Chris Apps, et al. Genie: Generative interactive environments. In Forty-first
International Conference on Machine Learning, 2024.
YuzhengCai,SiqiCai,YuchenShi,ZihanXu,LichaoChen,YuleiQin,XiaoyuTan,GangLi,ZongyiLi,HaojiaLin,
Yong Mao, Ke Li, and Xing Sun. Training-free group relative policy optimization, 2025a. https://arxiv.org/
abs/2510.08191.
Zefan Cai, Yichi Zhang, Bofei Gao, Yuliang Liu, Tianyu Liu, Keming Lu, Wayne Xiong, Yue Dong, Baobao Chang,
JunjieHu,andWenXiao. Pyramidkv: DynamicKVcachecompressionbasedonpyramidalinformationfunneling.
CoRR,abs/2406.02069,2024. doi: 10.48550/ARXIV.2406.02069. https://doi.org/10.48550/arXiv.2406.02069.
Zhicheng Cai, Xinyuan Guo, Yu Pei, Jiangtao Feng, Jinsong Su, Jiangjie Chen, Ya-Qin Zhang, Wei-Ying Ma,
Mingxuan Wang, and Hao Zhou. Flex: Continuous agent evolution via forward learning from experience, 2025b.
https://arxiv.org/abs/2511.06449.
CAMEL-AI. Workforce —camel-ai documentation. https://docs.camel-ai.org/key_modules/workforce, 2025.
Accessed: 2025-08-09.
Nicola De Cao, Wilker Aziz, and Ivan Titov. Editing factual knowledge in language models. In Proceedings of the
2021 Conference on Empirical Methods in Natural Language Processing, pages 6491–6506, 2021.
Maitreyi Chatterjee and Devansh Agarwal. Semantic anchoring in agentic memory: Leveraging linguistic structures
72

for persistent conversational context. CoRR, abs/2508.12630, 2025. doi: 10.48550/ARXIV.2508.12630. https:
//doi.org/10.48550/arXiv.2508.12630.
Baian Chen, Chang Shu, Ehsan Shareghi, Nigel Collier, Karthik Narasimhan, and Shunyu Yao. Fireact: Toward
language agent fine-tuning, 2023a. https://arxiv.org/abs/2310.05915.
Dake Chen, Hanbin Wang, Yunhao Huo, Yuzhao Li, and Haoyang Zhang. GameGPT: Multi-agent Collaborative
Framework for Game Development. CoRR, abs/2310.08067, 2023b. doi: 10.48550/ARXIV.2310.08067.
Guoxin Chen, Zile Qiao, Xuanzhong Chen, Donglei Yu, Haotian Xu, Wayne Xin Zhao, Ruihua Song, Wenbiao Yin,
Huifeng Yin, Liwen Zhang, Kuan Li, Minpeng Liao, Yong Jiang, Pengjun Xie, Fei Huang, and Jingren Zhou.
Iterresearch: Rethinkinglong-horizonagentsviamarkovianstatereconstruction,2025a. https://arxiv.org/abs/
2511.07327.
KaiyuanChen,YixinRen,YangLiu,XiaoboHu,HaotongTian,TianbaoXie,FangfuLiu,HaoyeZhang,Hongzhang
Liu, Yuan Gong, Chen Sun, Han Hou, Hui Yang, James Pan, Jianan Lou, Jiayi Mao, Jizheng Liu, Jinpeng Li,
Kangyi Liu, Kenkun Liu, Rui Wang, Run Li, Tong Niu, Wenlong Zhang, Wenqi Yan, Xuanzheng Wang, Yuchen
Zhang, Yi-Hsin Hung, Yuan Jiang, Zexuan Liu, Zihan Yin, Zijian Ma, and Zhiwen Mo. xbench: Tracking agents
productivity scaling with profession-aligned real-world evaluations, 2025b. https://arxiv.org/abs/2506.13651.
NuoChen,HongguangLi,JianhuiChang,JuhuaHuang,BaoyuanWang,andJiaLi.Compresstoimpress: Unleashing
the potential of compressive memory in real-world long-term conversations. In Owen Rambow, Leo Wanner,
MariannaApidianaki,HendAl-Khalifa,BarbaraDiEugenio,andStevenSchockaert,editors,Proceedingsofthe31st
International Conference on Computational Linguistics, COLING 2025, Abu Dhabi, UAE, January 19-24, 2025,
pages755–773.AssociationforComputationalLinguistics,2025c.https://aclanthology.org/2025.coling-main.
51/.
Qiuhui Chen, Qiang Fu, Hao Bai, and Yi Hong. Longformer: Longitudinal transformer for alzheimer’s disease
classificationwithstructuralmris. InIEEE/CVF Winter Conference on Applications of Computer Vision, WACV
2024, Waikoloa, HI, USA, January 3-8, 2024, pages 3563–3572. IEEE, 2024a. doi: 10.1109/WACV57701.2024.
00354. https://doi.org/10.1109/WACV57701.2024.00354.
Weishu Chen, Jinyi Tang, Zhouhui Hou, Shihao Han, Mingjie Zhan, Zhiyuan Huang, Delong Liu, Jiawei Guo,
Zhicheng Zhao, and Fei Su. Moom: Maintenance, organization and optimization of memory in ultra-long role-
playing dialogues, 2025d. https://arxiv.org/abs/2509.11860.
XiuyingChen,ShenGao,MingzheLi,QingqingZhu,XinGao,andXiangliangZhang. Writesummarystep-by-step:
A pilot study of stepwise summarization. IEEE/ACM Transactions on Audio, Speech, and Language Processing,
32:1406–1415, 2024b.
Yinpeng Chen, DeLesley Hutchins, Aren Jansen, Andrey Zhmoginov, David Racz, and Jesper Andersen. Melodi:
Exploring memory compression for long contexts, 2024c. https://arxiv.org/abs/2410.03156.
ZhaorunChen,ZhuokaiZhao,KaiZhang,BoLiu,QiQi,YifanWu,TarunKalluri,SaraCao,YuanhaoXiong,Haibo
Tong,HuaxiuYao,HengduoLi,JiachengZhu,XianLi,DawnSong,BoLi,JasonWeston,andDatHuynh. Scaling
agent learning via experience synthesis, 2025e. https://arxiv.org/abs/2511.03773.
Ho Kei Cheng and Alexander G. Schwing. Xmem: Long-term video object segmentation with an atkinson-shiffrin
memory model, 2022. https://arxiv.org/abs/2207.07115.
AlexisChevalier,AlexanderWettig,AnirudhAjith,andDanqiChen.Adaptinglanguagemodelstocompresscontexts.
InHoudaBouamor,JuanPino,andKalikaBali,editors,Proceedingsofthe2023ConferenceonEmpiricalMethods
in Natural Language Processing, EMNLP 2023, Singapore, December 6-10, 2023,pages3829–3846.Associationfor
73

Computational Linguistics, 2023. doi: 10.18653/V1/2023.EMNLP-MAIN.232. https://doi.org/10.18653/v1/
2023.emnlp-main.232.
MaximeChevalier-Boisvert,DzmitryBahdanau,SalemLahlou,LucasWillems,ChitwanSaharia,ThienHuuNguyen,
and Yoshua Bengio. Babyai: A platform to study the sample eﬀiciency of grounded language learning, 2019.
https://arxiv.org/abs/1810.08272.
PrateekChhikara,DevKhant,SaketAryan,TaranjeetSingh,andDeshrajYadav. Mem0: Buildingproduction-ready
ai agents with scalable long-term memory. arXiv preprint arXiv:2504.19413, 2025.
Eunseong Choi, June Park, Hyeri Lee, and Jongwuk Lee. Conflict-aware soft prompting for retrieval-augmented
generation. CoRR,abs/2508.15253,2025. doi: 10.48550/ARXIV.2508.15253. https://doi.org/10.48550/arXiv.
2508.15253.
Cognee. GitHub-topoteretes/cognee: MemoryforAIAgentsin6linesofcode. https://github.com/topoteretes/
cognee, 2025. [Accessed 14-12-2025].
NelsonCowan.WorkingMemoryUnderpinsCognitiveDevelopment,Learning,andEducation.Educationalpsychology
review, 26(2):197–223, June 2014. ISSN 1040-726X. doi: 10.1007/s10648-013-9246-y.
Tri Dao. Flashattention-2: Faster attention with better parallelism and work partitioning. In The Twelfth Interna-
tional Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024. OpenReview.net,
2024. https://openreview.net/forum?id=mZn2Xyh9Ec.
Nicola De Cao, Wilker Aziz, and Ivan Titov. Editing factual knowledge in language models. In Marie-Francine
Moens, Xuanjing Huang, Lucia Specia, and Scott Wen-tau Yih, editors, Proceedings of the 2021 Conference
on Empirical Methods in Natural Language Processing, pages 6491–6506, Online and Punta Cana, Dominican
Republic, November 2021. Association for Computational Linguistics. doi: 10.18653/v1/2021.emnlp-main.522.
https://aclanthology.org/2021.emnlp-main.522/.
DeepSeek-AI,DayaGuo,DejianYang,HaoweiZhang,JunxiaoSong,RuoyuZhang,RunxinXu,QihaoZhu,Shirong
Ma,PeiyiWang,XiaoBi,XiaokangZhang,XingkaiYu,YuWu,Z.F.Wu,ZhibinGou,ZhihongShao,ZhuoshuLi,
Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi
Deng,ChenyuZhang, ChongRuan,DamaiDai, DeliChen,DongjieJi, ErhangLi, FangyunLin,FucongDai, Fuli
Luo,GuangboHao,GuantingChen,GuoweiLi,H.Zhang,HanBao,HanweiXu,HaochengWang,HonghuiDing,
Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang
Yuan,JunjieQiu,JunlongLi,J.L.Cai,JiaqiNi,JianLiang,JinChen,KaiDong,KaiHu,KaigeGao,KangGuan,
Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia,
Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan
Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji
Wang, R. J. Chen, R. L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu
Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S. S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun,
TianPei,TianyuSun,T.Wang,WangdingZeng,WanjiaZhao,WenLiu,WenfengLiang,WenjunGao,WenqinYu,
WentaoZhang,W.L.Xiao,WeiAn,XiaodongLiu,XiaohanWang,XiaokangChen,XiaotaoNie,XinCheng,Xin
Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X. Q. Li, Xiangyue Jin, Xiaojin
Shen,XiaoshaChen,XiaowenSun,XiaoxiangWang,XinnanSong,XinyiZhou,XianzuWang,XinxiaShan,Y.K.
Li, Y. Q. Wang, Y. X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu,
YichaoZhang,YifanShi,YiliangXiong,YingHe,YishiPiao,YisongWang,YixuanTan,YiyangMa,YiyuanLiu,
YongqiangGuo,YuanOu,YuduanWang,YueGong,YuhengZou,YujiaHe,YunfanXiong,YuxiangLuo,Yuxiang
You, Yuxuan Liu, Yuyang Zhou, Y. X. Zhu, Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu,
Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda
74

Xie,ZhengyanZhang,ZhewenHao,ZhichengMa,ZhigangYan,ZhiyuWu,ZihuiGu,ZijiaZhu,ZijunLiu,ZilinLi,
Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, and Zhen Zhang. Deepseek-r1:
Incentivizing reasoning capability in llms via reinforcement learning, 2025. https://arxiv.org/abs/2501.12948.
Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Samual Stevens, Boshi Wang, Huan Sun, and Yu Su.
Mind2Web: Towards a Generalist Agent for the Web. In Alice Oh, Tristan Naumann, Amir Globerson,
Kate Saenko, Moritz Hardt, and Sergey Levine, editors, Advances in Neural Information Processing Sys-
tems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023, New Or-
leans, LA, USA, December 10 - 16, 2023, 2023. http://papers.nips.cc/paper_files/paper/2023/hash/
5950bf290a1570ea401bf98882128160-Abstract-Datasets_and_Benchmarks.html.
Yang Deng, Xuan Zhang, Wenxuan Zhang, Yifei Yuan, See-Kiong Ng, and Tat-Seng Chua. On the multi-turn
instruction following for conversational web agents. In Proceedings of the 62nd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers), pages 8795–8812, Bangkok, Thailand, August 2024.
Association for Computational Linguistics. doi: 10.18653/v1/2024.acl-long.477. https://aclanthology.org/
2024.acl-long.477/.
Junnan Dong, Siyu An, Yifei Yu, Qian-Wen Zhang, Linhao Luo, Xiao Huang, Yunsheng Wu, Di Yin, and Xing
Sun. Youtu-graphrag: Vertically unified agents for graph retrieval-augmented complex reasoning, 2025a. https:
//arxiv.org/abs/2508.19855.
Yifei Dong, Fengyi Wu, Guangyu Chen, Zhi-Qi Cheng, Qiyu Hu, Yuxuan Zhou, Jingdong Sun, Jun-Yan He, Qi Dai,
and Alexander G Hauptmann. Unified world models: Memory-augmented planning and foresight for visual navi-
gation. arXiv preprint arXiv:2510.08713, 2025b.
Yiming Du, Hongru Wang, Zhengyi Zhao, Bin Liang, Baojun Wang, Wanjun Zhong, Zezhong Wang, and Kam-Fai
Wong. PerLTQA:Apersonallong-termmemorydatasetformemoryclassification,retrieval,andfusioninquestion
answering. In Proceedings of the 10th SIGHAN Workshop on Chinese Language Processing (SIGHAN-10), pages
152–164, Bangkok, Thailand, August 2024. Association for Computational Linguistics. https://aclanthology.
org/2024.sighan-1.18/.
Yiming Du, Wenyu Huang, Danna Zheng, Zhaowei Wang, Sebastien Montella, Mirella Lapata, Kam-Fai Wong,
and Jeff Z Pan. Rethinking memory in ai: Taxonomy, operations, topics, and future directions. arXiv preprint
arXiv:2505.00675, 2025a.
Yiming Du, Bingbing Wang, Yang He, Bin Liang, Baojun Wang, Zhongyang Li, Lin Gui, Jeff Z. Pan, Ruifeng Xu,
and Kam-FaiWong. Memguide: Intent-driven memory selection for goal-orientedmulti-sessionllm agents, 2025b.
https://arxiv.org/abs/2505.20231.
ZaneDurante,QiuyuanHuang,NaokiWake,RanGong,JaeSungPark,BidiptaSarkar,RohanTaori,YusukeNoda,
DemetriTerzopoulos,YejinChoi,KatsushiIkeuchi,HoiVo,LiFei-Fei,andJianfengGao. Agentai: Surveyingthe
horizons of multimodal interaction, 2024. https://arxiv.org/abs/2401.03568.
DarrenEdge,HaTrinh,NewmanCheng,JoshuaBradley,AlexChao,ApurvaMody,StevenTruitt,DashaMetropoli-
tansky,RobertOsazuwaNess,andJonathanLarson. Fromlocaltoglobal: Agraphragapproachtoquery-focused
summarization, 2025. https://arxiv.org/abs/2404.16130.
Yue Fan, Xiaojian Ma, Rongpeng Su, Jun Guo, Rujie Wu, Xi Chen, and Qing Li. Embodied videoagent: Per-
sistent memory from egocentric videos and embodied sensors enables dynamic scene understanding. CoRR,
abs/2501.00358, 2025. doi: 10.48550/ARXIV.2501.00358. https://doi.org/10.48550/arXiv.2501.00358.
Jinyuan Fang, Yanwen Peng, Xi Zhang, Yingxu Wang, Xinhao Yi, Guibin Zhang, Yi Xu, Bin Wu, Siwei Liu,
Zihao Li, Zhaochun Ren, Nikos Aletras, Xi Wang, Han Zhou, and Zaiqiao Meng. A comprehensive survey of
75

self-evolving ai agents: A new paradigm bridging foundation models and lifelong agentic systems, 2025a. https:
//arxiv.org/abs/2508.07407.
Jizhan Fang, Xinle Deng, Haoming Xu, Ziyan Jiang, Yuqi Tang, Ziwen Xu, Shumin Deng, Yunzhi Yao, Mengru
Wang, Shuofei Qiao, et al. Lightmem: Lightweight and eﬀicient memory-augmented generation. arXiv preprint
arXiv:2510.18866, 2025b.
Junfeng Fang, Houcheng Jiang, Kun Wang, Yunshan Ma, Shi Jie, Xiang Wang, Xiangnan He, and Tat seng Chua.
Alphaedit: Null-space constrained knowledge editing for language models, 2025c. https://arxiv.org/abs/2410.
02355.
Runnan Fang, Yuan Liang, Xiaobin Wang, Jialong Wu, Shuofei Qiao, Pengjun Xie, Fei Huang, Huajun Chen, and
Ningyu Zhang. Memp: Exploring agent procedural memory, 2025d. https://arxiv.org/abs/2508.06433.
Erhu Feng, Wenbo Zhou, Zibin Liu, Le Chen, Yunpeng Dong, Cheng Zhang, Yisheng Zhao, Dong Du, Zhi-Hua
Zhou, Yubin Xia, and Haibo Chen. Get experience from practice: LLM agents with record & replay. CoRR,
abs/2505.17716, 2025. doi: 10.48550/ARXIV.2505.17716. https://doi.org/10.48550/arXiv.2505.17716.
ZafeiriosFountas,MartinBenfeghoul,AdnanOomerjee,FeniaChristopoulou,GerasimosLampouras,HaithamBou-
Ammar,andJunWang.Human-inspiredepisodicmemoryforinfinitecontextllms.InTheThirteenthInternational
ConferenceonLearningRepresentations,ICLR2025,Singapore,April24-28,2025.OpenReview.net,2025. https:
//openreview.net/forum?id=BI2int5SAC.
Chen Gao, Xiaochong Lan, Zhihong Lu, Jinzhu Mao, Jinghua Piao, Huandong Wang, Depeng Jin, and Yong
Li. S\(^\mbox3\): Social-network Simulation System with Large Language Model-Empowered Agents. CoRR,
abs/2307.14984, 2023a. doi: 10.48550/ARXIV.2307.14984.
Hang Gao and Yongfeng Zhang. Memory sharing for large language model based agents. CoRR, abs/2404.09982,
2024a. doi: 10.48550/ARXIV.2404.09982. https://doi.org/10.48550/arXiv.2404.09982.
Hang Gao and Yongfeng Zhang. Memory Sharing for Large Language Model based Agents. CoRR, abs/2404.09982,
2024b. doi: 10.48550/ARXIV.2404.09982.
Hang Gao and Yongfeng Zhang. PTR: Precision-Driven Tool Recommendation for Large Language Models. CoRR,
abs/2411.09613,2024c.doi: 10.48550/ARXIV.2411.09613.https://doi.org/10.48550/arXiv.2411.09613.arXiv:
2411.09613.
Huan-angGao,JiayiGeng,WenyueHua,MengkangHu,XinzheJuan,HongzhangLiu,ShilongLiu,JiahaoQiu,Xuan
Qi, Yiran Wu, Hongru Wang, Han Xiao, Yuhang Zhou, Shaokun Zhang, Jiayi Zhang, Jinyu Xiang, Yixiong Fang,
QiwenZhao,DongruiLiu,QihanRen,ChengQian,ZhenhailongWang,MindaHu,HuazhengWang,QingyunWu,
HengJi,andMengdiWang. Asurveyofself-evolvingagents: Onpathtoartificialsuperintelligence,August2025.
Luyu Gao, Xueguang Ma, Jimmy Lin, and Jamie Callan. Precise zero-shot dense retrieval without relevance labels.
In Anna Rogers, Jordan L. Boyd-Graber, and Naoaki Okazaki, editors, Proceedings of the 61st Annual Meeting of
the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2023, Toronto, Canada, July 9-14,
2023,pages1762–1777.AssociationforComputationalLinguistics,2023b. doi: 10.18653/V1/2023.ACL-LONG.99.
https://doi.org/10.18653/v1/2023.acl-long.99.
Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Meng Wang, and
Haofen Wang. Retrieval-augmented generation for large language models: A survey, 2024. https://arxiv.org/
abs/2312.10997.
Tao Ge, Jing Hu, Lei Wang, Xun Wang, Si-Qing Chen, and Furu Wei. In-context Autoencoder for Context Com-
76

pressioninaLargeLanguageModel. InTheTwelfthInternationalConferenceonLearningRepresentations, ICLR
2024, Vienna, Austria, May 7-11, 2024. OpenReview.net, 2024.
Samuel J. Gershman, Ila Fiete, and Kazuki Irie. Key-value memory in the brain. CoRR, abs/2501.02950, 2025. doi:
10.48550/ARXIV.2501.02950. https://doi.org/10.48550/arXiv.2501.02950.
AaronGrattafiori,AbhimanyuDubey,AbhinavJauhri,AbhinavPandey,AbhishekKadian,AhmadAl-Dahle,Aiesha
Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd of models. arXiv preprint
arXiv:2407.21783, 2024.
Albert Gu and Tri Dao. Mamba: Linear-time sequence modeling with selective state spaces, 2024. https://arxiv.
org/abs/2312.00752.
Yanjiang Guo, Lucy Xiaoyang Shi, Jianyu Chen, and Chelsea Finn. Ctrl-world: A controllable generative world
model for robot manipulation. arXiv preprint arXiv:2510.10125, 2025.
Saket Gurukar and Asim Kadav. Long-vmnet: Accelerating long-form video understanding via fixed memory, 2025.
https://arxiv.org/abs/2503.13707.
Bernal Jimenez Gutierrez, Yiheng Shu, Yu Gu, Michihiro Yasunaga, and Yu Su. HippoRAG: Neurobiologically
inspired long-term memory for large language models. In Advances in Neural Information Processing Systems,
2024.
Bernal Jiménez Gutiérrez, Yiheng Shu, Weijian Qi, Sizhe Zhou, and Yu Su. From rag to memory: Non-parametric
continual learning for large language models, 2025. https://arxiv.org/abs/2502.14802.
Dongge Han, Camille Couturier, Daniel Madrigal Diaz, Xuchao Zhang, Victor Rühle, and Saravan Rajmohan.
LEGOMem: ModularProceduralMemoryforMulti-agentLLMSystemsforWorkflowAutomation,October2025a.
http://arxiv.org/abs/2510.04851. arXiv:2510.04851 [cs].
Haoyu Han, Yu Wang, Harry Shomer, Kai Guo, Jiayuan Ding, Yongjia Lei, Mahantesh Halappanavar, Ryan A.
Rossi,SubhabrataMukherjee,XianfengTang,QiHe,ZhigangHua,BoLong,TongZhao,NeilShah,AminJavari,
YinglongXia,andJiliangTang. Retrieval-augmentedgenerationwithgraphs(graphrag),2025b. https://arxiv.
org/abs/2501.00309.
Jinyi Han, Xinyi Wang, Haiquan Zhao, Tingyun li, Zishang Jiang, Sihang Jiang, Jiaqing Liang, Xin Lin, Weikang
Zhou, Zeye Sun, Fei Yu, and Yanghua Xiao. A stitch in time saves nine: Proactive self-refinement for language
models, 2025c. https://arxiv.org/abs/2508.12903.
Jackson Hassell, Dan Zhang, Hannah Kim, Tom Mitchell, and Estevam Hruschka. Learning from supervision with
semanticandepisodicmemory: Areflectiveapproachtoagentadaptation. arXivpreprintarXiv:2510.19897,2025.
Bo He, Hengduo Li, Young Kyun Jang, Menglin Jia, Xuefei Cao, Ashish Shah, Abhinav Shrivastava, and Ser-Nam
Lim.MA-LMM:Memory-AugmentedLargeMultimodalModelforLong-TermVideoUnderstanding.InIEEE/CVF
ConferenceonComputerVisionandPatternRecognition,CVPR2024,Seattle,WA,USA,June16-22,2024,pages
13504–13514. IEEE, 2024. doi: 10.1109/CVPR52733.2024.01282.
Junqing He, Liang Zhu, Rui Wang, Xi Wang, Gholamreza Haffari, and Jiaxing Zhang. MADial-bench: Towards
real-world evaluation of memory-augmented dialogue generation. In Proceedings of the 2025 Conference of the
Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies
(Volume1: LongPapers),pages9902–9921,Albuquerque,NewMexico,April2025.AssociationforComputational
Linguistics. ISBN 979-8-89176-189-6. doi: 10.18653/v1/2025.naacl-long.499. https://aclanthology.org/2025.
naacl-long.499/.
77

PengchengHe,XiaodongLiu,JianfengGao,andWeizhuChen. Deberta: Decoding-enhancedbertwithdisentangled
attention. arXiv preprint arXiv:2006.03654, 2020.
Dan Hendrycks, Dawn Song, Christian Szegedy, Honglak Lee, Yarin Gal, Erik Brynjolfsson, Sharon Li, Andy Zou,
Lionel Levine, Bo Han, et al. A definition of agi. arXiv preprint arXiv:2510.18212, 2025.
Xanh Ho, Anh-Khoa Duong Nguyen, Saku Sugawara, and Akiko Aizawa. Constructing a multi-hop qa dataset for
comprehensive evaluation of reasoning steps, 2020. https://arxiv.org/abs/2011.01060.
Sirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang,
Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, and Jürgen Schmid-
huber. MetaGPT: Meta programming for A multi-agent collaborative framework. In The Twelfth International
Conference on Learning Representations, 2024.
Cheng-Ping Hsieh, Simeng Sun, Samuel Kriman, Shantanu Acharya, Dima Rekesh, Fei Jia, Yang Zhang, and
Boris Ginsburg. Ruler: What’s the real context size of your long-context language models? arXiv preprint
arXiv:2404.06654, 2024.
Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu
Chen. LoRA: Low-rankadaptationoflargelanguagemodels. InThe Tenth International Conference on Learning
Representations, 2022.
MengkangHu, TianxingChen, QiguangChen, YaoMu, WenqiShao, andPingLuo. HiAgent: HierarchicalWorking
MemoryManagementforSolvingLong-HorizonAgentTaskswithLargeLanguageModel. InWanxiangChe,Joyce
Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar, editors, Proceedings of the 63rd Annual Meeting of
the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2025, Vienna, Austria, July 27 -
August 1, 2025, pages 32779–32798. Association for Computational Linguistics, 2025a.
Shengran Hu, Cong Lu, and Jeff Clune. Automated design of agentic systems. In The Thirteenth International
Conference on Learning Representations, 2025b.
XiangkunHu,DongyuRu,LinQiu,QipengGuo,TianhangZhang,YangXu,YunLuo,PengfeiLiu,YueZhang,and
Zheng Zhang. Refchecker: Reference-based fine-grained hallucination checker and benchmark for large language
models. arXiv preprint arXiv:2405.14486, 2024.
YuanzheHu,YuWang,andJulianMcAuley.Evaluatingmemoryinllmagentsviaincrementalmulti-turninteractions.
arXiv preprint arXiv:2507.05257, 2025c.
Jen-tseHuang,KaiserSun,WenxuanWang,andMarkDredze. LanguageModelsDoNotHaveHuman-LikeWorking
Memory, September 2025a.
JianiHuang,XingchenZou,LianghaoXia,andQingLi. Mr.rec: Synergizingmemoryandreasoningforpersonalized
recommendation assistant with llms. CoRR, abs/2510.14629, 2025b. doi: 10.48550/ARXIV.2510.14629. https:
//doi.org/10.48550/arXiv.2510.14629.
Tenghao Huang, Kinjal Basu, Ibrahim Abdelaziz, Pavan Kapanipathi, Jonathan May, and Muhao Chen. R2D2:
Remembering, Replaying and Dynamic Decision Making with a Reflective Agentic Memory. In Wanxiang
Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar, editors, Proceedings of the 63rd
Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2025, Vi-
enna, Austria, July 27 - August 1, 2025, pages 30318–30330. Association for Computational Linguistics, 2025c.
https://aclanthology.org/2025.acl-long.1464/.
Xu Huang, Jianxun Lian, Yuxuan Lei, Jing Yao, Defu Lian, and Xing Xie. Recommender AI agent: Integrating
78

large language models for interactive recommendations. ACM Trans. Inf. Syst., 43(4):96:1–96:33, 2025d. doi:
10.1145/3731446. https://doi.org/10.1145/3731446.
Zeyu Huang, Yikang Shen, Xiaofeng Zhang, Jie Zhou, Wenge Rong, and Zhang Xiong. Transformer-patcher: One
mistake worth one neuron, 2023. https://arxiv.org/abs/2301.09785.
Md Ashraful Islam, Mohammed Eunus Ali, and Md Rizwan Parvez. MapCoder: Multi-Agent Code Generation for
Competitive Problem Solving. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar, editors, Proceedings of the
62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2024,
Bangkok, Thailand, August 11-16, 2024, pages 4912–4944. Association for Computational Linguistics, 2024. doi:
10.18653/V1/2024.ACL-LONG.269. https://doi.org/10.18653/v1/2024.acl-long.269.
Kai Tzu iunn Ong, Namyoung Kim, Minju Gwak, Hyungjoo Chae, Taeyoon Kwon, Yohan Jo, Seung won Hwang,
Dongha Lee, and Jinyoung Yeo. Towards lifelong dialogue agents via timeline-based memory management, 2025.
https://arxiv.org/abs/2406.10996.
Jingyi Jia and Qinbin Li. Autotool: Eﬀicient tool selection for large language model agents, November 2025.
ZixiJia,QinghuaLiu,HexiaoLi,YuyanChen,andJiqiangLiu. Evaluatingthelong-termmemoryoflargelanguage
models. In Findings of the Association for Computational Linguistics: ACL 2025, pages 19759–19777, Vienna,
Austria, July 2025. Association for Computational Linguistics. ISBN 979-8-89176-256-5. doi: 10.18653/v1/2025.
findings-acl.1014. https://aclanthology.org/2025.findings-acl.1014/.
BowenJiang,ZhuoqunHao,Young-MinCho,BryanLi,YuanYuan,SihaoChen,LyleUngar,CamilloJTaylor,and
DanRoth. Knowme,respondtome: Benchmarkingllmsfordynamicuserprofilingandpersonalizedresponsesat
scale. arXiv preprint arXiv:2504.14225, 2025a.
Huiqiang Jiang, Qianhui Wu, Chin-Yew Lin, Yuqing Yang, and Lili Qiu. LLMLingua: Compressing Prompts
for Accelerated Inference of Large Language Models. In Houda Bouamor, Juan Pino, and Kalika Bali, edi-
tors, Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, EMNLP 2023,
Singapore, December 6-10, 2023, pages 13358–13376. Association for Computational Linguistics, 2023. doi:
10.18653/V1/2023.EMNLP-MAIN.825.
HuiqiangJiang,QianhuiWu,XufangLuo,DongshengLi,Chin-YewLin,YuqingYang,andLiliQiu.LongLLMLingua:
Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression. In Lun-Wei Ku, Andre
Martins,andVivekSrikumar,editors,Proceedingsofthe62ndAnnualMeetingoftheAssociationforComputational
Linguistics (Volume 1: Long Papers), ACL 2024, Bangkok, Thailand, August 11-16, 2024, pages 1658–1677.
Association for Computational Linguistics, 2024. doi: 10.18653/V1/2024.ACL-LONG.91.
Jiantong Jiang, Peiyu Yang, Rui Zhang, and Feng Liu. Towards eﬀicient large language model serving: A survey
onsystem-awareKVcacheoptimization. TechRxiv,2025b. doi: 10.36227/techrxiv.176046306.66521015/v2. http:
//dx.doi.org/10.36227/techrxiv.176046306.66521015/v2.
Tao Jiang, Zichuan Lin, Lihe Li, Yi-Chen Li, Cong Guan, Lei Yuan, Zongzhang Zhang, Yang Yu, and Deheng Ye.
Multi-agent in-context coordination via decentralized memory retrieval. arXiv preprint arXiv:2511.10030, 2025c.
Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik R. Narasimhan.
SWE-bench: Can language models resolve real-world github issues? In The Twelfth International Conference on
Learning Representations, 2024.
Bowen Jin, Hansi Zeng, Zhenrui Yue, Dong Wang, Hamed Zamani, and Jiawei Han. Search-r1: Training llms to
reason and leverage search engines with reinforcement learning. CoRR, abs/2503.09516, 2025. doi: 10.48550/
ARXIV.2503.09516. https://doi.org/10.48550/arXiv.2503.09516.
79

Kumara Kahatapitiya, Kanchana Ranasinghe, Jongwoo Park, and Michael S Ryoo. Language repository for long
video understanding. In Findings of the Association for Computational Linguistics: ACL 2025, pages 5627–5646,
2025.
Zhao Kaiya, Michelangelo Naim, Jovana Kondic, Manuel Cortes, Jiaxin Ge, Shuying Luo, Guangyu Robert Yang,
andAndrewAhn. Lyfeagents: Generativeagentsforlow-costreal-timesocialinteractions,2023. https://arxiv.
org/abs/2310.02172.
Jiazheng Kang, Mingming Ji, Zhe Zhao, and Ting Bai. Memory os of ai agent, 2025a. https://arxiv.org/abs/
2506.06326.
Jikun Kang, Wenqi Wu, Filippos Christianos, Alex J. Chan, Fraser Greenlee, George Thomas, Marvin Purtorab,
and Andy Toulis. LM2: large memory models. CoRR, abs/2502.06049, 2025b. doi: 10.48550/ARXIV.2502.06049.
https://doi.org/10.48550/arXiv.2502.06049.
MinkiKang,Wei-NingChen,DonggeHan,HuseyinA.Inan,LukasWutschitz,YanzhiChen,RobertSim,andSaravan
Rajmohan. Acon: Optimizing context compression for long-horizon llm agents, October 2025c.
DongkyuKim,ByoungwookKim,DonggeonHan,andMatousEibich. Autorag: Automatedframeworkforoptimiza-
tionofretrievalaugmentedgenerationpipeline. CoRR,abs/2410.20878,2024a. doi: 10.48550/ARXIV.2410.20878.
https://doi.org/10.48550/arXiv.2410.20878.
Gangwoo Kim, Sungdong Kim, Byeongguk Jeon, Joonsuk Park, and Jaewoo Kang. Tree of clarifications: Answer-
ing ambiguous questions with retrieval-augmented large language models, 2023a. https://arxiv.org/abs/2310.
14696.
Hana Kim, Kai Tzu iunn Ong, Seoyeon Kim, Dongha Lee, and Jinyoung Yeo. Commonsense-augmented memory
construction and management in long-term conversations via context-aware persona refinement, 2024b. https:
//arxiv.org/abs/2401.14215.
HyuntakKimandByung-HakKim. Nexussum: Hierarchicalllmagentsforlong-formnarrativesummarization. arXiv
preprint arXiv:2505.24575, 2025.
Namyoung Kim, Kai Tzu-iunn Ong, Yeonjun Hwang, Minseok Kang, Iiseo Jihn, Gayoung Kim, Minju Kim, and
Jinyoung Yeo. PRINCIPLES: synthetic strategy memory for proactive dialogue agents. CoRR, abs/2509.17459,
2025a. doi: 10.48550/ARXIV.2509.17459. https://doi.org/10.48550/arXiv.2509.17459.
Sangyeop Kim, Yohan Lee, Sanghwa Kim, Hyunjong Kim, and Sungzoon Cho. Pre-storage reasoning for episodic
memory: Shifting inference burden to memory for personalized dialogue. CoRR, abs/2509.10852, 2025b. doi:
10.48550/ARXIV.2509.10852. https://doi.org/10.48550/arXiv.2509.10852.
TaewoonKim,MichaelCochez,VincentFrançois-Lavet,MarkA.Neerincx,andPiekVossen. Amachinewithshort-
term, episodic, and semantic memory systems. In Brian Williams, Yiling Chen, and Jennifer Neville, editors,
Thirty-Seventh AAAI Conference on Artificial Intelligence, AAAI 2023, Thirty-Fifth Conference on Innovative
Applications of Artificial Intelligence, IAAI 2023, Thirteenth Symposium on Educational Advances in Artificial
Intelligence, EAAI 2023, Washington, DC, USA, February 7-14, 2023, pages 48–56. AAAI Press, 2023b. doi:
10.1609/AAAI.V37I1.25075. https://doi.org/10.1609/aaai.v37i1.25075.
Dharshan Kumaran, Demis Hassabis, and James L. McClelland. What learning systems do intelligent agents need?
complementary learning systems theory updated. Trends in Cognitive Sciences, 20(7):512–534, July 2016. ISSN
1879-307X. doi: 10.1016/j.tics.2016.05.004.
YuriKuratov,AydarBulatov,PetrAnokhin,IvanRodkin,DmitrySorokin,ArtyomY.Sorokin,andMikhailBurtsev.
Babilong: Testingthelimitsofllmswithlongcontextreasoning-in-a-haystack. InAmirGlobersons,LesterMackey,
80

DanielleBelgrave,AngelaFan,UlrichPaquet,JakubM.Tomczak,andChengZhang,editors,Advances in Neural
InformationProcessingSystems38: AnnualConferenceonNeuralInformationProcessingSystems2024, NeurIPS
2024,Vancouver,BC,Canada,December10-15,2024,2024.http://papers.nips.cc/paper_files/paper/2024/
hash/c0d62e70dbc659cc9bd44cbcf1cb652f-Abstract-Datasets_and_Benchmarks_Track.html.
TaeyoonKwon,DongwookChoi,SunghwanKim,HyojunKim,SeungjunMoon,Beong-wooKwak,Kuan-HaoHuang,
and Jinyoung Yeo. Embodied agents meet personalization: Exploring memory utilization for personalized assis-
tance. CoRR,abs/2505.16348,2025. doi: 10.48550/ARXIV.2505.16348. https://doi.org/10.48550/arXiv.2505.
16348.
LangChain. GitHub - langchain-ai/langmem — github.com. https://github.com/langchain-ai/langmem, 2025.
[Accessed 14-12-2025].
Gibbeum Lee, Volker Hartmann, Jongho Park, Dimitris Papailiopoulos, and Kangwook Lee. Prompted llms as
chatbotmodulesforlongopen-domainconversation.InAnnaRogers,JordanL.Boyd-Graber,andNaoakiOkazaki,
editors, Findings of the Association for Computational Linguistics: ACL 2023, Toronto, Canada, July 9-14, 2023,
pages 4536–4554. Association for Computational Linguistics, 2023. doi: 10.18653/V1/2023.FINDINGS-ACL.277.
https://doi.org/10.18653/v1/2023.findings-acl.277.
Kuang-Huei Lee, Xinyun Chen, Hiroki Furuta, John F. Canny, and Ian Fischer. A human-inspired reading agent
with gist memory of very long contexts. In Forty-first International Conference on Machine Learning, 2024a.
MyeonghwaLee,SeonhoAn,andMin-SooKim. Planrag: Aplan-then-retrievalaugmentedgenerationforgenerative
large language models as decision makers, 2024b. https://arxiv.org/abs/2406.12430.
Xiang Lei, Qin Li, and Min Zhang. D-smart: Enhancing llm dialogue consistency via dynamic structured memory
and reasoning tree. arXiv preprint arXiv:2510.13363, 2025.
PatrickLewis,EthanPerez,AleksandraPiktus,FabioPetroni,VladimirKarpukhin,NamanGoyal,HeinrichKüttler,
Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, and Douwe Kiela. Retrieval-augmented generation
forknowledge-intensiveNLPtasks.InHugoLarochelle,Marc’AurelioRanzato,RaiaHadsell,Maria-FlorinaBalcan,
andHsuan-TienLin,editors,AdvancesinNeuralInformationProcessingSystems33: AnnualConferenceonNeural
Information Processing Systems 2020, NeurIPS 2020, December 6-12, 2020, virtual,2020. https://proceedings.
neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html.
BaiqiLi,ZhiqiuLin,DeepakPathak,JiayaoLi,YixinFei,KewenWu,TiffanyLing,XideXia,PengchuanZhang,Gra-
hamNeubig,andDevaRamanan. Genai-bench: Evaluatingandimprovingcompositionaltext-to-visualgeneration,
2024a. https://arxiv.org/abs/2406.13743.
Caorui Li, Yu Chen, Yiyan Ji, Jin Xu, Zhenyu Cui, Shihao Li, Yuanxing Zhang, Jiafu Tang, Zhenghao Song,
Dingling Zhang, Ying He, Haoxiang Liu, Yuxuan Wang, Qiufeng Wang, Zhenhe Wu, Jiehui Luo, Zhiyu Pan,
WeihaoXie,ChenchenZhang,ZhaohuiWang,JiayiTian,YanghaiWang,ZheCao,MinxinDai,KeWang,Runzhe
Wen, Yinghao Ma, Yaning Pan, Sungkyun Chang, Termeh Taheri, Haiwen Xia, Christos Plachouras, Emmanouil
Benetos,YizhiLi,GeZhang,JianYang,TianhaoPeng,ZiliWang,MinghaoLiu, JunranPeng,ZhaoxiangZhang,
andJiahengLiu. Omnivideobench: Towardsaudio-visualunderstandingevaluationforomnimllms,2025a. https:
//arxiv.org/abs/2510.10689.
Cheng Li, Ziang Leng, Chenxi Yan, Junyi Shen, Hao Wang, Weishi Mi, Yaying Fei, Xiaoyang Feng, Song Yan,
HaoShengWang,LinkangZhan,YaokaiJia,PingyuWu,andHaozhenSun. Chatharuhi: Revivinganimecharacter
in reality via large language model. CoRR, abs/2308.09597, 2023a. doi: 10.48550/ARXIV.2308.09597. https:
//doi.org/10.48550/arXiv.2308.09597.
Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard Ghanem. CAMEL:
81

Communicative agents for ”mind” exploration of large language model society. In Thirty-seventh Conference on
Neural Information Processing Systems, 2023b.
Hao Li, Chenghao Yang, An Zhang, Yang Deng, Xiang Wang, and Tat-Seng Chua. Hello again! llm-powered
personalized agent for long-term dialogue, 2025b. https://arxiv.org/abs/2406.05925.
HaoyangLi,YimingLi,AnxinTian,TianhaoTang,ZhanchaoXu,XuejiaChen,NicoleHu,WeiDong,QingLi,and
Lei Chen. A survey on large language model acceleration based on KV cache management. Trans. Mach. Learn.
Res., 2025, 2025c. https://openreview.net/forum?id=z3JZzu9EA3.
Jiaang Li, Quan Wang, Zhongnan Wang, Yongdong Zhang, and Zhendong Mao. ELDER: enhancing lifelong model
editing with mixture-of-lora. In Toby Walsh, Julie Shah, and Zico Kolter, editors, AAAI-25, Sponsored by the
Association for the Advancement of Artificial Intelligence, February 25 - March 4, 2025, Philadelphia, PA, USA,
pages 24440–24448. AAAI Press, 2025d. doi: 10.1609/AAAI.V39I23.34622. https://doi.org/10.1609/aaai.
v39i23.34622.
Kuan Li, Zhongwang Zhang, Huifeng Yin, Liwen Zhang, Litu Ou, Jialong Wu, Wenbiao Yin, Baixuan Li, Zhengwei
Tao,XinyuWang,WeizhouShen,JunkaiZhang,DingchuZhang,XixiWu,YongJiang,MingYan,PengjunXie,Fei
Huang, and Jingren Zhou. Websailor: Navigating super-human reasoning for web agent. CoRR, abs/2507.02592,
2025e. doi: 10.48550/ARXIV.2507.02592. https://doi.org/10.48550/arXiv.2507.02592.
Rui Li, Zeyu Zhang, Xiaohe Bo, Zihang Tian, Xu Chen, Quanyu Dai, Zhenhua Dong, and Ruiming Tang. Cam: A
constructivist view of agentic memory for llm-based reading comprehension, October 2025f.
XiaoxiLi,GuantingDong,JiajieJin,YuyaoZhang,YujiaZhou,YutaoZhu,PeitianZhang,andZhichengDou.Search-
o1: Agentic search-enhanced large reasoning models. CoRR, abs/2501.05366, 2025g. doi: 10.48550/ARXIV.2501.
05366. https://doi.org/10.48550/arXiv.2501.05366.
XiaoxiLi, WenxiangJiao, JiaruiJin, GuantingDong, Jiajie Jin, YinuoWang, HaoWang, YutaoZhu, Ji-Rong Wen,
Yuan Lu, and Zhicheng Dou. DeepAgent: A General Reasoning Agent with Scalable Toolsets, October 2025h.
Xiaoxi Li, Jiajie Jin, Guanting Dong, Hongjin Qian, Yutao Zhu, Yongkang Wu, Ji-Rong Wen, and Zhicheng Dou.
Webthinker: Empoweringlargereasoningmodelswithdeepresearchcapability. CoRR,abs/2504.21776,2025i. doi:
10.48550/ARXIV.2504.21776. https://doi.org/10.48550/arXiv.2504.21776.
Xiaoxi Li, Jiajie Jin, Yujia Zhou, Yuyao Zhang, Peitian Zhang, Yutao Zhu, and Zhicheng Dou. From matching to
generation: A survey on generative information retrieval. ACM Trans. Inf. Syst., 43(3):83:1–83:62, 2025j. doi:
10.1145/3722552. https://doi.org/10.1145/3722552.
YuchengLi,BoDong,FrankGuerin,andChenghuaLin. Compressingcontexttoenhanceinferenceeﬀiciencyoflarge
languagemodels. InHoudaBouamor,JuanPino,andKalikaBali, editors, Proceedings of the 2023 Conference on
Empirical Methods in Natural Language Processing,pages6342–6353,Singapore,December2023c.Associationfor
Computational Linguistics. doi: 10.18653/v1/2023.emnlp-main.391.
YuhongLi,YingbingHuang,BowenYang,BharatVenkitesh,AcyrLocatelli,HanchenYe,TianleCai,PatrickLewis,
and Deming Chen. Snapkv: LLM knows what you are looking for before generation. In Amir Globersons, Lester
Mackey, Danielle Belgrave, Angela Fan, Ulrich Paquet, Jakub M. Tomczak, and Cheng Zhang, editors, Advances
inNeuralInformationProcessingSystems38: AnnualConferenceonNeuralInformationProcessingSystems2024,
NeurIPS 2024, Vancouver, BC, Canada, December 10 - 15, 2024, 2024b. http://papers.nips.cc/paper_files/
paper/2024/hash/28ab418242603e0f7323e54185d19bde-Abstract-Conference.html.
Yunxuan Li, Yibing Du, Jiageng Zhang, Le Hou, Peter Grabowski, Yeqing Li, and Eugene Ie. Improving multi-
agent debate with sparse communication topology. In Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen,
82

editors, Findings of the Association for Computational Linguistics: EMNLP 2024, Miami, Florida, USA, Novem-
ber 12-16, 2024, pages 7281–7294. Association for Computational Linguistics, 2024c. doi: 10.18653/V1/2024.
FINDINGS-EMNLP.427. https://doi.org/10.18653/v1/2024.findings-emnlp.427.
Zaijing Li, Yuquan Xie, Rui Shao, Gongwei Chen, Dongmei Jiang, and Liqiang Nie. Optimus-1: Hybrid multimodal
memory empowered agents excel in long-horizon tasks, 2024d. https://arxiv.org/abs/2408.03615.
Zhiyu Li, Shichao Song, Hanyu Wang, Simin Niu, Ding Chen, Jiawei Yang, Chenyang Xi, Huayi Lai, Jihao Zhao,
YezhaohuiWang,JunpengRen,ZehaoLin,JiahaoHuo,TianyiChen,KaiChen,KehangLi,ZhiqiangYin,Qingchen
Yu, Bo Tang, Hongkang Yang, Zhi-Qin John Xu, and Feiyu Xiong. Memos: An operating system for memory-
augmented generation (mag) in large language models, 2025k. https://arxiv.org/abs/2505.22101.
Zijian Li, Xin Guan, Bo Zhang, Shen Huang, Houquan Zhou, Shaopeng Lai, Ming Yan, Yong Jiang, Pengjun Xie,
Fei Huang, Jun Zhang, and Jingren Zhou. Webweaver: Structuring web-scale evidence with dynamic outlines for
open-ended deep research, October 2025l.
Xuechen Liang, Meiling Tao, Yinghui Xia, Jianhui Wang, Kun Li, Yijin Wang, Yangfan He, Jingsong Yang, Tianyu
Shi, Yuantao Wang, Miao Zhang, and Xueqian Wang. SAGE: self-evolving agents with reflective and memory-
augmented abilities. Neurocomputing, 647:130470, 2025. doi: 10.1016/J.NEUCOM.2025.130470. https://doi.
org/10.1016/j.neucom.2025.130470.
Huanxuan Liao, Wen Hu, Yao Xu, Shizhu He, Jun Zhao, and Kang Liu. Beyond Hard and Soft: Hybrid Context
CompressionforBalancingLocalandGlobalInformationRetention. CoRR,abs/2505.15774,2025a. doi: 10.48550/
ARXIV.2505.15774.
Yue Liao, Pengfei Zhou, Siyuan Huang, Donglin Yang, Shengcong Chen, Yuxin Jiang, Yue Hu, Jingbin Cai, Si Liu,
JianlanLuo,etal. Genieenvisioner: Aunifiedworldfoundationplatformforroboticmanipulation. arXivpreprint
arXiv:2508.05635, 2025b.
Opher Lieber, Barak Lenz, Hofit Bata, Gal Cohen, Jhonathan Osin, Itay Dalmedigos, Erez Safahi, Shaked Meirom,
Yonatan Belinkov, Shai Shalev-Shwartz, Omri Abend, Raz Alon, Tomer Asida, Amir Bergman, Roman Glozman,
MichaelGokhman,AvashalomManevich,NirRatner,NoamRozen,ErezShwartz,MorZusman,andYoavShoham.
Jamba: A hybrid transformer-mamba language model, 2024. https://arxiv.org/abs/2403.19887.
Thomas Limbacher and Robert Legenstein. H-mem: Harnessing synaptic plasticity with hebbian memory networks.
In Advances in Neural Information Processing Systems, volume 33, pages 21627–21637. Curran Associates, Inc.,
2020.
JessyLin,LukeZettlemoyer,GargiGhosh,Wen-TauYih,AramMarkosyan,Vincent-PierreBerges,andBarlasOğuz.
Continual learning via sparse memory finetuning, 2025. https://arxiv.org/abs/2510.15103.
GuangyiLiu,PengxiangZhao,LiangLiu,ZhimingChen,YuxiangChai,ShuaiRen,HaoWang,ShiboHe,andWen-
chaoMeng.Learnact: Few-shotmobileGUIagentwithaunifieddemonstrationbenchmark.CoRR,abs/2504.13805,
2025a. doi: 10.48550/ARXIV.2504.13805. https://doi.org/10.48550/arXiv.2504.13805.
Jiahao Liu, Shengkang Gu, Dongsheng Li, Guangping Zhang, Mingzhe Han, Hansu Gu, Peng Zhang, Tun Lu,
Li Shang, and Ning Gu. Agentcf++: Memory-enhanced llm-based agents for popularity-aware cross-domain
recommendations, 2025b. https://arxiv.org/abs/2502.13843.
Jiale Liu, Yifan Zeng, Malte Højmark-Bertelsen, Marie Normann Gadeberg, Huazheng Wang, and Qingyun Wu.
Memory-augmented agent training for business document understanding. CoRR, abs/2412.15274, 2024. doi:
10.48550/ARXIV.2412.15274. https://doi.org/10.48550/arXiv.2412.15274.
83

Jun Liu, Zhenglun Kong, Changdi Yang, Fan Yang, Tianqi Li, Peiyan Dong, Joannah Nanjekye, Hao Tang, Geng
Yuan, Wei Niu, Wenbin Zhang, Pu Zhao, Xue Lin, Dong Huang, and Yanzhi Wang. Rcr-router: Eﬀicient role-
aware context routing for multi-agent LLM systems with structured memory. CoRR, abs/2508.04903, 2025c. doi:
10.48550/ARXIV.2508.04903. https://doi.org/10.48550/arXiv.2508.04903.
Junming Liu, Yifei Sun, Weihua Cheng, Haodong Lei, Yirong Chen, Licheng Wen, Xuemeng Yang, Daocheng Fu,
PinlongCai,NianchenDeng,YiYu,ShuyueHu,BotianShi,andDingWang. Memverse: Multimodalmemoryfor
lifelong learning agents, 2025d. https://arxiv.org/abs/2512.03627.
KunhaoLiu,WenboHu,JialeXu,YingShan,andShijianLu. Rollingforcing: Autoregressivelongvideodiffusionin
real time. arXiv preprint arXiv:2509.25161, 2025e.
Lei Liu, Xiaoyan Yang, Yue Shen, Binbin Hu, Zhiqiang Zhang, Jinjie Gu, and Guannan Zhang. Think-in-memory:
Recalling and post-thinking enable llms with long-term memory. CoRR, abs/2311.08719, 2023a. doi: 10.48550/
ARXIV.2311.08719. https://doi.org/10.48550/arXiv.2311.08719.
Yanming Liu, Xinyue Peng, Jiannan Cao, Shi Bo, Yuwei Zhang, Xuhong Zhang, Sheng Cheng, Xun Wang, Jian-
wei Yin, and Tianyu Du. Tool-Planner: Task planning with clusters across multiple tools. In The Thirteenth
International Conference on Learning Representations, 2025f.
Yixin Liu, Guibin Zhang, Kun Wang, Shiyuan Li, and Shirui Pan. Graph-augmented large language model agents:
Current progress and future prospects. arXiv preprint arXiv:2507.21407, 2025g.
Zeting Liu, Zida Yang, Zeyu Zhang, and Hao Tang. Evovla: Self-evolving vision-language-action model, 2025h.
https://arxiv.org/abs/2511.16166.
Zichang Liu, Aditya Desai, Fangshuo Liao, Weitao Wang, Victor Xie, Zhaozhuo Xu, Anastasios Kyrillidis, and
Anshumali Shrivastava. Scissorhands: Exploiting the persistence of importance hypothesis for LLM KV cache
compressionattesttime. InAliceOh,TristanNaumann,AmirGloberson,KateSaenko,MoritzHardt,andSergey
Levine,editors,AdvancesinNeuralInformationProcessingSystems36: AnnualConferenceonNeuralInformation
ProcessingSystems2023,NeurIPS2023,NewOrleans,LA,USA,December10-16,2023,2023b. http://papers.
nips.cc/paper_files/paper/2023/hash/a452a7c6c463e4ae8fbdc614c6e983e6-Abstract-Conference.html.
Lin Long, Yichen He, Wentao Ye, Yiyuan Pan, Yuan Lin, Hang Li, Junbo Zhao, and Wei Li. Seeing, listening,
remembering,andreasoning: Amultimodalagentwithlong-termmemory. arXivpreprintarXiv:2508.09736,2025.
Junfeng Lu and Yueyan Li. Dynamic affective memory management for personalized llm agents, 2025. https:
//arxiv.org/abs/2510.27418.
Junru Lu, Siyu An, Mingbao Lin, Gabriele Pergola, Yulan He, Di Yin, Xing Sun, and Yunsheng Wu. MemoChat:
TuningLLMstousememosforconsistentlong-rangeopen-domainconversation. arXivpreprintarXiv:2308.08239,
2023.
Miao Lu, Weiwei Sun, Weihua Du, Zhan Ling, Xuesong Yao, Kang Liu, and Jiecao Chen. Scaling llm multi-turn rl
with end-to-end summarization-based context management, 2025a. https://arxiv.org/abs/2510.06727.
Miao Lu, Weiwei Sun, Weihua Du, Zhan Ling, Xuesong Yao, Kang Liu, and Jiecao Chen. Scaling llm multi-turn rl
with end-to-end summarization-based context management, October 2025b.
Pengqian Lu, Jie Lu, Anjin Liu, and Guangquan Zhang. Spad: Seven-source token probability attribution with
syntactic aggregation for detecting hallucinations in rag. arXiv preprint arXiv:2512.07515, 2025c.
EliasLumer,AnmolGulati,VamseKumarSubbiah,PradeepHonaganahalliBasavaraju,andJamesABurke. Mem-
tool: Optimizing short-term memory management for dynamic tool calling in llm agent multi-turn conversations.
arXiv preprint arXiv:2507.21428, 2025.
84

Junyu Luo, Weizhi Zhang, Ye Yuan, Yusheng Zhao, Junwei Yang, Yiyang Gu, Bohan Wu, Binqi Chen, Ziyue
Qiao, Qingqing Long, Rongcheng Tu, Xiao Luo, Wei Ju, Zhiping Xiao, Yifan Wang, Meng Xiao, Chenwu Liu,
Jingyang Yuan, Shichang Zhang, Yiqiao Jin, Fan Zhang, Xian Wu, Hanqing Zhao, Dacheng Tao, Philip S. Yu,
and Ming Zhang. Large language model agent: A survey on methodology, applications and challenges, 2025.
https://arxiv.org/abs/2503.21460.
Weiyao Luo, Suncong Zheng, Heming Xia, Weikang Wang, Yan Lei, Tianyu Liu, Shuang Chen, and Zhifang Sui.
Taking a deep breath: Enhancing language modeling of large language models with sentinel tokens. In Yaser
Al-Onaizan, Mohit Bansal, and Yun-Nung Chen, editors, Findings of the Association for Computational Linguis-
tics: EMNLP 2024, Miami, Florida, USA, November 12-16, 2024, pages 4034–4040. Association for Computa-
tional Linguistics, 2024. doi: 10.18653/V1/2024.FINDINGS-EMNLP.233. https://doi.org/10.18653/v1/2024.
findings-emnlp.233.
Huan Ma, Changqing Zhang, Yatao Bian, Lemao Liu, Zhirui Zhang, Peilin Zhao, Shu Zhang, Huazhu Fu, Qinghua
Hu,andBingzheWu. Fairness-guidedfew-shotpromptingforlargelanguagemodels,2023a. https://arxiv.org/
abs/2303.13217.
Jun-Yu Ma, Zhen-Hua Ling, Ningyu Zhang, and Jia-Chen Gu. Neighboring perturbations of knowledge editing on
largelanguagemodels. InForty-firstInternationalConferenceonMachineLearning,ICML2024,Vienna,Austria,
July 21-27, 2024. OpenReview.net, 2024. https://openreview.net/forum?id=K9NTPRvVRI.
Xinbei Ma, Yeyun Gong, Pengcheng He, Hai Zhao, and Nan Duan. Query rewriting in retrieval-augmented large
language models. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing,
pages 5303–5315, 2023b.
AmanMadaan,NiketTandon,PrakharGupta,SkylerHallinan,LuyuGao,SarahWiegreffe,UriAlon,NouhaDziri,
ShrimaiPrabhumoye,YimingYang,etal. Self-Refine: Iterativerefinementwithself-feedback. Advances in Neural
Information Processing Systems, pages 46534–46594, 2023.
Adyasha Maharana, Dong-Ho Lee, Sergey Tulyakov, Mohit Bansal, Francesco Barbieri, and Yuwei Fang. Evaluating
verylong-termconversationalmemoryofLLMagents.InProceedingsofthe62ndAnnualMeetingoftheAssociation
for Computational Linguistics (Volume 1: Long Papers), pages 13851–13870, Bangkok, Thailand, August 2024.
Association for Computational Linguistics. doi: 10.18653/v1/2024.acl-long.747. https://aclanthology.org/
2024.acl-long.747/.
Shengyu Mao, Xiaohan Wang, Mengru Wang, Yong Jiang, Pengjun Xie, Fei Huang, and Ningyu Zhang. Editing
personality for large language models. In Derek F. Wong, Zhongyu Wei, and Muyun Yang, editors, Natural
Language Processing and Chinese Computing - 13th National CCF Conference, NLPCC 2024, Hangzhou, China,
November 1-3, 2024, Proceedings, Part II, volume 15360 of Lecture Notes in Computer Science, pages 241–254.
Springer, 2024. doi: 10.1007/978-981-97-9434-8\_19. https://doi.org/10.1007/978-981-97-9434-8_19.
SamueleMarro,EmanueleLaMalfa,JesseWright,GuohaoLi,NigelShadbolt,MichaelWooldridge,andPhilipTorr.
A scalable communication protocol for networks of large language models, 2024. https://arxiv.org/abs/2410.
11905.
AndreaMatarazzoandRiccardoTorlone. Asurveyonlargelanguagemodelswithsomeinsightsontheircapabilities
and limitations, 2025. https://arxiv.org/abs/2501.04040.
Marcelo G. Mattar and Nathaniel D. Daw. Prioritized memory access explains planning and hippocampal replay.
Nature Neuroscience, 21(11):1609–1617, November 2018. ISSN 1546-1726. doi: 10.1038/s41593-018-0232-z.
JamesL.McClelland,BruceL.McNaughton,andRandallC.O’Reilly.Whytherearecomplementarylearningsystems
85

inthehippocampusandneocortex: Insightsfromthesuccessesandfailuresofconnectionistmodelsoflearningand
memory. Psychological Review, 102(3):419–457, July 1995. ISSN 0033-295X. doi: 10.1037/0033-295X.102.3.419.
Michael McCloskey and Neal J. Cohen. Catastrophic interference in connectionist networks: The sequential learn-
ing problem. volume 24 of Psychology of Learning and Motivation, pages 109–165. Academic Press, 1989.
doi: https://doi.org/10.1016/S0079-7421(08)60536-8. https://www.sciencedirect.com/science/article/pii/
S0079742108605368.
LingruiMei,JiayuYao,YuyaoGe,YiweiWang,BaolongBi,YujunCai,JiazhiLiu,MingyuLi,Zhong-ZhiLi,Duzhen
Zhang, Chenlin Zhou, Jiayi Mao, Tianze Xia, Jiafeng Guo, and Shenghua Liu. A Survey of Context Engineering
for Large Language Models, July 2025.
Memary. GitHub-kingjulio8238/Memary: TheOpenSourceMemoryLayerForAutonomousAgents—github.com.
https://github.com/kingjulio8238/Memary, 2025. [Accessed 14-12-2025].
Memobase. GitHub - memodb-io/memobase: User Profile-Based Long-Term Memory for AI Chatbot Applications.
https://github.com/memodb-io/memobase, 2025. [Accessed 12-12-2025].
Kevin Meng, David Bau, Alex Andonian, and Yonatan Belinkov. Locating and editing factual associations in GPT.
In Sanmi Koyejo, S. Mohamed, A. Agarwal, Danielle Belgrave, K. Cho, and A. Oh, editors, Advances in Neural
InformationProcessingSystems35: AnnualConferenceonNeuralInformationProcessingSystems2022, NeurIPS
2022, New Orleans, LA, USA, November 28 - December 9, 2022, 2022. http://papers.nips.cc/paper_files/
paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html.
Kevin Meng, Arnab Sen Sharma, Alex J. Andonian, Yonatan Belinkov, and David Bau. Mass-editing memory in a
transformer. InThe Eleventh International Conference on Learning Representations, ICLR 2023, Kigali, Rwanda,
May 1-5, 2023. OpenReview.net, 2023. https://openreview.net/forum?id=MkbcAHIYgyS.
Lina Mezghani, Sainbayar Sukhbaatar, Thibaut Lavril, Oleksandr Maksymets, Dhruv Batra, Piotr Bojanowski, and
KarteekAlahari.Memory-augmentedreinforcementlearningforimage-goalnavigation.InIEEE/RSJInternational
Conference on Intelligent Robots and Systems, IROS 2022, Kyoto, Japan, October 23-27, 2022, pages 3316–3323.
IEEE, 2022. doi: 10.1109/IROS47612.2022.9981090. https://doi.org/10.1109/IROS47612.2022.9981090.
Grégoire Mialon, Clémentine Fourrier, Thomas Wolf, Yann LeCun, and Thomas Scialom. GAIA: a benchmark for
general ai assistants. In The Twelfth International Conference on Learning Representations, 2023.
ShervinMinaee,TomasMikolov,NarjesNikzad,MeysamChenaghlu,RichardSocher,XavierAmatriain,andJianfeng
Gao. Large language models: A survey, 2025. https://arxiv.org/abs/2402.06196.
MineContext. GitHub-volcengine/MineContext: MineContextisyourproactivecontext-awareAIpartner(Context-
Engineering+ChatGPT Pulse) — github.com. https://github.com/volcengine/MineContext, 2025. [Accessed
14-12-2025].
EricMitchell,CharlesLin,AntoineBosselut,ChelseaFinn,andChristopherD.Manning. Fastmodeleditingatscale.
InTheTenthInternationalConferenceonLearningRepresentations,ICLR2022,VirtualEvent,April25-29,2022.
OpenReview.net, 2022. https://openreview.net/forum?id=0DcZxeWfOPt.
AtsuyukiMiyai,ZaiyingZhao,KazukiEgashira,AtsukiSato,TatsumiSunada,ShotaOnohara,HiromasaYamanishi,
Mashiro Toyooka, Kunato Nishina, Ryoma Maeda, et al. Webchorearena: Evaluating web browsing agents on
realistic tedious web tasks. arXiv preprint arXiv:2506.01952, 2025.
Ali Modarressi, Ayyoob Imani, Mohsen Fayyaz, and Hinrich Schütze. RET-LLM: Towards a general read-write
memory for large language models. arXiv preprint arXiv:2305.14322, 2023.
86

Sajad Mousavi, Ricardo Luna Gutiérrez, Desik Rengarajan, Vineet Gundecha, Ashwin Ramesh Babu, Avisek Naug,
Antonio Guillen, and Soumyendu Sarkar. N-critics: Self-refinement of large language models with ensemble of
critics, 2023. https://arxiv.org/abs/2310.18679.
Jesse Mu, Xiang Li, and Noah D. Goodman. Learning to compress prompts with gist tokens. In Alice Oh, Tristan
Naumann,AmirGloberson,KateSaenko,MoritzHardt,andSergeyLevine,editors,Advances in Neural Informa-
tion Processing Systems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023,
NewOrleans, LA,USA,December10-16, 2023,2023. http://papers.nips.cc/paper_files/paper/2023/hash/
3d77c6dcc7f143aa2154e7f4d5e22d68-Abstract-Conference.html.
Subhabrata Mukherjee, Arindam Mitra, Ganesh Jawahar, Sahaj Agarwal, Hamid Palangi, and Ahmed Awadallah.
Orca: Progressivelearningfromcomplexexplanationtracesofgpt-4,2023. https://arxiv.org/abs/2306.02707.
Hyungho Na, Yunkyeong Seo, and Il-Chul Moon. Eﬀicient episodic memory utilization of cooperative multi-agent
reinforcementlearning.InTheTwelfthInternationalConferenceonLearningRepresentations,ICLR2024,Vienna,
Austria, May 7-11, 2024. OpenReview.net, 2024. https://openreview.net/forum?id=LjivA1SLZ6.
JiayanNan,WenquanMa,WenlongWu,andYizeChen. Nemori: Self-organizingagentmemoryinspiredbycognitive
science. CoRR, abs/2508.03341, 2025. doi: 10.48550/ARXIV.2508.03341. https://doi.org/10.48550/arXiv.
2508.03341.
ThangNguyen,PeterChin,andYu-WingTai.MA-RAG:multi-agentretrieval-augmentedgenerationviacollaborative
chain-of-thought reasoning. CoRR, abs/2505.20096, 2025. doi: 10.48550/ARXIV.2505.20096. https://doi.org/
10.48550/arXiv.2505.20096.
Shen Nie, Fengqi Zhu, Zebin You, Xiaolu Zhang, Jingyang Ou, Jun Hu, Jun Zhou, Yankai Lin, Ji-Rong Wen, and
Chongxuan Li. Large language diffusion models, 2025. https://arxiv.org/abs/2502.09992.
Cheng Niu, Yuanhao Wu, Juno Zhu, Siliang Xu, Kashun Shum, Randy Zhong, Juntong Song, and Tong Zhang.
Ragtruth: Ahallucinationcorpusfordevelopingtrustworthyretrieval-augmentedlanguagemodels. InProceedings
of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages
10862–10878, 2024.
OpenAI. Memory and new controls for chatgpt, 2024. https://openai.com/index/
memory-and-new-controls-for-chatgpt/.
Siru Ouyang, Jun Yan, I-Hung Hsu, Yanfei Chen, Ke Jiang, Zifeng Wang, Rujun Han, Long T. Le, Samira Daruki,
Xiangru Tang, Vishy Tirumalashetty, George Lee, Mahsan Rofouei, Hangfei Lin, Jiawei Han, Chen-Yu Lee, and
Tomas Pfister. Reasoningbank: Scaling agent self-evolving with reasoning memory, 2025. https://arxiv.org/
abs/2509.25140.
Charles Packer, Vivian Fang, Shishir G. Patil, Kevin Lin, Sarah Wooders, and Joseph E. Gonzalez. MemGPT:
Towards LLMs as Operating Systems. CoRR, abs/2310.08560, 2023a. doi: 10.48550/ARXIV.2310.08560.
Charles Packer, Vivian Fang, ShishirG Patil, Kevin Lin, Sarah Wooders, and JosephE Gonzalez. Memgpt: Towards
llms as operating systems. arXiv preprint arXiv:2310.08560, 2023b.
LawrencePage,SergeyBrin,RajeevMotwani,andTerryWinograd. Thepagerankcitationranking: Bringingorder
to the web. In The Web Conference, 1999. https://api.semanticscholar.org/CorpusID:1508503.
YiyuanPan,YunzheXu,ZheLiu,andHeshengWang. Planningfromimagination: Episodicsimulationandepisodic
memory for vision-and-language navigation, 2024. https://arxiv.org/abs/2412.01857.
Zhuoshi Pan, Qianhui Wu, Huiqiang Jiang, Xufang Luo, Hao Cheng, Dongsheng Li, Yuqing Yang, Chin-Yew Lin,
H. Vicky Zhao, Lili Qiu, and Jianfeng Gao. Secom: On memory construction and retrieval for personalized
87

conversational agents. In The Thirteenth International Conference on Learning Representations, ICLR 2025,
Singapore, April 24-28, 2025. OpenReview.net, 2025. https://openreview.net/forum?id=xKDZAW0He3.
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S Bernstein.
Generativeagents: Interactivesimulacraofhumanbehavior. InProceedings of the 36th annual acm symposium on
user interface software and technology, pages 1–22, 2023.
Shishir G. Patil, Tianjun Zhang, Xin Wang, and Joseph E. Gonzalez. Gorilla: Large Language Model Con-
nected with Massive APIs. In Amir Globersons, Lester Mackey, Danielle Belgrave, Angela Fan, Ulrich
Paquet, Jakub M. Tomczak, and Cheng Zhang, editors, Advances in Neural Information Processing Sys-
tems 38: Annual Conference on Neural Information Processing Systems 2024, NeurIPS 2024, Vancou-
ver, BC, Canada, December 10 - 15, 2024, 2024. http://papers.nips.cc/paper_files/paper/2024/hash/
e4c61f578ff07830f5c37378dd3ecb0d-Abstract-Conference.html.
Bo Peng, Eric Alcaide, Quentin Anthony, Alon Albalak, Samuel Arcadinho, Stella Biderman, Huanqi Cao, Xin
Cheng, Michael Chung, Matteo Grella, Kranthi Kiran GV, Xuzheng He, Haowen Hou, Jiaju Lin, Przemyslaw
Kazienko,JanKocon,JiamingKong,BartlomiejKoptyra,HaydenLau,KrishnaSriIpsitMantri,FerdinandMom,
Atsushi Saito, Guangyu Song, Xiangru Tang, Bolun Wang, Johan S. Wind, Stanislaw Wozniak, Ruichong Zhang,
Zhenyuan Zhang, Qihang Zhao, Peng Zhou, Qinghua Zhou, Jian Zhu, and Rui-Jie Zhu. Rwkv: Reinventing rnns
for the transformer era, 2023. https://arxiv.org/abs/2305.13048.
Boci Peng, Yun Zhu, Yongchao Liu, Xiaohe Bo, Haizhou Shi, Chuntao Hong, Yan Zhang, and Siliang Tang. Graph
retrieval-augmented generation: A survey, 2024. https://arxiv.org/abs/2408.08921.
Jayr Alencar Pereira, Robson do Nascimento Fidalgo, Roberto A. Lotufo, and Rodrigo Nogueira. Visconde: Multi-
document QA with GPT-3 and neural reranking. In Jaap Kamps, Lorraine Goeuriot, Fabio Crestani, Maria
Maistro, Hideo Joho, Brian Davis, Cathal Gurrin, Udo Kruschwitz, and Annalina Caputo, editors, Advances in
Information Retrieval - 45th European Conference on Information Retrieval, ECIR 2023, Dublin, Ireland, April
2-6, 2023, Proceedings, Part II, volume 13981 of Lecture Notes in Computer Science, pages 534–543. Springer,
2023. doi: 10.1007/978-3-031-28238-6\_44. https://doi.org/10.1007/978-3-031-28238-6_44.
Jinghua Piao, Yuwei Yan, Jun Zhang, Nian Li, Junbo Yan, Xiaochong Lan, Zhihong Lu, Zhiheng Zheng, Jing Yi
Wang, Di Zhou, Chen Gao, Fengli Xu, Fang Zhang, Ke Rong, Jun Su, and Yong Li. Agentsociety: Large-scale
simulationofllm-drivengenerativeagentsadvancesunderstandingofhumanbehaviorsandsociety,February2025.
Ryan Po, Yotam Nitzan, Richard Zhang, Berlin Chen, Tri Dao, Eli Shechtman, Gordon Wetzstein, and Xun Huang.
Long-context state-space video world models. arXiv preprint arXiv:2505.20171, 2025.
Hadi Pouransari, David Grangier, C Thomas, Michael Kirchhof, and Oncel Tuzel. Pretraining with hierarchical
memories: separating long-tail and common knowledge, 2025. https://arxiv.org/abs/2510.02375.
Shrimai Prabhumoye, Rafal Kocielnik, Mohammad Shoeybi, Anima Anandkumar, and Bryan Catanzaro. Few-shot
instruction prompts for pretrained language models to detect social biases, 2022. https://arxiv.org/abs/2112.
07868.
Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, Jiahao Li, Cheng Yang, Weize Chen, Yusheng Su,
Xin Cong, Juyuan Xu, Dahai Li, Zhiyuan Liu, and Maosong Sun. ChatDev: Communicative agents for software
development. InProceedingsofthe62ndAnnualMeetingoftheAssociationforComputationalLinguistics(Volume
1: Long Papers), pages 15174–15186, 2024.
ChengQian,ChiHan,YiRenFung,YujiaQin,ZhiyuanLiu,andHengJi.CREATOR:ToolCreationforDisentangling
Abstract and Concrete Reasoning of Large Language Models. In Houda Bouamor, Juan Pino, and Kalika Bali,
editors,FindingsoftheAssociationforComputationalLinguistics: EMNLP2023,Singapore,December6-10,2023,
88

pages 6922–6939. Association for Computational Linguistics, 2023. doi: 10.18653/V1/2023.FINDINGS-EMNLP.
462. https://doi.org/10.18653/v1/2023.findings-emnlp.462.
Hongjin Qian, Zheng Liu, Peitian Zhang, Kelong Mao, Defu Lian, Zhicheng Dou, and Tiejun Huang. Memorag:
Boostinglongcontextprocessingwithglobalmemory-enhancedretrievalaugmentation. InGuodongLong,Michale
Blumestein, Yi Chang, Liane Lewin-Eytan, Zi Helen Huang, and Elad Yom-Tov, editors, Proceedings of the ACM
on Web Conference 2025, WWW 2025, Sydney, NSW, Australia, 28 April 2025- 2 May 2025, pages 2366–2377.
ACM, 2025. doi: 10.1145/3696410.3714805. https://doi.org/10.1145/3696410.3714805.
TianruiQin,QianbenChen,SinuoWang,HeXing,KingZhu,HeZhu,DingfengShi,XinxinLiu,GeZhang,Jiaheng
Liu, Yuchen Eleanor Jiang, Xitong Gao, and Wangchunshu Zhou. Flash-searcher: Fast and effective web agents
via dag-based parallel execution, 2025. https://arxiv.org/abs/2509.25301.
Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, Yaxi Lu, Yankai Lin, Xin Cong, Xiangru Tang, Bill
Qian,SihanZhao,LaurenHong,RunchuTian,RuobingXie,JieZhou,MarkGerstein,DahaiLi,ZhiyuanLiu,and
Maosong Sun. ToolLLM: Facilitating large language models to master 16000+ real-world apis. In The Twelfth
International Conference on Learning Representations, 2024a.
Zhen Qin, Weigao Sun, Dong Li, Xuyang Shen, Weixuan Sun, and Yiran Zhong. Various lengths, constant speed:
Eﬀicientlanguagemodelingwithlightningattention. InForty-firstInternationalConferenceonMachineLearning,
ICML 2024, Vienna, Austria, July 21-27, 2024. OpenReview.net, 2024b. https://openreview.net/forum?id=
Lwm6TiUP4X.
Zhen Qin, Weigao Sun, Dong Li, Xuyang Shen, Weixuan Sun, and Yiran Zhong. Lightning attention-2: A free
lunch for handling unlimited sequence lengths in large language models. CoRR, abs/2401.04658, 2024c. doi:
10.48550/ARXIV.2401.04658. https://doi.org/10.48550/arXiv.2401.04658.
Jiahao Qiu, Xinzhe Juan, Yimin Wang, Ling Yang, Xuan Qi, Tongcheng Zhang, Jiacheng Guo, Yifu Lu, Zixin Yao,
Hongru Wang, Shilong Liu, Xun Jiang, Liu Leqi, and Mengdi Wang. Agentdistill: Training-free agent distillation
with generalizable mcp boxes, 2025a. https://arxiv.org/abs/2506.14728.
Jiahao Qiu, Xuan Qi, Hongru Wang, Xinzhe Juan, Yimin Wang, Zelin Zhao, Jiayi Geng, Jiacheng Guo, Peihang Li,
JingzheShi,ShilongLiu,andMengdiWang. Alita-g: Self-evolvinggenerativeagentforagentgeneration,October
2025b.
Jiahao Qiu, Xuan Qi, Tongcheng Zhang, Xinzhe Juan, Jiacheng Guo, Yifu Lu, Yimin Wang, Zixin Yao, Qihan
Ren, Xun Jiang, Xing Zhou, Dongrui Liu, Ling Yang, Yue Wu, Kaixuan Huang, Shilong Liu, Hongru Wang, and
MengdiWang. Alita: Generalistagentenablingscalableagenticreasoningwithminimalpredefinitionandmaximal
self-evolution, 2025c. https://arxiv.org/abs/2505.20286.
ChangleQu,SunhaoDai,XiaochiWei,HengyiCai,ShuaiqiangWang,DaweiYin,JunXu,andJi-RongWen. COLT:
Towards Completeness-Oriented Tool Retrieval for Large Language Models. CoRR, abs/2405.16089, 2024. doi:
10.48550/ARXIV.2405.16089. https://doi.org/10.48550/arXiv.2405.16089. arXiv: 2405.16089.
Changle Qu, Sunhao Dai, Xiaochi Wei, Hengyi Cai, Shuaiqiang Wang, Dawei Yin, Jun Xu, and Ji-Rong Wen. From
exploration to mastery: Enabling llms to master tools via self-driven interactions, February 2025a.
Changle Qu, Sunhao Dai, Xiaochi Wei, Hengyi Cai, Shuaiqiang Wang, Dawei Yin, Jun Xu, and Ji-rong Wen. Tool
learning with large language models: a survey. Frontiers of Computer Science, 19(8), January 2025b. ISSN
2095-2236. doi: 10.1007/s11704-024-40678-2. http://dx.doi.org/10.1007/s11704-024-40678-2.
Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry,
Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sutskever. Learning transferable visual
models from natural language supervision. In Marina Meila and Tong Zhang, editors, Proceedings of the 38th
89

International Conference on Machine Learning, ICML 2021, 18-24 July 2021, Virtual Event, volume 139 of
Proceedings of Machine Learning Research, pages 8748–8763. PMLR, 2021. http://proceedings.mlr.press/
v139/radford21a.html.
Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct
preferenceoptimization: Yourlanguagemodelissecretlyarewardmodel. InThirty-seventh Conference on Neural
Information Processing Systems, 2023.
KrishanRana,JesseHaviland,SouravGarg,JadAbou-Chakra,IanD.Reid,andNikoSünderhauf.SayPlan: Ground-
ingLargeLanguageModelsusing3DSceneGraphsforScalableRobotTaskPlanning. InJieTan,MarcToussaint,
andKouroshDarvish,editors,ConferenceonRobotLearning,CoRL2023,6-9November2023,Atlanta,GA,USA,
volume 229 of Proceedings of Machine Learning Research, pages 23–72. PMLR, 2023.
Preston Rasmussen, Pavlo Paliychuk, Travis Beauvais, Jack Ryan, and Daniel Chalef. Zep: A temporal knowledge
graph architecture for agent memory. CoRR, abs/2501.13956, 2025. doi: 10.48550/ARXIV.2501.13956. https:
//doi.org/10.48550/arXiv.2501.13956.
Paul J. Reber. The neural basis of implicit learning and memory: A review of neuropsychological and neuroimaging
research. Neuropsychologia, 51(10):2026–2042, August 2013. ISSN 1873-3514. doi: 10.1016/j.neuropsychologia.
2013.06.019.
Nils Reimers and Iryna Gurevych. Sentence-bert: Sentence embeddings using siamese bert-networks. In Kentaro
Inui,JingJiang,VincentNg,andXiaojunWan,editors,Proceedingsofthe2019ConferenceonEmpiricalMethods
in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing,
EMNLP-IJCNLP2019, HongKong, China, November3-7, 2019,pages3980–3990.AssociationforComputational
Linguistics, 2019. doi: 10.18653/V1/D19-1410. https://doi.org/10.18653/v1/D19-1410.
Alireza Rezazadeh, Zichao Li, Ange Lou, Yuying Zhao, Wei Wei, and Yujia Bao. Collaborative memory: Multi-user
memory sharing in llm agents with dynamic access control. arXiv preprint arXiv:2505.18279, 2025a.
Alireza Rezazadeh, Zichao Li, Ange Lou, Yuying Zhao, Wei Wei, and Yujia Bao. Collaborative memory: Multi-user
memory sharing in llm agents with dynamic access control, 2025b. https://arxiv.org/abs/2505.18279.
Alireza Rezazadeh, Zichao Li, Wei Wei, and Yujia Bao. From Isolated Conversations to Hierarchical Schemas:
DynamicTreeMemoryRepresentationforLLMs. InThe Thirteenth International Conference on Learning Repre-
sentations, ICLR 2025, Singapore, April 24-28, 2025. OpenReview.net, 2025c.
Wim J. Riedel and Arjan Blokland. Declarative memory. Handbook of Experimental Pharmacology, 228:215–236,
2015. ISSN 0171-2004. doi: 10.1007/978-3-319-16522-6_7.
StephenE.RobertsonandHugoZaragoza. Theprobabilisticrelevanceframework: BM25andbeyond. Found.Trends
Inf. Retr., 3(4):333–389, 2009. doi: 10.1561/1500000019. https://doi.org/10.1561/1500000019.
Dongyu Ru, Lin Qiu, Xiangkun Hu, Tianhang Zhang, Peng Shi, Shuaichen Chang, Cheng Jiayang, Cunxiang Wang,
Shichao Sun, Huanyu Li, et al. Ragchecker: A fine-grained framework for diagnosing retrieval-augmented genera-
tion. Advances in Neural Information Processing Systems, 37:21999–22027, 2024.
Jingqing Ruan, Yihong Chen, Bin Zhang, Zhiwei Xu, Tianpeng Bao, Guoqing Du, Shiwei Shi, Hangyu Mao, Ziyue
Li, Xingyu Zeng, and Rui Zhao. Tptu: Large language model-based ai agents for task planning and tool usage,
2023. https://arxiv.org/abs/2308.03427.
RanaSalama,JasonCai,MichelleYuan,AnnaCurrey,MonicaSunkara,YiZhang,andYassineBenajiba.Meminsight:
Autonomous memory augmentation for llm agents, 2025. https://arxiv.org/abs/2503.21760.
90

Jitao Sang, Jinlin Xiao, Jiarun Han, Jilin Chen, Xiaoyi Chen, Shuyu Wei, Yongjie Sun, and Yuhang Wang. Beyond
pipelines: A survey of the paradigm shift toward model-native agentic ai, 2025. https://arxiv.org/abs/2510.
16720.
Parth Sarthi, Salman Abdullah, Aditi Tuli, Shubh Khanna, Anna Goldie, and Christopher D. Manning. Raptor:
Recursive abstractive processing for tree-organized retrieval. ArXiv, abs/2401.18059, 2024.
DanielL.SchacterandDonnaRoseAddis. Constructivememory: Theghostsofpastandfuture. Nature,445(7123):
27, January 2007. ISSN 1476-4687. doi: 10.1038/445027a.
Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer,
NicolaCancedda,andThomasScialom. ToolFormer: Languagemodelscanteachthemselvestousetools. Advances
in Neural Information Processing Systems, 36:68539–68551, 2023.
John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization
algorithms. arXiv preprint arXiv:1707.06347, 2017.
CarolA.SegerandBrianJ.Spiering. AcriticalreviewofhabitlearningandtheBasalGanglia. FrontiersinSystems
Neuroscience, 5:66, 2011. ISSN 1662-5137. doi: 10.3389/fnsys.2011.00066.
Jay Shah, Ganesh Bikshandi, Ying Zhang, Vijay Thakkar, Pradeep Ramani, and Tri Dao. Flashattention-3: Fast
and accurate attention with asynchrony and low-precision. In Amir Globersons, Lester Mackey, Danielle Bel-
grave,AngelaFan,UlrichPaquet,JakubM.Tomczak,andChengZhang,editors,AdvancesinNeuralInformation
Processing Systems 38: Annual Conference on Neural Information Processing Systems 2024, NeurIPS 2024, Van-
couver, BC, Canada, December 10 - 15, 2024, 2024. http://papers.nips.cc/paper_files/paper/2024/hash/
7ede97c3e082c6df10a8d6103a2eebd2-Abstract-Conference.html.
Yunfan Shao, Linyang Li, Junqi Dai, and Xipeng Qiu. Character-llm: A trainable agent for role-playing. In Houda
Bouamor, Juan Pino, and Kalika Bali, editors, Proceedings of the 2023 Conference on Empirical Methods in
Natural Language Processing, EMNLP 2023, Singapore, December 6-10, 2023, pages 13153–13187. Association for
Computational Linguistics, 2023. doi: 10.18653/V1/2023.EMNLP-MAIN.814. https://doi.org/10.18653/v1/
2023.emnlp-main.814.
ZhihongShao,PeiyiWang,QihaoZhu,RunxinXu,JunxiaoSong,XiaoBi,HaoweiZhang,MingchuanZhang,YKLi,
Yang Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv
preprint arXiv:2402.03300, 2024.
JunxiaoShen,JohnJ.Dudley,andPerOlaKristensson.Encode-Store-Retrieve: AugmentingHumanMemorythrough
Language-EncodedEgocentricPerception.InUlrichEck,MishaSra,JeanineK.Stefanucci,MakiSugimoto,Markus
Tatzgern, and Ian Williams, editors, IEEE International Symposium on Mixed and Augmented Reality, ISMAR
2024,Bellevue,WA,USA,October21-25,2024,pages923–931.IEEE,2024.doi: 10.1109/ISMAR62088.2024.00108.
Hao Shi, Bin Xie, Yingfei Liu, Lin Sun, Fengrong Liu, Tiancai Wang, Erjin Zhou, Haoqiang Fan, Xiangyu Zhang,
and Gao Huang. Memoryvla: Perceptual-cognitive memory in vision-language-action models for robotic manip-
ulation. CoRR, abs/2508.19236, 2025a. doi: 10.48550/ARXIV.2508.19236. https://doi.org/10.48550/arXiv.
2508.19236.
Yaorui Shi, Yuxin Chen, Siyuan Wang, Sihang Li, Hengxing Cai, Qi Gu, Xiang Wang, and An Zhang. Look back to
reason forward: Revisitable memory for long-context llm agents, 2025b. https://arxiv.org/abs/2509.23040.
ZhengliangShi,YuhanWang,LingyongYan,PengjieRen,ShuaiqiangWang,DaweiYin,andZhaochunRen.Retrieval
models aren’t tool-savvy: Benchmarking tool retrieval for large language models, May 2025c.
91

ZitongShi,GuanchengWan,WenkeHuang,GuibinZhang,JiaweiShao,MangYe,andCarlYang. Privacy-enhancing
paradigms within federated multi-agent systems. arXiv preprint arXiv:2503.08175, 2025d.
NoahShinn,FedericoCassano,AshwinGopinath,KarthikNarasimhan,andShunyuYao.Reflexion: Languageagents
with verbal reinforcement learning. Advances in Neural Information Processing Systems, 36:8634–8652, 2023a.
Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion: lan-
guage agents with verbal reinforcement learning. In Alice Oh, Tristan Naumann, Amir Globerson,
Kate Saenko, Moritz Hardt, and Sergey Levine, editors, Advances in Neural Information Processing Sys-
tems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023, New Or-
leans, LA, USA, December 10 - 16, 2023, 2023b. http://papers.nips.cc/paper_files/paper/2023/hash/
1b44b878bb782e6954cd888628510e90-Abstract-Conference.html.
Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Côté, Yonatan Bisk, Adam Trischler, and Matthew J. Hausknecht.
Alfworld: Aligning text and embodied environments for interactive learning. In 9th International Conference on
Learning Representations, 2021.
AditiSingh,AbulEhtesham,SaketKumar,andTalaTalaeiKhoei. Agenticretrieval-augmentedgeneration: Asurvey
on agentic rag, 2025. https://arxiv.org/abs/2501.09136.
Anton Sinitsin, Vsevolod Plokhotnyuk, Dmitry V. Pyrkin, Sergei Popov, and Artem Babenko. Editable neural
networks. In8th International Conference on Learning Representations, ICLR 2020, Addis Ababa, Ethiopia, April
26-30, 2020. OpenReview.net, 2020. https://openreview.net/forum?id=HJedXaEtvS.
Chan Hee Song, Brian M. Sadler, Jiaman Wu, Wei-Lun Chao, Clayton Washington, and Yu Su. LLM-Planner:
Few-Shot Grounded Planning for Embodied Agents with Large Language Models. In IEEE/CVF International
ConferenceonComputerVision,ICCV2023,Paris,France,October1-6,2023,pages2986–2997.IEEE,2023. doi:
10.1109/ICCV51070.2023.00280.
Enxin Song, Wenhao Chai, Guanhong Wang, Yucheng Zhang, Haoyang Zhou, Feiyang Wu, Haozhe Chi, Xun Guo,
Tian Ye, Yanting Zhang, Yan Lu, Jenq-Neng Hwang, and Gaoang Wang. Moviechat: From dense token to sparse
memory for long video understanding. In IEEE/CVF Conference on Computer Vision and Pattern Recognition,
CVPR 2024, Seattle, WA, USA, June 16-22, 2024, pages 18221–18232. IEEE, 2024. doi: 10.1109/CVPR52733.
2024.01725. https://doi.org/10.1109/CVPR52733.2024.01725.
HuatongSong,JinhaoJiang,YingqianMin,JieChen,ZhipengChen,WayneXinZhao,LeiFang,andJi-RongWen.
R1-searcher: Incentivizingthesearchcapabilityinllmsviareinforcementlearning. CoRR,abs/2503.05592,2025a.
doi: 10.48550/ARXIV.2503.05592. https://doi.org/10.48550/arXiv.2503.05592.
Xinshuai Song, Weixing Chen, Yang Liu, Weikai Chen, Guanbin Li, and Liang Lin. Towards long-
horizon vision-language navigation: Platform, benchmark and method. In IEEE/CVF Conference
on Computer Vision and Pattern Recognition, CVPR 2025, Nashville, TN, USA, June 11-15, 2025,
pages 12078–12088. Computer Vision Foundation / IEEE, 2025b. doi: 10.1109/CVPR52734.2025.01128.
https://openaccess.thecvf.com/content/CVPR2025/html/Song_Towards_Long-Horizon_Vision-Language_
Navigation_Platform_Benchmark_and_Method_CVPR_2025_paper.html.
KAREN SPARCK JONES. A STATISTICAL INTERPRETATION OF TERM SPECIFICITY AND ITS AP-
PLICATION IN RETRIEVAL. Journal of Documentation, 28(1):11–21, January 1972. ISSN 0022-0418. doi:
10.1108/eb026526.
Larry R. Squire. Memory systems of the brain: A brief history and current perspective. Neurobiology of Learning
and Memory, 82(3):171–177, November 2004. ISSN 1074-7427. doi: 10.1016/j.nlm.2004.06.005.
92

LiangcaiSu, ZhenZhang, GuangyuLi, ZhuoChen, ChenxiWang, MaojiaSong, XinyuWang, KuanLi, JialongWu,
Xuanzhong Chen, Zile Qiao, Zhongwang Zhang, Huifeng Yin, Shihao Cai, Runnan Fang, Zhengwei Tao, Wenbiao
Yin, Chenxiong Qian, Yong Jiang, Pengjun Xie, Fei Huang, and Jingren Zhou. Scaling agents via continual pre-
training. CoRR, abs/2509.13310, 2025. doi: 10.48550/ARXIV.2509.13310. https://doi.org/10.48550/arXiv.
2509.13310.
Haoran Sun and Shaoning Zeng. Hierarchical memory for high-eﬀiciency long-term reasoning in llm agents. ArXiv,
abs/2507.22925, 2025.
Jingwei Sun, Zhixu Du, and Yiran Chen. Knowledge graph tuning: Real-time large language model personalization
based on human feedback, 2024. https://arxiv.org/abs/2405.19686.
Weiwei Sun, Miao Lu, Zhan Ling, Kang Liu, Xuesong Yao, Yiming Yang, and Jiecao Chen. Scaling long-horizon
LLM agent via context-folding. CoRR, abs/2510.11967, 2025a. doi: 10.48550/ARXIV.2510.11967. https://doi.
org/10.48550/arXiv.2510.11967.
Zeyi Sun, Ziyu Liu, Yuhang Zang, Yuhang Cao, Xiaoyi Dong, Tong Wu, Dahua Lin, and Jiaqi Wang. SEAgent:
Self-evolving computer use agent with autonomous learning from experience. arXiv preprint arXiv:2508.04700,
2025b.
ZhongxiangSun,ZihuaSi,XiaoxueZang,KaiZheng,YangSong,XiaoZhang,andJunXu.Largepigforhallucination-
freequerygeneration: Yourlargelanguagemodelissecretlyapointergenerator.InProceedingsoftheACMonWeb
Conference2025,WWW’25,page4766–4779,NewYork,NY,USA,2025c.AssociationforComputingMachinery.
ISBN 9798400712746. doi: 10.1145/3696410.3714800. https://doi.org/10.1145/3696410.3714800.
Zhongxiang Sun, Qipeng Wang, Weijie Yu, Xiaoxue Zang, Kai Zheng, Jun Xu, Xiao Zhang, Yang Song, and Han
Li. Rearter: Retrieval-augmented reasoning with trustworthy process rewarding. In Proceedings of the 48th
International ACM SIGIR Conference on Research and Development in Information Retrieval, pages 1251–1261,
2025d.
ZhongXiang Sun, Xiaoxue Zang, Kai Zheng, Jun Xu, Xiao Zhang, Weijie Yu, Yang Song, and Han Li. Redeep:
Detecting hallucination in retrieval-augmented generation via mechanistic interpretability. In The Thirteenth In-
ternational Conference on Learning Representations, 2025e.
Supermemory. Supermemory —Universal Memory API for AI apps — supermemory.ai. https://supermemory.ai/,
2025. [Accessed 14-12-2025].
David Silver Sutton, Richard S. Welcome to the Era of Experience, April 2025.
Mirac Suzgun, Mert Yuksekgonul, Federico Bianchi, Dan Jurafsky, and James Zou. Dynamic cheatsheet: Test-time
learning with adaptive memory, 2025. https://arxiv.org/abs/2504.07952.
Jihoon Tack, Jaehyung Kim, Eric Mitchell, Jinwoo Shin, Yee Whye Teh, and Jonathan Richard Schwarz. Online
adaptationoflanguagemodelswithamemoryofamortizedcontexts. InAmirGlobersons,LesterMackey,Danielle
Belgrave,AngelaFan,UlrichPaquet,JakubM.Tomczak,andChengZhang,editors,AdvancesinNeuralInforma-
tion Processing Systems 38: Annual Conference on Neural Information Processing Systems 2024, NeurIPS 2024,
Vancouver,BC,Canada,December10-15,2024,2024.http://papers.nips.cc/paper_files/paper/2024/hash/
eaf956b52bae51fbf387b8be4cc3ce18-Abstract-Conference.html.
Haoran Tan, Zeyu Zhang, Chen Ma, Xu Chen, Quanyu Dai, and Zhenhua Dong. MemBench: Towards more com-
prehensive evaluation on the memory of LLM-based agents. In Findings of the Association for Computational
Linguistics: ACL 2025, pages 19336–19352, Vienna, Austria, July 2025a. Association for Computational Lin-
guistics. ISBN 979-8-89176-256-5. doi: 10.18653/v1/2025.findings-acl.989. https://aclanthology.org/2025.
findings-acl.989/.
93

XingyuTan,XiaoyangWang,XiweiXu,XinYuan,LimingZhu,andWenjieZhang. Memotime: Memory-augmented
temporal knowledge graph enhanced large language model reasoning. arXiv preprint arXiv:2510.13614, 2025b.
Zhen Tan, Jun Yan, I-Hung Hsu, Rujun Han, Zifeng Wang, Long T. Le, Yiwen Song, Yanfei Chen, Hamid Palangi,
George Lee, Anand Rajan Iyer, Tianlong Chen, Huan Liu, Chen-Yu Lee, and Tomas Pfister. In prospect and
retrospect: Reflective memory management for long-term personalized dialogue agents. In Wanxiang Che, Joyce
Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar, editors, Proceedings of the 63rd Annual Meeting of
the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2025, Vienna, Austria, July 27 -
August 1, 2025,pages8416–8439.AssociationforComputationalLinguistics,2025c. https://aclanthology.org/
2025.acl-long.413/.
Hanlin Tang, Yang Lin, Jing Lin, Qingsen Han, Danning Ke, Shikuan Hong, Yiwu Yao, and Gongyi Wang.
Razorattention: Eﬀicient KV cache compression through retrieval heads. In The Thirteenth International
Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025. OpenReview.net, 2025a.
https://openreview.net/forum?id=tkiZQlL04w.
Qiaoyu Tang, Hao Xiang, Le Yu, Bowen Yu, Yaojie Lu, Xianpei Han, Le Sun, WenJuan Zhang, Pengbo Wang,
Shixuan Liu, Zhenru Zhang, Jianhong Tu, Hongyu Lin, and Junyang Lin. Beyond turn limits: Training deep
search agents with dynamic context window, October 2025b.
Xiangru Tang, Tianyu Hu, Muyang Ye, Yanjun Shao, Xunjian Yin, Siru Ouyang, Wangchunshu Zhou, Pan Lu,
Zhuosheng Zhang, Yilun Zhao, Arman Cohan, and Mark Gerstein. Chemagent: Self-updating library in large
language models improves chemical reasoning, 2025c. https://arxiv.org/abs/2501.06590.
Xiangru Tang, Tianrui Qin, Tianhao Peng, Ziyang Zhou, Daniel Shao, Tingting Du, Xinming Wei, Peng Xia, Fang
Wu, He Zhu, Ge Zhang, Jiaheng Liu, Xingyao Wang, Sirui Hong, Chenglin Wu, Hao Cheng, Chi Wang, and
Wangchunshu Zhou. Agent kb: Leveraging cross-domain experience for agentic problem solving, 2025d. https:
//arxiv.org/abs/2507.06229.
Yimin Tang, Yurong Xu, Ning Yan, and Masood Mortazavi. Enhancing long context performance in llms through
inner loop query mechanism, 2024. https://arxiv.org/abs/2410.12859.
DmitriiTarasov,ElizavetaGoncharova,andKuznetsovAndrey. Sentence-anchoredgistcompressionforlong-context
llms, 2025. https://arxiv.org/abs/2511.08128.
Yi Tay, Vinh Tran, Mostafa Dehghani, Jianmo Ni, Dara Bahri, Harsh Mehta, Zhen Qin, Kai Hui, Zhe Zhao,
Jai Prakash Gupta, Tal Schuster, William W. Cohen, and Donald Metzler. Transformer memory as a differ-
entiablesearchindex. InSanmiKoyejo, S.Mohamed, A.Agarwal, Danielle Belgrave, K.Cho, andA. Oh, editors,
Advances in Neural Information Processing Systems 35: Annual Conference on Neural Information Processing
Systems 2022, NeurIPS 2022, New Orleans, LA, USA, November 28 - December 9, 2022, 2022. http://papers.
nips.cc/paper_files/paper/2022/hash/892840a6123b5ec99ebaab8be1530fba-Abstract-Conference.html.
ShulinTian,ZiniuZhang,LiangyuChen,andZiweiLiu.Mmina: Benchmarkingmultihopmultimodalinternetagents,
2025. https://arxiv.org/abs/2404.09992.
Hieu Tran, Zonghai Yao, Nguyen Luong Tran, Zhichao Yang, Feiyun Ouyang, Shuo Han, Razieh Rahimi, and Hong
Yu. PRIME:planningandretrieval-integratedmemoryforenhancedreasoning. CoRR,abs/2509.22315,2025. doi:
10.48550/ARXIV.2509.22315. https://doi.org/10.48550/arXiv.2509.22315.
Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot, and Ashish Sabharwal. Musique: Multihop questions via
single-hop question composition, 2022. https://arxiv.org/abs/2108.00573.
EndelTulving. Episodicandsemanticmemory. InOrganizationofMemory,pagesxiii,423–xiii,423.AcademicPress,
Oxford, England, 1972.
94

EndelTulving. Episodicmemory: Frommindtobrain. AnnualReviewofPsychology,53:1–25,2002. ISSN0066-4308.
doi: 10.1146/annurev.psych.53.100901.135114.
LewisTunstall,EdwardBeeching,NathanLambert,NazneenRajani,KashifRasul,YounesBelkada,ShengyiHuang,
LeandrovonWerra,ClémentineFourrier,NathanHabib,NathanSarrazin,OmarSanseviero,AlexanderM.Rush,
and Thomas Wolf. Zephyr: Direct distillation of lm alignment, 2023. https://arxiv.org/abs/2310.16944.
Szymon Tworkowski, Konrad Staniszewski, Mikolaj Pacek, Yuhuai Wu, Henryk Michalewski, and Piotr Milos.
Focused transformer: Contrastive training for context scaling. In Alice Oh, Tristan Naumann, Amir Glober-
son, Kate Saenko, Moritz Hardt, and Sergey Levine, editors, Advances in Neural Information Processing
Systems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023, New Or-
leans, LA, USA, December 10 - 16, 2023, 2023. http://papers.nips.cc/paper_files/paper/2023/hash/
8511d06d5590f4bda24d42087802cc81-Abstract-Conference.html.
LuanboWanandWeizhiMa. Storybench: Adynamicbenchmarkforevaluatinglong-termmemorywithmultiturns.
arXiv preprint arXiv:2506.13356, 2025.
ZiyuWan,YunxiangLi,XiaoyuWen,YanSong,HanjingWang,LinyiYang,MarkSchmidt,JunWang,WeinanZhang,
ShuyueHu,andYingWen. Rema: Learningtometa-thinkforllmswithmulti-agentreinforcementlearning,2025.
https://arxiv.org/abs/2503.09501.
Bing Wang, Xinnian Liang, Jian Yang, Hui Huang, Shuangzhi Wu, Peihao Wu, Lu Lu, Zejun Ma, and Zhoujun Li.
Scm: Enhancing large language model with self-controlled memory framework, 2025a. https://arxiv.org/abs/
2304.13343.
Bo Wang, Weiyi He, Shenglai Zeng, Zhen Xiang, Yue Xing, Jiliang Tang, and Pengfei He. Unveiling privacy risks in
llm agent memory, 2025b. https://arxiv.org/abs/2502.13172.
FeiWang,XingchenWan,RuoxiSun,JiefengChen,andSercanOArik. Astuterag: Overcomingimperfectretrieval
augmentationandknowledgeconflictsforlargelanguagemodels. InProceedingsofthe63rdAnnualMeetingofthe
Association for Computational Linguistics (Volume 1: Long Papers), pages 30553–30571, 2025c.
Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima Anand-
kumar. Voyager: An open-ended embodied agent with large language models. Trans. Mach. Learn. Res., 2024,
2024a. https://openreview.net/forum?id=ehfRiF0R3a.
GuanzhiWang,YuqiXie,YunfanJiang,AjayMandlekar,ChaoweiXiao,YukeZhu,LinxiFan,andAnimaAnandku-
mar. Voyager: An Open-Ended Embodied Agent with Large Language Models. Trans. Mach. Learn. Res., 2024,
2024b. https://openreview.net/forum?id=ehfRiF0R3a.
HanWang,ArchikiPrasad,EliasStengel-Eskin,andMohitBansal. Retrieval-augmentedgenerationwithconflicting
evidence. arXiv preprint arXiv:2504.13079, 2025d.
Haochun Wang, Chi Liu, Nuwa Xi, Zewen Qiang, Sendong Zhao, Bing Qin, and Ting Liu. Huatuo: Tuning llama
model with chinese medical knowledge, 2023a. https://arxiv.org/abs/2304.06975.
Hengyi Wang, Haizhou Shi, Shiwei Tan, Weiyi Qin, Wenyuan Wang, Tunyu Zhang, Akshay Nambi, Tanuja Ganu,
and Hao Wang. Multimodal needle in a haystack: Benchmarking long-context capability of multimodal large
language models. In Luis Chiruzzo, Alan Ritter, and Lu Wang, editors, Proceedings of the 2025 Conference of the
Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies
(Volume1: LongPapers),pages3221–3241,Albuquerque,NewMexico,April2025e.AssociationforComputational
Linguistics. ISBN 979-8-89176-189-6. doi: 10.18653/v1/2025.naacl-long.166. https://aclanthology.org/2025.
naacl-long.166/.
95

Juyuan Wang, Rongchen Zhao, Wei Wei, Yufeng Wang, Mo Yu, Jie Zhou, Jin Xu, and Liyan Xu. Comorag: A
cognitive-inspired memory-organized RAG for stateful long narrative reasoning. CoRR, abs/2508.10419, 2025f.
doi: 10.48550/ARXIV.2508.10419. https://doi.org/10.48550/arXiv.2508.10419.
Mengru Wang, Ningyu Zhang, Ziwen Xu, Zekun Xi, Shumin Deng, Yunzhi Yao, Qishen Zhang, Linyi Yang, Jindong
Wang, and Huajun Chen. Detoxifying large language models via knowledge editing. In Lun-Wei Ku, Andre
Martins,andVivekSrikumar,editors,Proceedingsofthe62ndAnnualMeetingoftheAssociationforComputational
Linguistics (Volume 1: Long Papers), ACL 2024, Bangkok, Thailand, August 11-16, 2024, pages 3093–3118.
Association for Computational Linguistics, 2024c. doi: 10.18653/V1/2024.ACL-LONG.171. https://doi.org/
10.18653/v1/2024.acl-long.171.
Noah Wang, Zhongyuan Peng, Haoran Que, Jiaheng Liu, Wangchunshu Zhou, Yuhan Wu, Hongcheng Guo, Ruitong
Gan, Zehao Ni, Jian Yang, Man Zhang, Zhaoxiang Zhang, Wanli Ouyang, Ke Xu, Wenhao Huang, Jie Fu, and
Junran Peng. Rolellm: Benchmarking, eliciting, and enhancing role-playing abilities of large language models.
In Lun-Wei Ku, Andre Martins, and Vivek Srikumar, editors, Findings of the Association for Computational
Linguistics,ACL2024,Bangkok,Thailandandvirtualmeeting,August11-16,2024,pages14743–14777.Association
forComputationalLinguistics,2024d. doi: 10.18653/V1/2024.FINDINGS-ACL.878. https://doi.org/10.18653/
v1/2024.findings-acl.878.
PengWang,ZexiLi,NingyuZhang,ZiwenXu,YunzhiYao,YongJiang,PengjunXie,FeiHuang,andHuajunChen.
WISE:rethinkingtheknowledgememoryforlifelongmodeleditingoflargelanguagemodels. InAmirGlobersons,
Lester Mackey, Danielle Belgrave, Angela Fan, Ulrich Paquet, Jakub M. Tomczak, and Cheng Zhang, editors,
Advances in Neural Information Processing Systems 38: Annual Conference on Neural Information Processing
Systems 2024, NeurIPS 2024, Vancouver, BC, Canada, December 10 - 15, 2024,2024e. http://papers.nips.cc/
paper_files/paper/2024/hash/60960ad78868fce5c165295fbd895060-Abstract-Conference.html.
Piaohong Wang, Motong Tian, Jiaxian Li, Yuan Liang, Yuqing Wang, Qianben Chen, Tiannan Wang, Zhicong Lu,
Jiawei Ma, Yuchen Eleanor Jiang, and Wangchunshu Zhou. O-mem: Omni memory system for personalized, long
horizon, self-evolving agents, 2025g. https://arxiv.org/abs/2511.13593.
QingyueWang,YanheFu,YananCao,ShuaiWang,ZhiliangTian,andLiangDing. Recursivelysummarizingenables
long-term dialogue memory in large language models. Neurocomputing, 639:130193, 2025h.
RenxiWang,XudongHan,LeiJi,ShuWang,TimothyBaldwin,andHaonanLi. ToolGen: Unifiedtoolretrievaland
calling via generation. In The Thirteenth International Conference on Learning Representations, 2025i.
RuizeWang,DuyuTang,NanDuan,ZhongyuWei,XuanjingHuang,JianshuJi,GuihongCao,DaxinJiang,andMing
Zhou. K-adapter: Infusing knowledge into pre-trained models with adapters. In Chengqing Zong, Fei Xia, Wenjie
Li, and Roberto Navigli, editors, Findings of the Association for Computational Linguistics: ACL/IJCNLP 2021,
OnlineEvent, August1-6, 2021,volumeACL/IJCNLP2021ofFindingsofACL,pages1405–1418.Associationfor
Computational Linguistics, 2021. doi: 10.18653/V1/2021.FINDINGS-ACL.121. https://doi.org/10.18653/v1/
2021.findings-acl.121.
Ruoyao Wang, Peter Jansen, Marc-Alexandre Côté, and Prithviraj Ammanabrolu. Scienceworld: Is your agent
smarter than a 5th grader?, 2022a. https://arxiv.org/abs/2203.07540.
TiannanWang,MeilingTao,RuoyuFang,HuilinWang,ShuaiWang,YuchenEleanorJiang,andWangchunshuZhou.
Ai persona: Towards life-long personalization of llms, 2024f. https://arxiv.org/abs/2412.13103.
Weizhi Wang, Li Dong, Hao Cheng, Xiaodong Liu, Xifeng Yan, Jianfeng Gao, and Furu Wei. Aug-
menting language models with long-term memory. In Alice Oh, Tristan Naumann, Amir Globerson,
Kate Saenko, Moritz Hardt, and Sergey Levine, editors, Advances in Neural Information Processing Sys-
96

tems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023, New Or-
leans, LA, USA, December 10 - 16, 2023, 2023b. http://papers.nips.cc/paper_files/paper/2023/hash/
ebd82705f44793b6f9ade5a669d0f0bf-Abstract-Conference.html.
Wenyi Wang, Piotr Piękos, Li Nanbo, Firas Laakom, Yimeng Chen, Mateusz Ostaszewski, Mingchen Zhuge, and
Jürgen Schmidhuber. Huxley-godel machine: Human-level coding agent development by an approximation of the
optimal self-improving machine, 2025j. https://arxiv.org/abs/2510.21614.
Xiaohan Wang, Yuhui Zhang, Orr Zohar, and Serena Yeung-Levy. VideoAgent: Long-Form Video Understanding
with Large Language Model as Agent. In Ales Leonardis, Elisa Ricci, Stefan Roth, Olga Russakovsky, Torsten
Sattler,andGülVarol,editors,ComputerVision-ECCV2024-18thEuropeanConference,Milan,Italy,September
29-October 4, 2024, Proceedings, Part LXXX, volume 15138 of Lecture Notes in Computer Science, pages 58–76.
Springer, 2024g. doi: 10.1007/978-3-031-72989-8_4.
Yancheng Wang, Ziyan Jiang, Zheng Chen, Fan Yang, Yingxue Zhou, Eunah Cho, Xing Fan, Yanbin Lu, Xiaojiang
Huang,andYingzhenYang.RecMind: LargeLanguageModelPoweredAgentForRecommendation.InKevinDuh,
Helena Gómez-Adorno, and Steven Bethard, editors, Findings of the Association for Computational Linguistics:
NAACL2024,MexicoCity,Mexico,June16-21,2024,pages4351–4364.AssociationforComputationalLinguistics,
2024h. doi: 10.18653/V1/2024.FINDINGS-NAACL.271. https://doi.org/10.18653/v1/2024.findings-naacl.
271.
Yanlin Wang, Wanjun Zhong, Yanxian Huang, Ensheng Shi, Min Yang, Jiachi Chen, Hui Li, Yuchi Ma, Qianxiang
Wang, and Zibin Zheng. Agents in software engineering: Survey, landscape, and vision, 2024i. https://arxiv.
org/abs/2409.09030.
Yingxu Wang, Siwei Liu, Jinyuan Fang, and Zaiqiao Meng. EvoAgentX: An automated framework for evolving
agentic workflows. arXiv preprint arXiv:2507.03616, 2025k.
YipingWang,QingYang,ZhiyuanZeng,LiliangRen,LiyuanLiu,BaolinPeng,HaoCheng,XuehaiHe,KuanWang,
Jianfeng Gao, Weizhu Chen, Shuohang Wang, Simon Shaolei Du, and Yelong Shen. Reinforcement learning for
reasoning in large language models with one training example, 2025l. https://arxiv.org/abs/2504.20571.
YuWangandXiChen. MIRIX: Multi-agentmemorysystemforllm-basedagents. arXiv preprint arXiv:2507.07957,
2025.
Yu Wang, Xiusi Chen, Jingbo Shang, and Julian McAuley. Memoryllm: Towards self-updatable large language
models. ArXiv, abs/2402.04624, 2024j. https://api.semanticscholar.org/CorpusID:267523037.
YuWang,DmitryKrotov,YuanzheHu,YifanGao,WangchunshuZhou,JulianJ.McAuley,DanGutfreund,Rogério
Feris,andZexueHe. M+: extendingmemoryllmwithscalablelong-termmemory. CoRR,abs/2502.00592,2025m.
doi: 10.48550/ARXIV.2502.00592. https://doi.org/10.48550/arXiv.2502.00592.
YuWang,XinshuangLiu,XiusiChen,SeanO’Brien,JundaWu,andJulianJ.McAuley.Self-updatablelargelanguage
models by integrating context into model parameters. In The Thirteenth International Conference on Learning
Representations, ICLR 2025, Singapore, April 24-28, 2025. OpenReview.net, 2025n. https://openreview.net/
forum?id=aCPFCDL9QY.
YuWang,RyuichiTakanobu,ZhiqiLiang,YuzhenMao,YuanzheHu,JulianJ.McAuley,andXiaojianWu. Mem-α:
Learning memory construction via reinforcement learning. CoRR, abs/2509.25911, 2025o. doi: 10.48550/ARXIV.
2509.25911. https://doi.org/10.48550/arXiv.2509.25911.
YujingWang,YingyanHou,HaonanWang,ZimingMiao,ShibinWu,QiChen,YuqingXia,ChengminChi,Guoshuai
Zhao,ZhengLiu,XingXie,HaoSun,WeiweiDeng,QiZhang,andMaoYang.Aneuralcorpusindexerfordocument
retrieval. InSanmiKoyejo,S.Mohamed, A.Agarwal,DanielleBelgrave, K.Cho, andA.Oh, editors, Advances in
97

Neural Information Processing Systems 35: Annual Conference on Neural Information Processing Systems 2022,
NeurIPS2022,NewOrleans,LA,USA,November28-December9,2022,2022b. http://papers.nips.cc/paper_
files/paper/2022/hash/a46156bd3579c3b268108ea6aca71d13-Abstract-Conference.html.
Zheng Wang, Zhongyang Li, Zeren Jiang, Dandan Tu, and Wei Shi. Crafting personalized agents through retrieval-
augmented generation on editable memory graphs, 2024k. https://arxiv.org/abs/2409.19401.
Zihao Wang, Shaofei Cai, Anji Liu, Yonggang Jin, Jinbing Hou, Bowei Zhang, Haowei Lin, Zhaofeng He, Zilong
Zheng, Yaodong Yang, Xiaojian Ma, and Yitao Liang. JARVIS-1: open-world multi-task agents with memory-
augmented multimodal language models. IEEE Trans. Pattern Anal. Mach. Intell., 47(3):1894–1907, 2025p. doi:
10.1109/TPAMI.2024.3511593. https://doi.org/10.1109/TPAMI.2024.3511593.
Zixuan Wang, Bo Yu, Junzhe Zhao, Wenhao Sun, Sai Hou, Shuai Liang, Xing Hu, Yinhe Han, and Yiming Gan.
KARMA: Augmenting Embodied AI Agents with Long-and-Short Term Memory Systems. In IEEE International
Conference on Robotics and Automation, ICRA 2025, Atlanta, GA, USA, May 19-23, 2025, pages 1–8. IEEE,
2025q. doi: 10.1109/ICRA55743.2025.11128047.
Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, and Graham Neubig. Agent workflow memory. In Forty-second
International Conference on Machine Learning, 2024l.
Zora Zhiruo Wang, Apurva Gandhi, Graham Neubig, and Daniel Fried. Inducing programmatic skills for agentic
tasks, 2025r. https://arxiv.org/abs/2504.06821.
JoelWard. Memoriesdb: Atemporal-semantic-relationaldatabaseforlong-termagentmemory/modelingexperience
as a graph of temporal-semantic surfaces. arXiv preprint arXiv:2511.06179, 2025.
Christopher Watkins and Peter Dayan. Q-learning. Machine Learning, 8:279–292, 1992. https://api.
semanticscholar.org/CorpusID:208910339.
Haoran Wei, Yaofeng Sun, and Yukun Li. Deepseek-ocr: Contexts optical compression. arXiv preprint
arXiv:2510.18234, 2025a.
Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai,
and Quoc V. Le. Finetuned language models are zero-shot learners, 2022. https://arxiv.org/abs/2109.01652.
JasonWei,ZhiqingSun,SpencerPapay,ScottMcKinney,JeffreyHan,IsaFulford,HyungWonChung,AlexTachard
Passos,WilliamFedus,andAmeliaGlaese.BrowseComp: Asimpleyetchallengingbenchmarkforbrowsingagents.
arXiv preprint arXiv:2504.12516, 2025b.
Jiaqi Wei, Yuejin Yang, Xiang Zhang, Yuhan Chen, Xiang Zhuang, Zhangyang Gao, Dongzhan Zhou, Guangshuai
Wang,ZhiqiangGao,JuntaiCao,ZijieQiu,MingHu,ChenglongMa,ShixiangTang,JunjunHe,ChunfengSong,
Xuming He, Qiang Zhang, Chenyu You, Shuangjia Zheng, Ning Ding, Wanli Ouyang, Nanqing Dong, Yu Cheng,
Siqi Sun, Lei Bai, and Bowen Zhou. From ai for science to agentic science: A survey on autonomous scientific
discovery, 2025c. https://arxiv.org/abs/2508.14111.
RubinWei,JiaqiCao,JiaruiWang,JushiKai,QipengGuo,BowenZhou,andZhouhanLin.MLPmemory: Language
modeling with retriever-pretrained external memory. CoRR, abs/2508.01832, 2025d. doi: 10.48550/ARXIV.2508.
01832. https://doi.org/10.48550/arXiv.2508.01832.
TianxinWei,NoveenSachdeva,BenjaminColeman,ZhankuiHe, YuanchenBei,XuyingNing,MengtingAi, Yunzhe
Li, Jingrui He, Ed H Chi, et al. Evo-memory: Benchmarking llm agent test-time learning with self-evolving
memory. arXiv preprint arXiv:2511.20857, 2025e.
Yixuan Weng, Minjun Zhu, Qiujie Xie, Qiyao Sun, Zhen Lin, Sifan Liu, and Yue Zhang. Deepscientist: Advancing
frontier-pushing scientific findings progressively, 2025. https://arxiv.org/abs/2509.26603.
98

Rebecca Westhäußer, Wolfgang Minker, and Sebastian Zepf. Enabling personalized long-term interactions in llm-
based agents through persistent memory and user profiles. CoRR, abs/2510.07925, 2025. doi: 10.48550/ARXIV.
2510.07925. https://doi.org/10.48550/arXiv.2510.07925.
Martin Wistuba, Prabhu Teja Sivaprasad, Lukas Balles, and Giovanni Zappella. Continual learning with low rank
adaptation. CoRR,abs/2311.17601,2023. doi: 10.48550/ARXIV.2311.17601. https://doi.org/10.48550/arXiv.
2311.17601.
Cheng-Kuang Wu, Zhi Rui Tam, Chieh-Yen Lin, Yun-Nung Chen, and Hung-yi Lee. Streambench: Towards bench-
marking continuous improvement of language agents. In Amir Globersons, Lester Mackey, Danielle Belgrave,
Angela Fan, Ulrich Paquet, Jakub M. Tomczak, and Cheng Zhang, editors, Advances in Neural Information
Processing Systems 38: Annual Conference on Neural Information Processing Systems 2024, NeurIPS 2024, Van-
couver, BC, Canada, December 10 - 15, 2024, 2024a. http://papers.nips.cc/paper_files/paper/2024/hash/
c189915371c4474fe9789be3728113fc-Abstract-Datasets_and_Benchmarks_Track.html.
Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, and Dong Yu. Longmemeval: Benchmarking
chat assistants on long-term interactive memory. In The Thirteenth International Conference on Learning Repre-
sentations, ICLR 2025, Singapore, April 24-28, 2025. OpenReview.net, 2025a. https://openreview.net/forum?
id=pZiyCaVuti.
Jeff Wu, Long Ouyang, Daniel M Ziegler, Nisan Stiennon, Ryan Lowe, Jan Leike, and Paul Christiano. Recursively
summarizing books with human feedback. arXiv preprint arXiv:2109.10862, 2021.
Jialong Wu, Baixuan Li, Runnan Fang, Wenbiao Yin, Liwen Zhang, Zhengwei Tao, Dingchu Zhang, Zekun Xi,
Yong Jiang, Pengjun Xie, Fei Huang, and Jingren Zhou. Webdancer: Towards autonomous information seeking
agency. CoRR, abs/2505.22648, 2025b. doi: 10.48550/ARXIV.2505.22648. https://doi.org/10.48550/arXiv.
2505.22648.
Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang, Shaokun
Zhang, Jiale Liu, et al. Autogen: Enabling next-gen llm applications via multi-agent conversations. In First
Conference on Language Modeling, 2024b.
Rong Wu, Xiaoman Wang, Jianbiao Mei, Pinlong Cai, Daocheng Fu, Cheng Yang, Licheng Wen, Xuemeng Yang,
YufanShen,YuxinWang,andBotianShi. Evolver: Self-evolvingllmagentsthroughanexperience-drivenlifecycle,
2025c. https://arxiv.org/abs/2510.16079.
WenyiWu,ZixuanSong,KunZhou,YifeiShao,ZhitingHu,andBiweiHuang. Towardsgeneralcontinuousmemory
for vision-language models. ArXiv, abs/2505.17670, 2025d.
Wenyi Wu, Kun Zhou, Ruoxin Yuan, Vivian Yu, Stephen Wang, Zhiting Hu, and Biwei Huang. Auto-scaling
continuous memory for GUI agent. CoRR, abs/2510.09038, 2025e. doi: 10.48550/ARXIV.2510.09038. https:
//doi.org/10.48550/arXiv.2510.09038.
Xixi Wu, Kuan Li, Yida Zhao, Liwen Zhang, Litu Ou, Huifeng Yin, Zhongwang Zhang, Yong Jiang, Pengjun Xie,
FeiHuang,MinhaoCheng,ShuaiWang,HongCheng,andJingrenZhou. ReSum: UnlockingLong-HorizonSearch
Intelligence via Context Summarization. CoRR, abs/2509.13313, 2025f. doi: 10.48550/ARXIV.2509.13313.
Yaxiong Wu, Sheng Liang, Chen Zhang, Yichao Wang, Yongyue Zhang, Huifeng Guo, Ruiming Tang, and Yong
Liu. From human memory to ai memory: A survey on memory mechanisms in the era of llms, 2025g. https:
//arxiv.org/abs/2504.15965.
Yaxiong Wu, Yongyue Zhang, Sheng Liang, and Yong Liu. Sgmem: Sentence graph memory for long-term conversa-
tional agents. ArXiv, abs/2509.21212, 2025h.
99

Yiran Wu, Feiran Jia, Shaokun Zhang, Hangyu Li, Erkang Zhu, Yue Wang, Yin Tat Lee, Richard Peng, Qingyun
Wu, and Chi Wang. Mathchat: Converse to tackle challenging math problems with llm agents, 2024c. https:
//arxiv.org/abs/2306.01337.
Yisha Wu, Cen Zhao, Yuanpei Cao, Xiaoqing Xu, Yashar Mehdad, Mindy Ji, and Claire Na Cheng. Incremental
summarization for customer support via progressive note-taking and agent feedback. In Proceedings of the 2025
Conference on Empirical Methods in Natural Language Processing: Industry Track, pages 2000–2015, 2025i.
Yuhuai Wu, Markus Norman Rabe, DeLesley Hutchins, and Christian Szegedy. Memorizing transformers. In The
TenthInternationalConferenceonLearningRepresentations,ICLR2022,VirtualEvent,April25-29,2022.Open-
Review.net, 2022. https://openreview.net/forum?id=TrjbxzRcnf-.
ZijunWu,YongchangHao,andLiliMou. Tokmem: Tokenizedproceduralmemoryforlargelanguagemodels,2025j.
https://arxiv.org/abs/2510.00444.
RuiXiandXianghanWang. Livia: Anemotion-awareARcompanionpoweredbymodularAIagentsandprogressive
memory compression. CoRR, abs/2509.05298, 2025. doi: 10.48550/ARXIV.2509.05298. https://doi.org/10.
48550/arXiv.2509.05298.
Yunjia Xi, Weiwen Liu, Jianghao Lin, Bo Chen, Ruiming Tang, Weinan Zhang, and Yong Yu. Memocrs: Memory-
enhanced sequential conversational recommender systems with large language models. In Edoardo Serra and
FrancescaSpezzano,editors,Proceedingsofthe33rdACMInternationalConferenceonInformationandKnowledge
Management, CIKM 2024, Boise, ID, USA, October 21-25, 2024, pages 2585–2595. ACM, 2024a. doi: 10.1145/
3627673.3679599. https://doi.org/10.1145/3627673.3679599.
ZhihengXi,YiwenDing,WenxiangChen,BoyangHong,HonglinGuo,JunzheWang,DingwenYang,ChenyangLiao,
Xin Guo, Wei He, Songyang Gao, Lu Chen, Rui Zheng, Yicheng Zou, Tao Gui, Qi Zhang, Xipeng Qiu, Xuanjing
Huang, Zuxuan Wu, and Yu-Gang Jiang. Agentgym: Evolving large language model-based agents across diverse
environments, 2024b. https://arxiv.org/abs/2406.04151.
Siyu Xia, Zekun Xu, Jiajun Chai, Wentian Fan, Yan Song, Xiaohan Wang, Guojun Yin, Wei Lin, Haifeng Zhang,
andJunWang. Fromexperiencetostrategy: Empoweringllmagentswithtrainablegraphmemory. arXivpreprint
arXiv:2511.07800, 2025.
Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis. Eﬀicient streaming language models
with attention sinks. In The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna,
Austria, May 7-11, 2024. OpenReview.net, 2024. https://openreview.net/forum?id=NG7sS51zVF.
Yuan-An Xiao, Pengfei Gao, Chao Peng, and Yingfei Xiong. Improving the eﬀiciency of llm agent systems through
trajectory reduction, 2025a. https://arxiv.org/abs/2509.23586.
YunzhongXiao,YangminLi,HeweiWang,YunlongTang,andZoraZhiruoWang. ToolMem: EnhancingMultimodal
AgentswithLearnableToolCapabilityMemory.CoRR,abs/2510.06664,2025b.doi: 10.48550/ARXIV.2510.06664.
https://doi.org/10.48550/arXiv.2510.06664. arXiv: 2510.06664.
Zeqi Xiao, Yushi Lan, Yifan Zhou, Wenqi Ouyang, Shuai Yang, Yanhong Zeng, and Xingang Pan. Worldmem:
Long-term consistent world simulation with memory. arXiv preprint arXiv:2504.12369, 2025c.
Junlin Xie, Zhihong Chen, Ruifei Zhang, Xiang Wan, and Guanbin Li. Large multimodal agents: A survey, 2024.
https://arxiv.org/abs/2402.15116.
Haoran Xu, Jiacong Hu, Ke Zhang, Lei Yu, Yuxin Tang, Xinyuan Song, Yiqun Duan, Lynn Ai, and Bill Shi. Sedm:
Scalable self-evolving distributed memory for agents, 2025a. https://arxiv.org/abs/2509.09498.
100

MufanXu, GewenLiang, KehaiChen, WeiWang, XunZhou, MuyunYang, TiejunZhao, andMinZhang. Memory-
augmentedqueryreconstructionforllm-basedknowledgegraphreasoning,2025b. https://arxiv.org/abs/2503.
05193.
Renjun Xu and Jingwen Peng. A comprehensive survey of deep research: Systems, methodologies, and applications,
2025. https://arxiv.org/abs/2506.12594.
WujiangXu,ZujieLiang,KaiMei,HangGao,JuntaoTan,andYongfengZhang. A-MEM:AgenticMemoryforLLM
Agents. CoRR, abs/2502.12110, 2025c. doi: 10.48550/ARXIV.2502.12110.
Yige Xu, Xu Guo, Zhiwei Zeng, and Chunyan Miao. Softcot: Soft chain-of-thought for eﬀicient reasoning with llms.
In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar, editors, Proceedings of
the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2025,
Vienna, Austria, July 27 - August 1, 2025, pages 23336–23351. Association for Computational Linguistics, 2025d.
https://aclanthology.org/2025.acl-long.1137/.
B.Y.Yan,ChaofanLi,HongjinQian,ShuqiLu,andZhengLiu.Generalagenticmemoryviadeepresearch,November
2025a.
MingYan,RuihaoLi,HaoZhang,HaoWang,ZhilanYang,andJiYan.Larp: Language-agentroleplayforopen-world
games, 2023. https://arxiv.org/abs/2312.17653.
SikuanYan,XiufengYang,ZuchaoHuang,ErcongNie,ZifengDing,ZonggenLi,XiaowenMa,HinrichSchütze,Volker
Tresp, and Yunpu Ma. Memory-R1: Enhancing large language model agents to manage and utilize memories via
reinforcement learning. arXiv preprint arXiv:2508.19828, 2025b.
Hongkang Yang, Zehao Lin, Wenjin Wang, Hao Wu, Zhiyu Li, Bo Tang, Wenqiang Wei, Jinbo Wang, Zeyun Tang,
3
Shichao Song, Chenyang Xi, Yu Yu, Kai Chen, Feiyu Xiong, Linpeng Tang, and Weinan E. Memory : Language
modeling with explicit memory. CoRR, abs/2407.01178, 2024a. doi: 10.48550/ARXIV.2407.01178. https://doi.
org/10.48550/arXiv.2407.01178.
Ling Yang, Zhaochen Yu, Tianjun Zhang, Shiyi Cao, Minkai Xu, Wentao Zhang, Joseph E. Gonzalez, and Bin Cui.
Bufferofthoughts: Thought-augmentedreasoningwithlargelanguagemodels.InAmirGlobersons,LesterMackey,
DanielleBelgrave,AngelaFan,UlrichPaquet,JakubM.Tomczak,andChengZhang,editors,Advances in Neural
InformationProcessingSystems38: AnnualConferenceonNeuralInformationProcessingSystems2024, NeurIPS
2024, Vancouver, BC, Canada, December 10 - 15, 2024, 2024b. http://papers.nips.cc/paper_files/paper/
2024/hash/cde328b7bf6358f5ebb91fe9c539745e-Abstract-Conference.html.
ZhilinYang,PengQi,SaizhengZhang,YoshuaBengio,WilliamW.Cohen,RuslanSalakhutdinov,andChristopherD.
Manning. Hotpotqa: A dataset for diverse, explainable multi-hop question answering, 2018. https://arxiv.org/
abs/1809.09600.
Ziyi Yang, Zaibin Zhang, Zirui Zheng, Yuxian Jiang, Ziyue Gan, Zhiyu Wang, Zijian Ling, Jinsong Chen, Martz
Ma, Bowen Dong, Prateek Gupta, Shuyue Hu, Zhenfei Yin, Guohao Li, Xu Jia, Lijun Wang, Bernard Ghanem,
Huchuan Lu, Chaochao Lu, Wanli Ouyang, Yu Qiao, Philip Torr, and Jing Shao. Oasis: Open agent social
interaction simulations with one million agents, 2025. https://arxiv.org/abs/2411.11581.
Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan. Webshop: Towards scalable real-world web
interaction with grounded language agents, 2023a. https://arxiv.org/abs/2207.01206.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik R Narasimhan, and Yuan Cao. ReAct:
Synergizing reasoning and acting in language models. In The Eleventh International Conference on Learning
Representations, 2023b.
101

Weiran Yao, Shelby Heinecke, Juan Carlos Niebles, Zhiwei Liu, Yihao Feng, Le Xue, Rithesh R. N., Zeyuan Chen,
JianguoZhang,DevanshArpit,RanXu,PhilMui,HuanWang,CaimingXiong,andSilvioSavarese. Retroformer:
Retrospective large language agents with policy gradient optimization. In The Twelfth International Conference
on Learning Representations, 2024a.
Yao Yao, Zuchao Li, and Hai Zhao. Sirllm: Streaming infinite retentive LLM. In Lun-Wei Ku, Andre Martins, and
VivekSrikumar,editors,Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), ACL 2024, Bangkok, Thailand, August 11-16, 2024, pages 2611–2624. Association
for Computational Linguistics, 2024b. doi: 10.18653/V1/2024.ACL-LONG.143. https://doi.org/10.18653/v1/
2024.acl-long.143.
Rui Ye, Zhongwang Zhang, Kuan Li, Huifeng Yin, Zhengwei Tao, Yida Zhao, Liangcai Su, Liwen Zhang, Zile Qiao,
Xinyu Wang, et al. Agentfold: Long-horizon web agents with proactive context management. arXiv preprint
arXiv:2510.24699, 2025a.
2
Shicheng Ye, Chao Yu, Kaiqiang Ke, Chengdong Xu, and Yinqi Wei. H r: Hierarchical hindsight reflection for
multi-task LLM agents. CoRR, abs/2509.12810, 2025b. doi: 10.48550/ARXIV.2509.12810. https://doi.org/10.
48550/arXiv.2509.12810.
RyanYenandJianZhao.Memolet: ReifyingtheReuseofUser-AIConversationalMemories.InProceedingsofthe37th
Annual ACM Symposium on User Interface Software and Technology,UIST’24,pages1–22,NewYork,NY,USA,
October 2024. Association for Computing Machinery. ISBN 979-8-4007-0628-8. doi: 10.1145/3654777.3676388.
Xunjian Yin, Xinyi Wang, Liangming Pan, Li Lin, Xiaojun Wan, and William Yang Wang. Gödel agent: A self-
referentialagentframeworkforrecursivelyself-improvement.InWanxiangChe,JoyceNabende,EkaterinaShutova,
and Mohammad Taher Pilehvar, editors, Proceedings of the 63rd Annual Meeting of the Association for Computa-
tional Linguistics (Volume 1: Long Papers), ACL 2025, Vienna, Austria, July 27 - August 1, 2025, pages 27890–
27913. Association for Computational Linguistics, 2025. https://aclanthology.org/2025.acl-long.1354/.
ChanwoongYoon,TaewhooLee,HyeonHwang,MinbyulJeong,andJaewooKang.CompAct: CompressingRetrieved
Documents Actively for Question Answering. In Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen, editors,
Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, EMNLP 2024, Miami,
FL, USA, November 12-16, 2024, pages 21424–21439. Association for Computational Linguistics, 2024. doi: 10.
18653/V1/2024.EMNLP-MAIN.1194.
Zeng You, Zhiquan Wen, Yaofo Chen, Xin Li, Runhao Zeng, Yaowei Wang, and Mingkui Tan. Towards long video
understanding via fine-detailed video story generation. IEEE Transactions on Circuits and Systems for Video
Technology, 2024.
Hongli Yu, Tinghong Chen, Jiangtao Feng, Jiangjie Chen, Weinan Dai, Qiying Yu, Ya-Qin Zhang, Wei-Ying Ma,
Jingjing Liu, Mingxuan Wang, et al. Memagent: Reshaping long-context llm with multi-conv rl-based memory
agent. arXiv preprint arXiv:2507.02259, 2025a.
Jiwen Yu, Jianhong Bai, Yiran Qin, Quande Liu, Xintao Wang, Pengfei Wan, Di Zhang, and Xihui Liu. Context as
memory: Scene-consistentinteractivelongvideogenerationwithmemoryretrieval. CoRR,abs/2506.03141,2025b.
doi: 10.48550/ARXIV.2506.03141. https://doi.org/10.48550/arXiv.2506.03141.
Jiwen Yu, Jianhong Bai, Yiran Qin, Quande Liu, Xintao Wang, Pengfei Wan, Di Zhang, and Xihui Liu. Con-
text as memory: Scene-consistent interactive long video generation with memory retrieval. arXiv preprint
arXiv:2506.03141, 2025c.
TaoYu,ZhengboZhang,ZhihengLyu,JunhaoGong,HongzhuYi,XinmingWang,YuxuanZhou,JiabingYang,Ping
102

Nie, Yan Huang, and Wenhu Chen. BrowserAgent: Building Web Agents with Human-Inspired Web Browsing
Actions, October 2025d. http://arxiv.org/abs/2510.10666. arXiv:2510.10666 [cs].
Xinlei Yu, Chengming Xu, Guibin Zhang, Zhangquan Chen, Yudong Zhang, Yongbo He, Peng-Tao Jiang, Jiangning
Zhang, Xiaobin Hu, and Shuicheng Yan. Vismem: Latent vision memory unlocks potential of vision-language
models, 2025e. https://arxiv.org/abs/2511.11007.
Yangyang Yu, Zhiyuan Yao, Haohang Li, Zhiyang Deng, Yuechen Jiang, Yupeng Cao, Zhi Chen, Jordan Suchow,
Zhenyu Cui, Rong Liu, et al. Fincon: A synthesized llm multi-agent system with conceptual verbal reinforcement
for enhanced financial decision making. Advances in Neural Information Processing Systems, 37:137010–137045,
2024.
YifeiYu,XiaoshanWu,XintingHu,TaoHu,YangtianSun,XiaoyangLyu,BoWang,LinMa,YuewenMa,Zhongrui
Wang, et al. Videossm: Autoregressive long video generation with hybrid state-space memory. arXiv preprint
arXiv:2512.04519, 2025f.
LifanYuan,YangyiChen,XingyaoWang,YiFung,HaoPeng,andHengJi. CRAFT:CustomizingLLMsbyCreating
and Retrieving from Specialized Toolsets. In The Twelfth International Conference on Learning Representations,
ICLR 2024, Vienna, Austria, May 7-11, 2024. OpenReview.net, 2024a. https://openreview.net/forum?id=
G0vdDSt9XM.
Peiwen Yuan, Xinglin Wang, Shaoxiong Feng, Boyuan Pan, Yiwei Li, Heda Wang, Xupeng Miao, and Kan Li.
Generativedenseretrieval: Memorycanbeaburden. InYvetteGrahamandMatthewPurver,editors,Proceedings
of the 18th Conference of the European Chapter of the Association for Computational Linguistics, EACL 2024 -
Volume 1: Long Papers, St. Julian’s, Malta, March 17-22, 2024, pages 2835–2845. Association for Computational
Linguistics, 2024b. https://aclanthology.org/2024.eacl-long.173.
Qianhao Yuan, Jie Lou, Zichao Li, Jiawei Chen, Yaojie Lu, Hongyu Lin, Le Sun, Debing Zhang, and Xianpei Han.
MemSearcher: Training LLMs to Reason, Search and Manage Memory via End-to-End Reinforcement Learning,
November 2025a.
Ruifeng Yuan, Shichao Sun, Yongqi Li, Zili Wang, Ziqiang Cao, and Wenjie Li. Personalized large language model
assistant with evolving conditional memory. In Owen Rambow, Leo Wanner, Marianna Apidianaki, Hend Al-
Khalifa, Barbara Di Eugenio, and Steven Schockaert, editors, Proceedings of the 31st International Conference on
Computational Linguistics, COLING 2025, Abu Dhabi, UAE, January 19-24, 2025, pages 3764–3777. Association
for Computational Linguistics, 2025b. https://aclanthology.org/2025.coling-main.254/.
WeizheYuan,RichardYuanzhePang,KyunghyunCho,XianLi,SainbayarSukhbaatar,JingXu,andJasonWeston.
Self-rewardinglanguagemodels.InForty-firstInternationalConferenceonMachineLearning,ICML2024,Vienna,
Austria, July 21-27, 2024. OpenReview.net, 2024c. https://openreview.net/forum?id=0NphYCmgua.
SizheYuen,FranciscoGomezMedina,TingSu,YaliDu,andAdamJ.Sobey.Intrinsicmemoryagents: Heterogeneous
multi-agent llm systems through structured contextual memory, 2025. https://arxiv.org/abs/2508.08997.
Manzil Zaheer, Guru Guruganesh, Kumar Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontañón, Philip
Pham, Anirudh Ravula, Qifan Wang, Li Yang, and Amr Ahmed. Big bird: Transformers for longer sequences.
In Hugo Larochelle, Marc’Aurelio Ranzato, Raia Hadsell, Maria-Florina Balcan, and Hsuan-Tien Lin, editors,
Advances in Neural Information Processing Systems 33: Annual Conference on Neural Information Processing
Systems 2020, NeurIPS 2020, December 6-12, 2020, virtual, 2020. https://proceedings.neurips.cc/paper/
2020/hash/c8512d142a2d849725f31a9a7a361ab9-Abstract.html.
Eric Zelikman, Yuhuai Wu, Jesse Mu, and Noah Goodman. STaR: Bootstrapping reasoning with reasoning. In
Advances in Neural Information Processing Systems, volume 35, pages 15476–15488, 2022.
103

Hansi Zeng, Chen Luo, Bowen Jin, Sheikh Muhammad Sarwar, Tianxin Wei, and Hamed Zamani. Scalable and
effective generative information retrieval. In Tat-Seng Chua, Chong-Wah Ngo, Ravi Kumar, Hady W. Lauw, and
Roy Ka-Wei Lee, editors, Proceedings of the ACM on Web Conference 2024, WWW 2024, Singapore, May 13-17,
2024,pages1441–1452.ACM,2024. doi: 10.1145/3589334.3645477. https://doi.org/10.1145/3589334.3645477.
Yunpeng Zhai, Shuchang Tao, Cheng Chen, Anni Zou, Ziqian Chen, Qingxu Fu, Shinji Mai, Li Yu, Jiaji Deng,
Zouying Cao, Zhaoyang Liu, Bolin Ding, and Jingren Zhou. Agentevolver: Towards eﬀicient self-evolving agent
system, 2025. https://arxiv.org/abs/2511.10395.
Chaoyun Zhang, He Huang, Chiming Ni, Jian Mu, Si Qin, Shilin He, Lu Wang, Fangkai Yang, Pu Zhao, Chao Du,
Liqun Li, Yu Kang, Zhao Jiang, Suzhen Zheng, Rujia Wang, Jiaxu Qian, Minghua Ma, Jian-Guang Lou, Qingwei
Lin, Saravan Rajmohan, and Dongmei Zhang. UFO2: the desktop agentos. CoRR, abs/2504.14603, 2025a. doi:
10.48550/ARXIV.2504.14603. https://doi.org/10.48550/arXiv.2504.14603.
Gaoke Zhang, Bo Wang, Yunlong Ma, Dongming Zhao, and Zifei Yu. Multiple memory systems for enhancing the
long-termmemoryofagent. CoRR,abs/2508.15294,2025b. doi: 10.48550/ARXIV.2508.15294. https://doi.org/
10.48550/arXiv.2508.15294.
Gui-Min Zhang, Muxin Fu, Guancheng Wan, Miao Yu, Kun Wang, and Shuicheng Yan. G-memory: Tracing hierar-
chical memory for multi-agent systems. ArXiv, abs/2506.07398, 2025c.
Gui-MinZhang,MuxinFu,andShuichengYan. Memgen: Weavinggenerativelatentmemoryforself-evolvingagents.
ArXiv, abs/2509.24704, 2025d.
GuibinZhang,MuxinFu,GuanchengWan,MiaoYu,KunWang,andShuichengYan.G-Memory: Tracinghierarchical
memory for multi-agent systems. arXiv preprint arXiv:2506.07398, 2025e.
GuibinZhang,HejiaGeng,XiaohangYu,ZhenfeiYin,ZaibinZhang,ZelinTan,HengZhou,ZhongzhiLi,Xiangyuan
Xue,YijiangLi,YifanZhou,YangChen,ChenZhang,YutaoFan,ZihuWang,SongtaoHuang,YueLiao,Hongru
Wang, Mengyue Yang, Heng Ji, Michael Littman, Jun Wang, Shuicheng Yan, Philip Torr, and Lei Bai. The
landscape of agentic reinforcement learning for llms: A survey, 2025f. https://arxiv.org/abs/2509.02547.
Guibin Zhang, Fanci Meng, Guancheng Wan, Zherui Li, Kun Wang, Zhenfei Yin, Lei Bai, and Shuicheng Yan.
Latentevolve: Self-evolving test-time scaling in latent space, 2025g. https://arxiv.org/abs/2509.24771.
Jenny Zhang, Shengran Hu, Cong Lu, Robert T. Lange, and Jeff Clune. Darwin Godel Machine: Open-Ended
Evolution of Self-Improving Agents. CoRR, abs/2505.22954, 2025h. doi: 10.48550/ARXIV.2505.22954. https:
//doi.org/10.48550/arXiv.2505.22954. arXiv: 2505.22954.
Jiarui Zhang. Guided profile generation improves personalization with llms. arXiv preprint arXiv:2409.13093, 2024.
Jiayi Zhang, Jinyu Xiang, Zhaoyang Yu, Fengwei Teng, Xiong-Hui Chen, Jiaqi Chen, Mingchen Zhuge, Xin Cheng,
Sirui Hong, Jinlin Wang, Bingnan Zheng, Bang Liu, Yuyu Luo, and Chenglin Wu. AFlow: Automating agentic
workflow generation. In The Thirteenth International Conference on Learning Representations, 2025i.
Kai Zhang, Xiangchao Chen, Bo Liu, Tianci Xue, Zeyi Liao, Zhihan Liu, Xiyao Wang, Yuting Ning, Zhaorun Chen,
Xiaohan Fu, Jian Xie, Yuxuan Sun, Boyu Gou, Qi Qi, Zihang Meng, Jianwei Yang, Ning Zhang, Xian Li, Ashish
Shah,DatHuynh,HengduoLi,ZiYang,SaraCao,LawrenceJang,ShuyanZhou,JiachengZhu,HuanSun,Jason
Weston, Yu Su, and Yifan Wu. Agent learning via early experience, 2025j. https://arxiv.org/abs/2510.08558.
Kaiyan Zhang, Yuxin Zuo, Bingxiang He, Youbang Sun, Runze Liu, Che Jiang, Yuchen Fan, Kai Tian, Guoli Jia,
Pengfei Li, Yu Fu, Xingtai Lv, Yuchen Zhang, Sihang Zeng, Shang Qu, Haozhan Li, Shijie Wang, Yuru Wang,
Xinwei Long, Fangfu Liu, Xiang Xu, Jiaze Ma, Xuekai Zhu, Ermo Hua, Yihao Liu, Zonglin Li, Huayu Chen,
Xiaoye Qu, Yafu Li, Weize Chen, Zhenzhao Yuan, Junqi Gao, Dong Li, Zhiyuan Ma, Ganqu Cui, Zhiyuan Liu,
104

Biqing Qi, Ning Ding, and Bowen Zhou. A survey of reinforcement learning for large reasoning models, 2025k.
https://arxiv.org/abs/2509.08827.
LingfengZhang,YuechengLiu,ZhanguangZhang,MatinAghaei,YaochenHu,HongjianGu,MohammadAliAlom-
rani, David Gamaliel Arcos Bravo, Raika Karimi, Atia Hamidizadeh, Haoping Xu, Guowei Huang, Zhanpeng
Zhang,TongtongCao,WeichaoQiu,XingyueQuan,JianyeHao,YuzhengZhuang,andYingxueZhang. Mem2ego:
Empowering vision-language models with global-to-ego memory for long-horizon embodied navigation. CoRR,
abs/2502.14254, 2025l. doi: 10.48550/ARXIV.2502.14254. https://doi.org/10.48550/arXiv.2502.14254.
Qizheng Zhang, Changran Hu, Shubhangi Upasani, Boyuan Ma, Fenglu Hong, Vamsidhar Kamanuru, Jay Rain-
ton, Chen Wu, Mengmeng Ji, Hanchen Li, Urmish Thakker, James Zou, and Kunle Olukotun. Agentic con-
text engineering: Evolving contexts for self-improving language models. CoRR, abs/2510.04618, 2025m. doi:
10.48550/ARXIV.2510.04618. https://doi.org/10.48550/arXiv.2510.04618.
Shaohua Zhang, Yuan Lin, and Hang Li. Memory retrieval and consolidation in large language models through
function tokens, 2025n. https://arxiv.org/abs/2510.08203.
Wenlin Zhang, Xiaopeng Li, Yingyi Zhang, Pengyue Jia, Yichao Wang, Huifeng Guo, Yong Liu, and Xiangyu Zhao.
Deep research: A survey of autonomous research agents, 2025o. https://arxiv.org/abs/2508.12752.
Wentao Zhang, Lingxuan Zhao, Haochong Xia, Shuo Sun, Jiaze Sun, Molei Qin, Xinyi Li, Yuqing Zhao, Yilei Zhao,
Xinyu Cai, Longtao Zheng, Xinrun Wang, and Bo An. A multimodal foundation agent for financial trading:
Tool-augmented, diversified, and generalist, 2024. https://arxiv.org/abs/2402.18485.
Yaoze Zhang, Rong Wu, Pinlong Cai, Xiaoman Wang, Guohang Yan, Song Mao, Ding Wang, and Botian Shi.
Leanrag: Knowledge-graph-based generation with semantic aggregation and hierarchical retrieval, 2025p. https:
//arxiv.org/abs/2508.10391.
YuxiangZhang,JiangmingShu,YeMa,XueyuanLin,ShangxiWu,andJitaoSang. Memoryasaction: Autonomous
contextcurationforlong-horizonagentictasks. CoRR,abs/2510.12635,2025q. doi: 10.48550/ARXIV.2510.12635.
https://doi.org/10.48550/arXiv.2510.12635.
Zeyu Zhang, Quanyu Dai, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen, Jieming Zhu, Zhenhua Dong, and Ji-Rong Wen.
A survey on the memory mechanism of large language model-based agents. ACM Transactions on Information
Systems, 43(6):1–47, 2025r.
ZeyuZhang, QuanyuDai, XuChen, RuiLi, ZhongyangLi, andZhenhuaDong. Memengine: Aunifiedandmodular
library for developing advanced memory of llm-based agents, 2025s. https://arxiv.org/abs/2505.02099.
Zeyu Zhang, Quanyu Dai, Rui Li, Xiaohe Bo, Xu Chen, and Zhenhua Dong. Learn to memorize: Optimizing llm-
basedagentswithadaptivememoryframework. CoRR,abs/2508.16629,2025t. doi: 10.48550/ARXIV.2508.16629.
https://doi.org/10.48550/arXiv.2508.16629.
Zeyu Zhang, Yang Zhang, Haoran Tan, Rui Li, and Xu Chen. Explicit vs implicit memory: Exploring multi-hop
complex reasoning over personalized information. arXiv preprint arXiv:2508.13250, 2025u.
Zhenyu Zhang, Ying Sheng, Tianyi Zhou, Tianlong Chen, Lianmin Zheng, Ruisi Cai, Zhao Song, Yuandong
Tian, Christopher Ré, Clark W. Barrett, Zhangyang Wang, and Beidi Chen. H2O: heavy-hitter oracle for
eﬀicient generative inference of large language models. In Alice Oh, Tristan Naumann, Amir Globerson,
Kate Saenko, Moritz Hardt, and Sergey Levine, editors, Advances in Neural Information Processing Sys-
tems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023, New Or-
leans, LA, USA, December 10 - 16, 2023, 2023. http://papers.nips.cc/paper_files/paper/2023/hash/
6ceefa7b15572587b78ecfcebb2827f8-Abstract-Conference.html.
105

Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, and Gao Huang. Expel: LLM agents are
experiential learners. In Michael J. Wooldridge, Jennifer G. Dy, and Sriraam Natarajan, editors, Thirty-Eighth
AAAI Conference on Artificial Intelligence, AAAI 2024, Thirty-Sixth Conference on Innovative Applications of
ArtificialIntelligence,IAAI2024,FourteenthSymposiumonEducationalAdvancesinArtificialIntelligence,EAAI
2014, February 20-27, 2024, Vancouver, Canada, pages 19632–19642. AAAI Press, 2024. doi: 10.1609/AAAI.
V38I17.29936. https://doi.org/10.1609/aaai.v38i17.29936.
Di Zhao, Longhui Ma, Siwei Wang, Miao Wang, and Zhao Lv. COLA: A Scalable Multi-Agent Framework For
Windows UI Task Automation. CoRR, abs/2503.09263, 2025a. doi: 10.48550/ARXIV.2503.09263. https://doi.
org/10.48550/arXiv.2503.09263. arXiv: 2503.09263.
LinxiZhao,SofianZalouk,ChristianK.Belardi,JustinLovelace,JinPengZhou,RyanThomasNoonan,Dongyoung
Go, Kilian Q. Weinberger, Yoav Artzi, and Jennifer J. Sun. Pre-training limited memory language models with
internal and external knowledge, 2025b. https://arxiv.org/abs/2505.15962.
ShitianZhao,HaoquanZhang,ShaohengLin,MingLi,QilongWu,KaipengZhang,andChenWei. Pyvision: Agentic
vision with dynamic tooling, 2025c. https://arxiv.org/abs/2507.07998.
Siyan Zhao, Mingyi Hong, Yang Liu, Devamanyu Hazarika, and Kaixiang Lin. Do llms recognize your preferences?
evaluating personalized preference following in llms. In The Thirteenth International Conference on Learning
Representations, ICLR 2025, Singapore, April 24-28, 2025. OpenReview.net, 2025d. https://openreview.net/
forum?id=QWunLKbBGF.
Boyuan Zheng, Michael Y. Fatemi, Xiaolong Jin, Zora Zhiruo Wang, Apurva Gandhi, Yueqi Song, Yu Gu, Jayanth
Srinivasa, Gaowen Liu, Graham Neubig, and Yu Su. Skillweaver: Web agents can self-improve by discovering and
honing skills. CoRR, abs/2504.07079, 2025a. doi: 10.48550/ARXIV.2504.07079. https://doi.org/10.48550/
arXiv.2504.07079.
Junhao Zheng, Xidi Cai, Qiuke Li, Duzhen Zhang, ZhongZhi Li, Yingying Zhang, Le Song, and Qianli Ma. Lifelon-
gagentbench: Evaluating llm agents as lifelong learners. arXiv preprint arXiv:2505.11942, 2025b.
Longtao Zheng, Rundong Wang, Xinrun Wang, and Bo An. Synapse: Trajectory-as-Exemplar Prompting with
MemoryforComputerControl. InTheTwelfthInternationalConferenceonLearningRepresentations,ICLR2024,
Vienna, Austria, May 7-11, 2024. OpenReview.net, 2024a. https://openreview.net/forum?id=Pc8AU1aF5e.
Yicong Zheng, Kevin L. McKee, Thomas Miconi, Zacharie Bugaud, Mick van Gelderen, and Jed McCaleb. Goal-
directed search outperforms goal-agnostic memory compression in long-context memory tasks, 2025c. https:
//arxiv.org/abs/2511.21726.
Yuanhang Zheng, Peng Li, Wei Liu, Yang Liu, Jian Luan, and Bin Wang. ToolRerank: Adaptive and Hierarchy-
Aware Reranking for Tool Retrieval. In Nicoletta Calzolari, Min-Yen Kan, Véronique Hoste, Alessandro Lenci,
SakrianiSakti,andNianwenXue,editors,Proceedingsofthe2024JointInternationalConferenceonComputational
Linguistics, Language Resources and Evaluation, LREC/COLING 2024, 20-25 May, 2024, Torino, Italy, pages
16263–16273. ELRA and ICCL, 2024b. https://aclanthology.org/2024.lrec-main.1413.
Siru Zhong, Weilin Ruan, Ming Jin, Huan Li, Qingsong Wen, and Yuxuan Liang. Time-vlm: Exploring multimodal
vision-languagemodelsforaugmentedtimeseriesforecasting.CoRR,abs/2502.04395,2025.doi: 10.48550/ARXIV.
2502.04395. https://doi.org/10.48550/arXiv.2502.04395.
WanjunZhong,LianghongGuo,QiqiGao,HeYe,andYanlinWang. Memorybank: Enhancinglargelanguagemodels
withlong-termmemory.InProceedingsoftheAAAIConferenceonArtificialIntelligence,pages19724–19731,2024.
HuichiZhou,YihangChen,SiyuanGuo,XueYan,KinHeiLee,ZihanWang,KaYiuLee,GuchunZhang,KunShao,
106

LinyiYang,andJunWang. Memento: Fine-tuningLLMagentswithoutfine-tuningllms. CoRR,abs/2508.16153,
2025a. doi: 10.48550/ARXIV.2508.16153. https://doi.org/10.48550/arXiv.2508.16153.
Jinfeng Zhou, Zhuang Chen, Dazhen Wan, Bosi Wen, Yi Song, Jifan Yu, Yongkang Huang, Pei Ke, Guanqun Bi,
LibiaoPeng,JiamingYang,XiyaoXiao,SahandSabour,XiaohanZhang,WenjingHou,YijiaZhang,YuxiaoDong,
Hongning Wang, Jie Tang, and Minlie Huang. Characterglm: Customizing social characters with large language
models. In Franck Dernoncourt, Daniel Preotiuc-Pietro, and Anastasia Shimorina, editors, Proceedings of the
2024 Conference on Empirical Methods in Natural Language Processing: EMNLP 2024 - Industry Track, Miami,
Florida, USA, November 12-16, 2024, pages 1457–1476. Association for Computational Linguistics, 2024a. doi:
10.18653/V1/2024.EMNLP-INDUSTRY.107. https://doi.org/10.18653/v1/2024.emnlp-industry.107.
ShuyanZhou,FrankFXu,HaoZhu,XuhuiZhou,RobertLo,AbishekSridhar,XianyiCheng,TianyueOu,Yonatan
Bisk, Daniel Fried, et al. Webarena: A realistic web environment for building autonomous agents. arXiv preprint
arXiv:2307.13854, 2023a.
ShuyanZhou,FrankF.Xu,HaoZhu,XuhuiZhou,RobertLo,AbishekSridhar,XianyiCheng,TianyueOu,Yonatan
Bisk,DanielFried,UriAlon,andGrahamNeubig.Webarena: Arealisticwebenvironmentforbuildingautonomous
agents, 2024b. https://arxiv.org/abs/2307.13854.
WangchunshuZhou,YuchenEleanorJiang,PengCui,TiannanWang,ZhenxinXiao,YifanHou,RyanCotterell,and
Mrinmaya Sachan. Recurrentgpt: Interactive generation of (arbitrarily) long text, 2023b. https://arxiv.org/
abs/2305.13304.
WangchunshuZhou,YuchenEleanorJiang,LongLi,JialongWu,TiannanWang,ShiQiu,JintianZhang,JingChen,
Ruipu Wu, Shuai Wang, Shiding Zhu, Jiyu Chen, Wentao Zhang, Ningyu Zhang, Huajun Chen, Peng Cui, and
Mrinmaya Sachan. Agents: An open-source framework for autonomous language agents. CoRR, abs/2309.07870,
2023c. doi: 10.48550/ARXIV.2309.07870. https://doi.org/10.48550/arXiv.2309.07870.
Wangchunshu Zhou, Yixin Ou, Shengwei Ding, Long Li, Jialong Wu, Tiannan Wang, Jiamin Chen, Shuai Wang,
Xiaohua Xu, Ningyu Zhang, Huajun Chen, and Yuchen Eleanor Jiang. Symbolic learning enables self-evolving
agents. CoRR, abs/2406.18532, 2024c. doi: 10.48550/ARXIV.2406.18532. https://doi.org/10.48550/arXiv.
2406.18532.
Zijian Zhou, Ao Qu, Zhaoxuan Wu, Sunghwan Kim, Alok Prakash, Daniela Rus, Jinhua Zhao, Bryan Kian Hsiang
Low, and Paul Pu Liang. MEM1: Learning to synergize memory and reasoning for eﬀicient long-horizon agents.
arXiv preprint arXiv:2506.15841, 2025b.
AndrewZhu,LaraMartin,AndrewHead,andChrisCallison-Burch.CALYPSO:LLMsasdungeonmasters’assistants.
InProceedingsoftheNineteenthAAAIConferenceonArtificialIntelligenceandInteractiveDigitalEntertainment,
volume19ofAIIDE ’23,pages380–390,SaltLakeCity,October2023.AAAIPress. ISBN978-1-57735-883-1. doi:
10.1609/aiide.v19i1.27534.
Wazeer Deen Zulfikar, Samantha W. T. Chan, and Pattie Maes. Memoro: Using large language models to real-
ize a concise interface for real-time memory augmentation. In Florian ’Floyd’ Mueller, Penny Kyburz, Julie R.
Williamson, Corina Sas, Max L. Wilson, Phoebe O. Toups Dugas, and Irina Shklovski, editors, Proceedings of the
CHIConferenceonHumanFactorsinComputingSystems,CHI2024,Honolulu,HI,USA,May11-16,2024,pages
450:1–450:18. ACM, 2024. doi: 10.1145/3613904.3642450. https://doi.org/10.1145/3613904.3642450.
Jialong Zuo, Yongtai Deng, Lingdong Kong, Jingkang Yang, Rui Jin, Yiwei Zhang, Nong Sang, Liang Pan, Ziwei
Liu, and Changxin Gao. Videolucy: Deep memory backtracking for long video understanding, 2025. https:
//arxiv.org/abs/2510.12422.
107

Table 4 事实记忆方法的分类体系。我们根据主要目标实体对现有工作进行分类：用户事实记忆侧重于维持交互的一致
性，而环境事实记忆则确保与外部世界的一致性。方法在三个技术维度上进行比较：(1)载体(Section3)识别存储介质，
(2) 结构遵循 token 级别记忆的分类体系 (Section 3.1)，以及 (3) 最优化表示集成策略，其中 PE 包含无需参数更新的
提示工程和推理时技术，与基于梯度的方法如 SFT 和 RL 相区分。
Method Carrier Structure Task Optimization
I. User factual Memory
(a) Dialogue Coherence
MemGPT(Packeretal.,2023b) Token-level 1D Long-termdialogue PE
TiM(Parketal.,2023) Token-level 2D QA PE
MemoryBank(Zhongetal.,2024) Token-level 1D EmotionalCompanion PE
AIPersona(Wangetal.,2024f) Token-level 1D EmotionalCompanion PE
Encode-Store-Retrieve (Shen et al., Token-level 1D MultimodalQA PE
2024)
Livia(XiandWang,2025) Token-level 1D EmotionalCompanion PE
mem0(Chhikaraetal.,2025) Token-level 1D Long-termdialogue,QA PE
RMM(Tanetal.,2025c) Token-level 2D Personalization PE,RL
D-SMART(Leietal.,2025) Token-level 2D Reasoning PE
Comedy(Chenetal.,2025c) Token-level 1D Summary,Compression,QA PE
MEMENTO(Kwonetal.,2025) Token-level 1D Embodied,Personalization PE
O-Mem(Wangetal.,2025g) Token-level 3D PersonalizedDialogue PE
DAM-LLM(LuandLi,2025) Token-level 1D EmotionalCompanion PE
MemInsight(Salamaetal.,2025) Token-level 1D PersonalizedDialogue PE
(b) Goal Consistency
RecurrentGPT(Zhouetal.,2023b) Token-level 1D Long-ContextGeneration,Per- PE
sonalizedInteractiveFiction
Memolet(YenandZhao,2024) Token-level 2D QA,DocumentReasoning PE
MemGuide(Duetal.,2025b) Token-level 1D Long-convQA PE,SFT
SGMem(Wuetal.,2025h) Token-level 2D Long-context PE
A-Mem(Xuetal.,2025c) Token-level 2D QA,Reasoning PE
M3-agent(Longetal.,2025) Token-level 2D MultimodalQA PE,SFT
II. Environment factual Memory
(a) Knowledge Persistence
MemGPT(Packeretal.,2023b) Token-level 1D DocumentQA PE
CALYPSO(Zhuetal.,2023) Token-level 1D TabletopGaming PE
AriGraph(Anokhinetal.,2024) Token-level 3D Game,Multi-opQA PE
HippoRAG(Gutierrezetal.,2024) Token-level 3D QA PE
WISE(Wangetal.,2024e) Parametric / DocumentReasoning,QA SFT
MemoryLLM(Wangetal.,2024j) Parametric / DocumentReasoning SFT
Zep(Rasmussenetal.,2025) Token-level 3D Documentanalysis PE
MemTree(Rezazadehetal.,2025c) Token-level 2D Document Reasoning, Dia- PE
logue
LMLM(Zhaoetal.,2025b) Token-level 1D QA SFT
M+ (Wangetal.,2025m) Latent / DocumentReasoning,QA SFT
CAM(Lietal.,2025f) Token-level 3D Multi-hopQA SFT,RFT
MemAct(Zhangetal.,2025q) Token-level 1D Multi-objQA RL
Mem-α(Wangetal.,2025o) Token-Level 1D DocumentReasoning RL
WebWeaver(Lietal.,2025l) Token-level 1D DeepResearch SFT
(b) Shared Access
GameGPT(Chenetal.,2023b) Token-level 1D GameDevelopment PE
GenerativeAgent(Parketal.,2023) Token-level 2D SocialSimulation PE
S³(Gaoetal.,2023a) Token-level 1D SocialSimulation PE
Memory Sharing (Gao and Zhang, Token-level 1D DocumentReasoning PE
2024a)
MetaGPT(Hongetal.,2024) Token-level 1D SoftwareDevelopment PE
G-Memory(Zhangetal.,2025e) Token-level 3D QA PE
OASIS (Yangetal.,2025) Token-level,Parametric 1D SocialSimulation PE
108

Table 6 工作记忆方法的分类。我们根据交互动态将方法分为 单轮和 多轮两种情景。方法在三个技术维度上进行比较：
(1)载体(Section3)识别存储介质，(2)任务指定评估领域或应用情景，(3)最优化表示集成策略，其中PE包含提示工
程和推理时技术而无需参数更新，与基于梯度的方法（如 SFT 和 RL）相区别。
Method Carrier Task Optimization
I. Single-turn Working Memory
(a) Input Condensation
Gist(Muetal.,2023) Latent InstructionFine-tuning SFT
ICAE(Geetal.,2024) Latent LanguageModeling,InstructionFine-tuning Pretrain,LoRA
AutoCompressors (Chevalier et al., Latent LangagueModeling SFT
2023)
LLMLingua(Jiangetal.,2023) Token-level Reasoning,Conversation,Summarization PE
LongLLMLingua(Jiangetal.,2024) Token-level Multi-docQA,Long-context,Multi-hopQA PE
CompAct(Yoonetal.,2024) Token-level DocumentQA SFT
HyCo2(Liaoetal.,2025a) Hybrid Summarization,Open-domainQA,Multi-hopQA SFT
Sentence-Anchor(Tarasovetal.,2025) Latent DocumentQA SFT
MELODI(Chenetal.,2024c) Hybrid Pretraining Pretrain
(b) Observation Abstraction
Synapse(Zhengetal.,2024a) Token-level ComputerControl,WebNavigation PE
VideoAgent(Wangetal.,2024g) Token-level Long-termVideoUnderstanding PE
MA-LMM(Heetal.,2024) Latent Long-termVideoUnderstanding SFT
ContextasMemory(Yuetal.,2025b) Token-level Long-termVideoGeneration PE
II. Multi-turn Working Memory
(c) State Consolidation
MEM1(Zhouetal.,2025b) Latent Retrieval,Open-domainQA,Shopping RL
MemGen(Zhangetal.,2025d) Latent Reasoning, Embodied Action, Web Search, Cod- RL
ing
MemAgent(Yuetal.,2025a) Token-level Long-termDoc. QA RL
ReMemAgent(Shietal.,2025b) Token-level Long-termDoc. QA RL
ReSum(Wuetal.,2025f) Token-level Long-horizonWebSearch RL
MemSearcher(Yuanetal.,2025a) Token-level Multi-hopQA SFT,RL
ACON(Kangetal.,2025c) Token-level Appuse,Multi-objectiveQA PE
IterResearch(Chenetal.,2025a) Token-level Reasoning,WebNavigation,Long-HorizonQA RL
SUPO(Luetal.,2025a) Token-level Long-horizontask RL
AgentDiet(Xiaoetal.,2025a) Token-level Long-horizontask PE
SUMER(Zhengetal.,2025c) Token-level QA RL
(d) Hierarchical Folding
HiAgent(Huetal.,2025a) Token-level Long-horizonAgentTask PE
Context-Folding(Zhangetal.,2025q) Token-level DeepResearch,SWE RL
AgentFold(Yeetal.,2025a) Token-level WebSearch SFT
DeepAgent(Lietal.,2025h) Token-level ToolUse,Shopping,Reasoning RL
(e) Cognitive Planning
SayPlan(Ranaetal.,2023) Token-level 3DSceneGraph,Robotics PE
KARMA(Wangetal.,2025q) Token-level Household PE
Agent-S(Agasheetal.,2025) Token-level ComputerUse PE
PRIME(Tranetal.,2025) Token-level Multi-hopQA,Knowledge-intensiveReasoning PE
109

Table7 记忆形成方法的分类。我们根据记忆形成操作对方法进行分类。方法在三个技术维度上进行分析：(1)子类型识
别具体的变体或范围，(2) 表示形式指定输出格式，以及 (3) 关键机制表示核心算法策略。
Method Sub-Type RepresentationForm KeyMechanism
I.SemanticSummarization
MemGPT(Packeretal.,2023a) Incremental TextualSummary Mergingnewchunksintotheworkingcontext
Mem0(Chhikaraetal.,2025) Incremental TextualSummary LLM-drivensummarization
Mem1(Zhouetal.,2025b) Incremental TextualSummary RL-optimizedsummarization(PPO)
MemAgent(Yuetal.,2025a) Incremental TextualSummary RL-optimizedsummarization(GRPO)
MemoryBank(Zhongetal.,2024) Partitioned TextualSummary Daily/Session-basedsegmentation
ReadAgent(Leeetal.,2024a) Partitioned TextualSummary Semanticclusteringbeforesummarization
LightMem(Fangetal.,2025b) Partitioned TextualSummary Topic-clusteredsummarization
DeepSeek-OCR(Weietal.,2025a) Partitioned VisualTokenMapping Optical2Dmappingcompression
FDVS(Youetal.,2024) Partitioned MultimodalSummary Multi-sourcesignalintegration(Subtitle/Object)
LangRepo(Kahatapitiyaetal.,2025) Partitioned MultimodalSummary Hierarchicalvideoclipaggregation
II.KnowledgeDistillation
TiM(Liuetal.,2023a) Factual TextualInsight Abstractionofdialogueintothoughts
RMM(Tanetal.,2025b) Factual TopicInsight Abstractionofdialogueintotopic-basedmemory
MemGuide(Duetal.,2025b) Factual UserIntent Capturinghigh-leveluserintent
M3-Agent(Longetal.,2025) Factual Text-addressableFacts Compressingegocentricvisualobservations
AWM(Wangetal.,2024l) Experiential WorkflowPatterns Workflowextractionfromsuccesstrajectories
Memp (Fangetal.,2025d) Experiential ProceduralKnowledge Distillinggoldtrajectoriesintoabstractprocedures
ExpeL(Zhaoetal.,2024) Experiential ExperienceInsight Contrastivereflectionandsuccessfulpractices
R2D2(Huangetal.,2025c) Experiential ReflectiveInsight Reflectiononreasoningtracesvs. groundtruth
H2R(Yeetal.,2025b) Experiential HierarchicalInsight Two-tierreflection(Plan&Subgoal)
Memory-R1(Yanetal.,2025b) Experiential TextualKnowledge RL-trainedLLMExtractmodule
Mem-α(Wangetal.,2025o) Experiential TextualInsight Learnableinsightextractionpolicy
III.StructuredConstruction
KGT(Sunetal.,2024) Entity-Level UserGraph Encodinguserpreferencesasnodes/edges
Mem0g (Chhikaraetal.,2025) Entity-Level KnowledgeGraph LLM-basedentityandtripletextraction
D-SMART(Leietal.,2025) Entity-Level DynamicMemoryGraph ConstructinganOWL-compliantgraph
GraphRAG(Edgeetal.,2025) Entity-Level HierarchicalKG Communitydetectionanditerativesummarization
AriGraph(Anokhinetal.,2024) Entity-Level Semantic+EpisodicGraph Dual-layer(Semanticnodes+Episodiclinks)
Zep(Rasmussenetal.,2025) Entity-Level TemporalKG 3-layergraph(Episodic,Semantic,Community)
RAPTOR(Sarthietal.,2024) Chunk-Level TreeStructure RecursiveGMMclusteringandsummarization
MemTree(Rezazadehetal.,2025c) Chunk-Level TreeStructure Bottom-upinsertionandsummaryupdates
H-MEM(SunandZeng,2025) Chunk-Level HierarchicalJSON Top-down4-levelhierarchyorganization
A-MEM(Xuetal.,2025c) Chunk-Level NetworkedNotes Discretenoteswithsemanticlinks
PREMem(Kimetal.,2025b) Chunk-Level ReasoningPatterns Cross-sessionreasoningpatternclustering
CAM(Lietal.,2025f) Chunk-Level HierarchicalGraph Disentanglingoverlappingclustersviareplication
G-Memory(Zhangetal.,2025c) Chunk-Level HierarchicalGraph 3-tiergraph(interaction,query,insight)
IV.LatentRepresentation
MemoryLLM(Wangetal.,2024j) Textual LatentVector Self-updatablelatentembeddings
M+(Wangetal.,2025m) Textual LatentVector Cross-layerlong-termmemorytokens
MemGen(Zhangetal.,2025d) Textual LatentToken Latentmemorytriggerandweaver
ESR(Shenetal.,2024) Multimodal LatentVector Video-to-Language-to-Vectorencoding
CoMEM(Wuetal.,2025d) Multimodal ContinuousEmbedding Vision-languagecompressionviaQ-Former
Mem2Ego(Zhangetal.,2025l) Multimodal MultimodalEmbedding Embeddinglandmarksemanticsaslatentmemory
KARMA(Wangetal.,2025q) Multimodal MultimodalEmbedding Hybridlong/short-termmemoryencoding
V.ParametricInternalization
MEND(Mitchelletal.,2022) Knowledge GradientDecomposition Auxiliarynetworkforfastedits
ROME(Mengetal.,2022) Knowledge ModelParameters Causaltracingandrank-oneupdate
MEMIT(Mengetal.,2023) Knowledge ModelParameters Mass-editingviaresidualdistribution
CoLoR(Wistubaetal.,2023) Knowledge LoRAParameters Low-rankadaptertraining
ToolFormer(Schicketal.,2023) Capability ModelParameters Supervisedfine-tuningonAPIcalls
110

Table 8 与大语言模型智能体记忆、长期性、终身学习及自我演化评估相关的基准概述。该表格涵盖两类基准：(i)专门
设计用于评估记忆、终身学习或自我演化智能体的基准，以及 (ii) 其他面向智能体的基准，通过序列化、多步或多项任
务交互隐式强调长时程记忆。Fac. 与Exp. 分别表示基准是否评估事实性记忆或经验性（交互衍生）记忆。MM.表示是
否存在多模态输入，而 Env. 表示基准是在模拟环境还是真实环境中进行。Feature 总结了主要评估能力，Scale 报告了
基准的大致规模，以 样本（s.）或 任务（t.）为单位。PDDL 表示常用的基于 PDDL 的规划子集。
Name Link Fac. Exp. MM. Env. Feature Scale
Memory/Lifelong-learning/Self-evolving-oriented Benchmarks
MemBench (cid:97)GitHub ✔ ✔ ✘ simulated interactive scenarios 53,000 s.
MemoryAgentBench (cid:97)GitHub ✔ ✔ ✘ simulated multi-turn interactions 4 t.
LoCoMo (cid:231)Website ✔ ✘ ✔ real conversational memory 300 s.
WebChoreArena (cid:97)GitHub ✔ ✔ ✔ real tedious web browsing 4 t./532 s.
MT-Mind2Web (cid:97)GitHub ✔ ✔ ✘ real conversational web navigation 720 s.
PersonaMem (cid:231)Website ✔ ✘ ✘ simulated dynamic user profiling 15 t./180 s.
LongMemEval (cid:97)GitHub ✔ ✘ ✘ simulated interactive memory 5 t./500 s.
PerLTQA (cid:231)Website ✔ ✘ ✘ simulated social personalized interactions 8,593 s.
MemoryBank (cid:231)Website ✔ ✘ ✘ simulated user memory updating 194 s.
MPR (cid:97)GitHub ✔ ✘ ✘ simulated user personalization 108,000 s.
PrefEval (cid:231)Website ✔ ✘ ✘ simulated personal preferences 3,000 s.
LOCCO (cid:231)Website ✔ ✘ ✘ simulated chronological conversations 3,080 s.
StoryBench (cid:231)Website ✔ ✔ ✘ mixed interactive fiction games 3 t.
MemoryBench (cid:231)Website ✔ ✔ ✘ simulated continual learning 4 t./∼ 20,000 s.
Madial-Bench (cid:97)GitHub ✔ ✘ ✘ simulated memory recalling 331 s.
Evo-Memory (cid:231)Website ✔ ✔ ✘ simulated test-time learning 10 t./∼ 3,700 s.
LifelongAgentBench (cid:231)Website ✔ ✔ ✘ simulated lifelong learning 1,396 s.
StreamBench (cid:231)Website ✔ ✔ ✘ simulated continuous online learning 9,702 s.
DialSim (cid:231)Website ✔ ✔ ✘ real multi-dialogue understanding ∼ 1,300 s.
LongBench (cid:231)Website ✔ ✘ ✘ mixed long-context understanding 21 t./4,750 s.
LongBench v2 (cid:231)Website ✔ ✘ ✘ mixed long-context multitasks 20 t./503 s.
RULER (cid:97)GitHub ✔ ✘ ✘ simulated long-context retrieval 13 t.
BABILong (cid:97)GitHub ✔ ✘ ✘ simulated long-context reasoning 20 t.
MM-Needle (cid:231)Website ✔ ✘ ✔ simulated multimodal long-context retrieval ∼ 280,000 s.
HaluMem (cid:97)GitHub ✔ ✘ ✘ simulated memory hallucinations 3,467 s.
HotpotQA (cid:231)Website ✔ ✘ ✘ simulated long-context QA 113k s.
Other Related Benchmarks
ALFWorld (cid:231)Website ✔ ✔ ✘ simulated text-based embodied environment 3,353 t.
ScienceWorld (cid:97)GitHub ✔ ✔ ✘ simulated interactive embodied environment 10 t./30 t.
AgentGym (cid:231)Website ✘ ✔ ✘ mixed multiple environments 89 t./20,509 s.
AgentBoard (cid:97)GitHub ✘ ✔ ✘ mixed multi-round interaction 9 t./1013 s.
PDDL ∗ (cid:231)Website ✘ ✔ ✘ simulated strategy game -
BabyAI (cid:231)Website ✘ ✔ ✘ simulated language learning 19 t.
WebShop (cid:231)Website ✘ ✔ ✔ simulated e-commerce web interaction 12,087 s.
WebArena (cid:231)Website ✘ ✔ ✔ real web interaction 812 s.
MMInA (cid:231)Website ✔ ✔ ✔ real multihop web interaction 1,050 s.
SWE-Bench Verified (cid:231)Website ✘ ✔ ✘ real code repair 500 s.
GAIA (cid:231)Website ✘ ✔ ✔ real human-level deep research 466 s.
xBench-DS (cid:231)Website ✘ ✔ ✔ real deep-search evaluation 100 s.
ToolBench (cid:97)GitHub ✘ ✔ ✘ real API tool use 126,486 s.
GenAI-Bench (cid:231)Website ✘ ✔ ✔ real visual generation evaluation ∼ 40,000 s.
111

Table 9 基于大语言模型智能体的代表性开源记忆框架概览。该表格从智能体所支持的记忆类型（事实性与经验性）、多
模态性、内部记忆结构以及报告的评估基准等方面对广泛使用的框架进行了比较。Fac. 和 Exp. 分别表示事实性记忆与
经验性记忆，MM. 表示支持多模态记忆，Structure 总结了各框架采用的核心记忆抽象或组织机制。Evaluation 列出了
公开报告的用于评估记忆相关能力的基准测试，若可用则列出。
Framework Links Fac. Exp. MM. Structure Evaluation
MemGPT (cid:97)GitHub ✔ ✔ ✘ hierachical (S/LTM) LoCoMo
(cid:231)Website
Mem0 (cid:97)GitHub ✔ ✔ ✘ graph + vector LoCoMo
(cid:231)Website
Memobase (cid:97)GitHub ✔ ✔ ✘ structured profiles LoCoMo
(cid:231)Website
MIRIX (cid:97)GitHub ✔ ✔ ✔ structured memory LoCoMo, MemoryA-
(cid:231)Website gentBench
MemoryOS (cid:97)GitHub ✔ ✔ ✘ hierarchical (S/M/LTM) LoCoMo, Memory-
(cid:231)Website Bank
MemOS (cid:97)GitHub ✔ ✔ ✘ tree memory + memcube LoCoMo, PreFEval,
(cid:231)Website LongMemEval, Per-
sonaMem
Zep (cid:97)GitHub ✔ ✔ ✘ temporal knowledge graph LongMemEval
(cid:231)Website
LangMem (cid:97)GitHub ✔ ✔ ✘ core API + manager -
(cid:231)Website
SuperMemory (cid:97)GitHub ✔ ✔ ✔ vector + semantic -
(cid:231)Website
Cognee (cid:97)GitHub ✔ ✔ ✔ knowledge graph -
(cid:231)Website
Memary (cid:97)GitHub ✔ ✔ ✘ stream + entity store -
(cid:231)Website
Pinecone (cid:97)GitHub ✔ ✘ ✘ vector database -
(cid:231)Website
Chroma (cid:97)GitHub ✔ ✘ ✔ vector database -
(cid:231)Website
Weaviate (cid:97)GitHub ✔ ✘ ✔ vector + graph -
(cid:231)Website
Second Me (cid:97)GitHub ✔ ✘ ✘ agent ego -
(cid:231)Website
MemU (cid:97)GitHub ✔ ✔ ✔ hierachical layers -
(cid:231)Website
MemEngine (cid:97)GitHub ✔ ✔ ✔ modular space -
Memori (cid:97)GitHub ✔ ✔ ✘ memory database -
(cid:231)Website
ReMe (cid:97)GitHub ✔ ✔ ✘ memory management -
(cid:231)Website
AgentMemory (cid:97)GitHub ✔ ✔ ✘ memory management -
(cid:231)Website
MineContext (cid:97)GitHub ✔ ✔ ✔ context engineering -
(cid:231)Website
Acontext (cid:97)GitHub ✔ ✔ ✔ context engineering + skill -
learning
112
