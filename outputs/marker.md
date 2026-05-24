# **Voxtral 语音合成**

![](_page_0_Picture_2.jpeg)

### **Abstract**

我们介绍 Voxtral TTS,这是一种富有表现力的多语言文本到语音模型,仅 需 3 秒的参考音频即可生成自然语音。Voxtral TTS 采用混合架构,结合 了语义语音 token 的自回归生成与声学 token 的流匹配。这些 token 使 用 Voxtral Codec 进行编码和解码,该语音分词器从零开始训练,采用混 合 VQ-FSQ 量化方案。在由母语者进行的人类评估中,由于其自然性和表 现力,Voxtral TTS 在多语言语音克隆方面更受青睐,相较于 ElevenLabs Flash v2.5 的胜率高达 68.4%。我们以 CC BY-NC 许可证发布该模型权重。

**Webpage:** <https://mistral.ai/news/voxtral-tts>

**Model weights:** <https://huggingface.co/mistralai/Voxtral-4B-TTS-2603>

![](_page_0_Figure_7.jpeg)

**图 1: Voxtral TTS 在人工评估中优于 ElevenLabs Flash v2.5。**我们绘制了 Voxtral TTS 与 ElevenLabs Flash v2.5 在两类人工评估中的胜率。对于旗舰音色,我们使用各模型的默认音色以及 77 个不同的文本示例。在音色克隆设置中,我们提供一段简短的音频参考片段和 60 个文本提示。在两类 评估中,人工标注者会盲评两个模型之间的音频哪个更优。Voxtral TTS 在 58.3% 和 68.4% 的实例 中更受青睐。

# **1 引言**

自然且富有表现力的文本转语音(TTS)仍是灵活人机交互的核心,其应用涵盖虚拟助手、 有声读物和无障碍工具。尽管近期的神经网络 TTS 模型在语音可懂性方面表现优异,但在 zero-shot 语音情景下捕捉人类语音的细微差别与表现力仍是一个未解决的挑战。

最近的 zero-shot TTS 系统通常以从短语音提示中提取的离散语音 token 作为生成条件,从 而实现对未见说话人的泛化以及在长序列上的自然合成 [[Borsos et al.](#page-14-0), [2023](#page-14-0), [Wang et al.](#page-16-0), [2023\]](#page-16-0)。与此同时,扩散模型和基于流的模型在建模语音生成中的丰富声学变化方面表现出 色 [\[Popov et al.](#page-15-0), [2021](#page-15-0), [Le et al.,](#page-15-1) [2023\]](#page-15-1)。最近的语音编解码器表明,语音可以分解为低速率 语义流和更高速率的声学流 [\[Défossez et al.,](#page-14-1) [2024\]](#page-14-1)。层次化生成器如 Moshi 已经利用这种结 构,采用时间 Transformer 对时间步进行建模,并使用深度 Transformer 对编解码器层级进 行建模。然而,这些系统中的声学生成仍保持深度方向的自回归特性。对于 TTS 来说,这 就引出了一个问题:稠密的声学组件是否必须始终以自回归方式建模,或者是否可以通过一 种条件连续模型更有效地生成?

在本工作中,我们提出了 Voxtral TTS,这是一种基于表示感知混合架构的多语言 zero-shot 文本到语音系统。通过 Voxtral 编码器对语音提示进行分词,该编码器是一种低比特率语音 分词器,包含经语音识别(ASR)蒸馏得到的语义 token 以及有限标量量化(FSQ)的声学 token[[Mentzer et al.](#page-15-2), [2023](#page-15-2)]。基于这种分解表示,仅解码器的 Transformer 模型自回归地预 测语义 token 序列,而一个轻量级的流匹配模型则根据解码器状态预测声学 token。该设计 结合了自回归建模在长程一致性方面的优势与连续流匹配在丰富声学细节方面的优势。我们 通过将标准语义 token 生成偏好目标与基于流的声学预测偏好目标相结合,将直接偏好优化 (DPO) [[Rafailov et al.](#page-16-1), [2023](#page-16-1)] 适配到这种离散-连续混合设置中 [\[Ziv et al.,](#page-16-2) [2025\]](#page-16-2)。

Voxtral TTS 支持 9 种语言,支持最短 3 秒的语音提示,并专为低延迟流式推理设计。在 SEED-TTS [\[Anastassiou et al.,](#page-14-2) [2024](#page-14-2)] 和 MiniMax-TTS [\[Zhang et al.](#page-16-3), [2025](#page-16-3)] 的自动评估 中,其表现出优异的可懂性和自然度,在说话人相似度得分上超越 ElevenLabs v3。在多语 言 zero-shot 语音克隆的人类评估中,其胜率高达 68.4%,优于 ElevenLabs Flash v2.5,同 时在富有表现力的旗舰语音评估中与强大的专有系统保持竞争力。

# **2 建模**

图 [2](#page-2-0) 展示了 Voxtral TTS 的架构。该架构包含一种新型音频编解码器——Voxtral 编解码 器——可将参考语音样本编码为由语义 token 和声学 token 组成的音频 token。这些音频 token 与文本 token 结合,构成语言模型解码器主干的输入。为了生成语音,解码器主干逐 个自回归地生成语义 token 输出。一个流匹配 Transformer 用于生成声学 token。编解码器 解码器将输出 token 映射为对应的音频波形。

#### **2.1 Voxtral 编解码器**

Voxtral 编解码器是一种卷积-Transformer 自编码器 [[Défossez et al.](#page-14-3), [2022](#page-14-3)],可将原始的 24 kHz 单声道波形压缩为每秒 12.5 Hz 的 37 个离散 token(1 个语义 + 36 个声学),总比 特率为 2.14 kbps。这些 token 作为 Voxtral TTS 的输入音频表示。通过一种新颖的架构与 训练目标改进组合,Voxtral 编解码器优于现有的基准模型如 Mimi [\[Défossez et al.,](#page-14-1) [2024](#page-14-1)], 结果见第 [4.1](#page-7-0) 节。

**波形自编码器** 受基于 Transformer 的音频编码器先前工作 [[Parker et al.](#page-15-3), [2024](#page-15-3), [Wu et al.](#page-16-4), [2024\]](#page-16-4) 的启发,我们的音频分词器作用于"分块化"的波形。24 kHz 的单声道输入波形被分

<span id="page-2-0"></span>![](_page_2_Figure_0.jpeg)

**图 2: Voxtral TTS 架构概览。**一段长度为 3 秒至 30 秒的语音参考输入到 Voxtral Codec 编码器 中,以获得帧率为 12.5 Hz 的音频 token。每个音频帧(标注为 **A**)包含一个语义 token 和声学 token。 语音参考的音频 token 与文本提示 token(标注为 **T**)一同输入到解码器主干网络中。解码器自回归 地生成一串语义 token,直到遇到特殊的音频结束 token(**<EOA>**)。在每个时间步,解码器主干网 络输出的语义 token 被送入一个流匹配 Transformer,该模块多次运行以预测声学 token。最终,语 义 token 和声学 token 被输入到 Voxtral Codec 解码器中,生成目标波形。

割为不重叠的 240 样本块,从而得到编码器的 100 Hz 输入。这些 100 Hz 的输入帧首先通 过核大小为 7 的因果卷积投影到 1024 维嵌入,然后经过 4 个编码器块,每个块包含:

- 一个 2 层的因果自注意力 Transformer,采用滑动窗口注意力(窗口大小为 16 → 8 → 4 → 2 ,在每个下采样阶段减半),ALiBi 位置偏置 [\[Press et al.](#page-15-4), [2021\]](#page-15-4),QK 范 数,以及初始值为 0.01 的 LayerScale[[Touvron et al.,](#page-16-5) [2021\]](#page-16-5)。
- 一个因果卷积神经网络层。在前三个块中,卷积神经网络通过 2× 下采样(步幅为 2),从 100 Hz 到 12.5 Hz 累计减少了 8× 。在第四个块中,卷积神经网络的步幅为 1,并将 1024 维的表示投影到 292 维的潜在空间。

292 维的潜在表示随后被量化为音频 token(详情见下文)。解码器以相反顺序模仿编码器:首 先通过一个因果卷积神经网络将 292 维的潜在表示映射回 1024 维,接着经过 4 个块,每个 块包含一个转置卷积神经网络(用于 2× 上采样)和一个两层的因果自注意力 Transformer, 逐步将 12.5 Hz 的潜在表示恢复至 100 Hz。最后,一个核大小为 7 的因果卷积将 1024 维映 射回 240 样本的块大小,以重建波形。

**表示量化。** 292 维的潜在变量被拆分为一个 256 维的语义分量和一个 36 维的声学分量, 这两个分量分别独立进行量化:

![](_page_3_Figure_0.jpeg)

**图 3: Voxtral Codec 的架构概览与训练。**它包含一个分离的语义 VQ 编码字典和声学 FSQ 编码 字典。语义 token 和声学 token 一同用于重构。语义 token 还从监督的 ASR 模型中获得额外的蒸馏 损失。

- 语义组件通过一个学成的向量量化器(VQ; [\[Van Den Oord et al.](#page-16-6), [2017](#page-16-6)])进行量 化,码本大小为 8192。在训练过程中,以 50% 的概率应用 VQ;其余样本则未经量 化直接通过。
- 每个 36 个声学维度的信号都经过一个 tanh 激活,并通过有限标量量化(FSQ; [[Mentzer et al.,](#page-15-2) [2023](#page-15-2)])独立地量化为 21 个均匀等级。在训练过程中,我们采用 类似抖动的 FSQ[[Parker et al.,](#page-15-3) [2024\]](#page-15-3):50% 的样本使用 FSQ 进行量化,25% 的样 本添加幅度为 1/L 的均匀噪声(其中 L=21 为等级数),另有 25% 的样本不经过量 化直接通过。

总比特率为 12.5 × (log<sup>2</sup> 8192 + 36 × log<sup>2</sup> 21) ≈ 2.14 kbps。

**语义 token 学习** 为了更好地将语音的语义内容融入语义 token 中,我们采用了一种辅助的 ASR 蒸馏损失。与之前通过蒸馏自监督语音表示来学习"语义"token 的方法不同 [[Zhang](#page-16-7) [et al.,](#page-16-7) [2023](#page-16-7), [Défossez et al.](#page-14-1), [2024\]](#page-14-1),这些表示更偏向于 语音而非语义 [\[Liu et al.,](#page-15-5) [2024](#page-15-5)], 我们从一个监督式 ASR 模型中进行蒸馏。研究表明,这种方法能够生成更有效的语义表 示 [\[Vashishth et al.,](#page-16-8) [2024\]](#page-16-8)。

一个冻结的 Whisper [\[Radford et al.,](#page-15-6) [2023\]](#page-15-6) 模型在输入音频上以自回归方式运行,生成解码 器隐状态和交叉注意力权重。后置 VQ 的语义嵌入被线性投影以匹配 Whisper 的隐状态维 度,然后使用余弦距离损失与最后一层解码器的隐状态对齐:

$$\mathcal{L}_{ASR} = 1 - \frac{1}{L} \sum_{l=1}^{L} \frac{\tilde{\boldsymbol{z}}_l \cdot \boldsymbol{h}_l}{\|\tilde{\boldsymbol{z}}_l\| \|\boldsymbol{h}_l\|}, \qquad \tilde{\boldsymbol{z}}_l = \sum_{f=1}^{F} A_{l,f} \, \boldsymbol{z}_f$$
 (1)

其中,z<sup>f</sup> 是在编码器帧 f 处经过投影的后 VQ 语义嵌入,h<sup>l</sup> 是 Whisper 在 token 位置 l 处 的最末层解码器隐状态,而 A ∈ R <sup>L</sup>×<sup>F</sup> 是通过动态时间规整(DTW) [[Berndt and Clizord](#page-14-4), [1994\]](#page-14-4) 识别出与词级时间戳相关性最强的一组 Whisper 交叉注意力头所导出的软对齐矩阵。 为了计算 A,这些头的交叉注意力权重在解码器 token 维度上进行规范化,经中值滤波后在

头之间取平均。得到的矩阵沿编码器帧轴进行线性插值,以匹配编码器帧率(12.5 Hz),因 此 z˜<sup>l</sup> 是与第 l 个解码器 token 对齐的编码器嵌入的注意力加权和。

该设计使分词器能够在无需外部强制对齐工具或配对转录文本的情况下,学习与文本对齐的 语义 token,因为对齐信息是通过 Whisper 的交叉注意力权重隐式推导得出的。从连续隐状 态中提炼信息,而非依赖硬性转录标签,能够提供更丰富的监督信号,包括模型置信度和语 音相似性。

**对抗训练** 一个具有 8 个 STFT 大小(2296, 1418, 876, 542, 334, 206, 126, 76)的多分辨率 判别器与编码器一同训练。每个判别器作为二分类器,使用铰链损失在真实音频 x 和重建 音频 xˆ 之间进行训练。在每个判别器的每一层活性值上计算基于 L<sup>1</sup> 的特征匹配损失:

$$\mathcal{L}_{\text{feature}}(\boldsymbol{x}, \hat{\boldsymbol{x}}) = \frac{1}{MN} \sum_{m=1}^{M} \sum_{n=1}^{N} ||D_n^m(\boldsymbol{x}) - D_n^m(\hat{\boldsymbol{x}})||_1$$
 (2)

此处,D<sup>m</sup> <sup>n</sup> 表示第 n 个判别器的第 m 层,其中每个 N 个判别器均具有 M 层。根据 [Défossez](#page-14-1) [et al.](#page-14-1) [[2024\]](#page-14-1), [Parker et al.](#page-15-3) [\[2024](#page-15-3)],我们使用该特征匹配损失 替代标准 GAN 生成器损失,因 为不断演化的判别器特征在整个训练过程中提供了越来越具有区分性的重构信号。

**训练目标。** Voxtral 编码器以端到端方式训练,使用以下损失函数:

$$\alpha \mathcal{L}_{\text{feature}} + \beta \mathcal{L}_{\text{ASR}} + \gamma \mathcal{L}_{\text{L1}} + \gamma \mathcal{L}_{\text{STFT}} + \delta \mathcal{L}_{\text{commit}}$$
(3)

其中 α=1.0 ,β=1.0 ,γ=0.9999<sup>t</sup> (t 为当前训练步骤),以及 δ=0.1 。LL1 是原始波形与 重构波形之间的 L<sup>1</sup> 距离,LSTFT 是其短时傅里叶变换(STFT)幅度上的 L<sup>1</sup> 损失。两种 重构损失共享相同的指数衰减调度 γ ,该调度在训练初期促进学习,并随着对抗信号的增 强而逐渐减弱其影响 [[Parker et al.,](#page-15-3) [2024\]](#page-15-3)。Lcommit = ∥z<sup>e</sup> − sg(zq)∥ 2 <sup>2</sup> 是向量量化(VQ)承 诺损失 [[Van Den Oord et al.,](#page-16-6) [2017\]](#page-16-6),其中 sg 表示停止梯度操作符。

表 [1](#page-5-0) 给出了 Voxtral Codec 配置的概要。该完整模型大约有 300M 个参数。所有决策均经过 消融实验,最终配置在最优化方面表现稳定,并达到了最佳音质。

# **2.2 解码器骨干网络**

Voxtral TTS 的解码器主干遵循 Ministral 3B[[Liu et al.,](#page-15-7) [2026](#page-15-7)] 的架构,一个自回归的仅解 码器 Transformer。输入序列由语音参考音频 token 和文本 token 组成,输出音频 token 由 此自回归生成。每个音频帧由 37 个离散 token 表示(1 个语义,36 个声学)。每个码本都有 其独立的嵌入查找表(语义码本为 8192 项,每个声学码本为 21 项),这些查找表的嵌入值 相加后生成每个音频帧的单一嵌入。

解码器主干生成一系列隐状态。线性头部将每个隐状态 h 投影到语义码本词表(8192 个条 目加上一个特殊的音频结束 (**<EOA>**) token)的 Logit 值上,使用标准交叉熵损失进行训 练。为了预测声学 token,h 被输入到一个流匹配 Transformer 中,其描述见第 [2.3](#page-4-0) 节。流匹 配 Transformer 的浮点输出在进入下一步自回归处理前被离散化,以保持完全离散的 token 接口。

#### <span id="page-4-0"></span>**2.3 流匹配 Transformer**

为了预测声学 token,流匹配(FM)Transformer 在解码器主干中每个生成步骤的隐状态 h 上独立运行。我们将在连续空间中建模声学 token 以利用 FM 的平滑速度场,并仅在输出 时进行离散化,以与自回归主干的离散 token 词表对接。

**表 1:** Voxtral 编解码器的关键超参数。

<span id="page-5-0"></span>

| Parameter                            | Value                                   |  |  |  |  |  |
|--------------------------------------|-----------------------------------------|--|--|--|--|--|
| Input / Preprocessing                |                                         |  |  |  |  |  |
| Sampling rate                        | 24000                                   |  |  |  |  |  |
| Patch size                           | 240                                     |  |  |  |  |  |
| AutoEncoder                          |                                         |  |  |  |  |  |
| Encoder patch projection kernel size | 7                                       |  |  |  |  |  |
| Encoder patch projection dimension   | 1024                                    |  |  |  |  |  |
| Encoder transformer layers1          | 2<br>→<br>2<br>→<br>2<br>→<br>2         |  |  |  |  |  |
| Encoder sliding window size          | 16<br>→<br>8<br>→<br>4<br>→<br>2        |  |  |  |  |  |
| Encoder conv kernels                 | 4<br>→<br>4<br>→<br>4<br>→<br>3         |  |  |  |  |  |
| Encoder conv strides                 | 2<br>→<br>2<br>→<br>2<br>→<br>1         |  |  |  |  |  |
| (Decoder ~ips all →<br>to ←          | and uses transposed convolutions)       |  |  |  |  |  |
| Discrete bottleneck                  |                                         |  |  |  |  |  |
| Semantic VQ2<br>codebook size        | 8192                                    |  |  |  |  |  |
| Acoustic FSQ3<br>codebook count×size | 36<br>×<br>21                           |  |  |  |  |  |
| Discriminator                        |                                         |  |  |  |  |  |
| FFT sizes                            | 2296, 1418, 876, 542, 334, 206, 126, 76 |  |  |  |  |  |
| Channels                             | 256                                     |  |  |  |  |  |

<sup>1</sup> For training stability, we use LayerScale with initial scale of 0.01 and QK normalization with ϵ = 10−<sup>6</sup>

FM Transformer 由一个双向的三层 Transformer 组成,其宽度与解码器主干网络相同。它 建模了将高斯噪声 (x<sup>0</sup> ) 传输到声学嵌入 (x<sup>1</sup> ) 的速度场,该过程通过一系列函数评估步骤 0 ≤ t ≤ 1 完成。它接收以下输入:h ,当前的函数评估步骤 t (编码为正弦嵌入),以及当 前的声学嵌入 x<sup>t</sup> ∈ R <sup>36</sup> 。我们为每个输入 h 、t 和 x<sup>t</sup> 使用独立的投影层,因为它们的活性 值尺度不同。我们还对使用 DiT 风格的自适应 LayerNorm (AdaLN) 层进行条件控制进行 了消融实验 [[Peebles and Xie](#page-15-8), [2023](#page-15-8)],但发现我们的方法更优。

训练期间,对于"无条件"建模,隐状态有 10% 的概率被丢弃。在推理阶段,我们使用欧拉 方法对速度向量场 v<sup>t</sup> 进行积分,共进行 8 次函数求值(NFEs),并采用无分类器引导(CFG) [[Ho and Salimans,](#page-14-5) [2022\]](#page-14-5)。具体而言,v<sup>t</sup> 和 x<sup>t</sup> 的形式为:

$$v_t = \alpha v_\theta(x_t, t, h) + (1 - \alpha)v_\theta(x_t, t, \emptyset) \tag{4}$$

$$x_{t-\Delta t} = x_t - v_t \cdot \Delta t \tag{5}$$

,其中 h 为解码器主干网络的隐状态,∅ 为无条件情况,即我们传递一个与 h 形状相同的零 向量。vθ(xt, t, h) 为在时间步 t 时预测的速度场,样本 x<sup>t</sup> 以及条件输入 h。我们根据第 [5.2](#page-10-0) 节中的分析设定 ∆t = 1/8 和 α = 1.2。

注意,在我们的架构中,CFG 在 FM Transformer 的每一帧上独立应用。因此,它仅需额 外进行一次 FM Transformer 的前向传播,相比在解码器主干中应用 CFG 要显著便宜。由 FM Transformer 预测的浮点值通过量化至 21 个 FSQ 级别转换为离散整数值。这些离散化 的 token 将作为输入提供给下一解码步骤中的解码器主干。

<sup>2</sup> During training, VQ is applied with 50% probability.

<sup>3</sup> During training: 50% quantized with FSQ, 25% dithered (uniform noise of magnitude 1/L), 25% unquantized.

由于解码器主干网络的输入是经过嵌入查找的离散 token,我们还考虑了受 MaskGIT [[Chang et al.](#page-14-6), [2022](#page-14-6)] 和 Depth Transformer[[Défossez et al.,](#page-14-1) [2024](#page-14-1)] 启发的替代架构。这两 种方法表现尚可,但在人类评估中仍不如 FM,尤其是在表现力方面。此外,MaskGIT 需 要对全部 36 个声学码本位置和条件 token 进行注意力计算,导致每帧的序列长度为 38,而 FM Transformer 仅需 3 个(h , t , x<sup>t</sup> )。类似地,Depth Transformer 需要 36 步自回归解码, 而 FM 仅需 8 次非自回归求解步骤(NFE)。因此,FM 在质量、计算量和延迟方面均更优。

# **3 训练**

#### **3.1 预训练**

我们使用经过 Voxtral Mini Transcribe [\[Liu et al.](#page-15-9), [2025](#page-15-9)] 伪标记的配对音频和转录文本对来 训练模型。每个训练样本由一个元组 (A1, T2, A2) 组成,其中 A<sup>1</sup> 为语音参考,T<sup>2</sup> 为 A<sup>2</sup> 的 转录文本,这是我们生成的目标。与 Voxtral 类似,我们在 A<sup>1</sup> 与 T<sup>2</sup> 之间插入一个 <next> 特殊 token,在 T<sup>2</sup> 与 A<sup>2</sup> 之间插入一个 <repeat> 特殊 token。我们确保 A<sup>1</sup> 与 A<sup>2</sup> 来自同 一说话人且为单说话人片段,但不一定在时间上相邻。A<sup>1</sup> 与 A<sup>2</sup> 的最大时长为 180 秒,且 我们确保 A<sup>1</sup> 至少为 1 秒长。由于自然对话中人类语音持续时间具有长尾分布特性,我们 发现模型在 3 至 25 秒之间的语音提示(A1)上表现最佳。

损失仅在 A<sup>2</sup> 的 token 上计算。我们使用由两部分组成的损失函数来优化模型,其中包括在 语义 token Lsemantic 上的交叉熵损失以及在声学 token 上的 ~ow-matching 损失 Lacoustic。 我们采用如下的简单条件 ~ow-matching 目标:

$$\mathcal{L}_{\text{acoustic}} = \mathbb{E}_{t \sim \mathcal{U}[0,1], x_0 \sim \mathcal{D}, x_1 \sim \mathcal{N}(0,1)} \|v_{\theta}(x_t, t) - u_t(x_t | x_1, x_0)\|_2^2$$
(6)

$$u_t(x_t|x_1, x_0) = x_1 - x_0 (7)$$

其中 u<sup>t</sup> 为目标条件速度,v<sup>θ</sup> 为 FM Transformer 预测的速度,x<sup>1</sup> 从正态分布中采样得到, x<sup>0</sup> 为数据分布 D。我们使用 Ministral 3B 初始化解码器主干网络。新引入的模块,如 FM Transformer、音频代码本嵌入查找表和输出投影层,均进行随机初始化。在训练过程中, 我们冻结解码器主干中的文本嵌入层,以提高对 Voxtral Mini Transcribe 转录中低频出现 的文本 token 的鲁棒性。为避免对静音部分过拟合,我们还对语音活动检测(VAD)模型 判定无语音的帧采用较低的损失权重,并将极长静音段的损失权重设为 0。此外,我们还对 转录文本进行简单的基于大语言模型的重写,以增强对规范化的与非规范化的文本(例如 "5 - 4"与"}ve minus four")的鲁棒性。

# **3.2 直接偏好最优化**

我们使用直接偏好优化(DPO) [\[Rafailov et al.](#page-16-1), [2023\]](#page-16-1) 对模型进行后训练,重点关注提升词 错误率(WER)和说话人相似度。对于语义码本,我们采用标准的 DPO 目标。鉴于声学码 本是通过流匹配预测的,我们将目标函数从 [Ziv et al.](#page-16-2) [\[2025](#page-16-2)] 进行调整:

$$\mathcal{L}(\theta) = -\mathbb{E}_{t \sim \mathcal{U}(0,1), x^w, x^l} \log \sigma \left( -\beta \left( \Delta_{\theta}(x^w, x^l, t) - \Delta_{\theta_{\text{ref}}}(x^w, x^l, t) \right) \right), \tag{8}$$

其中

$$\Delta_{\theta}(x^{w}, x^{l}, t) = \|v_{\theta}(x_{t}^{w}, t) - u_{t}(x_{t}^{w}|x^{w})\|_{2}^{2} - \|v_{\theta}(x_{t}^{l}, t) - u_{t}(x_{t}^{l}|x^{l})\|_{2}^{2}.$$

$$(9)$$

我们通过计算使目标适用于我们的自回归设置(注意加粗的 t 表示每个 token 都有不同的采 样 t),从而实现:

$$\Delta_{\theta}(x^{w}, x^{l}, t) = \sum_{i=1}^{N_{w}} \|v_{\theta}(x_{i, t_{i}}^{w}, t_{i}) - u_{i, t_{i}}^{w}\|_{2}^{2} - \sum_{i=1}^{N_{l}} \|v_{\theta}(x_{i, t_{i}}^{l}, t_{i}) - u_{i, t_{i}}^{l}\|_{2}^{2}$$

$$(10)$$

发现长度规范化(除以获胜者的长度)会导致不稳定性。

我们确保在序列的每个位置采样的 t 和 x<sup>0</sup> 对策略模型 θ 和参考模型 θref 保持一致。两个 DPO 损失以均匀权重相加,但由于训练对 ~ow-DPO 损失敏感,我们使用了 βsemantic = 0.1 和 βacoustic = 0.5 。为保证训练稳定性,采用较低的学习率 8e−8 。

DPO 的数据通过拒绝采样流水线收集,该流水线以一组保留的单说话人语音样本和多样化 的合成文本提示作为输入。我们使用 Mistral Small Creative 进行提示。[1](#page-7-1) 使用语音提示的 转录文本和随机选择的人物设定,合成一系列多样化的文本,以延续或回应对话上下文。随 后,预训练检查点将语音和文本提示作为输入,从每个输入生成多个样本,从中可构建出胜 者与败者配对。胜者与败者通过字错误率(WER)、说话人相似度、音量一致性、UTMOSv2 [\[Baba et al.,](#page-14-7) [2024](#page-14-7)] 以及其他语言模型评判指标来确定。我们使用结合了 DPO 损失和高 质量语音上的预训练目标,在 1 轮次内优化模型,因为我们发现,在合成数据上进行更长时 间的训练会导致语音更加机械化。

# **4 结果**

#### <span id="page-7-0"></span>**4.1 Voxtral 编解码器**

表 [2](#page-7-2) 展示了在 Expresso 数据集 [\[Nguyen et al.](#page-15-10), [2023\]](#page-15-10) 上 Voxtral Codec 与 Mimi 的对比。我 们评估了以下目标指标:梅尔距离、STFT 距离、语音质量感知评价(PESQ)、扩展短时客 观可懂度(ESTOI)、使用对应源音频和重构音频的自动语音识别模型生成的转录文本之间 的词错误率(ASR-WER),以及使用说话人嵌入模型计算的说话人相似度得分。我们还报告 了比特率和每秒帧数(fps),这些指标在自回归解码器模型的应用场景中具有相关性。由于 Mimi 采用 RVQ 设计的声学码本,因此可以选择子集码本以权衡比特率与质量。当 Voxtral Codec 与 Mimi 在 16 个码本配置下进行比较,使得比特率相近时,Voxtral Codec 在所有 目标指标上均表现更优。在内部主观评估中,我们发现对于以语音为主要关注内容的音频, Voxtral Codec 在 16 个码本配置下的表现与 Mimi 相当或更优。

<span id="page-7-2"></span>

| Model<br>fps       | token/frame × |                        | bitrate | Reconstruction (↓) |       | Intrusive (↑) |              | Perceptual   |       |
|--------------------|---------------|------------------------|---------|--------------------|-------|---------------|--------------|--------------|-------|
|                    | vocab. size   | (kbps)                 | Mel     | STFT               | PESQ  | ESTOI         | ASR-WER (%)↓ | Speaker Sim↑ |       |
| Mimi – 8cb (Moshi) | 12.5          | 8 × (2048)             | 1.1     | 0.702              | 1.177 | 2.07          | 0.803        | 11.75        | 0.672 |
| Mimi – 16cb        | 12.5          | 16 × (2048)            | 2.2     | 0.618              | 1.100 | 2.67          | 0.865        | 11.01        | 0.829 |
| Mimi – full 32cb   | 12.5          | 32 × (2048)            | 4.4     | 0.552              | 1.040 | 3.18          | 0.910        | 10.25        | 0.902 |
| Voxtral Codec      | 12.5          | 1 × (8192) + 36 × (21) | 2.1     | 0.545              | 0.982 | 3.05          | 0.882        | 10.66        | 0.843 |

**表 2:** Voxtral 编解码器与 Mimi 在 Expresso 数据集上的对比。

#### **4.2 自动评估**

我们使用自动化指标对 Voxtral TTS、ElevenLabs v3 和 ElevenLabs Flash v2.5 在 SEED-TTS [\[Anastassiou et al.](#page-14-2), [2024\]](#page-14-2) 以及 MiniMax-TTS[[Zhang et al.](#page-16-3), [2025\]](#page-16-3) 中支持的九种语言 进行评估:

<span id="page-7-1"></span><sup>1</sup> <https://docs.mistral.ai/models/mistral-small-creative-25-12>

- 1. **字错误率(WER)**:通过 Voxtral Mini 转录 v2 测量,以捕捉语音的可理解性。
- 2. **UTMOS-v2** [\[Baba et al.](#page-14-7), [2024](#page-14-7)]:预测生成语音的平均意见得分(MOS)。
- 3. **说话人相似度**: 使用 ECAPA-TDNN 模型 [\[Desplanques et al.,](#page-14-8) [2020\]](#page-14-8) 预测说话人嵌 入,并与参考嵌入计算余弦相似度。这评估了生成语音与提供的语音参考的相似度。

三种模型的结果如表 [3](#page-8-0)所示。尽管两个 ElevenLabs 模型在各类语言中均实现了较低的 WER, 但 Voxtral TTS 在说话人相似度指标上显著优于 ElevenLabs。令人意外的是,我们发现 ElevenLabs Flash v2.5 在大多数自动评估指标上表现更佳,而 ElevenLabs v3 在人工评估中 表现更优,尤其是在情感控制方面。这凸显了结合人工评估与自动评估的重要性。

<span id="page-8-0"></span>**表 3:** Voxtral TTS、ElevenLabs v3 和 ElevenLabs Flash v2.5 的 WER、UTMOS 及说话人相似度 得分。

| WER (%) ↓  |         |               | UTMOS ↑          |         |               | Speaker Sim ↑    |         |               |                  |
|------------|---------|---------------|------------------|---------|---------------|------------------|---------|---------------|------------------|
| Task       | Voxtral | ElevenLabs v3 | ElevenLabs Flash | Voxtral | ElevenLabs v3 | ElevenLabs Flash | Voxtral | ElevenLabs v3 | ElevenLabs Flash |
| MiniMax    |         |               |                  |         |               |                  |         |               |                  |
| Arabic     | 2.68    | 3.67          | 2.86             | 3.07    | 2.50          | 2.89             | 0.746   | 0.546         | 0.539            |
| German     | 0.83    | 0.45          | 1.08             | 3.12    | 2.90          | 3.27             | 0.721   | 0.457         | 0.489            |
| English    | 0.63    | 0.48          | 0.33             | 4.30    | 4.27          | 4.27             | 0.786   | 0.484         | 0.489            |
| Spanish    | 0.51    | 0.87          | 0.49             | 3.41    | 3.18          | 2.99             | 0.762   | 0.443         | 0.541            |
| French     | 3.22    | 2.34          | 2.26             | 2.83    | 2.90          | 2.94             | 0.587   | 0.339         | 0.378            |
| Hindi      | 4.99    | 8.71          | 5.08             | 3.56    | 3.56          | 3.35             | 0.839   | 0.707         | 0.679            |
| Italian    | 1.32    | 0.58          | 0.55             | 3.43    | 3.08          | 3.09             | 0.739   | 0.527         | 0.485            |
| Dutch      | 1.99    | 1.52          | 0.83             | 3.89    | 3.53          | 3.68             | 0.720   | 0.397         | 0.598            |
| Portuguese | 1.02    | 0.92          | 1.15             | 3.66    | 3.41          | 3.41             | 0.785   | 0.571         | 0.642            |
| Seed TTS   | 1.23    | 1.26          | 0.86             | 4.11    | 3.92          | 4.09             | 0.628   | 0.392         | 0.413            |

#### **4.3 人为评估**

自动化指标无法衡量语音合成模型的自然度和表现力,尤其是模型表达特定情感的能力。我 们发现 UTMOS 仅是一个松散的代理指标,在不同语言间校准不佳,且与人类偏好相关性 较弱。因此,我们进行了两组人工评估,标注者在不知晓模型身份的情况下比较两个模型生 成的结果。评估共包含 77 个提示语,其中 11 个为中性提示,66 个带有预期情感。所有评 估中,标注者被要求判断其中一个生成结果是"稍好"、"明显更好",还是"两者都好"或 "两者都差"。在标注过程中,所有音频样本均重采样为 24 kHz 的 WAV 格式(包括参考样 本),以确保不会因音频质量产生偏差。

### **4.3.1 旗舰声音**

首先,我们将我们的旗舰语音(英国女性、英国男性、美国男性、法国女性)与竞争对手提 供的同性别和同口音的旗舰语音进行对比。我们进行了两次子评估:

- 1. **显式引导**:我们测试了将语音合成模型的生成结果偏向特定情感的能力。对于带有 相关情感(非中性)的语音合成提示,我们以自由格式指令的形式提供给 Gemini 2.5 Flash TTS,因其支持自由格式指令,例如"用愤怒的语调说话"。对于 ElevenLabs v3,我们则提供括号包裹的情感标签 [2](#page-8-1) . 虽然 Voxtral TTS 不支持情感标签/文本指 令,但我们通过利用同一说话人提供的、体现所需情感的另一语音提示来引导生成。
- 2. **隐式引导**: 我们测试模型从给定文本中推断情感的能力(例如:"这是我一生中最美 好的一天!")。不会向模型提供任何情感标签或指令。对于 Voxtral TTS,我们使用 中性语音提示。

<span id="page-8-1"></span><sup>2</sup> [https://elevenlabs.io/blog/eleven-v3-audio-tags-expressing-emotional-context-i](https://elevenlabs.io/blog/eleven-v3-audio-tags-expressing-emotional-context-in-speech) [n-speech](https://elevenlabs.io/blog/eleven-v3-audio-tags-expressing-emotional-context-in-speech)

我们为每种语言的每一对使用三位同方言的母语者作为标注者。表 [4](#page-9-0) 展示了 Voxtral TTS(不 包括平局)的胜率。Gemini 2.5 Flash TTS 是表现最强的模型,而 Voxtral TTS 与 ElevenLabs v3 相比具有竞争力。在隐式引导设置下,Voxtral TTS 始终优于两个 ElevenLabs 模型。

<span id="page-9-0"></span>**表 4: Voxtral TTS 在不同控制类型下的胜率。**在显式控制情景下,Voxtral TTS 与 ElevenLabs v3 相当,而在隐式控制情景下,其胜率高于两个 ElevenLabs 模型。

| Emotion steering | Opponent Model        | Voxtral TTS Win Rate (%) |
|------------------|-----------------------|--------------------------|
| Explicit         | ElevenLabs v3         | 51.0                     |
|                  | Gemini 2.5 Flash TTS  | 35.4                     |
|                  | ElevenLabs Flash v2.5 | 58.3                     |
| Implicit         | ElevenLabs v3         | 55.4                     |
|                  | Gemini 2.5 Flash TTS  | 37.1                     |

#### **4.3.2 Zero-shot 语音克隆**

为评估语音克隆能力,我们在每种语言中选取两位知名演讲者的高质量音频作为音源。在 zero-shot 情景下,从每个模型生成语音,并指示标注人员根据(a)生成音频与语音提示的 相似度以及(b)语音的自然度和表现力对生成结果进行评分。

<span id="page-9-1"></span>**表 5: Voxtral TTS 在各语言上对 ElevenLabs Flash v2.5 的胜率。** Voxtral TTS 在每种语言上 的表现均达到或超过 ElevenLabs Flash v2.5,整体微平均胜率为 68.4%。

| Language   | Voxtral TTS Win Rate (%) |
|------------|--------------------------|
| Arabic     | 72.9                     |
| Dutch      | 49.4                     |
| English    | 60.8                     |
| French     | 54.4                     |
| German     | 72.0                     |
| Hindi      | 79.8                     |
| Italian    | 57.1                     |
| Portuguese | 74.4                     |
| Spanish    | 87.8                     |
| Overall    | 68.4                     |

表 [5](#page-9-1) 展示了 Voxtral TTS 在不同语言下对 ElevenLabs Flash v2.5 的胜率。总体而言,Voxtral TTS 的胜率为 68.4%,在高资源和低资源语言(如阿拉伯语和印地语)中均表现出显著更优 的结果。值得注意的是,Voxtral TTS 在 zero-shot 情景下的胜率(68.4%)远高于旗舰语音 (58.3%),突显出 Voxtral TTS 是一个更具泛化能力的模型,能够捕捉多样化的用户语音特 征。

# **5 分析**

在本节中,我们对预训练模型和 DPO 检查点进行了比较,并对相关的推理参数进行了消融 实验。

### **5.1 DPO 优化**

表 [6](#page-10-1) 展示了预训练模型和 DPO 检查点的 WER 与 UTMOS 指标。总体而言,DPO 在两 项指标上均有所提升,其中德语和法语的提升最为显著,而印地语则出现下降。定性分析发 现,DPO 模型的幻觉现象更少,漏读单词的情况也更少。此外,DPO 还缓解了预训练模型 在音频播放过程中音量明显衰减的偶发倾向。有趣的是,DPO 对说话人相似度的影响极小, 其值与预训练检查点相差不超过 ±0.01(为简洁起见,此处未展示)。

<span id="page-10-1"></span>

|            |          | WER (%)<br>↓    | UTMOS<br>↑ |              |  |  |  |  |  |
|------------|----------|-----------------|------------|--------------|--|--|--|--|--|
| Task       | Pretrain | DPO             | Pretrain   | DPO          |  |  |  |  |  |
| MiniMax    |          |                 |            |              |  |  |  |  |  |
| Arabic     | 2.80     | 2.68 (-0.12)    | 3.01       | 3.07 (+0.06) |  |  |  |  |  |
| German     | 4.08     | 0.83 (-3.25)    | 3.05       | 3.12 (+0.07) |  |  |  |  |  |
| English    | 0.84     | 0.63 (-0.21)    | 4.25       | 4.30 (+0.05) |  |  |  |  |  |
| Spanish    | 0.56     | 0.51 (-0.06)    | 3.38       | 3.41 (+0.04) |  |  |  |  |  |
| French     | 5.01     | 3.22 (-1.79)    | 2.76       | 2.83 (+0.07) |  |  |  |  |  |
| Hindi      | 3.39     | 4.99<br>(+1.61) | 3.43       | 3.56 (+0.13) |  |  |  |  |  |
| Italian    | 2.18     | 1.32 (-0.85)    | 3.36       | 3.43 (+0.07) |  |  |  |  |  |
| Dutch      | 3.10     | 1.99 (-1.11)    | 3.85       | 3.89 (+0.04) |  |  |  |  |  |
| Portuguese | 1.17     | 1.02 (-0.15)    | 3.60       | 3.66 (+0.06) |  |  |  |  |  |
| Seed TTS   | 1.58     | 1.23 (-0.35)    | 4.07       | 4.11 (+0.04) |  |  |  |  |  |

**表 6:** DPO 在多种语言中均提升了 WER 和 UTMOS。

#### <span id="page-10-0"></span>**5.2 推理参数**

图 [4](#page-11-0) 展示了在功能评估次数(NFEs)和 CFG α 选择变化时,自动评估指标的影响。当 NFEs 从 2 增加到 8 时,各项指标均有显著提升。我们发现,将 NFEs 进一步增加至 8 以上对说 话人相似度的提升效果微乎其微,且在词错误率(WER)上出现轻微下降。因此,我们将 8 个 NFEs 作为默认的推理设置。

增大 CFG α 的值,我们发现除 UTMOS-v2 外,所有指标均呈现近乎单调的提升。然而,内 部人工评估发现,较高的 α 会导致模型过度遵循提供的语音提示,无法对文本提示中隐含 的情感进行合理偏向。此外,我们还发现较低的 α = 1.2 在高质量音频(如专业录音)上表 现最佳,而野外录制的音频可能从较高的 α 中受益。

# **6 vLLM-Omni 中的推理与服务**

Voxtral TTS 通过 vLLM-Omni[[Yin et al.](#page-16-9), [2026](#page-16-9)] 提供服务,这是针对多阶段多模态模型的 vLLM [\[Kwon et al.](#page-14-9), [2023](#page-14-9)] 扩展。Voxtral TTS 被分解为两阶段流水线:第一阶段为生成阶 段,预测音频 token(语义和声学),随后是编码器解码阶段,将 token 转换为波形。两个阶 段通过共享内存上的异步分块流协议进行通信,实现在完整波形生成之前即可实现首个音频 输出的低延迟。

<span id="page-11-0"></span>![](_page_11_Figure_0.jpeg)

**图 4: NFEs 和 CFG 对自动评估的影响。**指标在 SEED-TTS 和 MiniMax 中的 9 种语言上取平均 值。将 NFEs 从 2 增加到 8 可以提升说话人相似度和 UTMOS 指标。当 NFEs 超过此值时,WER 指标略有下降。随着 CFG 值提高,各项指标单调上升,但人工评估指出,在高 α 情况下存在文本一 致性下降的问题。

### **6.1 用于流匹配 Transformer 的 CUDA 图加速**

生成阶段的流匹配 Transformer 是计算瓶颈。每个解码步骤在使用 CFG 时需要 N 次函数 求值,每生成一帧需进行 2 × N 次前向传播。

为消除 Python 层开销和内核启动延迟,整个常微分方程求解器被捕捉为 CUDA 图。在启 动时,会对每个桶的大小执行一次即时预热遍历,并相应地捕捉 CUDA 图。在推理过程中, 实际批量大小会被向上舍入到最近的桶大小,通过用零填充输入实现。接着,重放 CUDA 图,并将输出切片回实际批量大小。如果批量大小超过已捕捉的最大桶大小,则模型退回到 即时执行模式。

<span id="page-11-1"></span>为了评估 CUDA 图加速的效果,我们对比了在急切模式(eager mode)和 CUDA 图下解码 时的延迟和实时因子(RTF)。表 [7](#page-11-1) 报告了在单个 H200 上,输入 500 个字符文本、10 秒 音频参考以及并发数为 1 的情况下的结果。启用 CUDA 图后,延迟改善了 47%,实时因子 (RTF)降低了 2.5 倍。

**表 7:** CUDA 图加速对流匹配 Transformer 的影响。

| Con}guration | Latency | RTF   |
|--------------|---------|-------|
| Eager mode   | 133 ms  | 0.258 |
| CUDA graph   | 70 ms   | 0.103 |

### **6.2 异步分块流**

两个流水线阶段在分离的调度环中运行。为了将自回归生成阶段的解码与编解码器解码阶段 的波形合成重叠,引入了一种异步分块流协议。

在每次生成步骤后,vLLM-Omni 传输管理器会将音频 token 存储到每个请求的缓冲区中。 当缓冲区长度达到预定义值时,便会将一段 token 发送到编解码器解码阶段。为了确保各段 之间的连贯性,每段输出都包含一部分先前的帧以及新生成的帧。这种重叠使得编解码器解 码器的因果滑动窗口注意力机制能够在段边界之间保持时间上的连贯性。

### **6.3 推理吞吐量**

通过本节介绍的技术,Voxtral TTS 实现了低延迟、高通量的推理。表 [8](#page-12-0) 展示了在单个 NVIDIA H200 上,从并发度 1 到 32 的服务性能,输入为 500 字符的文本和 10 秒的音 频参考。当并发度从 1 增加到 32 时,吞吐量从每秒 119 字符提升至每 GPU 每秒 1,431 字 符,提升了 12 倍,而延迟始终保持在 1 秒以下。等待率(定义为客户端因等待输出而必须 停顿的音频块比例)在所有并发级别下均保持为零。随着并发度增加,每个请求的 RTF 在 并发度 32 时仅小幅上升至 0.302,仍远低于实时边界。

<span id="page-12-0"></span>这些结果表明,Voxtral TTS 适合用于生产环境部署:单个 H200 可以同时为超过 30 个用 户提供不间断的流式输出,并实现亚秒级的首音频延迟。

| Concurrency | Latency | RTF   | Throughput (char/s/GPU) | Wait Rate |
|-------------|---------|-------|-------------------------|-----------|
| 1           | 70 ms   | 0.103 | 119.14                  | 0%        |
| 16          | 331 ms  | 0.237 | 879.11                  | 0%        |
| 32          | 552 ms  | 0.302 | 1430.78                 | 0%        |

**表 8:** Voxtral TTS 在单个 H200 上的推理性能。

# **7 结论**

我们介绍了 Voxtral TTS,这是一种多语言文本到语音模型,采用混合架构实现语义 token 的 自回归生成以及声学 token 的流匹配。这些 token 对应于 Voxtral Codec 中的 token,Voxtral Codec 是一种语音分词器,结合了通过语音识别(ASR)蒸馏得到的语义 token 与矢量量化 (FSQ)声学 token。

Voxtral TTS 能够仅需 3 秒的参考音频即可生成富有表现力的语音克隆,且在人类评估中 优于 API 基准。我们以 CC BY-NC 许可证发布 Voxtral TTS 的开源权重,以支持更具表 现力的语音合成系统的研究与开发。

### **核心贡献者**

刘弘毅、艾利克斯·塔克内、安迪·艾伦伯格、安迪·罗、孙晨佑、古斯塔夫·兰普尔、亨 利·拉加德、让-马洛·德利尼翁、金载永、约翰·哈维尔、克亚提·拉加维·钱杜、洛伦佐· 西诺雷蒂、玛格丽特·詹宁斯、帕特里克·冯·普拉滕、帕万卡马尔·雷迪·穆迪雷迪、罗 欣·阿罗拉、桑奇特·甘地、塞缪尔·休梅奥、索汉·戈什、斯里詹·米什拉、范春。

### **贡献者们**

阿卜杜拉齐兹·布纳尔,阿比纳夫·拉斯特吉,阿德里安·萨德,艾伦·杰法雷斯,阿尔伯 特·江,亚历山大·卡希尔,亚历山大·加瓦丹,亚历山大·萨布雷洛,阿梅莉·埃利乌,阿 莫斯·尤,安德鲁·白,安德鲁·赵,安热勒·兰格莱梅茨,安莫尔·阿加瓦尔,安东·埃 利谢耶夫,安东尼娅·卡尔维,阿琼·马朱姆达尔,阿瑟·福尼耶,阿特约姆·乔森,阿维· 苏里亚拉奇,艾森努尔·卡拉杜曼·乌图尔,巴普蒂斯特·布,巴普蒂斯特·罗齐埃尔,鲍 杜因·德·莫尼克奥,本杰明·提比,鲍文·杨,夏洛特·克龙杰尔,克莱芒斯·兰弗朗奇, 康纳·陈,科伦坦·巴罗,科伦坦·索蒂埃,西普里安·库尔托,达里乌斯·达贝尔特,迭 戈·德拉斯卡萨斯,叶丽扎维塔·德米亚年科,埃利奥特·查内-萨内,埃马纽埃尔·戈特洛 布,昂格兰·帕昆,埃蒂安·戈菲内,法比安·尼埃尔,法鲁克·艾哈迈德,费德里科·巴 尔达萨雷,加布里埃勒·贝拉达,盖坦·埃克雷庞,戈蒂埃·古内,琴妮薇芙·海耶斯,乔 治·诺维科夫,吉达·皮斯蒂利,古斯塔夫·昆什,古斯塔夫·马丁,古斯塔夫·雷亚尔,冈 詹·丹胡卡,贡希·古普塔,周汉,哈希尔·沙阿,霍普·麦戈文,雨果·蒂蒙尼耶,因德 拉尼尔·穆克赫吉,张伊蕾,贾克·孙,扬·卢德兹耶夫斯基,贾森·鲁特,杰雷米·丹坦, 乔阿基姆·施特尼亚,乔纳斯·阿玛,约瑟芬·德尔阿斯,乔塞尔·索默维尔·罗伯茨,朱 利安·陶兰,卡梅什·亚达夫,卡蒂克·坎德尔瓦尔,基利安·特普,库什·贾因,劳伦斯· 艾奇森,劳伦特·费因辛,莱昂纳德·布利耶,赵凌霄,路易斯·马丁,露西尔·索尔尼耶, 高璐瑜,马滕·布伊尔,马南·夏尔马,玛丽·佩拉特,马克·普林斯,马蒂亚·亚历山大, 马蒂厄·波里,马蒂厄·施密特,马蒂尔德·吉利亚米,马蒂厄·迪诺,马蒂厄·富泰拉尔, 马克西姆·达林,马克斯米连·奥古斯丁,梅特·翁萨尔,米娅·奇基尔,米哈伊尔·比鲁 钦斯基,阮明光,米尔切亚·利卡,莫尔甘·里维耶尔,内哈·古普塔,奥利维耶·布谢,奥 利维耶·杜尚,帕特里夏·王,保罗·雅各布,保罗·瓦姆贝格,保利娜·库里洛维奇,菲 利普·皮奈尔,菲洛梅娜·尚尼亚,皮埃尔·斯托克,皮奥特尔·米洛斯,普拉泰克·古普 塔,普拉韦什·阿格拉瓦尔,昆汀·托罗巴,拉姆·拉姆拉克亚,兰德尔·伊斯恩豪尔,里 希·沙阿,罗曼·索维斯特,罗曼·索列茨基,罗莎莉·米勒,鲁珀特·门尼尔,萨加尔·瓦 泽,塞缪尔·巴里,塞缪尔·贝尔卡迪,桑迪普·苏布拉马尼亚,肖恩·查,沙夏瓦特·维 尔马,西德汉特·瓦格贾勒,锡德哈特·甘地,西蒙·勒帕日,苏穆克·艾萨尔,西蒙·安 东尼亚克,塔鲁恩·库马尔·万加尼,特文·勒斯卡奥,让·卡歇,托马斯·西蒙·索尔格, 蒂博·拉夫里尔,托马斯·查巴尔,托马斯·富贝尔,托马斯·罗伯特,托马斯·王,蒂姆· 劳森,汤姆·贝威利,汤姆·爱德华兹,泰勒·王,乌马尔·贾米尔,翁贝托·托马西尼,瓦 莱里亚·尼姆奇诺娃,维丹·南达,维克多·儒奥,文丁·李,威廉·哈瓦德,威廉·马歇 尔,李兴辉,郭兴然,杨欣宇,扬尼克·诺豪斯,亚辛·埃尔奥瓦希迪,亚西尔·本杜,王 一涵,潘一木,扎克查里·拉姆齐,许振林

#### **7.1 致谢**

我们感谢 vLLM-Omni 团队的高晗、刘洪胜、王睿和林悦千在将 Voxtral TTS 集成到 vLLM-Omni 框架过程中提供的支持与贡献。

# **参考文献**

- <span id="page-14-2"></span>Philip Anastassiou, Jiawei Chen, Jitong Chen, Yuanzhe Chen, Zhuo Chen, Ziyi Chen, Jian Cong, Lelai Deng, Chuang Ding, Lu Gao, Mingqing Gong, Peisong Huang, Qingqing Huang, Zhiying Huang, Yuanyuan Huo, Dongya Jia, Chumin Li, Feiya Li, Hui Li, Jiaxin Li, Xiaoyang Li, Xingxing Li, Lin Liu, Shouda Liu, Sichao Liu, Xudong Liu, Yuchen Liu, Zhengxi Liu, Lu Lu, Junjie Pan, Xin Wang, Yuping Wang, Yuxuan Wang, Zhengnan Wei, Jian Wu, Chao Yao, Yifeng Yang, Yuanhao Yi, Junteng Zhang, Qidi Zhang, Shuo Zhang, Wenjie Zhang, Yang Zhang, Zilin Zhao, Dejian Zhong, and Xiaobin Zhuang. Seed-tts: A family of high-quality versatile speech generation models, 2024. URL [https:](https://arxiv.org/abs/2406.02430) [//arxiv.org/abs/2406.02430](https://arxiv.org/abs/2406.02430).
- <span id="page-14-7"></span>Kaito Baba, Wataru Nakata, Yuki Saito, and Hiroshi Saruwatari. The t05 system for the VoiceMOS Challenge 2024: Transfer learning from deep image classi}er to naturalness MOS prediction of high-quality synthetic speech. In *IEEE Spoken Language Technology Workshop (SLT)*, pages 818–824, 2024. doi: 10.1109/SLT61566.2024.10832315.
- <span id="page-14-4"></span>Donald J. Berndt and James Clizord. Using dynamic time warping to }nd patterns in time series. In *Proceedings of the 3rd International Conference on Knowledge Discovery and Data Mining*, AAAIWS'94, page 359–370. AAAI Press, 1994.
- <span id="page-14-0"></span>Zalán Borsos, Raphaël Marinier, Damien Vincent, Eugene Kharitonov, Olivier Pietquin, Matt Shari}, Dominik Roblek, Olivier Teboul, David Grangier, Marco Tagliasacchi, and Neil Zeghidour. Audiolm: A language modeling approach to audio generation. *IEEE/ACM Transactions on Audio, Speech, and Language Processing*, 31:2523–2533, 2023. doi: 10.1109/TASLP.2023.3288409.
- <span id="page-14-6"></span>Huiwen Chang, Han Zhang, Lu Jiang, Ce Liu, and William T. Freeman. Maskgit: Masked generative image transformer. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, pages 11315–11325, June 2022.
- <span id="page-14-3"></span>Alexandre Défossez, Jade Copet, Gabriel Synnaeve, and Yossi Adi. High }delity neural audio compression. *arXiv preprint arXiv:2210.13438*, 2022.
- <span id="page-14-1"></span>Alexandre Défossez, Laurent Mazaré, Manu Orsini, Amélie Royer, Patrick Pérez, Hervé Jégou, Edouard Grave, and Neil Zeghidour. Moshi: a speech-text foundation model for real-time dialogue. *arXiv preprint arXiv:2410.00037*, 2024.
- <span id="page-14-8"></span>Brecht Desplanques, Jenthe Thienpondt, and Kris Demuynck. ECAPA-TDNN: Emphasized channel attention, propagation and aggregation in TDNN based speaker veri}cation. In *Interspeech 2020*, pages 3830–3834, 2020. doi: 10.21437/Interspeech.2020-2650.
- <span id="page-14-5"></span>Jonathan Ho and Tim Salimans. Classi}er-free dizusion guidance. *arXiv preprint arXiv:2207.12598*, 2022. URL <https://arxiv.org/abs/2207.12598>.
- <span id="page-14-9"></span>Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, and Ion Stoica. E{cient memory management for large language model serving with PagedAttention. In *Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles*, 2023. doi: 10.1145/3600006.3613165.

- <span id="page-15-1"></span>Matt Le, Apoorv Vyas, Bowen Shi, Brian Karrer, Leda Sari, Rashel Moritz, Mary Williamson, Vimal Manohar, Yossi Adi, Jay Mahadeokar, and Wei-Ning Hsu. Voicebox: Text-guided multilingual universal speech generation at scale. In *Advances in Neural Information Processing Systems*, volume 36, 2023. URL [https://proceedings.neurips.](https://proceedings.neurips.cc/paper_files/paper/2023/hash/2d8911db9ecedf866015091b28946e15-Abstract-Conference.html) [cc/paper\\_files/paper/2023/hash/2d8911db9ecedf866015091b28946e15-Abstrac](https://proceedings.neurips.cc/paper_files/paper/2023/hash/2d8911db9ecedf866015091b28946e15-Abstract-Conference.html) [t-Conference.html](https://proceedings.neurips.cc/paper_files/paper/2023/hash/2d8911db9ecedf866015091b28946e15-Abstract-Conference.html).
- <span id="page-15-5"></span>Alexander H Liu, Sung-Lin Yeh, and James R Glass. Revisiting self-supervised learning of speech representation from a mutual information perspective. In *ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, pages 12051–12055. IEEE, 2024.
- <span id="page-15-9"></span>Alexander H. Liu, Andy Ehrenberg, Andy Lo, Clément Denoix, Corentin Barreau, Guillaume Lample, Jean-Malo Delignon, Khyathi Raghavi Chandu, Patrick von Platen, Pavankumar Reddy Muddireddy, Sanchit Gandhi, Soham Ghosh, Srijan Mishra, and Thomas Foubert. Voxtral, 2025. URL <https://arxiv.org/abs/2507.13264>.
- <span id="page-15-7"></span>Alexander H Liu, Kartik Khandelwal, Sandeep Subramanian, Victor Jouault, Abhinav Rastogi, Adrien Sadé, Alan Jezares, Albert Jiang, Alexandre Cahill, Alexandre Gavaudan, et al. Ministral 3. *arXiv preprint arXiv:2601.08584*, 2026.
- <span id="page-15-2"></span>Fabian Mentzer, David Minnen, Eirikur Agustsson, and Michael Tschannen. Finite scalar quantization: VQ-VAE made simple, 2023.
- <span id="page-15-10"></span>Tu Anh Nguyen, Wei-Ning Hsu, Antony d'Avirro, Bowen Shi, Itai Gat, Maryam Fazel-Zarani, Tal Remez, Jade Copet, Gabriel Synnaeve, Michael Hassid, et al. Expresso: A benchmark and analysis of discrete expressive speech resynthesis. *arXiv preprint arXiv:2308.05725*, 2023.
- <span id="page-15-3"></span>Julian D Parker, Anton Smirnov, Jordi Pons, CJ Carr, Zack Zukowski, Zach Evans, and Xubo Liu. Scaling transformers for low-bitrate high-quality speech coding. *arXiv preprint arXiv:2411.19842*, 2024.
- <span id="page-15-8"></span>William Peebles and Saining Xie. Scalable dizusion models with transformers. In *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)*, pages 4195– 4205, October 2023.
- <span id="page-15-0"></span>Vadim Popov, Ivan Vovk, Vladimir Gogoryan, Tasnima Sadekova, and Mikhail Kudinov. Grad-TTS: A dizusion probabilistic model for text-to-speech. In *Proceedings of the 38th International Conference on Machine Learning*, volume 139 of *Proceedings of Machine Learning Research*, pages 8599–8608. PMLR, 2021. URL [https://proceedings.mlr.pr](https://proceedings.mlr.press/v139/popov21a.html) [ess/v139/popov21a.html](https://proceedings.mlr.press/v139/popov21a.html).
- <span id="page-15-4"></span>O}r Press, Noah A Smith, and Mike Lewis. Train short, test long: Attention with linear biases enables input length extrapolation. *arXiv preprint arXiv:2108.12409*, 2021.
- <span id="page-15-6"></span>Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, and Ilya Sutskever. Robust speech recognition via large-scale weak supervision. In *International conference on machine learning*, pages 28492–28518. PMLR, 2023.

- <span id="page-16-1"></span>Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. In *Advances in Neural Information Processing Systems*, 2023. URL [https:](https://arxiv.org/abs/2305.18290) [//arxiv.org/abs/2305.18290](https://arxiv.org/abs/2305.18290).
- <span id="page-16-5"></span>Hugo Touvron, Matthieu Cord, Alexandre Sablayrolles, Gabriel Synnaeve, and Hervé Jégou. Going deeper with image transformers. In *Proceedings of the IEEE/CVF international conference on computer vision*, pages 32–42, 2021.
- <span id="page-16-6"></span>Aaron Van Den Oord, Oriol Vinyals, et al. Neural discrete representation learning. *Advances in neural information processing systems*, 30, 2017.
- <span id="page-16-8"></span>Shikhar Vashishth, Harman Singh, Shikhar Bharadwaj, Sriram Ganapathy, Chulayuth Asawaroengchai, Kartik Audhkhasi, Andrew Rosenberg, Ankur Bapna, and Bhuvana Ramabhadran. Stab: Speech tokenizer assessment benchmark. *arXiv preprint arXiv:2409.02384*, 2024.
- <span id="page-16-0"></span>Chengyi Wang, Sanyuan Chen, Yu Wu, Ziqiang Zhang, Long Zhou, Shujie Liu, Zhuo Chen, Yanqing Liu, Huaming Wang, Jinyu Li, Lei He, Sheng Zhao, and Furu Wei. Neural codec language models are zero-shot text to speech synthesizers. *arXiv preprint arXiv:2301.02111*, 2023. URL <https://arxiv.org/abs/2301.02111>.
- <span id="page-16-4"></span>Haibin Wu, Naoyuki Kanda, Se}k Emre Eskimez, and Jinyu Li. Ts3-codec: Transformerbased simple streaming single codec. *arXiv preprint arXiv:2411.18803*, 2024.
- <span id="page-16-9"></span>Peiqi Yin, Jiangyun Zhu, Han Gao, Chenguang Zheng, Yongxiang Huang, Taichang Zhou, Ruirui Yang, Weizhi Liu, Weiqing Chen, Canlin Guo, Didan Deng, Zifeng Mo, Cong Wang, James Cheng, Roger Wang, and Hongsheng Liu. vllm-omni: Fully disaggregated serving for any-to-any multimodal models, 2026. URL [https://arxiv.org/abs/2602.0](https://arxiv.org/abs/2602.02204) [2204](https://arxiv.org/abs/2602.02204).
- <span id="page-16-3"></span>Bowen Zhang, Congchao Guo, Geng Yang, Hang Yu, Haozhe Zhang, Heidi Lei, Jialong Mai, Junjie Yan, Kaiyue Yang, Mingqi Yang, Peikai Huang, Ruiyang Jin, Sitan Jiang, Weihua Cheng, Yawei Li, Yichen Xiao, Yiying Zhou, Yongmao Zhang, Yuan Lu, and Yucen He. Minimax-speech: Intrinsic zero-shot text-to-speech with a learnable speaker encoder, 2025. URL <https://arxiv.org/abs/2505.07916>.
- <span id="page-16-7"></span>Xin Zhang, Dong Zhang, Shimin Li, Yaqian Zhou, and Xipeng Qiu. Speechtokenizer: Uni}ed speech tokenizer for speech large language models. *arXiv preprint arXiv:2308.16692*, 2023.
- <span id="page-16-2"></span>Alon Ziv, Sanyuan Chen, Andros Tjandra, Yossi Adi, Wei-Ning Hsu, and Bowen Shi. Mr- ~owdpo: Multi-reward direct preference optimization for ~ow-matching text-to-music generation, 2025. URL <https://arxiv.org/abs/2512.10264>.