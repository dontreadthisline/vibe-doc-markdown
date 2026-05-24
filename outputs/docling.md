## Voxtral 语⾳合成

<!-- image -->

## Abstract

我们介绍 Voxtral TTS ，这是⼀种富有表现⼒的多语⾔⽂本到语⾳模型，仅 需 3 秒的参考⾳频即可⽣成⾃然语⾳。 Voxtral TTS 采⽤混合架构，结合 了语义语⾳ token 的⾃回归⽣成与声学 token 的流匹配。这些 token 使 ⽤ Voxtral Codec 进⾏编码和解码，该语⾳分词器从零开始训练，采⽤混 合 VQ-FSQ 量化⽅案。在由母语者进⾏的⼈类评估中，由于其⾃然性和表 现⼒， Voxtral TTS 在多语⾔语⾳克隆⽅⾯更受青睐，相较于 ElevenLabs Flash v2.5 的胜率⾼达 68.4% 。 我们以 CC BY-NC 许可证发布该模型权重。

Webpage:

https://mistral.ai/news/voxtral-tts

Model weights:

https://huggingface.co/mistralai/Voxtral-4B-TTS-2603

Win Rate

图 1: Voxtral TTS 在⼈⼯评估中优于 ElevenLabs Flash v2.5 。 我们绘制了 Voxtral TTS 与 ElevenLabs Flash v2.5 在两类⼈⼯评估中的胜率。对于旗舰⾳⾊，我们使⽤各模型的默认⾳⾊以及 77 个不同的⽂本⽰例。在⾳⾊克隆设置中，我们提供⼀段简短的⾳频参考⽚段和 60 个⽂本提⽰。在两类 评估中，⼈⼯标注者会盲评两个模型之间的⾳频哪个更优。 Voxtral TTS 在 58.3% 和 68.4% 的实例 中更受青睐。

<!-- image -->

## 1 引⾔

⾃然且富有表现⼒的⽂本转语⾳（ TTS ）仍是灵活⼈机交互的核⼼，其应⽤涵盖虚拟助⼿、 有声读物和⽆障碍⼯具。尽管近期的神经⽹络 TTS 模型在语⾳可懂性⽅⾯表现优异，但在 zero-shot 语⾳情景下捕捉⼈类语⾳的细微差别与表现⼒仍是⼀个未解决的挑战。

最近的 zero-shot TTS 系统通常以从短语⾳提⽰中提取的离散语⾳ token 作为⽣成条件，从 ⽽实现对未见说话⼈的泛化以及在长序列上的⾃然合成 [Borsos et al., 2023, Wang et al., 2023] 。与此同时，扩散模型和基于流的模型在建模语⾳⽣成中的丰富声学变化⽅⾯表现出 ⾊ [Popov et al., 2021, Le et al., 2023] 。最近的语⾳编解码器表明，语⾳可以分解为低速率 语义流和更⾼速率的声学流 [Défossez et al., 2024] 。层次化⽣成器如 Moshi 已经利⽤这种结 构，采⽤时间 Transformer 对时间步进⾏建模，并使⽤深度 Transformer 对编解码器层级进 ⾏建模。然⽽，这些系统中的声学⽣成仍保持深度⽅向的⾃回归特性。对于 TTS 来说，这 就引出了⼀个问题：稠密的声学组件是否必须始终以⾃回归⽅式建模，或者是否可以通过⼀ 种条件连续模型更有效地⽣成？

在本⼯作中，我们提出了 Voxtral TTS ，这是⼀种基于表⽰感知混合架构的多语⾔ zero-shot ⽂本到语⾳系统。通过 Voxtral 编码器对语⾳提⽰进⾏分词，该编码器是⼀种低⽐特率语⾳ 分词器，包含经语⾳识别（ ASR ）蒸馏得到的语义 token 以及有限标量量化（ FSQ ）的声学 token [Mentzer et al., 2023] 。基于这种分解表⽰，仅解码器的 Transformer 模型⾃回归地预 测语义 token 序列，⽽⼀个轻量级的流匹配模型则根据解码器状态预测声学 token 。该设计 结合了⾃回归建模在长程⼀致性⽅⾯的优势与连续流匹配在丰富声学细节⽅⾯的优势。我们 通过将标准语义 token ⽣成偏好⽬标与基于流的声学预测偏好⽬标相结合，将直接偏好优化 （ DPO ） [Rafailov et al., 2023] 适配到这种离散 -连续混合设置中 [Ziv et al., 2025] 。

Voxtral TTS ⽀持 9 种语⾔，⽀持最短 3 秒的语⾳提⽰，并专为低延迟流式推理设计。在 SEED-TTS [Anastassiou et al., 2024] 和 MiniMax-TTS [Zhang et al., 2025] 的⾃动评估 中，其表现出优异的可懂性和⾃然度，在说话⼈相似度得分上超越 ElevenLabs v3 。在多语 ⾔ zero-shot 语⾳克隆的⼈类评估中，其胜率⾼达 68.4% ，优于 ElevenLabs Flash v2.5 ，同 时在富有表现⼒的旗舰语⾳评估中与强⼤的专有系统保持竞争⼒。

## 2 建模

图 2 展⽰了 Voxtral TTS 的架构。该架构包含⼀种新型⾳频编解码器-Voxtral 编解码 器--可将参考语⾳样本编码为由语义 token 和声学 token 组成的⾳频 token 。这些⾳频 token 与⽂本 token 结合，构成语⾔模型解码器主⼲的输⼊。为了⽣成语⾳，解码器主⼲逐 个⾃回归地⽣成语义 token 输出。⼀个流匹配 Transformer ⽤于⽣成声学 token 。编解码器 解码器将输出 token 映射为对应的⾳频波形。

## 2.1 Voxtral 编解码器

Voxtral 编解码器是⼀种卷积 -Transformer ⾃编码器 [Défossez et al., 2022] ，可将原始的 24 kHz 单声道波形压缩为每秒 12.5 Hz 的 37 个离散 token （ 1 个语义 + 36 个声学） ，总⽐ 特率为 2.14 kbps 。这些 token 作为 Voxtral TTS 的输⼊⾳频表⽰。通过⼀种新颖的架构与 训练⽬标改进组合， Voxtral 编解码器优于现有的基准模型如 Mimi [Défossez et al., 2024] ， 结果见第 4.1 节。

波形⾃编码器 受基于 Transformer 的⾳频编码器先前⼯作 [Parker et al., 2024, Wu et al., 2024] 的启发，我们的⾳频分词器作⽤于'分块化'的波形。 24 kHz 的单声道输⼊波形被分

<!-- image -->

图 2: Voxtral TTS 架构概览。 ⼀段长度为 3 秒⾄ 30 秒的语⾳参考输⼊到 Voxtral Codec 编码器 中，以获得帧率为 12.5 Hz 的⾳频 token 。每个⾳频帧（标注为 A ）包含⼀个语义 token 和声学 token 。 语⾳参考的⾳频 token 与⽂本提⽰ token （标注为 T ）⼀同输⼊到解码器主⼲⽹络中。解码器⾃回归 地⽣成⼀串语义 token ，直到遇到特殊的⾳频结束 token （ &lt;EOA&gt; ） 。在每个时间步，解码器主⼲⽹ 络输出的语义 token 被送⼊⼀个流匹配 Transformer ，该模块多次运⾏以预测声学 token 。最终，语 义 token 和声学 token 被输⼊到 Voxtral Codec 解码器中，⽣成⽬标波形。

割为不重叠的 240 样本块，从⽽得到编码器的 100 Hz 输⼊。这些 100 Hz 的输⼊帧⾸先通 过核⼤⼩为 7 的因果卷积投影到 1024 维嵌⼊，然后经过 4 个编码器块，每个块包含：

- ⼀个 2 层的因果⾃注意⼒ Transformer ，采⽤滑动窗⼝注意⼒（窗⼝⼤⼩为 16 → 8 → 4 → 2 ，在每个下采样阶段减半） ， ALiBi 位置偏置 [Press et al., 2021] ， QK 范 数，以及初始值为 0.01 的 LayerScale [Touvron et al., 2021] 。
- ⼀个因果卷积神经⽹络层。在前三个块中，卷积神经⽹络通过 2 × 下采样（步幅为 2 ） ，从 100 Hz 到 12.5 Hz 累计减少了 8 × 。在第四个块中，卷积神经⽹络的步幅为 1 ，并将 1024 维的表⽰投影到 292 维的潜在空间。

292 维的潜在表⽰随后被量化为⾳频 token （详情见下⽂） 。 解码器以相反顺序模仿编码器： ⾸ 先通过⼀个因果卷积神经⽹络将 292 维的潜在表⽰映射回 1024 维，接着经过 4 个块，每个 块包含⼀个转置卷积神经⽹络（⽤于 2 × 上采样）和⼀个两层的因果⾃注意⼒ Transformer ， 逐步将 12.5 Hz 的潜在表⽰恢复⾄ 100 Hz 。最后，⼀个核⼤⼩为 7 的因果卷积将 1024 维映 射回 240 样本的块⼤⼩，以重建波形。

表⽰量化。 292 维的潜在变量被拆分为⼀个 256 维的 语义 分量和⼀个 36 维的 声学 分量， 这两个分量分别独⽴进⾏量化：

图 3: Voxtral Codec 的架构概览与训练。 它包含⼀个分离的语义 VQ 编码字典和声学 FSQ 编码 字典。语义 token 和声学 token ⼀同⽤于重构。语义 token 还从监督的 ASR 模型中获得额外的蒸馏 损失。

<!-- image -->

- 语义组件通过⼀个学成的向量量化器（ VQ ； [Van Den Oord et al., 2017] ）进⾏量 化，码本⼤⼩为 8192 。在训练过程中，以 50% 的概率应⽤ VQ ；其余样本则未经量 化直接通过。
- 每个 36 个声学维度的信号都经过⼀个 tanh 激活，并通过有限标量量化（ FSQ ； [Mentzer et al., 2023] ）独⽴地量化为 21 个均匀等级。在训练过程中，我们采⽤ 类似抖动的 FSQ [Parker et al., 2024] ： 50% 的样本使⽤ FSQ 进⾏量化， 25% 的样 本添加幅度为 1/ L 的均匀噪声（其中 L =21 为等级数） ，另有 25% 的样本不经过量 化直接通过。

总⽐特率为 12 . 5 × ( log 2 8192 + 36 × log 2 21) ≈ 2 . 14 kbps 。

语义 token 学习 为了更好地将语⾳的语义内容融⼊语义 token 中， 我们采⽤了⼀种辅助的 ASR 蒸馏损失。与之前通过蒸馏⾃监督语⾳表⽰来学习'语义' token 的⽅法不同 [Zhang et al., 2023, Défossez et al., 2024] ，这些表⽰更偏向于 语⾳ ⽽⾮语义 [Liu et al., 2024] ， 我们从⼀个监督式 ASR 模型中进⾏蒸馏。研究表明，这种⽅法能够⽣成更有效的语义表 ⽰ [Vashishth et al., 2024] 。

⼀个冻结的 Whisper [Radford et al., 2023] 模型在输⼊⾳频上以⾃回归⽅式运⾏，⽣成解码 器隐状态和交叉注意⼒权重。后置 VQ 的语义嵌⼊被线性投影以匹配 Whisper 的隐状态维 度，然后使⽤余弦距离损失与最后⼀层解码器的隐状态对齐：

<!-- formula-not-decoded -->

其中， z f 是在编码器帧 f 处经过投影的后 VQ 语义嵌⼊， h l 是 Whisper 在 token 位置 l 处 的最末层解码器隐状态，⽽ A ∈ R L × F 是通过动态时间规整（ DTW ） [Berndt and Clizord, 1994] 识别出与词级时间戳相关性最强的⼀组 Whisper 交叉注意⼒头所导出的软对齐矩阵。 为了计算 A ，这些头的交叉注意⼒权重在解码器 token 维度上进⾏规范化，经中值滤波后在

头之间取平均。得到的矩阵沿编码器帧轴进⾏线性插值，以匹配编码器帧率（ 12.5 Hz ） ，因 此 ˜ z l 是与第 l 个解码器 token 对齐的编码器嵌⼊的注意⼒加权和。

该设计使分词器能够在⽆需外部强制对齐⼯具或配对转录⽂本的情况下，学习与⽂本对齐的 语义 token ，因为对齐信息是通过 Whisper 的交叉注意⼒权重隐式推导得出的。从连续隐状 态中提炼信息，⽽⾮依赖硬性转录标签，能够提供更丰富的监督信号，包括模型置信度和语 ⾳相似性。

对抗训练 ⼀个具有 8 个 STFT ⼤⼩（ 2296, 1418, 876, 542, 334, 206, 126, 76 ）的多分辨率 判别器与编码器⼀同训练。每个判别器作为⼆分类器，使⽤铰链损失在真实⾳频 x 和重建 ⾳频 ˆ x 之间进⾏训练。在每个判别器的每⼀层活性值上计算基于 L 1 的特征匹配损失：

<!-- formula-not-decoded -->

此处， D m n 表⽰第 n 个判别器的第 m 层，其中每个 N 个判别器均具有 M 层。根据 Défossez et al. [2024], Parker et al. [2024] ，我们使⽤该特征匹配损失 替代 标准 GAN ⽣成器损失，因 为不断演化的判别器特征在整个训练过程中提供了越来越具有区分性的重构信号。

训练⽬标。 Voxtral 编码器以端到端⽅式训练，使⽤以下损失函数：

<!-- formula-not-decoded -->

其中 α =1 . 0 ， β =1 . 0 ， γ =0 . 9999 t （ t 为当前训练步骤） ，以及 δ =0 . 1 。 L L1 是原始波形与 重构波形之间的 L 1 距离， L STFT 是其短时傅⾥叶变换（ STFT ）幅度上的 L 1 损失。两种 重构损失共享相同的指数衰减调度 γ ，该调度在训练初期促进学习，并随着对抗信号的增 强⽽逐渐减弱其影响 [Parker et al., 2024] 。 L commit = ‖ z e -sg ( z q ) ‖ 2 2 是向量量化（ VQ ）承 诺损失 [Van Den Oord et al., 2017] ，其中 sg 表⽰停⽌梯度操作符。

表 1 给出了 Voxtral Codec 配置的概要。该完整模型⼤约有 300M 个参数。所有决策均经过 消融实验，最终配置在最优化⽅⾯表现稳定，并达到了最佳⾳质。

## 2.2 解码器⾻⼲⽹络

Voxtral TTS 的解码器主⼲遵循 Ministral 3B [Liu et al., 2026] 的架构，⼀个⾃回归的仅解 码器 Transformer 。输⼊序列由语⾳参考⾳频 token 和⽂本 token 组成，输出⾳频 token 由 此⾃回归⽣成。每个⾳频帧由 37 个离散 token 表⽰（ 1 个语义， 36 个声学） 。每个码本都有 其独⽴的嵌⼊查找表（语义码本为 8192 项，每个声学码本为 21 项） ，这些查找表的嵌⼊值 相加后⽣成每个⾳频帧的单⼀嵌⼊。

解码器主⼲⽣成⼀系列隐状态。线性头部将每个隐状态 h 投影到语义码本词表（ 8192 个条 ⽬加上⼀个特殊的⾳频结束 ( &lt;EOA&gt; ) token ）的 Logit 值上，使⽤标准交叉熵损失进⾏训 练。为了预测声学 token ， h 被输⼊到⼀个流匹配 Transformer 中，其描述见第 2.3 节。流匹 配 Transformer 的浮点输出在进⼊下⼀步⾃回归处理前被离散化，以保持完全离散的 token 接⼝。

## 2.3 流匹配 Transformer

为了预测声学 token ，流匹配（ FM ） Transformer 在解码器主⼲中每个⽣成步骤的隐状态 h 上独⽴运⾏。我们将在连续空间中建模声学 token 以利⽤ FM 的平滑速度场，并仅在输出 时进⾏离散化，以与⾃回归主⼲的离散 token 词表对接。

表 1: Voxtral 编解码器的关键超参数。

| Parameter                                    | Value                                   |
|----------------------------------------------|-----------------------------------------|
| Input / Preprocessing                        |                                         |
| Sampling rate                                | 24000                                   |
| Patch size                                   | 240                                     |
| AutoEncoder                                  |                                         |
| Encoder patch projection kernel size         | 7                                       |
| Encoder patch projection dimension           | 1024                                    |
| Encoder transformer layers 1                 | 2 → 2 → 2 → 2                           |
| Encoder sliding window size                  | 16 → 8 → 4 → 2                          |
| Encoder conv kernels                         | 4 → 4 → 4 → 3                           |
| Encoder conv strides                         | 2 → 2 → 2 → 1                           |
| (Decoder ~ips all → to ← and uses transposed | convolutions)                           |
| Discrete bottleneck                          |                                         |
| Semantic VQ 2 codebook size                  | 8192                                    |
| Acoustic FSQ 3 codebook count × size         | 36 × 21                                 |
| Discriminator                                |                                         |
| FFT sizes                                    | 2296, 1418, 876, 542, 334, 206, 126, 76 |
| Channels                                     | 256                                     |

FM Transformer 由⼀个双向的三层 Transformer 组成，其宽度与解码器主⼲⽹络相同。它 建模了将⾼斯噪声 ( x 0 ) 传输到声学嵌⼊ ( x 1 ) 的速度场，该过程通过⼀系列函数评估步骤 0 ≤ t ≤ 1 完成。它接收以下输⼊： h ，当前的函数评估步骤 t （编码为正弦嵌⼊） ，以及当 前的声学嵌⼊ x t ∈ R 36 。我们为每个输⼊ h 、 t 和 x t 使⽤独⽴的投影层，因为它们的活性 值尺度不同。我们还对使⽤ DiT 风格的⾃适应 LayerNorm (AdaLN) 层进⾏条件控制进⾏ 了消融实验 [Peebles and Xie, 2023] ，但发现我们的⽅法更优。

训练期间，对于'⽆条件'建模，隐状态有 10% 的概率被丢弃。在推理阶段，我们使⽤欧拉 ⽅法对速度向量场 v t 进⾏积分，共进⾏ 8 次函数求值（ NFEs ） ， 并采⽤⽆分类器引导（ CFG ） [Ho and Salimans, 2022] 。具体⽽⾔， v t 和 x t 的形式为：

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

，其中 h 为解码器主⼲⽹络的隐状态， ∅ 为⽆条件情况，即我们传递⼀个与 h 形状相同的零 向量。 v θ ( x t , t, h ) 为在时间步 t 时预测的速度场，样本 x t 以及条件输⼊ h 。我们根据第 5.2 节中的分析设定 ∆ t = 1/8 和 α = 1 . 2 。

注意，在我们的架构中， CFG 在 FM Transformer 的每⼀帧上独⽴应⽤。因此，它仅需额 外进⾏⼀次 FM Transformer 的前向传播，相⽐在解码器主⼲中应⽤ CFG 要显著便宜。由 FM Transformer 预测的浮点值通过量化⾄ 21 个 FSQ 级别转换为离散整数值。这些离散化 的 token 将作为输⼊提供给下⼀解码步骤中的解码器主⼲。

由于解码器主⼲⽹络的输⼊是经过嵌⼊查找的离散 token ，我们还考虑了受 MaskGIT [Chang et al., 2022] 和 Depth Transformer [Défossez et al., 2024] 启发的替代架构。这两 种⽅法表现尚可，但在⼈类评估中仍不如 FM ，尤其是在表现⼒⽅⾯。此外， MaskGIT 需 要对全部 36 个声学码本位置和条件 token 进⾏注意⼒计算，导致每帧的序列长度为 38 ，⽽ FM Transformer 仅需 3 个（ h , t , x t ） 。 类似地， Depth Transformer 需要 36 步⾃回归解码， ⽽ FM 仅需 8 次⾮⾃回归求解步骤（ NFE ） 。 因此， FM 在质量、计算量和延迟⽅⾯均更优。

## 3 训练

## 3.1 预训练

我们使⽤经过 Voxtral Mini Transcribe [Liu et al., 2025] 伪标记的配对⾳频和转录⽂本对来 训练模型。每个训练样本由⼀个元组 ( A 1 , T 2 , A 2 ) 组成，其中 A 1 为语⾳参考， T 2 为 A 2 的 转录⽂本，这是我们⽣成的⽬标。与 Voxtral 类似，我们在 A 1 与 T 2 之间插⼊⼀个 &lt;next&gt; 特殊 token ，在 T 2 与 A 2 之间插⼊⼀个 &lt;repeat&gt; 特殊 token 。我们确保 A 1 与 A 2 来⾃同 ⼀说话⼈且为单说话⼈⽚段，但不⼀定在时间上相邻。 A 1 与 A 2 的最⼤时长为 180 秒，且 我们确保 A 1 ⾄少为 1 秒长。由于⾃然对话中⼈类语⾳持续时间具有长尾分布特性，我们 发现模型在 3 ⾄ 25 秒之间的语⾳提⽰（ A 1 ）上表现最佳。

损失仅在 A 2 的 token 上计算。我们使⽤由两部分组成的损失函数来优化模型，其中包括在 语义 token L semantic 上的交叉熵损失以及在声学 token 上的 ~ow-matching 损失 L acoustic 。 我们采⽤如下的简单条件 ~ow-matching ⽬标：

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

其中 u t 为⽬标条件速度， v θ 为 FM Transformer 预测的速度， x 1 从正态分布中采样得到， x 0 为数据分布 D 。我们使⽤ Ministral 3B 初始化解码器主⼲⽹络。新引⼊的模块，如 FM Transformer 、⾳频代码本嵌⼊查找表和输出投影层，均进⾏随机初始化。在训练过程中， 我们冻结解码器主⼲中的⽂本嵌⼊层，以提⾼对 Voxtral Mini Transcribe 转录中低频出现 的⽂本 token 的鲁棒性。为避免对静⾳部分过拟合，我们还对语⾳活动检测（ VAD ）模型 判定⽆语⾳的帧采⽤较低的损失权重，并将极长静⾳段的损失权重设为 0 。此外，我们还对 转录⽂本进⾏简单的基于⼤语⾔模型的重写，以增强对规范化的与⾮规范化的⽂本（例如 ' 5 - 4 '与' }ve minus four ' ）的鲁棒性。

## 3.2 直接偏好最优化

我们使⽤直接偏好优化（ DPO ） [Rafailov et al., 2023] 对模型进⾏后训练，重点关注提升词 错误率（ WER ）和说话⼈相似度。对于语义码本，我们采⽤标准的 DPO ⽬标。鉴于声学码 本是通过流匹配预测的，我们将⽬标函数从 Ziv et al. [2025] 进⾏调整：

<!-- formula-not-decoded -->

其中

<!-- formula-not-decoded -->

我们通过计算使⽬标适⽤于我们的⾃回归设置（注意加粗的 t 表⽰每个 token 都有不同的采 样 t ） ，从⽽实现：

<!-- formula-not-decoded -->

发现长度规范化（除以获胜者的长度）会导致不稳定性。

我们确保在序列的每个位置采样的 t 和 x 0 对策略模型 θ 和参考模型 θ ref 保持⼀致。两个 DPO 损失以均匀权重相加，但由于训练对 ~ow-DPO 损失敏感，我们使⽤了 β semantic = 0 . 1 和 β acoustic = 0 . 5 。为保证训练稳定性，采⽤较低的学习率 8 e -8 。

DPO 的数据通过拒绝采样流⽔线收集，该流⽔线以⼀组保留的单说话⼈语⾳样本和多样化 的合成⽂本提⽰作为输⼊。我们使⽤ Mistral Small Creative 进⾏提⽰。 1 使⽤语⾳提⽰的 转录⽂本和随机选择的⼈物设定，合成⼀系列多样化的⽂本，以延续或回应对话上下⽂。随 后，预训练检查点将语⾳和⽂本提⽰作为输⼊，从每个输⼊⽣成多个样本，从中可构建出胜 者与败者配对。胜者与败者通过字错误率（ WER ） 、说话⼈相似度、⾳量⼀致性、 UTMOSv2 [Baba et al., 2024] 以及其他语⾔模型评判指标来确定。我们使⽤结合了 DPO 损失和⾼ 质量语⾳上的预训练⽬标，在 1 轮次内优化模型，因为我们发现，在合成数据上进⾏更长时 间的训练会导致语⾳更加机械化。

## 4 结果

## 4.1 Voxtral 编解码器

表 2 展⽰了在 Expresso 数据集 [Nguyen et al., 2023] 上 Voxtral Codec 与 Mimi 的对⽐。我 们评估了以下⽬标指标：梅尔距离、 STFT 距离、语⾳质量感知评价（ PESQ ） 、扩展短时客 观可懂度（ ESTOI ） 、使⽤对应源⾳频和重构⾳频的⾃动语⾳识别模型⽣成的转录⽂本之间 的词错误率（ ASR-WER ） ， 以及使⽤说话⼈嵌⼊模型计算的说话⼈相似度得分。我们还报告 了⽐特率和每秒帧数（ fps ） ，这些指标在⾃回归解码器模型的应⽤场景中具有相关性。由于 Mimi 采⽤ RVQ 设计的声学码本，因此可以选择⼦集码本以权衡⽐特率与质量。当 Voxtral Codec 与 Mimi 在 16 个码本配置下进⾏⽐较，使得⽐特率相近时， Voxtral Codec 在所有 ⽬标指标上均表现更优。在内部主观评估中，我们发现对于以语⾳为主要关注内容的⾳频， Voxtral Codec 在 16 个码本配置下的表现与 Mimi 相当或更优。

表 2: Voxtral 编解码器与 Mimi 在 Expresso 数据集上的对⽐。

| Model              | fps   | token/frame × vocab. size   | bitrate   | Reconstruction ( ↓ )   | Reconstruction ( ↓ )   | Intrusive ( ↑ )   | Intrusive ( ↑ )   | Perceptual   | Perceptual    |
|--------------------|-------|-----------------------------|-----------|------------------------|------------------------|-------------------|-------------------|--------------|---------------|
| Model              | fps   | token/frame × vocab. size   | (kbps)    | Mel                    | STFT                   | PESQ              | ESTOI             | ASR-WER (%)  | Speaker Sim ↑ |
| Mimi - 8cb (Moshi) | 12.5  | 8 × (2048)                  | 1.1       | 0.702                  | 1.177                  | 2.07              | 0.803             | 11.75        | 0.672         |
| Mimi - 16cb        | 12.5  | 16 × (2048)                 | 2.2       | 0.618                  | 1.100                  | 2.67              | 0.865             | 11.01        | 0.829         |
| Mimi - full 32cb   | 12.5  | 32 × (2048)                 | 4.4       | 0.552                  | 1.040                  | 3.18              | 0.910             | 10.25        | 0.902         |
| Voxtral Codec      | 12.5  | 1 × (8192) + 36 × (21)      | 2.1       | 0.545                  | 0.982                  | 3.05              | 0.882             | 10.66        | 0.843         |

## 4.2 ⾃动评估

我们使⽤⾃动化指标对 Voxtral TTS 、 ElevenLabs v3 和 ElevenLabs Flash v2.5 在 SEEDTTS [Anastassiou et al., 2024] 以及 MiniMax-TTS [Zhang et al., 2025] 中⽀持的九种语⾔ 进⾏评估：

[1 https://docs.mistral.ai/models/mistral-small-creative-25-12](https://docs.mistral.ai/models/mistral-small-creative-25-12)

1. 字错误率（ WER ） ：通过 Voxtral Mini 转录 v2 测量，以捕捉语⾳的可理解性。
2. UTMOS-v2 [Baba et al., 2024] ：预测⽣成语⾳的平均意见得分（ MOS ） 。
3. 说话⼈相似度 : 使⽤ ECAPA-TDNN 模型 [Desplanques et al., 2020] 预测说话⼈嵌 ⼊，并与参考嵌⼊计算余弦相似度。这评估了⽣成语⾳与提供的语⾳参考的相似度。

三种模型的结果如表 3 所⽰。 尽管两个 ElevenLabs 模型在各类语⾔中均实现了较低的 WER ， 但 Voxtral TTS 在说话⼈相似度指标上显著优于 ElevenLabs 。令⼈意外的是，我们发现 ElevenLabs Flash v2.5 在⼤多数⾃动评估指标上表现更佳，⽽ ElevenLabs v3 在⼈⼯评估中 表现更优，尤其是在情感控制⽅⾯。这凸显了结合⼈⼯评估与⾃动评估的重要性。

表 3: Voxtral TTS 、 ElevenLabs v3 和 ElevenLabs Flash v2.5 的 WER 、 UTMOS 及说话⼈相似度 得分。

|            | WER (%) ↓   | WER (%) ↓     | WER (%) ↓        | UTMOS ↑   | UTMOS ↑       | UTMOS ↑          | Speaker Sim ↑   | Speaker Sim ↑   | Speaker Sim ↑    |
|------------|-------------|---------------|------------------|-----------|---------------|------------------|-----------------|-----------------|------------------|
| Task       | Voxtral     | ElevenLabs v3 | ElevenLabs Flash | Voxtral   | ElevenLabs v3 | ElevenLabs Flash | Voxtral         | ElevenLabs v3   | ElevenLabs Flash |
| MiniMax    |             |               |                  |           |               |                  |                 |                 |                  |
| Arabic     | 2.68        | 3.67          | 2.86             | 3.07      | 2.50          | 2.89             | 0.746           | 0.546           | 0.539            |
| German     | 0.83        | 0.45          | 1.08             | 3.12      | 2.90          | 3.27             | 0.721           | 0.457           | 0.489            |
| English    | 0.63        | 0.48          | 0.33             | 4.30      | 4.27          | 4.27             | 0.786           | 0.484           | 0.489            |
| Spanish    | 0.51        | 0.87          | 0.49             | 3.41      | 3.18          | 2.99             | 0.762           | 0.443           | 0.541            |
| French     | 3.22        | 2.34          | 2.26             | 2.83      | 2.90          | 2.94             | 0.587           | 0.339           | 0.378            |
| Hindi      | 4.99        | 8.71          | 5.08             | 3.56      | 3.56          | 3.35             | 0.839           | 0.707           | 0.679            |
| Italian    | 1.32        | 0.58          | 0.55             | 3.43      | 3.08          | 3.09             | 0.739           | 0.527           | 0.485            |
| Dutch      | 1.99        | 1.52          | 0.83             | 3.89      | 3.53          | 3.68             | 0.720           | 0.397           | 0.598            |
| Portuguese | 1.02        | 0.92          | 1.15             | 3.66      | 3.41          | 3.41             | 0.785           | 0.571           | 0.642            |
| Seed TTS   | 1.23        | 1.26          | 0.86             | 4.11      | 3.92          | 4.09             | 0.628           | 0.392           | 0.413            |

## 4.3 ⼈为评估

⾃动化指标⽆法衡量语⾳合成模型的⾃然度和表现⼒，尤其是模型表达特定情感的能⼒。我 们发现 UTMOS 仅是⼀个松散的代理指标，在不同语⾔间校准不佳，且与⼈类偏好相关性 较弱。因此，我们进⾏了两组⼈⼯评估，标注者在不知晓模型⾝份的情况下⽐较两个模型⽣ 成的结果。评估共包含 77 个提⽰语，其中 11 个为中性提⽰， 66 个带有预期情感。所有评 估中，标注者被要求判断其中⼀个⽣成结果是'稍好' 、 '明显更好' ，还是'两者都好'或 '两者都差' 。在标注过程中，所有⾳频样本均重采样为 24 kHz 的 WAV 格式（包括参考样 本） ，以确保不会因⾳频质量产⽣偏差。

## 4.3.1 旗舰声⾳

⾸先，我们将我们的旗舰语⾳（英国⼥性、英国男性、美国男性、法国⼥性）与竞争对⼿提 供的同性别和同⼝⾳的旗舰语⾳进⾏对⽐。我们进⾏了两次⼦评估：

1. 显式引导 ：我们测试了将语⾳合成模型的⽣成结果偏向特定情感的能⼒。对于带有 相关情感（⾮中性）的语⾳合成提⽰，我们以⾃由格式指令的形式提供给 Gemini 2.5 Flash TTS ，因其⽀持⾃由格式指令，例如'⽤愤怒的语调说话' 。对于 ElevenLabs v3 ，我们则提供括号包裹的情感标签 2 . 虽然 Voxtral TTS 不⽀持情感标签 / ⽂本指 令，但我们通过利⽤同⼀说话⼈提供的、体现所需情感的另⼀语⾳提⽰来引导⽣成。
2. 隐式引导 : 我们测试模型从给定⽂本中推断情感的能⼒（例如： '这是我⼀⽣中最美 好的⼀天！ ' ） 。不会向模型提供任何情感标签或指令。对于 Voxtral TTS ，我们使⽤ 中性语⾳提⽰。

2 https://elevenlabs.io/blog/eleven-v3-audio-tags-expressing-emotional-context-i n-speech

我们为每种语⾔的每⼀对使⽤三位同⽅⾔的母语者作为标注者。 表 4 展⽰了 Voxtral TTS （不 包括平局） 的胜率。 Gemini 2.5 Flash TTS 是表现最强的模型， ⽽ Voxtral TTS 与 ElevenLabs v3 相⽐具有竞争⼒。在隐式引导设置下， Voxtral TTS 始终优于两个 ElevenLabs 模型。

表 4: Voxtral TTS 在不同控制类型下的胜率。 在显式控制情景下， Voxtral TTS 与 ElevenLabs v3 相当，⽽在隐式控制情景下，其胜率⾼于两个 ElevenLabs 模型。

| Emotion steering   | Opponent Model                                           | Voxtral TTS Win Rate (%)   |
|--------------------|----------------------------------------------------------|----------------------------|
| Explicit           | ElevenLabs v3 Gemini 2.5 Flash TTS                       | 51.0 35.4                  |
| Implicit           | ElevenLabs Flash v2.5 ElevenLabs v3 Gemini 2.5 Flash TTS | 58.3 55.4 37.1             |

## 4.3.2 Zero-shot 语⾳克隆

为评估语⾳克隆能⼒，我们在每种语⾔中选取两位知名演讲者的⾼质量⾳频作为⾳源。在 zero-shot 情景下，从每个模型⽣成语⾳，并指⽰标注⼈员根据（ a ）⽣成⾳频与语⾳提⽰的 相似度以及（ b ）语⾳的⾃然度和表现⼒对⽣成结果进⾏评分。

表 5: Voxtral TTS 在各语⾔上对 ElevenLabs Flash v2.5 的胜率。 Voxtral TTS 在每种语⾔上 的表现均达到或超过 ElevenLabs Flash v2.5 ，整体微平均胜率为 68.4% 。

| Language   |   Voxtral TTS Win Rate (%) |
|------------|----------------------------|
| Arabic     |                       72.9 |
| Dutch      |                       49.4 |
| English    |                       60.8 |
| French     |                       54.4 |
| German     |                       72.0 |
| Hindi      |                       79.8 |
| Italian    |                       57.1 |
| Portuguese |                       74.4 |
| Spanish    |                       87.8 |
| Overall    |                       68.4 |

表 5 展⽰了 Voxtral TTS 在不同语⾔下对 ElevenLabs Flash v2.5 的胜率。 总体⽽⾔， Voxtral TTS 的胜率为 68.4% ，在⾼资源和低资源语⾔（如阿拉伯语和印地语）中均表现出显著更优 的结果。值得注意的是， Voxtral TTS 在 zero-shot 情景下的胜率（ 68.4% ）远⾼于旗舰语⾳ （ 58.3% ） ，突显出 Voxtral TTS 是⼀个更具泛化能⼒的模型，能够捕捉多样化的⽤户语⾳特 征。

## 5 分析

在本节中，我们对预训练模型和 DPO 检查点进⾏了⽐较，并对相关的推理参数进⾏了消融 实验。

## 5.1 DPO 优化

表 6 展⽰了预训练模型和 DPO 检查点的 WER 与 UTMOS 指标。总体⽽⾔， DPO 在两 项指标上均有所提升，其中德语和法语的提升最为显著，⽽印地语则出现下降。定性分析发 现， DPO 模型的幻觉现象更少，漏读单词的情况也更少。此外， DPO 还缓解了预训练模型 在⾳频播放过程中⾳量明显衰减的偶发倾向。有趣的是， DPO 对说话⼈相似度的影响极⼩， 其值与预训练检查点相差不超过 ± 0 . 01 （为简洁起见，此处未展⽰） 。

表 6: DPO 在多种语⾔中均提升了 WER 和 UTMOS 。

|            | WER (%) ↓   |   WER (%) ↓ | WER (%) ↓   | UTMOS ↑   |   UTMOS ↑ | UTMOS ↑   |
|------------|-------------|-------------|-------------|-----------|-----------|-----------|
| Task       | Pretrain    |             | DPO         | Pretrain  |           | DPO       |
| MiniMax    |             |             |             |           |           |           |
| Arabic     | 2.80        |        2.68 | (-0.12)     | 3.01      |      3.07 | (+0.06)   |
| German     | 4.08        |        0.83 | (-3.25)     | 3.05      |      3.12 | (+0.07)   |
| English    | 0.84        |        0.63 | (-0.21)     | 4.25      |      4.30 | (+0.05)   |
| Spanish    | 0.56        |        0.51 | (-0.06)     | 3.38      |      3.41 | (+0.04)   |
| French     | 5.01        |        3.22 | (-1.79)     | 2.76      |      2.83 | (+0.07)   |
| Hindi      | 3.39        |        4.99 | (+1.61)     | 3.43      |      3.56 | (+0.13)   |
| Italian    | 2.18        |        1.32 | (-0.85)     | 3.36      |      3.43 | (+0.07)   |
| Dutch      | 3.10        |        1.99 | (-1.11)     | 3.85      |      3.89 | (+0.04)   |
| Portuguese | 1.17        |        1.02 | (-0.15)     | 3.60      |      3.66 | (+0.06)   |
| Seed TTS   | 1.58        |        1.23 | (-0.35)     | 4.07      |      4.11 | (+0.04)   |

## 5.2 推理参数

图 4 展⽰了在功能评估次数（ NFEs ）和 CFG α 选择变化时，⾃动评估指标的影响。当 NFEs 从 2 增加到 8 时，各项指标均有显著提升。我们发现，将 NFEs 进⼀步增加⾄ 8 以上对说 话⼈相似度的提升效果微乎其微，且在词错误率（ WER ）上出现轻微下降。因此，我们将 8 个 NFEs 作为默认的推理设置。

增⼤ CFG α 的值，我们发现除 UTMOS-v2 外，所有指标均呈现近乎单调的提升。然⽽，内 部⼈⼯评估发现，较⾼的 α 会导致模型过度遵循提供的语⾳提⽰，⽆法对⽂本提⽰中隐含 的情感进⾏合理偏向。此外，我们还发现较低的 α = 1 . 2 在⾼质量⾳频（如专业录⾳）上表 现最佳，⽽野外录制的⾳频可能从较⾼的 α 中受益。

## 6 vLLM-Omni 中的推理与服务

Voxtral TTS 通过 vLLM-Omni [Yin et al., 2026] 提供服务，这是针对多阶段多模态模型的 vLLM [Kwon et al., 2023] 扩展。 Voxtral TTS 被分解为两阶段流⽔线：第⼀阶段为⽣成阶 段，预测⾳频 token （语义和声学） ，随后是编码器解码阶段，将 token 转换为波形。两个阶 段通过共享内存上的异步分块流协议进⾏通信，实现在完整波形⽣成之前即可实现⾸个⾳频 输出的低延迟。

)

WER (

## Effect of NFEs

图 4: NFEs 和 CFG 对⾃动评估的影响。 指标在 SEED-TTS 和 MiniMax 中的 9 种语⾔上取平均 值。将 NFEs 从 2 增加到 8 可以提升说话⼈相似度和 UTMOS 指标。当 NFEs 超过此值时， WER 指标略有下降。随着 CFG 值提⾼，各项指标单调上升，但⼈⼯评估指出，在⾼ α 情况下存在⽂本⼀ 致性下降的问题。

<!-- image -->

## 6.1 ⽤于流匹配 Transformer 的 CUDA 图加速

⽣成阶段的流匹配 Transformer 是计算瓶颈。每个解码步骤在使⽤ CFG 时需要 N 次函数 求值，每⽣成⼀帧需进⾏ 2 × N 次前向传播。

为消除 Python 层开销和内核启动延迟，整个常微分⽅程求解器被捕捉为 CUDA 图。在启 动时，会对每个桶的⼤⼩执⾏⼀次即时预热遍历，并相应地捕捉 CUDA 图。在推理过程中， 实际批量⼤⼩会被向上舍⼊到最近的桶⼤⼩，通过⽤零填充输⼊实现。接着，重放 CUDA 图，并将输出切⽚回实际批量⼤⼩。如果批量⼤⼩超过已捕捉的最⼤桶⼤⼩，则模型退回到 即时执⾏模式。

为了评估 CUDA 图加速的效果，我们对⽐了在急切模式（ eager mode ）和 CUDA 图下解码 时的延迟和实时因⼦（ RTF ） 。表 7 报告了在单个 H200 上，输⼊ 500 个字符⽂本、 10 秒 ⾳频参考以及并发数为 1 的情况下的结果。启⽤ CUDA 图后，延迟改善了 47% ，实时因⼦ （ RTF ）降低了 2.5 倍。

表 7: CUDA 图加速对流匹配 Transformer 的影响。

| Con}guration   | Latency   |   RTF |
|----------------|-----------|-------|
| Eager mode     | 133 ms    | 0.258 |
| CUDA graph     | 70 ms     | 0.103 |

## 6.2 异步分块流

两个流⽔线阶段在分离的调度环中运⾏。为了将⾃回归⽣成阶段的解码与编解码器解码阶段 的波形合成重叠，引⼊了⼀种异步分块流协议。

在每次⽣成步骤后， vLLM-Omni 传输管理器会将⾳频 token 存储到每个请求的缓冲区中。 当缓冲区长度达到预定义值时，便会将⼀段 token 发送到编解码器解码阶段。为了确保各段 之间的连贯性，每段输出都包含⼀部分先前的帧以及新⽣成的帧。这种重叠使得编解码器解 码器的因果滑动窗⼝注意⼒机制能够在段边界之间保持时间上的连贯性。

## 6.3 推理吞吐量

通过本节介绍的技术， Voxtral TTS 实现了低延迟、⾼通量的推理。表 8 展⽰了在单个 NVIDIA H200 上，从并发度 1 到 32 的服务性能，输⼊为 500 字符的⽂本和 10 秒的⾳ 频参考。当并发度从 1 增加到 32 时，吞吐量从每秒 119 字符提升⾄每 GPU 每秒 1,431 字 符，提升了 12 倍，⽽延迟始终保持在 1 秒以下。等待率（定义为客户端因等待输出⽽必须 停顿的⾳频块⽐例）在所有并发级别下均保持为零。随着并发度增加，每个请求的 RTF 在 并发度 32 时仅⼩幅上升⾄ 0.302 ，仍远低于实时边界。

这些结果表明， Voxtral TTS 适合⽤于⽣产环境部署：单个 H200 可以同时为超过 30 个⽤ 户提供不间断的流式输出，并实现亚秒级的⾸⾳频延迟。

表 8: Voxtral TTS 在单个 H200 上的推理性能。

|   Concurrency | Latency   |   RTF |   Throughput (char/s/GPU) | Wait Rate   |
|---------------|-----------|-------|---------------------------|-------------|
|             1 | 70 ms     | 0.103 |                    119.14 | 0%          |
|            16 | 331 ms    | 0.237 |                    879.11 | 0%          |
|            32 | 552 ms    | 0.302 |                   1430.78 | 0%          |

## 7 结论

我们介绍了 Voxtral TTS ， 这是⼀种多语⾔⽂本到语⾳模型， 采⽤混合架构实现语义 token 的 ⾃回归⽣成以及声学 token 的流匹配。这些 token 对应于 Voxtral Codec 中的 token ， Voxtral Codec 是⼀种语⾳分词器，结合了通过语⾳识别（ ASR ）蒸馏得到的语义 token 与⽮量量化 （ FSQ ）声学 token 。

Voxtral TTS 能够仅需 3 秒的参考⾳频即可⽣成富有表现⼒的语⾳克隆，且在⼈类评估中 优于 API 基准。我们以 CC BY-NC 许可证发布 Voxtral TTS 的开源权重，以⽀持更具表 现⼒的语⾳合成系统的研究与开发。

## 核⼼贡献者

刘弘毅、艾利克斯·塔克内、安迪·艾伦伯格、安迪·罗、孙晨佑、古斯塔夫·兰普尔、亨 利·拉加德、让 -马洛·德利尼翁、⾦载永、约翰·哈维尔、克亚提·拉加维·钱杜、洛伦佐· 西诺雷蒂、玛格丽特·詹宁斯、帕特⾥克·冯·普拉滕、帕万卡马尔·雷迪·穆迪雷迪、罗 欣·阿罗拉、桑奇特·⽢地、塞缪尔·休梅奥、索汉·⼽什、斯⾥詹·⽶什拉、范春。

## 贡献者们

阿⼘杜拉齐兹·布纳尔，阿⽐纳夫·拉斯特吉，阿德⾥安·萨德，艾伦·杰法雷斯，阿尔伯 特·江，亚历⼭⼤·卡希尔，亚历⼭⼤·加⽡丹，亚历⼭⼤·萨布雷洛，阿梅莉·埃利乌，阿 莫斯·尤，安德鲁·⽩，安德鲁·赵，安热勒·兰格莱梅茨，安莫尔·阿加⽡尔，安东·埃 利谢耶夫，安东尼娅·卡尔维，阿琼·马朱姆达尔，阿瑟·福尼耶，阿特约姆·乔森，阿维·

苏⾥亚拉奇，艾森努尔·卡拉杜曼·乌图尔，巴普蒂斯特·布，巴普蒂斯特·罗齐埃尔，鲍 杜因·德·莫尼克奥，本杰明·提⽐，鲍⽂·杨，夏洛特·克龙杰尔，克莱芒斯·兰弗朗奇， 康纳·陈，科伦坦·巴罗，科伦坦·索蒂埃，西普⾥安·库尔托，达⾥乌斯·达贝尔特，迭 ⼽·德拉斯卡萨斯，叶丽扎维塔·德⽶亚年科，埃利奥特·查内 -萨内，埃马纽埃尔·⼽特洛 布，昂格兰·帕昆，埃蒂安·⼽菲内，法⽐安·尼埃尔，法鲁克·艾哈迈德，费德⾥科·巴 尔达萨雷，加布⾥埃勒·贝拉达，盖坦·埃克雷庞，⼽蒂埃·古内，琴妮薇芙·海耶斯，乔 治·诺维科夫，吉达·⽪斯蒂利，古斯塔夫·昆什，古斯塔夫·马丁，古斯塔夫·雷亚尔，冈 詹·丹胡卡，贡希·古普塔，周汉，哈希尔·沙阿，霍普·麦⼽⽂，⾬果·蒂蒙尼耶，因德 拉尼尔·穆克赫吉，张伊蕾，贾克·孙，扬·卢德兹耶夫斯基，贾森·鲁特，杰雷⽶·丹坦， 乔阿基姆·施特尼亚，乔纳斯·阿玛，约瑟芬·德尔阿斯，乔塞尔·索默维尔·罗伯茨，朱 利安·陶兰，卡梅什·亚达夫，卡蒂克·坎德尔⽡尔，基利安·特普，库什·贾因，劳伦斯· 艾奇森，劳伦特·费因⾟，莱昂纳德·布利耶，赵凌霄，路易斯·马丁，露西尔·索尔尼耶， ⾼璐瑜，马滕·布伊尔，马南·夏尔马，玛丽·佩拉特，马克·普林斯，马蒂亚·亚历⼭⼤， 马蒂厄·波⾥，马蒂厄·施密特，马蒂尔德·吉利亚⽶，马蒂厄·迪诺，马蒂厄·富泰拉尔， 马克西姆·达林，马克斯⽶连·奥古斯丁，梅特·翁萨尔，⽶娅·奇基尔，⽶哈伊尔·⽐鲁 钦斯基，阮明光，⽶尔切亚·利卡，莫尔⽢·⾥维耶尔，内哈·古普塔，奥利维耶·布谢，奥 利维耶·杜尚，帕特⾥夏·王，保罗·雅各布，保罗·⽡姆贝格，保利娜·库⾥洛维奇，菲 利普·⽪奈尔，菲洛梅娜·尚尼亚，⽪埃尔·斯托克，⽪奥特尔·⽶洛斯，普拉泰克·古普 塔，普拉韦什·阿格拉⽡尔，昆汀·托罗巴，拉姆·拉姆拉克亚，兰德尔·伊斯恩豪尔，⾥ 希·沙阿，罗曼·索维斯特，罗曼·索列茨基，罗莎莉·⽶勒，鲁珀特·门尼尔，萨加尔·⽡ 泽，塞缪尔·巴⾥，塞缪尔·贝尔卡迪，桑迪普·苏布拉马尼亚，肖恩·查，沙夏⽡特·维 尔马，西德汉特·⽡格贾勒，锡德哈特·⽢地，西蒙·勒帕⽇，苏穆克·艾萨尔，西蒙·安 东尼亚克，塔鲁恩·库马尔·万加尼，特⽂·勒斯卡奥，让·卡歇，托马斯·西蒙·索尔格， 蒂博·拉夫⾥尔，托马斯·查巴尔，托马斯·富贝尔，托马斯·罗伯特，托马斯·王，蒂姆· 劳森，汤姆·贝威利，汤姆·爱德华兹，泰勒·王，乌马尔·贾⽶尔，翁贝托·托马西尼，⽡ 莱⾥亚·尼姆奇诺娃，维丹·南达，维克多·儒奥，⽂丁·李，威廉·哈⽡德，威廉·马歇 尔，李兴辉，郭兴然，杨欣宇，扬尼克·诺豪斯，亚⾟·埃尔奥⽡希迪，亚西尔·本杜，王 ⼀涵，潘⼀⽊，扎克查⾥·拉姆齐，许振林

## 7.1 致谢

我们感谢 vLLM-Omni 团队的⾼晗、刘洪胜、王睿和林悦千在将 Voxtral TTS 集成到 vLLMOmni 框架过程中提供的⽀持与贡献。

## 参考⽂献

- Philip Anastassiou, Jiawei Chen, Jitong Chen, Yuanzhe Chen, Zhuo Chen, Ziyi Chen, Jian Cong, Lelai Deng, Chuang Ding, Lu Gao, Mingqing Gong, Peisong Huang, Qingqing Huang, Zhiying Huang, Yuanyuan Huo, Dongya Jia, Chumin Li, Feiya Li, Hui Li, Jiaxin Li, Xiaoyang Li, Xingxing Li, Lin Liu, Shouda Liu, Sichao Liu, Xudong Liu, Yuchen Liu, Zhengxi Liu, Lu Lu, Junjie Pan, Xin Wang, Yuping Wang, Yuxuan Wang, Zhengnan Wei, Jian Wu, Chao Yao, Yifeng Yang, Yuanhao Yi, Junteng Zhang, Qidi Zhang, Shuo Zhang, Wenjie Zhang, Yang Zhang, Zilin Zhao, Dejian Zhong, and Xiaobin Zhuang. Seed-tts: A family of high-quality versatile speech generation models, 2024. URL https: //arxiv.org/abs/2406.02430 .
- Kaito Baba, Wataru Nakata, Yuki Saito, and Hiroshi Saruwatari. The t05 system for the VoiceMOS Challenge 2024: Transfer learning from deep image classi}er to naturalness MOS prediction of high-quality synthetic speech. In IEEE Spoken Language Technology Workshop (SLT) , pages 818-824, 2024. doi: 10.1109/SLT61566.2024.10832315.
- Donald J. Berndt and James Clizord. Using dynamic time warping to }nd patterns in time series. In Proceedings of the 3rd International Conference on Knowledge Discovery and Data Mining , AAAIWS'94, page 359 -370. AAAI Press, 1994.
- Zalán Borsos, Raphaël Marinier, Damien Vincent, Eugene Kharitonov, Olivier Pietquin, Matt Shari}, Dominik Roblek, Olivier Teboul, David Grangier, Marco Tagliasacchi, and Neil Zeghidour. Audiolm: A language modeling approach to audio generation. IEEE/ACM Transactions on Audio, Speech, and Language Processing , 31:2523-2533, 2023. doi: 10.1109/TASLP.2023.3288409.
- Huiwen Chang, Han Zhang, Lu Jiang, Ce Liu, and William T. Freeman. Maskgit: Masked generative image transformer. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , pages 11315-11325, June 2022.
- Alexandre Défossez, Jade Copet, Gabriel Synnaeve, and Yossi Adi. High }delity neural audio compression. arXiv preprint arXiv:2210.13438 , 2022.
- Alexandre Défossez, Laurent Mazaré, Manu Orsini, Amélie Royer, Patrick Pérez, Hervé Jégou, Edouard Grave, and Neil Zeghidour. Moshi: a speech-text foundation model for real-time dialogue. arXiv preprint arXiv:2410.00037 , 2024.
- Brecht Desplanques, Jenthe Thienpondt, and Kris Demuynck. ECAPA-TDNN: Emphasized channel attention, propagation and aggregation in TDNN based speaker veri}cation. In Interspeech 2020 , pages 3830-3834, 2020. doi: 10.21437/Interspeech.2020-2650.
- Jonathan Ho and Tim Salimans. Classi}er-free dizusion guidance. arXiv preprint arXiv:2207.12598 , 2022. URL https://arxiv.org/abs/2207.12598 .
- Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, and Ion Stoica. E{cient memory management for large language model serving with PagedAttention. In Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles , 2023. doi: 10.1145/3600006.3613165.

- Matt Le, Apoorv Vyas, Bowen Shi, Brian Karrer, Leda Sari, Rashel Moritz, Mary Williamson, Vimal Manohar, Yossi Adi, Jay Mahadeokar, and Wei-Ning Hsu. Voicebox: Text-guided multilingual universal speech generation at scale. In Advances in Neural Information Processing Systems , volume 36, 2023. URL https://proceedings.neurips. cc/paper\_files/paper/2023/hash/2d8911db9ecedf866015091b28946e15-Abstrac t-Conference.html .
- Alexander H Liu, Sung-Lin Yeh, and James R Glass. Revisiting self-supervised learning of speech representation from a mutual information perspective. In ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) , pages 12051-12055. IEEE, 2024.
- Alexander H. Liu, Andy Ehrenberg, Andy Lo, Clément Denoix, Corentin Barreau, Guillaume Lample, Jean-Malo Delignon, Khyathi Raghavi Chandu, Patrick von Platen, Pavankumar Reddy Muddireddy, Sanchit Gandhi, Soham Ghosh, Srijan Mishra, and Thomas Foubert. Voxtral, 2025. URL https://arxiv.org/abs/2507.13264 .
- Alexander H Liu, Kartik Khandelwal, Sandeep Subramanian, Victor Jouault, Abhinav Rastogi, Adrien Sadé, Alan Jezares, Albert Jiang, Alexandre Cahill, Alexandre Gavaudan, et al. Ministral 3. arXiv preprint arXiv:2601.08584 , 2026.
- Fabian Mentzer, David Minnen, Eirikur Agustsson, and Michael Tschannen. Finite scalar quantization: VQ-VAE made simple, 2023.
- Tu Anh Nguyen, Wei-Ning Hsu, Antony d'Avirro, Bowen Shi, Itai Gat, Maryam FazelZarani, Tal Remez, Jade Copet, Gabriel Synnaeve, Michael Hassid, et al. Expresso: A benchmark and analysis of discrete expressive speech resynthesis. arXiv preprint arXiv:2308.05725 , 2023.
- Julian D Parker, Anton Smirnov, Jordi Pons, CJ Carr, Zack Zukowski, Zach Evans, and Xubo Liu. Scaling transformers for low-bitrate high-quality speech coding. arXiv preprint arXiv:2411.19842 , 2024.
- William Peebles and Saining Xie. Scalable dizusion models with transformers. In Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) , pages 41954205, October 2023.
- Vadim Popov, Ivan Vovk, Vladimir Gogoryan, Tasnima Sadekova, and Mikhail Kudinov. Grad-TTS: A dizusion probabilistic model for text-to-speech. In Proceedings of the 38th International Conference on Machine Learning , volume 139 of Proceedings of Machine Learning Research , pages 8599-8608. PMLR, 2021. URL https://proceedings.mlr.pr ess/v139/popov21a.html .
- O}r Press, Noah A Smith, and Mike Lewis. Train short, test long: Attention with linear biases enables input length extrapolation. arXiv preprint arXiv:2108.12409 , 2021.
- Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, and Ilya Sutskever. Robust speech recognition via large-scale weak supervision. In International conference on machine learning , pages 28492-28518. PMLR, 2023.

- Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. In Advances in Neural Information Processing Systems , 2023. URL https: //arxiv.org/abs/2305.18290 .
- Hugo Touvron, Matthieu Cord, Alexandre Sablayrolles, Gabriel Synnaeve, and Hervé Jégou. Going deeper with image transformers. In Proceedings of the IEEE/CVF international conference on computer vision , pages 32-42, 2021.
- Aaron Van Den Oord, Oriol Vinyals, et al. Neural discrete representation learning. Advances in neural information processing systems , 30, 2017.
- Shikhar Vashishth, Harman Singh, Shikhar Bharadwaj, Sriram Ganapathy, Chulayuth Asawaroengchai, Kartik Audhkhasi, Andrew Rosenberg, Ankur Bapna, and Bhuvana Ramabhadran. Stab: Speech tokenizer assessment benchmark. arXiv preprint arXiv:2409.02384 , 2024.
- Chengyi Wang, Sanyuan Chen, Yu Wu, Ziqiang Zhang, Long Zhou, Shujie Liu, Zhuo Chen, Yanqing Liu, Huaming Wang, Jinyu Li, Lei He, Sheng Zhao, and Furu Wei. Neural codec language models are zero-shot text to speech synthesizers. arXiv preprint arXiv:2301.02111 , 2023. URL https://arxiv.org/abs/2301.02111 .
- Haibin Wu, Naoyuki Kanda, Se}k Emre Eskimez, and Jinyu Li. Ts3-codec: Transformerbased simple streaming single codec. arXiv preprint arXiv:2411.18803 , 2024.
- Peiqi Yin, Jiangyun Zhu, Han Gao, Chenguang Zheng, Yongxiang Huang, Taichang Zhou, Ruirui Yang, Weizhi Liu, Weiqing Chen, Canlin Guo, Didan Deng, Zifeng Mo, Cong Wang, James Cheng, Roger Wang, and Hongsheng Liu. vllm-omni: Fully disaggregated serving for any-to-any multimodal models, 2026. URL https://arxiv.org/abs/2602.0 2204 .
- Bowen Zhang, Congchao Guo, Geng Yang, Hang Yu, Haozhe Zhang, Heidi Lei, Jialong Mai, Junjie Yan, Kaiyue Yang, Mingqi Yang, Peikai Huang, Ruiyang Jin, Sitan Jiang, Weihua Cheng, Yawei Li, Yichen Xiao, Yiying Zhou, Yongmao Zhang, Yuan Lu, and Yucen He. Minimax-speech: Intrinsic zero-shot text-to-speech with a learnable speaker encoder, 2025. URL https://arxiv.org/abs/2505.07916 .
- Xin Zhang, Dong Zhang, Shimin Li, Yaqian Zhou, and Xipeng Qiu. Speechtokenizer: Uni}ed speech tokenizer for speech large language models. arXiv preprint arXiv:2308.16692 , 2023.
- Alon Ziv, Sanyuan Chen, Andros Tjandra, Yossi Adi, Wei-Ning Hsu, and Bowen Shi. Mr~owdpo: Multi-reward direct preference optimization for ~ow-matching text-to-music generation, 2025. URL https://arxiv.org/abs/2512.10264 .