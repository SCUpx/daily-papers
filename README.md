# Daily Papers - 自动化每日精选 arxiv 论文

**自动抓取ArXiv论文，使用 Google Gemini 评分筛选高质量内容**

专为 **计算机科学学者/程序员** 设计

## ✨ 特性

- **🆓 完全免费** - 使用 Google AI Studio 免费 API
- **🤖 自动运行** - GitHub Actions 每天自动运行
- **🎯 智能评分** - 四维度评估（0-100分）
- **💡 AI摘要** - 自动生成论文核心贡献摘要

## 🚀 快速开始

1. **Fork 本仓库**
2. **配置 API Key** - 添加 `GOOGLE_AI_API_KEY` 到 GitHub Secrets（[获取地址](https://aistudio.google.com/apikey)）
3. **启用 Actions** - Actions → Daily Papers → Enable workflow
4. **订阅通知** - Watch → All Activity

完成！系统每天 UTC 17:00（北京时间 1:00）自动运行。

📖 **详细设置请查看 [SETUP.md](SETUP.md)**

## 📚 历史论文

查看所有历史精选论文：[papers](papers/)

---

<!-- PAPERS_START -->

## 2026-05-26

## Bayesian optimization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Gradient-Informed Bayesian and Interior Point Optimization for Efficient Inverse Design in Nanophotonics](https://arxiv.org/abs/2602.18148v2)** | ⭐ 86/100 | 提出BONNI算法用于光子器件逆设计 | 新颖性高，实用性强，方法严谨，表述清晰 | <details><summary>展开</summary>Inverse design, particularly geometric shape optimization, provides a systematic approach for developing high-performance nanophotonic devices. While numerous optimization algorithms exist, previous global approaches exhibit slow convergence and conversely local search strategies frequently become trapped in local optima. To address the limitations inherent to both local and global approaches, we introduce BONNI: Bayesian optimization through neural network ensemble surrogates with interior point optimization. It augments global optimization with an efficient incorporation of gradient information to determine optimal sampling points. This capability allows BONNI to circumvent the local optima found in many nanophotonic applications, while capitalizing on the efficiency of gradient-based optimization. We demonstrate BONNI's capabilities in the design of a distributed Bragg reflector as well as a dual-layer grating coupler through an exhaustive comparison against other optimization algorithms commonly used in literature. Using BONNI, we were able to design a 10-layer distributed Bragg reflector with only 4.5% mean spectral error, compared to the previously reported results of 7.8% error with 16 layers. Further designs of a broadband waveguide taper and photonic crystal waveguide transition validate the capabilities of BONNI.</details> |
| **[LAGO: A Local-Global Optimization Framework Combining Trust Region Methods and Bayesian Optimization](https://arxiv.org/abs/2603.02970v1)** | ⭐ 82/100 | LAGO结合了贝叶斯优化和信任域方法 | 新颖的混合优化框架，在探索和利用之间取得了良好平衡，具有较高的实用性和清晰度。 | <details><summary>展开</summary>We introduce LAGO, a LocAl-Global Optimization algorithm that combines gradient-enhanced Bayesian Optimization (BO) with gradient-based trust region local refinement through an adaptive competition mechanism. At each iteration, global and local optimization strategies independently propose candidate points, and the next evaluation is selected based on predicted improvement. LAGO separates global exploration from local refinement at the proposal level: the BO acquisition function is optimized outside the active trust region, while local function and gradient evaluations are incorporated into the global gradient-enhanced Gaussian process only when they satisfy a lengthscale-based minimum-distance criterion, reducing the risk of numerical instability during the local exploitation. This enables efficient local refinement when reaching promising regions, without sacrificing a global search of the design space. As a result, the method achieves an improved exploration of the full design space compared to standard non-linear local optimization algorithms for smooth functions, while maintaining fast local convergence in regions of interest.</details> |
| **[Deep learning-guided evolutionary optimization for protein design](https://arxiv.org/abs/2603.02753v1)** | ⭐ 82/100 | 提出结合贝叶斯优化与遗传算法的蛋白质设计框架 | 新颖性高，实用性强，方法严谨，表述清晰，综合评分较高 | <details><summary>展开</summary>Designing novel proteins with desired characteristics remains a significant challenge due to the large sequence space and the complexity of sequence-function relationships. Efficient exploration of this space to identify sequences that meet specific design criteria is crucial for advancing therapeutics and biotechnology. Here, we present BoGA (Bayesian Optimization Genetic Algorithm), a framework that combines evolutionary search with Bayesian optimization to efficiently navigate the sequence space. By integrating a genetic algorithm as a stochastic proposal generator within a surrogate modeling loop, BoGA prioritizes candidates based on prior evaluations and surrogate model predictions, enabling data-efficient optimization. We demonstrate the utility of BoGA through benchmarking on sequence and structure design tasks, followed by its application in designing peptide binders against pneumolysin, a key virulence factor of \textit{Streptococcus pneumoniae}. BoGA accelerates the discovery of high-confidence binders, demonstrating the potential for efficient protein design across diverse objectives. The algorithm is implemented within the BoPep suite and is available under an MIT license at \href{https://github.com/ErikHartman/bopep}{GitHub}.</details> |
| **[Randomized Kriging Believer for Parallel Bayesian Optimization with Regret Bounds](https://arxiv.org/abs/2603.01470v2)** | ⭐ 82/100 | 提出随机克里金信念并行贝叶斯优化方法 | 新颖性高，理论实验俱佳，实用性强，清晰易懂 | <details><summary>展开</summary>We consider an optimization problem of an expensive-to-evaluate black-box function, in which we can obtain noisy function values in parallel. For this problem, parallel Bayesian optimization (PBO) is a promising approach, which aims to optimize with fewer function evaluations by selecting a diverse input set for parallel evaluation. However, existing PBO methods suffer from poor practical performance or lack theoretical guarantees. In this study, we propose a PBO method, called randomized kriging believer (KB), based on a well-known KB heuristic and inheriting the advantages of the original KB: low computational complexity, a simple implementation, versatility across various BO methods, and applicability to asynchronous parallelization. Furthermore, we show that our randomized KB achieves Bayesian expected regret guarantees. We demonstrate the effectiveness of the proposed method through experiments on synthetic and benchmark functions and emulators of real-world data.</details> |
| **[Human-AI Collaborative Autonomous Experimentation With Proxy Modeling for Comparative Observation](https://arxiv.org/abs/2603.12618v1)** | ⭐ 78/100 | 提出代理模型贝叶斯优化实现人机协作自主实验 | 新颖性高，实用性强，方法严谨，表述清晰，人机协作是亮点 | <details><summary>展开</summary>Optimization for different tasks like material characterization, synthesis, and functional properties for desired applications over multi-dimensional control parameters need a rapid strategic search through active learning such as Bayesian optimization (BO). However, such high-dimensional experimental physical descriptors are complex and noisy, from which realization of a low-dimensional mathematical scalar metrics or objective functions can be erroneous. Moreover, in traditional purely data-driven autonomous exploration, such objective functions often ignore the subtle variation and key features of the physical descriptors, thereby can fail to discover unknown phenomenon of the material systems. To address this, here we present a proxy-modelled Bayesian optimization (px-BO) via on-the-fly teaming between human and AI agents. Over the loop of BO, instead of defining a mathematical objective function directly from the experimental data, we introduce a voting system on the fly where the new experimental outcome will be compared with existing experiments, and the human agents will choose the preferred samples. These human-guided comparisons are then transformed into a proxy-based objective function via fitting Bradley-Terry (BT) model. Then, to minimize human interaction, this iteratively trained proxy model also acts as an AI agent for future surrogate human votes. Finally, these surrogate votes are periodically validated by human agents, and the corrections are then learned by the proxy model on-the-fly. We demonstrated the performance of the proposed px-BO framework into simulated and BEPS data generated from PTO sample. We find that our approach provided better control of the domain experts for an improved search over traditional data-driven exploration, thus, signifies the importance of human-AI teaming in an accelerated and meaningful material space exploration.</details> |

