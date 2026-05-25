## 端到端重分割的重叠感知说话⼈分割

Hervé Bredin 1 &amp; Antoine Laurent 2

1 IRIT, Université de Toulouse, CNRS, Toulouse, France 2 LIUM , Université du Mans, France

herve.bredin@irit.fr, antoine.laurent@univ-lemans.fr

## Abstract

说话⼈分割旨在将⼀个或多个说话⼈之间的对话划分为各 个说话⼈的发⾔段。通常被视作三个⼦任务（语⾳活动检 测、说话⼈切换检测和重叠语⾳检测）的后期组合，我们 提出直接训练⼀个端到端的分割模型来完成该任务。受原 始端到端神经说话⼈分离⽅法（ EEND ）的启发，该任务 被建模为⼀种多标签分类问题，并采⽤排列不变训练。主 要区别在于，我们的模型在短⾳频⽚段（ 5 秒）上运⾏，但 具有更⾼的时间分辨率（每 16 毫秒） 。在多个说话⼈分离 数据集上的实验表明，我们的模型在语⾳活动检测和重叠 语⾳检测⽅⾯均取得了显著成功。所提出的模型还可作为 后处理步骤，⽤于检测并正确分配重叠语⾳区域。与最佳 考虑的基准（ VBx ）相⽐，相对说话⼈分离错误率改进在 AMI 数据集上达到 17% ，在 DIHARD 3 数据集上达到 13% ，在 VoxConverse 数据集上也达到 13% 。

关键词 ：说话⼈辨识，说话⼈分割，语⾳活动检测，重叠 语⾳检测，重新分割。

## 1. 引⾔

语⾳处理领域依赖术语 分割 来描述多种任务：从将 ⾳频信号分类为三类 { 语⾳ , ⾳乐 , 其他 } ，到检测呼吸单 元、定位词边界，甚⾄将语⾳区域划分为语⾳单元。在这 ⼀从粗到细的时间尺度上，说话⼈分割介于 { 语⾳ , ⾮语 ⾳ } 分类与呼吸单元检测之间。其核⼼在于将语⾳区域划 分为更⼩的⽚段，每个⽚段仅包含单⼀说话⼈的语⾳。过 去，该问题被视作多个⼦任务的组合：⾸先，语⾳活动检 测（ VAD ）剔除所有不包含语⾳的区域；随后，说话⼈切 换检测（ SCD ）通过寻找说话⼈发⽣变化的时间点，将剩 余的语⾳区域划分为不同的说话⼈发⾔段 [1] 。从表⾯看， 这种说话⼈分割的定义似乎清晰且⽆歧义。然⽽，深⼊观 察真实场景中的⾃发对话时，会发现诸多复杂现象--重 叠语⾳、打断以及回应性话语是最显著的⼏种。因此，研 究⼈员也开始关注重叠语⾳检测（ OSD ）任务 [2, 3, 4] 。

端到端说话⼈分割。 与将语⾳活动检测、说话⼈切换检 测和重叠语⾳检测作为三个独⽴任务处理不同，我们的 ⾸个贡献是训练⼀个独特的端到端说话⼈分割模型，其 输出涵盖了上述⼦任务。该模型直接受近期端到端说话 ⼈聚类进展的启发，特别是由 ⽇⽴ [5, 6, 7] 开发的不断 发展的 端到端神经聚类 （ EEND ）⽅法族。所提出的分 割模型优于（或⾄少不逊于）若⼲语⾳活动检测基准， 并在所有三个考虑的数据集上建⽴了重叠语⾳检测的 新状态： AMI Mix-Headset [8] 、 DIHARD 3 [9, 10] 和 VoxConverse [11] 。我们未进⾏说话⼈切换检测实验。

重叠感知的重新分割。 我们的第⼆个贡献涉及将检测到 的重叠语⾳区域分配给正确说话⼈的难题。尽管过去已

This work was granted access to the HPC resources of IDRIS under the allocation AD011012177 made by GENCI, and was partly funded by the French National Research Agency (ANR) through the PLUMCOT (ANR-16-CE92-0025) and the GEM (ANR-19-CE38-0012) projects.

图 1: 我们模型在来⾃同⼀对话中两个 5 秒⽚段 上的实际输出（数据源： DIHARD3 数据集中的⽂件 DH\_EVAL\_0035.~ac ） 。 上⾏为参考标注。 中⾏为模型摄⼊的 ⾳频⽚段。下⾏为模型返回的原始说话⼈活性值。得益于 排列不变训练，注意左侧蓝⾊说话⼈对应橙⾊活性值，右 侧则对应绿⾊活性值。

<!-- image -->

有少数尝试 [4, 12] ，但该问题仍然⾮常困难，⾄今尚 未有简单的启发式基准能够被超越 [13] 。我们通过⼤ 量实验表明，当我们的分割模型转化为重叠感知的重 新分割模块时，其性能始终优于该启发式基准--在 结合 VBx ⽅法时， 在 AMI 数据集上达到了新的状态⽔平。

可复现性研究。 最后但同样重要的是， 我们的最终贡献在于 分享预训练模型，并将其集成到 pyannote 开源库中，以实 现可复现性⽬的： huggingface.co/pyannote/segmentation . 所 提出⽅法（ VAD 、 OSD 和重分割）的预期输出也可在此地 址以 RTTM 格式获取，以便于未来⽐较。

## 2. 端到端说话⼈分割

与原始的 EEND ⽅法 [5] 类似，该任务被建模为⼀个 使⽤排列不变训练的多标签分类问题。如图 1 所⽰，主要 区别在于我们的模型处理的是短⾳频⽚段（ 5 秒） ，但具有 更⾼的时间分辨率（约每 16ms ⼀次）。处理短⾳频⽚段 也意味着说话⼈数量⽐原始 EEND ⽅法（处理完整对话） 要少且变化更⼩--这使得问题更容易解决。例如，我们 发现训练集中的每段可能的 5 秒⽚段（稍后在第 3 节中定 义）中，超过 99 % 含有少于 K max = 4 个说话⼈。

## 2.1. 置换不变训练

给定⼀个⾳频⽚段 X ，其参考分割可以编码为⼀系列 K max -维度的⼆值帧 y = { y1 , . . . , yT } ，其中当说话⼈ k 在帧 t 活动时 yt ∈ { 0 , 1 } K max 且 y k t = 1 ，否则 y k t = 0 。 我们可以任意按⾸次活动时间顺序对说话⼈进⾏排序，但 对 K max 个维度的任何排列都是参考分割的有效表⽰。因 此，对于此类多标签分类问题通常使⽤的⼆值交叉熵损失 函数 L BCE 必须转换为⼀种排列不变的损失函数 L ，通过

<!-- image -->

图 2: 为了获得最终的⼆值分割结果，说话⼈活性值经过 后处理：⾸先使⽤ θ on / θ oz 滞回阈值法，然后填充短于 δ oz 的间隙（右图中浅绿⾊区域） ，最后移除短于 δ on 的活性区 域（在这些⽰例中未发⽣） 。

在 y 所有 K max 个维度上的所有可能排列 perm ( y ) 上运 ⾏实现：

<!-- formula-not-decoded -->

with ^ y = f ( X ) where f 是我们的分割模型，其架构将在 本⽂后续部分描述。在实际应⽤中，为提⾼效率，我们⾸ 先计算所有 y 和 ^ y 维度成对之间的 K max × K max ⼆元交 叉熵损失，并依赖匈⽛利算法找到使总体⼆元交叉熵损失 最⼩化的排列。

## 2.2. 实时数据增强

训练时， 从训练集中随机裁剪出 5 秒的⾳频⽚段 （及其 对应的参考分割） 。为了进⼀步增加多样性，我们采⽤实时 随机数据增强。第⼀种增强⽅式是添加具有随机信噪⽐的 背景噪声。受我们之前关于重叠语⾳检测⼯作的启发 [4] ， 第⼆种增强⽅式是⼈为增加重叠语⾳的数量。具体做法是 将两个随机的 5 秒⾳频⽚段以随机信噪⽐相加（并相应合 并其参考分割）。若⽣成的⽚段中说话⼈数量超过 K max ， 则不⽤于训练。

## 2.3. 分割

模型训练完成后，可通过对其输出说话⼈活性值进⾏ 简单的后处理，⽤于分割任务或其他⼦任务。

- 对于 分割 或 说话⼈切换检测 ，单个 θ = 0 . 5 ⼆值化 阈值即可获得不错的结果，但通过采⽤来⾃ [14] 的 更⾼级后处理⽅法并如图 2 所⽰进⾏总结，可以获 得更好的性能。
- 对于 语⾳活动检测 ，我们⾸先计算所有 K max 个说 话⼈中的最⼤活性值：

<!-- formula-not-decoded -->

然后，仅对得到的⼀维 ^ y VAD 应⽤上述后处理。

- 对于 重叠语⾳检测 ，由于⾄少需要两个说话⼈同时 活跃才能表明存在重叠语⾳，我们计算第⼆⾼的（记 作 max 2nd ）活性值：

<!-- formula-not-decoded -->

并使⽤相同的⽅法对得到的⼀维 ^ y OSD 进⾏后处理。

## 2.4. 重叠感知的重新分割

尽管越来越多的说话⼈分离⽅法尝试考虑重叠语⾳问 题 [7] ，但最可靠的那些⽅法（如图 3 中使⽤的 VBx ⽅ 法 [15] ）在内部仍然假设任意时刻最多只有⼀个说话⼈处 于活跃状态。因此，有必要引⼊⼀个后处理步骤，为重叠 语⾳区域分配多个说话⼈标签 [4, 17] 。

给定⼀个已有的说话⼈聚类输出（包含 K 个说话⼈） ， 其被编码为⼀系列 K 维的⼆值帧 y DIA t ，我们提出使⽤分

图 3: 所提出的重分割⽅法（第三⾏）对 VBx 说话⼈分离 基准⽅法（第⼆⾏）的影响。我们突出显⽰了三个区域，其 中启发式⽅法表现更好 ( t ≈ 100 s ) 、相当 ( t ≈ 120 s ) 或 更差 ( t ≈ 115 s) 于所提出的⽅法（来源： DIHARD3 数 据集中的⽂件 DH\_EVAL\_0035.~ac ） 。

<!-- image -->

割模型作为局部的、能够感知重叠的重新分割模块。该分 割模型应⽤于在整段⾳频上滑动的 5 秒窗⼝。在每⼀步中， 我们寻找说话⼈活性值 ^ y 的排列，使得其与 y DIA 之间的 ⼆值交叉熵损失最⼩。随后，经过排列的滑动说话⼈活性 值将在时间维度上进⾏聚合，并通过第 2.3 节中提出的基 于阈值的⽅法进⾏后处理。

## 3. 实验

数据集与划分 . 我们在三个说话⼈聚类数据集上进⾏了 实验并报告了结果，这些数据集涵盖了⼴泛的领域：

DIHARD3 语料库 [9, 10] 不提供 训练 集。因此，我 们将它的 开发 集分成两部分： 192 个⽂件⽤作 训练 集，其余 62 个⽂件⽤作较⼩的 开发 集。在本⽂其余 部分中，后者简称为 开发 集。在定义这⼀划分（共享 于 huggingface.co/pyannote/segmentation ) 时，我们确保了 11 个领域在两个⼦集之间均匀分布。 评估 集保持不变。

VoxConverse 也没有提供 训练 集 [11] 。因此，我们也将 其 开发 集分为两部分：前 144 个⽂件（ abjxc 到 qouur ，按 字母顺序排列）构成 训练 集，剩下的 72 个⽂件（ qppll 到 zyzh ）⽤于实际的 开发 集。

AMI 提供了 Mix-Headset ⾳频⽂件的官⽅ { 训练 , 开发 , 评估 } 划分 [8] 。我们保持了 开发 和 评估 集不变，仅使⽤ 了 训练 集中每个⽂件的前 10 分钟，最终得到⼀个实际的 训练 集，其⼤⼩（ 22 ⼩时）与 DIHARD3 （ 25 ⼩时）和 VoxConverse （ 15 ⼩时）的 训练 集相似。

实验协议。 我们使⽤由三个 训练 集拼接⽽成的 合成 训练集 （ 62 ⼩时）训练了⼀个唯⼀的分割模型。 合成 开发集（ 24 ⼩时）⽤作验证，⽤于在学习率平缓时降低学习率，并最 终选择最佳模型检查点。在此过程结束后，仅有⼀个分割 模型可⽤（⽽⾮每个数据集⼀个模型） ，并⽤于所有实验。

然⽽，检测阈值（ θ on 、 θ oz 、 δ on 和 δ oz ）是针对每个 数据集使⽤其⾃⾝的 development 集进⾏专门调整的，因 为⼈⼯标注指南在不同数据集之间存在差异，尤其是在控 制是否连接说话⼈内部⼩停顿的 δ oz ⽅⾯。原因相同，检 测阈值针对本⽂所解决的每个任务进⾏了专门优化：

- 语⾳活动检测的阈值选择以最⼩化检测错误率（即 误报率和漏检率之和）为⽬标，且在语⾳段落边界

处不设置宽容区间；

- 重叠语⾳检测的阈值被选择为最⼤化检测 F 1 -得分， 且不采⽤任何宽容区间；
- 对于重新分割，检测阈值的选择旨在最⼩化说话⼈ 辨识错误率，不使⽤宽容区间但包含重叠语⾳区域。 这与 DIHARD3 评估⽅案 [10] 和 AMI Full 评估设 置 [15] ⼀致，但与使⽤ 250ms 宽容区间的 VoxConverse 挑战规则 [11] 不同。

所有指标均使⽤ pyannote.metrics [18] 开源 Python 库计 算。

实现细节。 我们的分割模型接收采样率为 16kHz 的 5 秒⾳ 频⽚段 （ i.e. 80000 个样本的序列） 。 输⼊序列通过 SincNet 卷积层，采⽤原始配置 [19] --除了第⼀层的步幅设置为 10 （使得 SincNet 帧每 16ms 提取⼀次） 。在两个额外的 全连接层（每个包含 128 个单元且使⽤ Leaky Relu 活性 值）之上堆叠了四个双向长短期记忆⽹络（ LSTM ）循环 层（每个⽅向各 128 个单元，前三个层使⽤ 50% 暂退法 (Dropout) ） 。 这些全连接层也在帧级上操作。最后，⼀个具 有 Sigmoid 激活函数的全连接分类层每 16ms 输出 K max -维的说话⼈活性值，取值范围为 0 到 1 。总体⽽⾔，我们 的模型包含 150 万个可训练参数--其中绝⼤部分（ 140 万个）来⾃循环层。

我们使⽤ Adam 优化器，采⽤ PyTorch 的默认参数， 并以批量⼤⼩为 128 进⾏模型训练。学习率初始值设为 10 -3 ，当其在开发集上的性能达到平台期时，学习率将按 因⼦ 2 减⼩。使⽤ 4 块 V100 GPU ，⼤约耗时 3 天达到 最佳性能。虽然我们在 huggingface.co/pyannote/segmentation 公开预训练模型以便复现结果，但整个训练过程同样可复 现，因为所有内容均已集成⾄ pyannote.audio 开源库版本 2.0 中 [16] 。

如第 2.2 节所介绍， 50% 的训练样本由两个⽚段的加 权和构成，其信号 -信号⽐在 0 到 10dB 之间均匀采样。我 们还使⽤来⾃ MUSAN 数据集 [20] 的加性背景噪声，其 信号 -噪声⽐在 5 到 15dB 之间均匀采样。

## 4. 结果与讨论

语⾳活动检测。 表 1 对⽐了所提出的语⾳活动检测⽅法与 官⽅ dihard3 基准 [9] 、 Landini 在 VoxConverse 挑战赛 中的提交结果 [12] ，以及 pyannote 1.1 语⾳活动检测模 型 [16] 的性能。主要结论是，尽管该模型是为分割任务训 练的，但其表现优于其他专为语⾳活动检测训练的模型。 然⽽，需要注意的是，不应轻易对 silero\_vad 模型 [21] 的性能做出判断，因为这是⼀个现成的模型，并未针对这 些数据集进⾏专门训练。

重叠语⾳检测。 为重叠语⾳检测任务找到良好且可复现的 基准证明是⼀项困难的任务。我们感谢 Kunesova 等⼈ [3] 和 Landini 等⼈ [12] 共享了他们检测流⽔线的输出结果。 表 2 中报告的结果显⽰，与语⾳活动检测类似，我们的分 割模型即使最初并未为此特定任务进⾏训练，仍可成功⽤ 于重叠语⾳检测。该模型的表现优于 pyannote 1.1 的重

表 1: 语⾳活动检测 // FA = 误报率 (%) / 漏检率 (%)

| VAD                 |     | AMI [8, 15]   | AMI [8, 15]   | DIHARD 3 [9]   | DIHARD 3 [9]   | DIHARD 3 [9]   | VoxConverse [11]   | VoxConverse [11]   | VoxConverse [11]   |
|---------------------|-----|---------------|---------------|----------------|----------------|----------------|--------------------|--------------------|--------------------|
|                     | FA  | Miss.         | FA+Miss.      | FA             | Miss.          | FA+Miss.       | FA                 | Miss.              | FA+Miss.           |
| silero_vad          | 9.4 | 1.7           | 11.0          | 17.0           | 4.0            | 21.0           | 3.0                | 1.1                | 4.2                |
| dihard3 [9]         | NA  | NA            | NA            | 4.0            | 4.2            | 8.2            | NA                 | NA                 | NA                 |
| Landini et al. [12] | NA  | NA            | NA            | NA             | NA             | NA             | 1.8                | 1.1                | 3.0                |
| pyannote 1.1 [16]   | 6.5 | 1.7           | 8.2           | 4.1            | 3.8            | 7.9            | 4.5                | 0.3                | 4.8                |
| Ours - pyannote 2.0 | 3.6 | 3.2           | 6.8           | 3.9            | 3.3            | 7.3            | 1.8                | 0.8                | 2.5                |

叠语⾳检测⽅法， 我们认为这此前是该任务的最新状态 [4] 。

重叠感知的重新分割。 尽管我们的分割模型在语⾳活动检 测和重叠语⾳检测中均表现出实⽤性，但其真正优势体现 在对现有说话⼈聚类流⽔线输出的后处理上。表 3 总结了 在三个基准流⽔线上的重新分割实验结果，这些基准按性 能从差到好排序： pyannote 1.1 预训练流⽔线 [16] 、 dihard3 官⽅基准 [9] 以及 BUT 的 VBx ⽅法 [15] 。选择这些基准 所采⽤（尽管存在错误）的准则为使⽤便捷性和可复现性。 由于 [15] 中报告的 VBx 基准结果依赖于理想语⾳活动检 测，⽽共享代码库并未提供官⽅的语⾳活动检测实现，因 此我们采⽤了⾃有的⽅法（表 1 中标记为 Ours ） ，并在其 基础上应⽤了 VBx 。我们提出的重新分割⽅法在所有数据 集上均持续提升了所有基准的输出效果。相较于最佳基准 （ VBx ） ，相对说话⼈聚类错误率改善分别达到 AMI 上的 17% 、 DIHARD 上的 13% ，以及 VoxConverse 上的 13% 。 为了便于⽐较，我们还实现了⼀种启发式⽅法，该⽅ 法通过将检测到的重叠语⾳区域分配给时间上最近的两个 说话⼈来处理 [13] 。尽管该⽅法简单，但其恰好成为⼀个 强⼤的基准，实际中很难被超越 [12] 。然⽽，在⼏乎所有实 验条件下，我们提出的重新分割⽅法均优于该启发式⽅法 （仅有两种情况下启发式⽅法略胜⼀筹，且优势微⼩） 。进 ⼀步分析说话⼈混淆错误率发现，我们的⽅法在识别重叠 说话⼈⽅⾯表现显著更优。这⼀点也得到了在使⽤理想聚 类结果（ y DIA = y ）基础上应⽤该⽅法时获得的低说话⼈ 混淆错误率的验证：在 AMI 、 DIHARD 和 VoxConverse 数据集上，分别仅有 1.4% 、 1.8% 和 0.6% 的语⾳被错误 重新分配。图 3 展⽰了它们在⼀段 20 秒短⽚段上的⾏为 表现，具有定性参考价值。特别地，可以看出这两种⽅法

（启发式与所提⽅法）的⾏为存在差异，具有互补潜⼒。

## 5. 结论

本⽂报告的整体最佳流⽔线是我们的语⾳活动检测、 现成的 VBx 聚类以及我们提出的重分割⽅法的组合，该 ⽅法能够处理重叠部分，在 AMI Mix-Headset 上达到 DER = 19 . 9 % ，使⽤的是 [15] 中引⼊的 完整 评估设置； 在 DIHARD 3 评估集上达到 DER = 19 . 3 % （ 完整 条件， ⽐第⼀名提交结果低 2.6% ）；在 VoxConverse 开发 集上 达到 DER = 7 . 1 % （或在加⼊ 250ms 宽容窗⼝后达到 DER = 3 . 4 % ） 。

即使使⽤了宽容标记，漏检和误报仍是所有三个数据 集中的主要错误来源（错误率是说话⼈混淆的两倍），这 表明尽管取得了进展，重叠语⾳检测仍然是⼀个尚未解决 （有时定义不清）的问题。

| OSD                  | AMI [8, 15]   | AMI [8, 15]   | AMI [8, 15]   | AMI [8, 15]   | DIHARD 3 [9]   | DIHARD 3 [9]   | DIHARD 3 [9]   | DIHARD 3 [9]   | DIHARD 3 [9]   | DIHARD 3 [9]   | VoxConverse [11]   | VoxConverse [11]   | VoxConverse [11]   | VoxConverse [11]   | VoxConverse [11]   |
|----------------------|---------------|---------------|---------------|---------------|----------------|----------------|----------------|----------------|----------------|----------------|--------------------|--------------------|--------------------|--------------------|--------------------|
|                      | FA            | Miss.         | Precision     | Recall        | F 1            | FA             | Miss.          | Precision      | Recall         | F 1            | FA                 | Miss.              | Precision          | Recall             | F 1                |
| Kunesova et al. [3]  | NA            | NA            | 71.5          | 46.1          | 56.0           | NA             | NA             | NA             | NA             | NA             | NA                 | NA                 | NA                 | NA                 | NA                 |
| Landini et al. [12]  | NA            | NA            | NA            | NA            | NA             | NA             | NA             | NA             | NA             | NA             | 10.4               | 71.8               | 73.0               | 28.2               | 40.7               |
| pyannote 1.1 [16, 4] | 51.1          | 12.1          | 63.2          | 87.9          | 73.5           | 48.2           | 45.2           | 53.2           | 54.8           | 54.0           | 130.4              | 17.7               | 38.7               | 82.3               | 52.6               |
| Ours - pyannote 2.0  | 16.9          | 29.4          | 80.7          | 70.5          | 75.3           | 46.9           | 37.2           | 57.2           | 62.8           | 59.9           | 26.3               | 24.5               | 74.2               | 75.5               | 74.8               |

表 3: 重新分割 // FA = 误报 / 漏检 = 漏检 / 混淆 = 说话⼈混淆 / DER = 说话⼈分离错误率

| Baseline            | Overlap-aware resegmentation                    | AMI [8, 15]   | AMI [8, 15]   | AMI [8, 15]   | AMI [8, 15]    | DIHARD 3 [9]   | DIHARD 3 [9]   | DIHARD 3 [9]   | DIHARD 3 [9]   | VoxConverse [11]   | VoxConverse [11]   | VoxConverse [11]   | VoxConverse [11]   |
|---------------------|-------------------------------------------------|---------------|---------------|---------------|----------------|----------------|----------------|----------------|----------------|--------------------|--------------------|--------------------|--------------------|
| Baseline            | Overlap-aware resegmentation                    | FA            | Miss.         | Conf.         | DER            | FA             | Miss.          | Conf.          | DER            | FA                 | Miss.              | Conf.              | DER                |
| pyannote 1.1 [16]   | _ Heuristic [13] w/ our OSD Ours - pyannote 2.0 | 5.0 6.9 4.0   | 16.2 7.9 13.0 | 8.5 10.9 9.1  | 29.7 25.7 26.1 | 3.4 6.3 5.1    | 13.2 8.9 9.8   | 12.6 12.8 10.3 | 29.2 28.1 25.2 | 2.0 2.8 2.4        | 10.1 7.3 3.1       | 9.5 10.1 9.8       | 21.5 20.3 15.4     |
| dihard3 [9]         | _ Heuristic [13] w/ our OSD Ours - pyannote 2.0 | NA NA NA      | NA NA NA      | NA NA NA      | NA NA NA       | 3.6 6.8 4.6    | 13.3 8.7 10.2  | 8.4 8.8 7.5    | 25.4 24.3 22.2 | NA NA NA           | NA NA NA           | NA NA NA           | NA NA NA           |
| VBx [15] w/ our VAD | _ Heuristic [13] w/ our OSD Ours - pyannote 2.0 | 3.1 5.1 4.3   | 17.2 8.7 10.9 | 3.8 6.1 4.7   | 24.1 19.9 19.9 | 3.6 7.0 4.7    | 12.5 7.8 9.7   | 6.2 6.4 4.9    | 22.3 21.2 19.3 | 1.7 2.7 2.7        | 5.1 2.1 2.6        | 1.4 2.0 1.8        | 8.3 6.8 7.1        |
| Oracle              | Ours - pyannote 2.0                             | 4.7           | 10.0          | 1.4           | 16.1           | 4.6            | 9.8            | 1.8            | 16.2           | 2.6                | 2.5                | 0.6                | 5.7                |

## 6. References

- [1] R. Yin, H. Bredin, and C. Barras, 'Speaker Change Detection in Broadcast TV Using Bidirectional Long Short-Term Memory Networks,' in Proc. Interspeech 2017 , 2017.
- [2] D. Charlet, C. Barras, and J. Liénard, 'Impact of overlapping speech detection on speaker diarization for broadcast news and debates,' in 2013 IEEE International Conference on Acoustics, Speech and Signal Processing , May 2013, pp. 7707-7711.
- [3] M. Kunešová, M. Hrúz, Z. Zajíc, and V. Radová, 'Detection of overlapping speech for the purposes of speaker diarization,' in Speech and Computer , A. A. Salah, A. Karpov, and R. Potapova, Eds. Cham: Springer International Publishing, 2019, pp. 247-257.
- [4] L. Bullock, H. Bredin, and L. P. Garcia-Perera, 'Overlapaware diarization: Resegmentation using neural end-to-end overlapped speech detection,' in Proc. ICASSP 2020 , 2020.
- [5] Y. Fujita, N. Kanda, S. Horiguchi, K. Nagamatsu, and S. Watanabe, 'End-to-End Neural Speaker Diarization with Permutation-free Objectives,' in Interspeech , 2019, pp. 43004304.
- [6] Y. Fujita, N. Kanda, S. Horiguchi, Y. Xue, K. Nagamatsu, and S. Watanabe, 'End-to-end neural speaker diarization with self-attention,' in 2019 IEEE Automatic Speech Recognition and Understanding Workshop (ASRU) , 2019, pp. 296303.
- [7] Y. Takashima, Y. Fujita, S. Watanabe, S. Horiguchi, P. García, and K. Nagamatsu, 'End-to-end speaker diarization conditioned on speech activity and overlap detection,' in 2021 IEEE Spoken Language Technology Workshop (SLT) , 2021, pp. 849-856.
- [8] J. Carletta, 'Unleashing the killer corpus: experiences in creating the multi-everything AMI Meeting Corpus,' Language Resources and Evaluation , vol. 41, no. 2, 2007.
- [9] N. Ryant, P. Singh, V. Krishnamohan, R. Varma, K. Church, C. Cieri, J. Du, S. Ganapathy, and M. Liberman, 'The Third DIHARD Diarization Challenge,' arXiv preprint arXiv:2012.01477 , 2020.
- [10] N. Ryant, K. Church, C. Cieri, J. Du, S. Ganapathy, and M. Liberman, 'Third DIHARD Challenge Evaluation Plan,' arXiv preprint arXiv:2006.05815 , 2020.
- [11] J. S. Chung, J. Huh, A. Nagrani, T. Afouras, and A. Zisserman, 'Spot the Conversation: Speaker Diarisation in the Wild,' in Proc. Interspeech 2020 , 2020, pp. 299-303. [Online]. Available: http://dx.doi.org/10.21437/Interspeech. 2020-2337
- [12] F. Landini, O. Glembek, P. Matějka, J. Rohdin, L. Burget, M. Diez, and A. Silnova, 'Analysis of the BUT Diarization System for VoxConverse Challenge,' in 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) , 2021.
- [13] S. Otterson and M. Ostendorf, 'E{cient use of overlap information in speaker diarization,' in 2007 IEEE Workshop on Automatic Speech Recognition &amp; Understanding (ASRU) . IEEE, 2007, pp. 683-686.
- [14] G. Gelly and J.-L. Gauvain, 'Optimization of RNN-Based Speech Activity Detection,' IEEE/ACM Transactions on Audio, Speech, and Language Processing , vol. 26, no. 3, pp. 646-656, March 2018.
- [15] F. Landini, J. Profant, M. Diez, and L. Burget, 'Bayesian hmm clustering of x-vector sequences (vbx) in speaker diarization: theory, implementation and analysis on standard tasks,' 2020.
- [16] H. Bredin, R. Yin, J. M. Coria, G. Gelly, P. Korshunov, M. Lavechin, D. Fustes, H. Titeux, W. Bouaziz, and M.P. Gill, 'pyannote.audio: neural building blocks for speaker diarization,' in Proc. ICASSP 2020 , 2020.
- [17] S. Horiguchi, P. Garcia, Y. Fujita, S. Watanabe, and K. Nagamatsu, 'End-to-end speaker diarization as postprocessing,' 2020.
- [18] H. Bredin, 'pyannote.metrics: a toolkit for reproducible evaluation, diagnostic, and error analysis of speaker diarization systems,' in Proc. Interspeech 2017 , Stockholm, Sweden, August 2017. [Online]. Available: http://pyannote. github.io/pyannote-metrics
- [19] M. Ravanelli and Y. Bengio, 'Speaker recognition from raw waveform with sincnet,' in Proc. SLT 2018 , 2018.
- [20] D. Snyder, G. Chen, and D. Povey, 'MUSAN: A Music, Speech, and Noise Corpus,' 2015.
- [21] Silero Team, 'Silero VAD: pre-trained enterprise-grade Voice Activity Detector (VAD), Number Detector and Language Classi}er,' https://github.com/snakers4/silero-vad, 2021.