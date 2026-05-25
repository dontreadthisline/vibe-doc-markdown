# 端到端重分割的重叠感知说话人分割

Hervé Bredin<sup>1</sup> & Antoine Laurent<sup>2</sup>

<sup>1</sup>IRIT, Université de Toulouse, CNRS, Toulouse, France <sup>2</sup>LIUM, Université du Mans, France

 $herve.bredin@irit.fr, \ antoine.laurent@univ-lemans.fr\\$ 

### Abstract

说话人分割旨在将一个或多个说话人之间的对话划分为各个说话人的发言段。通常被视作三个子任务(语音活动检测、说话人切换检测和重叠语音检测)的后期组合,我们提出直接训练一个端到端的分割模型来完成该任务。受原始端到端神经说话人分离方法(EEND)的启发,该任务被建模为一种多标签分类问题,并采用排列不变训练。主要区别在于,我们的模型在短音频片段(5秒)上运行,但具有更高的时间分辨率(每16毫秒)。在多个说话人分离数据集上的实验表明,我们的模型在语音活动检测和重叠语音检测方面均取得了显著成功。所提出的模型还可作为后处理步骤,用于检测并正确分配重叠语音区域。与最佳考虑的基准(VBx)相比,相对说话人分离错误率改进在AMI数据集上达到17%,在DIHARD3数据集上达到13%。在VoxConverse数据集上也达到13%。

**关键词**: 说话人辨识, 说话人分割, 语音活动检测, 重叠语音检测, 重新分割。

## 1. 引言

语音处理领域依赖术语 分割来描述多种任务: 从将音频信号分类为三类 {语音,音乐,其他},到检测呼吸单元、定位词边界,甚至将语音区域划分为语音单元。在这一从粗到细的时间尺度上,说话人分割介于 {语音,非语音} 分类与呼吸单元检测之间。其核心在于将语音区域划分为更小的片段,每个片段仅包含单一说话人的语音。过去,该问题被视作多个子任务的组合:首先,语音活动检测 (VAD)剔除所有不包含语音的区域;随后,说话人切换检测 (SCD)通过寻找说话人发生变化的时间点,将剩余的语音区域划分为不同的说话人发言段 [1]。从表面看,这种说话人分割的定义似乎清晰且无歧义。然而,深入观察真实场景中的自发对话时,会发现诸多复杂现象——重叠语音、打断以及回应性话语是最显著的几种。因此,研究人员也开始关注重叠语音检测 (OSD) 任务 [2,3,4]。

端到端说话人分割。与将语音活动检测、说话人切换检测和重叠语音检测作为三个独立任务处理不同,我们的首个贡献是训练一个独特的端到端说话人分割模型,其输出涵盖了上述子任务。该模型直接受近期端到端说话人聚类进展的启发,特别是由日立 [5, 6, 7] 开发的不断发展的端到端神经聚类(EEND)方法族。所提出的分割模型优于(或至少不逊于)若干语音活动检测基准,并在所有三个考虑的数据集上建立了重叠语音检测的新状态: AMI Mix-Headset [8]、DIHARD 3 [9, 10] 和VoxConverse [11]。我们未进行说话人切换检测实验。

**重叠感知的重新分割**。我们的第二个贡献涉及将检测到 的重叠语音区域分配给正确说话人的难题。尽管过去已

<span id="page-0-0"></span>![](_page_0_Figure_13.jpeg)

图 1: 我们模型在来自同一对话中两个 5 秒片段上的实际输出 (数据源: DIHARD3 数据集中的文件DH\_EVAL\_0035.flac)。上行为参考标注。中行为模型摄入的音频片段。下行为模型返回的原始说话人活性值。得益于排列不变训练,注意左侧蓝色说话人对应橙色活性值,右侧则对应绿色活性值。

有少数尝试 [4,12],但该问题仍然非常困难,至今尚未有简单的启发式基准能够被超越 [13]。我们通过大量实验表明,当我们的分割模型转化为重叠感知的重新分割模块时,其性能始终优于该启发式基准——在结合 VBx 方法时,在 AMI 数据集上达到了新的状态水平。

**可复现性研究**。最后但同样重要的是,我们的最终贡献在于分享预训练模型,并将其集成到 *pyannote* 开源库中,以实现可复现性目的: huggingface.co/pyannote/segmentation. 所提出方法 (VAD、OSD 和重分割) 的预期输出也可在此地址以 RTTM 格式获取,以便于未来比较。

### 2. 端到端说话人分割

与原始的 EEND 方法 [5] 类似,该任务被建模为一个使用排列不变训练的多标签分类问题。如图 1 所示,主要区别在于我们的模型处理的是短音频片段(5 秒),但具有更高的时间分辨率(约每 16ms 一次)。处理短音频片段也意味着说话人数量比原始 EEND 方法(处理完整对话)要少且变化更小——这使得问题更容易解决。例如,我们发现训练集中的每段可能的 5 秒片段(稍后在第 3 节中定义)中,超过 99% 含有少于  $K_{max}=4$  个说话人。

### 2.1. 置换不变训练

给定一个音频片段  $\mathbf{X}$ , 其参考分割可以编码为一系列  $K_{\max}$ -维度的二值帧  $\mathbf{y} = \{\mathbf{y_1}, \dots, \mathbf{y_T}\}$ , 其中当说话人 k 在帧 t 活动时  $\mathbf{y_t} \in \{0,1\}^{K_{\max}}$  且  $\mathbf{y_t}^k = 1$ , 否则  $\mathbf{y_t}^k = 0$ 。我们可以任意按首次活动时间顺序对说话人进行排序,但 对  $K_{\max}$  个维度的任何排列都是参考分割的有效表示。因此,对于此类多标签分类问题通常使用的二值交叉熵损失 函数  $\mathcal{L}_{\mathrm{BCE}}$  必须转换为一种排列不变的损失函数  $\mathcal{L}_{\mathrm{C}}$  通过

This work was granted access to the HPC resources of IDRIS under the allocation AD011012177 made by GENCI, and was partly funded by the French National Research Agency (ANR) through the PLUMCOT (ANR-16-CE92-0025) and the GEM (ANR-19-CE38-0012) projects.

<span id="page-1-1"></span>![](_page_1_Figure_0.jpeg)

图 2: 为了获得最终的二值分割结果, 说话人活性值经过后处理: 首先使用  $\theta$ on/ $\theta$ off 滞回阈值法, 然后填充短于  $\delta$ off 的间隙 (右图中浅绿色区域), 最后移除短于  $\delta$ on 的活性区域 (在这些示例中未发生)。

在  $\mathbf{y}$  所有  $K_{\text{max}}$  个维度上的所有可能排列  $\operatorname{perm}(\mathbf{y})$  上运行实现:

$$\mathcal{L}(\mathbf{y}, \widehat{\mathbf{y}}) = \min_{\text{perm}(\mathbf{y})} \mathcal{L}_{\text{BCE}}(\text{perm}(\mathbf{y}), \widehat{\mathbf{y}})$$
(1)

with  $\hat{\mathbf{y}} = f(\mathbf{X})$  where f 是我们的分割模型,其架构将在本文后续部分描述。在实际应用中,为提高效率,我们首先计算所有  $\mathbf{y}$  和  $\hat{\mathbf{y}}$  维度成对之间的  $K_{\text{max}} \times K_{\text{max}}$  二元交叉熵损失,并依赖匈牙利算法找到使总体二元交叉熵损失最小化的排列。

#### <span id="page-1-4"></span>2.2. 实时数据增强

训练时,从训练集中随机裁剪出 5 秒的音频片段(及其对应的参考分割)。为了进一步增加多样性,我们采用实时随机数据增强。第一种增强方式是添加具有随机信噪比的背景噪声。受我们之前关于重叠语音检测工作的启发 [4],第二种增强方式是人为增加重叠语音的数量。具体做法是将两个随机的 5 秒音频片段以随机信噪比相加(并相应合并其参考分割)。若生成的片段中说话人数量超过  $K_{\rm max}$ ,则不用于训练。

#### <span id="page-1-3"></span>2.3. 分割

模型训练完成后,可通过对其输出说话人活性值进行 简单的后处理,用于分割任务或其他子任务。

- 对于分割或说话人切换检测,单个 θ = 0.5 二值化 阈值即可获得不错的结果,但通过采用来自 [14] 的 更高级后处理方法并如图 2 所示进行总结,可以获 得更好的性能。
- 对于**语音活动检测**,我们首先计算所有  $K_{\text{max}}$  个说话人中的最大活性值:

$$\hat{y}_t^{\text{VAD}} = \max_k \hat{y}_t^k \tag{2}$$

然后,仅对得到的一维 $\hat{\mathbf{y}}^{VAD}$ 应用上述后处理。

 对于重叠语音检测,由于至少需要两个说话人同时 活跃才能表明存在重叠语音,我们计算第二高的(记作 max<sub>2nd</sub>)活性值:

$$\hat{y}_t^{\text{OSD}} = \max_{k} \hat{y}_t^k \tag{3}$$

并使用相同的方法对得到的一维  $\hat{\mathbf{y}}^{\mathrm{OSD}}$  进行后处理。

### 2.4. 重叠感知的重新分割

尽管越来越多的说话人分离方法尝试考虑重叠语音问题 [7],但最可靠的那些方法(如图 3 中使用的 VBx 方法 [15])在内部仍然假设任意时刻最多只有一个说话人处于活跃状态。因此,有必要引入一个后处理步骤,为重叠语音区域分配多个说话人标签 [4,17]。

给定一个已有的说话人聚类输出(包含 K 个说话人),其被编码为一系列 K 维的二值帧  $y_t^{\mathrm{DIA}}$ ,我们提出使用分

<span id="page-1-2"></span>![](_page_1_Figure_19.jpeg)

图 3: 所提出的重分割方法 (第三行) 对 VBx 说话人分离基准方法 (第二行) 的影响。我们突出显示了三个区域,其中启发式方法表现更好  $(t\approx 100s)$ 、相当  $(t\approx 120s)$ 或更差  $(t\approx 115s)$ 于所提出的方法 (来源: DIHARD3数据集中的文件 DH EVAL 0035.flac)。

割模型作为局部的、能够感知重叠的重新分割模块。该分割模型应用于在整段音频上滑动的 5 秒窗口。在每一步中,我们寻找说话人活性值  $\hat{y}$  的排列,使得其与  $y^{DIA}$  之间的二值交叉熵损失最小。随后,经过排列的滑动说话人活性值将在时间维度上进行聚合,并通过第 2.3 节中提出的基于阈值的方法进行后处理。

### 3. 实验

<span id="page-1-0"></span>**数据集与划分**. 我们在三个说话人聚类数据集上进行了 实验并报告了结果,这些数据集涵盖了广泛的领域:

DIHARD3 语料库 [9, 10] 不提供 训练集。因此,我们将它的 开发集分成两部分: 192 个文件用作 训练集,其余 62 个文件用作较小的 开发集。在本文其余部分中,后者简称为 开发集。在定义这一划分(共享于huggingface.co/pyannote/segmentation)时,我们确保了 11个领域在两个子集之间均匀分布。评估集保持不变。

VoxConverse 也没有提供 训练集 [11]。因此,我们也将其 开发集分为两部分:前 144 个文件 (abjxc 到 qouur,按字母顺序排列)构成 训练集,剩下的 72 个文件 (qppll 到zyffn)用于实际的 开发集。

AMI 提供了 Mix-Headset 音频文件的官方 {训练, 开发, 评估} 划分 [8]。我们保持了 开发和 评估集不变,仅使用了 训练集中每个文件的前 10 分钟,最终得到一个实际的训练集,其大小(22 小时)与 DIHARD3(25 小时)和 VoxConverse(15 小时)的 训练集相似。

**实验协议**。我们使用由三个训练集拼接而成的合成训练集 (62 小时)训练了一个唯一的分割模型。合成开发集(24 小时)用作验证,用于在学习率平缓时降低学习率,并最 终选择最佳模型检查点。在此过程结束后,仅有一个分割 模型可用(而非每个数据集一个模型),并用于所有实验。

然而,检测阈值( $\theta_{\rm on}$ 、 $\theta_{\rm off}$ 、 $\delta_{\rm on}$  和  $\delta_{\rm off}$ )是针对每个数据集使用其自身的 development 集进行专门调整的,因为人工标注指南在不同数据集之间存在差异,尤其是在控制是否连接说话人内部小停顿的  $\delta_{\rm off}$  方面。原因相同,检测阈值针对本文所解决的每个任务进行了专门优化:

语音活动检测的阈值选择以最小化检测错误率(即误报率和漏检率之和)为目标,且在语音段落边界

处不设置宽容区间;

- 重叠语音检测的阈值被选择为最大化检测 F<sup>1</sup> -得分, 且不采用任何宽容区间;
- 对于重新分割,检测阈值的选择旨在最小化说话人 辨识错误率,不使用宽容区间但包含重叠语音区域。 这与 DIHARD3 评估方案 [\[10\]](#page-3-9) 和 AMI *Full* 评估设 置 [[15\]](#page-3-14) 一致,但与使用 250ms 宽容区间的 VoxConverse 挑战规则 [\[11\]](#page-3-10) 不同。

所有指标均使用 *pyannote.metrics* [[18](#page-3-16)] 开源 Python 库计 算。

**实现细节。**我们的分割模型接收采样率为 16kHz 的 5 秒音 频片段(*i.e.* 80000 个样本的序列)。输入序列通过 *SincNet* 卷积层,采用原始配置 [\[19\]](#page-3-17)——除了第一层的步幅设置为 10(使得 *SincNet* 帧每 16ms 提取一次)。在两个额外的 全连接层(每个包含 128 个单元且使用 Leaky Relu 活性 值)之上堆叠了四个双向长短期记忆网络(LSTM)循环 层(每个方向各 128 个单元,前三个层使用 50% 暂退法 (Dropout))。这些全连接层也在帧级上操作。最后,一个具 有 Sigmoid 激活函数的全连接分类层每 16ms 输出 Kmax-维的说话人活性值,取值范围为 0 到 1。总体而言,我们 的模型包含 150 万个可训练参数——其中绝大部分(140 万个)来自循环层。

如第 [2.2](#page-1-4) 节所介绍,50% 的训练样本由两个片段的加 权和构成,其信号-信号比在 0 到 10dB 之间均匀采样。我 们还使用来自 MUSAN 数据集 [\[20](#page-3-18)] 的加性背景噪声,其 信号-噪声比在 5 到 15dB 之间均匀采样。

我们使用 *Adam* 优化器,采用 *PyTorch* 的默认参数, 并以批量大小为 128 进行模型训练。学习率初始值设为 10<sup>−</sup><sup>3</sup>,当其在开发集上的性能达到平台期时,学习率将按 因子 2 减小。使用 4 块 V100 GPU,大约耗时 3 天达到 最佳性能。虽然我们在[huggingface.co/pyannote/segmentation](https://huggingface.co/pyannote/segmentation) 公开预训练模型以便复现结果,但整个训练过程同样可复 现,因为所有内容均已集成至 *pyannote.audio* 开源库版本 2.0 中 [\[16](#page-3-19)]。

## **4. 结果与讨论**

**语音活动检测。**表 [1](#page-2-0) 对比了所提出的语音活动检测方法与 官方 *dihard3* 基准 [[9](#page-3-8)]、*Landini* 在 VoxConverse 挑战赛 中的提交结果 [[12\]](#page-3-11),以及 *pyannote 1.1* 语音活动检测模 型 [\[16](#page-3-19)] 的性能。主要结论是,尽管该模型是为分割任务训 练的,但其表现优于其他专为语音活动检测训练的模型。 然而,需要注意的是,不应轻易对 *silero\_vad* 模型 [[21\]](#page-3-20) 的性能做出判断,因为这是一个现成的模型,并未针对这 些数据集进行专门训练。

**重叠语音检测。**为重叠语音检测任务找到良好且可复现的 基准证明是一项困难的任务。我们感谢 *Kunesova* 等人 [\[3\]](#page-3-2) 和 *Landini* 等人 [[12](#page-3-11)] 共享了他们检测流水线的输出结果。 表 [2](#page-3-21) 中报告的结果显示,与语音活动检测类似,我们的分 割模型即使最初并未为此特定任务进行训练,仍可成功用 于重叠语音检测。该模型的表现优于 *pyannote 1.1* 的重

叠语音检测方法,我们认为这此前是该任务的最新状态 [\[4\]](#page-3-3)。

**重叠感知的重新分割。**尽管我们的分割模型在语音活动检 测和重叠语音检测中均表现出实用性,但其真正优势体现 在对现有说话人聚类流水线输出的后处理上。表 [3](#page-3-22) 总结了 在三个基准流水线上的重新分割实验结果,这些基准按性 能从差到好排序:*pyannote 1.1* 预训练流水线 [\[16\]](#page-3-19)、*dihard3* 官方基准 [\[9\]](#page-3-8) 以及 BUT 的 *VBx* 方法 [\[15](#page-3-14)]。选择这些基准 所采用(尽管存在错误)的准则为使用便捷性和可复现性。 由于 [[15\]](#page-3-14) 中报告的 *VBx* 基准结果依赖于理想语音活动检 测,而共享代码库并未提供官方的语音活动检测实现,因 此我们采用了自有的方法(表 [1](#page-2-0) 中标记为 **Ours**),并在其 基础上应用了 *VBx*。我们提出的重新分割方法在所有数据 集上均持续提升了所有基准的输出效果。相较于最佳基准 (*VBx*),相对说话人聚类错误率改善分别达到 AMI 上的 17%、DIHARD 上的 13%,以及 VoxConverse 上的 13%。

为了便于比较,我们还实现了一种启发式方法,该方 法通过将检测到的重叠语音区域分配给时间上最近的两个 说话人来处理 [\[13](#page-3-12)]。尽管该方法简单,但其恰好成为一个 强大的基准,实际中很难被超越 [[12](#page-3-11)]。然而,在几乎所有实 验条件下,我们提出的重新分割方法均优于该启发式方法 (仅有两种情况下启发式方法略胜一筹,且优势微小)。进 一步分析说话人混淆错误率发现,我们的方法在识别重叠 说话人方面表现显著更优。这一点也得到了在使用理想聚 类结果(y DIA = y)基础上应用该方法时获得的低说话人 混淆错误率的验证:在 AMI、DIHARD 和 VoxConverse 数据集上,分别仅有 1.4%、1.8% 和 0.6% 的语音被错误 重新分配。图 [3](#page-1-2)展示了它们在一段 20 秒短片段上的行为 表现,具有定性参考价值。特别地,可以看出这两种方法 (启发式与所提方法)的行为存在差异,具有互补潜力。

# **5. 结论**

本文报告的整体最佳流水线是我们的语音活动检测、 现成的 VBx 聚类以及我们提出的重分割方法的组合,该 方法能够处理重叠部分,在 AMI Mix-Headset 上达到 DER = 19.9%,使用的是 [\[15](#page-3-14)] 中引入的完整评估设置; 在 DIHARD 3 评估集上达到 DER = 19.3%(完整条件, 比第一名提交结果低 2.6%);在 VoxConverse 开发集上 达到 DER = 7.1%(或在加入 250ms 宽容窗口后达到 DER = 3.4%)。

即使使用了宽容标记,漏检和误报仍是所有三个数据 集中的主要错误来源(错误率是说话人混淆的两倍),这 表明尽管取得了进展,重叠语音检测仍然是一个尚未解决 (有时定义不清)的问题。

表 1: 语音活动检测 *// FA =* 误报率 *(%) /* 漏检率 *(%)*

<span id="page-2-0"></span>

| VAD                 |     | AMI [8, 15] |          |      | DIHARD 3 [9] |          | VoxConverse [11] |       |          |  |  |
|---------------------|-----|-------------|----------|------|--------------|----------|------------------|-------|----------|--|--|
|                     | FA  | Miss.       | FA+Miss. | FA   | Miss.        | FA+Miss. | FA               | Miss. | FA+Miss. |  |  |
| silero_vad          | 9.4 | 1.7         | 11.0     | 17.0 | 4.0          | 21.0     | 3.0              | 1.1   | 4.2      |  |  |
| dihard3 [9]         | NA  | NA          | NA       | 4.0  | 4.2          | 8.2      | NA               | NA    | NA       |  |  |
| Landini et al. [12] | NA  | NA          | NA       | NA   | NA           | NA       | 1.8              | 1.1   | 3.0      |  |  |
| pyannote 1.1 [16]   | 6.5 | 1.7         | 8.2      | 4.1  | 3.8          | 7.9      | 4.5              | 0.3   | 4.8      |  |  |
| Ours – pyannote 2.0 | 3.6 | 3.2         | 6.8      | 3.9  | 3.3          | 7.3      | 1.8              | 0.8   | 2.5      |  |  |

<span id="page-3-21"></span>

| OSD                  |      | AMI [8, 15] |           |        |      |      |       | DIHARD 3 [9] |        |      | VoxConverse [11] |       |           |        |      |  |
|----------------------|------|-------------|-----------|--------|------|------|-------|--------------|--------|------|------------------|-------|-----------|--------|------|--|
|                      | FA   | Miss.       | Precision | Recall | F1   | FA   | Miss. | Precision    | Recall | F1   | FA               | Miss. | Precision | Recall | F1   |  |
| Kunesova et al. [3]  | NA   | NA          | 71.5      | 46.1   | 56.0 | NA   | NA    | NA           | NA     | NA   | NA               | NA    | NA        | NA     | NA   |  |
| Landini et al. [12]  | NA   | NA          | NA        | NA     | NA   | NA   | NA    | NA           | NA     | NA   | 10.4             | 71.8  | 73.0      | 28.2   | 40.7 |  |
| pyannote 1.1 [16, 4] | 51.1 | 12.1        | 63.2      | 87.9   | 73.5 | 48.2 | 45.2  | 53.2         | 54.8   | 54.0 | 130.4            | 17.7  | 38.7      | 82.3   | 52.6 |  |
| Ours – pyannote 2.0  | 16.9 | 29.4        | 80.7      | 70.5   | 75.3 | 46.9 | 37.2  | 57.2         | 62.8   | 59.9 | 26.3             | 24.5  | 74.2      | 75.5   | 74.8 |  |

表 3: 重新分割 *// FA =* 误报 */* 漏检 *=* 漏检 */* 混淆 *=* 说话人混淆 */ DER =* 说话人分离错误率

<span id="page-3-22"></span>

|                     | Overlap-aware             |     | AMI [8, 15] |       |      |     |       | DIHARD 3 [9] |      |     | VoxConverse [11] |       |      |  |
|---------------------|---------------------------|-----|-------------|-------|------|-----|-------|--------------|------|-----|------------------|-------|------|--|
| Baseline            | resegmentation            | FA  | Miss.       | Conf. | DER  | FA  | Miss. | Conf.        | DER  | FA  | Miss.            | Conf. | DER  |  |
| pyannote 1.1 [16]   | _                         | 5.0 | 16.2        | 8.5   | 29.7 | 3.4 | 13.2  | 12.6         | 29.2 | 2.0 | 10.1             | 9.5   | 21.5 |  |
|                     | Heuristic [13] w/ our OSD | 6.9 | 7.9         | 10.9  | 25.7 | 6.3 | 8.9   | 12.8         | 28.1 | 2.8 | 7.3              | 10.1  | 20.3 |  |
|                     | Ours – pyannote 2.0       | 4.0 | 13.0        | 9.1   | 26.1 | 5.1 | 9.8   | 10.3         | 25.2 | 2.4 | 3.1              | 9.8   | 15.4 |  |
| dihard3 [9]         | _                         | NA  | NA          | NA    | NA   | 3.6 | 13.3  | 8.4          | 25.4 | NA  | NA               | NA    | NA   |  |
|                     | Heuristic [13] w/ our OSD | NA  | NA          | NA    | NA   | 6.8 | 8.7   | 8.8          | 24.3 | NA  | NA               | NA    | NA   |  |
|                     | Ours – pyannote 2.0       | NA  | NA          | NA    | NA   | 4.6 | 10.2  | 7.5          | 22.2 | NA  | NA               | NA    | NA   |  |
| VBx [15] w/ our VAD | _                         | 3.1 | 17.2        | 3.8   | 24.1 | 3.6 | 12.5  | 6.2          | 22.3 | 1.7 | 5.1              | 1.4   | 8.3  |  |
|                     | Heuristic [13] w/ our OSD | 5.1 | 8.7         | 6.1   | 19.9 | 7.0 | 7.8   | 6.4          | 21.2 | 2.7 | 2.1              | 2.0   | 6.8  |  |
|                     | Ours – pyannote 2.0       | 4.3 | 10.9        | 4.7   | 19.9 | 4.7 | 9.7   | 4.9          | 19.3 | 2.7 | 2.6              | 1.8   | 7.1  |  |
| Oracle              | Ours – pyannote 2.0       | 4.7 | 10.0        | 1.4   | 16.1 | 4.6 | 9.8   | 1.8          | 16.2 | 2.6 | 2.5              | 0.6   | 5.7  |  |

## **6. References**

- <span id="page-3-0"></span>[1] R. Yin, H. Bredin, and C. Barras, "Speaker Change Detection in Broadcast TV Using Bidirectional Long Short-Term Memory Networks," in *Proc. Interspeech 2017*, 2017.
- <span id="page-3-1"></span>[2] D. Charlet, C. Barras, and J. Liénard, "Impact of overlapping speech detection on speaker diarization for broadcast news and debates," in *2013 IEEE International Conference on Acoustics, Speech and Signal Processing*, May 2013, pp. 7707–7711.
- <span id="page-3-2"></span>[3] M. Kunešová, M. Hrúz, Z. Zajíc, and V. Radová, "Detection of overlapping speech for the purposes of speaker diarization," in *Speech and Computer*, A. A. Salah, A. Karpov, and R. Potapova, Eds. Cham: Springer International Publishing, 2019, pp. 247–257.
- <span id="page-3-3"></span>[4] L. Bullock, H. Bredin, and L. P. Garcia-Perera, "Overlapaware diarization: Resegmentation using neural end-to-end overlapped speech detection," in *Proc. ICASSP 2020*, 2020.
- <span id="page-3-4"></span>[5] Y. Fujita, N. Kanda, S. Horiguchi, K. Nagamatsu, and S. Watanabe, "End-to-End Neural Speaker Diarization with Permutation-free Objectives," in *Interspeech*, 2019, pp. 4300– 4304.
- <span id="page-3-5"></span>[6] Y. Fujita, N. Kanda, S. Horiguchi, Y. Xue, K. Nagamatsu, and S. Watanabe, "End-to-end neural speaker diarization with self-attention," in *2019 IEEE Automatic Speech Recognition and Understanding Workshop (ASRU)*, 2019, pp. 296– 303.
- <span id="page-3-6"></span>[7] Y. Takashima, Y. Fujita, S. Watanabe, S. Horiguchi, P. García, and K. Nagamatsu, "End-to-end speaker diarization conditioned on speech activity and overlap detection," in *2021 IEEE Spoken Language Technology Workshop (SLT)*, 2021, pp. 849–856.
- <span id="page-3-7"></span>[8] J. Carletta, "Unleashing the killer corpus: experiences in creating the multi-everything AMI Meeting Corpus," *Language Resources and Evaluation*, vol. 41, no. 2, 2007.
- <span id="page-3-8"></span>[9] N. Ryant, P. Singh, V. Krishnamohan, R. Varma, K. Church, C. Cieri, J. Du, S. Ganapathy, and M. Liberman, "The Third DIHARD Diarization Challenge," *arXiv preprint arXiv:2012.01477*, 2020.
- <span id="page-3-9"></span>[10] N. Ryant, K. Church, C. Cieri, J. Du, S. Ganapathy, and M. Liberman, "Third DIHARD Challenge Evaluation Plan," *arXiv preprint arXiv:2006.05815*, 2020.

- <span id="page-3-10"></span>[11] J. S. Chung, J. Huh, A. Nagrani, T. Afouras, and A. Zisserman, "Spot the Conversation: Speaker Diarisation in the Wild," in *Proc. Interspeech 2020*, 2020, pp. 299–303. [Online]. Available: [http://dx.doi.org/10.21437/Interspeech.](http://dx.doi.org/10.21437/Interspeech.2020-2337) [2020-2337](http://dx.doi.org/10.21437/Interspeech.2020-2337)
- <span id="page-3-11"></span>[12] F. Landini, O. Glembek, P. Matějka, J. Rohdin, L. Burget, M. Diez, and A. Silnova, "Analysis of the BUT Diarization System for VoxConverse Challenge," in *2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2021.
- <span id="page-3-12"></span>[13] S. Otterson and M. Ostendorf, "E{cient use of overlap information in speaker diarization," in *2007 IEEE Workshop on Automatic Speech Recognition & Understanding (ASRU)*. IEEE, 2007, pp. 683–686.
- <span id="page-3-13"></span>[14] G. Gelly and J.-L. Gauvain, "Optimization of RNN-Based Speech Activity Detection," *IEEE/ACM Transactions on Audio, Speech, and Language Processing*, vol. 26, no. 3, pp. 646–656, March 2018.
- <span id="page-3-14"></span>[15] F. Landini, J. Profant, M. Diez, and L. Burget, "Bayesian hmm clustering of x-vector sequences (vbx) in speaker diarization: theory, implementation and analysis on standard tasks," 2020.
- <span id="page-3-19"></span>[16] H. Bredin, R. Yin, J. M. Coria, G. Gelly, P. Korshunov, M. Lavechin, D. Fustes, H. Titeux, W. Bouaziz, and M.- P. Gill, "pyannote.audio: neural building blocks for speaker diarization," in *Proc. ICASSP 2020*, 2020.
- <span id="page-3-15"></span>[17] S. Horiguchi, P. Garcia, Y. Fujita, S. Watanabe, and K. Nagamatsu, "End-to-end speaker diarization as postprocessing," 2020.
- <span id="page-3-16"></span>[18] H. Bredin, "pyannote.metrics: a toolkit for reproducible evaluation, diagnostic, and error analysis of speaker diarization systems," in *Proc. Interspeech 2017*, Stockholm, Sweden, August 2017. [Online]. Available: [http://pyannote.](http://pyannote.github.io/pyannote-metrics) [github.io/pyannote-metrics](http://pyannote.github.io/pyannote-metrics)
- <span id="page-3-17"></span>[19] M. Ravanelli and Y. Bengio, "Speaker recognition from raw waveform with sincnet," in *Proc. SLT 2018*, 2018.
- <span id="page-3-18"></span>[20] D. Snyder, G. Chen, and D. Povey, "MUSAN: A Music, Speech, and Noise Corpus," 2015.
- <span id="page-3-20"></span>[21] Silero Team, "Silero VAD: pre-trained enterprise-grade Voice Activity Detector (VAD), Number Detector and Language Classi}er," [https://github.com/snakers4/silero-vad,](https://github.com/snakers4/silero-vad) 2021.