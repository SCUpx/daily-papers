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

## 2026-05-11

## Bayesian optimization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Adaptive Acquisition Selection for Bayesian Optimization with Large Language Models](https://arxiv.org/abs/2602.07904v1)** | ⭐ 82/100 | 利用LLM实现贝叶斯优化采集函数自适应选择 | 方法创新且实验详实，有效提升了优化效率。 | <details><summary>展开</summary>Bayesian Optimization critically depends on the choice of acquisition function, but no single strategy is universally optimal; the best choice is non-stationary and problem-dependent. Existing adaptive portfolio methods often base their decisions on past function values while ignoring richer information like remaining budget or surrogate model characteristics. To address this, we introduce LMABO, a novel framework that casts a pre-trained Large Language Model (LLM) as a zero-shot, online strategist for the BO process. At each iteration, LMABO uses a structured state representation to prompt the LLM to select the most suitable acquisition function from a diverse portfolio. In an evaluation across 50 benchmark problems, LMABO demonstrates a significant performance improvement over strong static, adaptive portfolio, and other LLM-based baselines. We show that the LLM's behavior is a comprehensive strategy that adapts to real-time progress, proving its advantage stems from its ability to process and synthesize the complete optimization state into an effective, adaptive policy.</details> |
| **[Nonparametric Bayesian Optimization for General Rewards](https://arxiv.org/abs/2602.07411v1)** | ⭐ 82/100 | 提出无限高斯过程以实现通用奖励贝叶斯优化 | 创新性强且理论严谨，解决了复杂噪声下的优化难题 | <details><summary>展开</summary>This work focuses on Bayesian optimization (BO) under reward model uncertainty. We propose the first BO algorithm that achieves no-regret guarantee in a general reward setting, requiring only Lipschitz continuity of the objective function and accommodating a broad class of measurement noise. The core of our approach is a novel surrogate model, termed as infinite Gaussian process ($\infty$-GP). It is a Bayesian nonparametric model that places a prior on the space of reward distributions, enabling it to represent a substantially broader class of reward models than classical Gaussian process (GP). The $\infty$-GP is used in combination with Thompson Sampling (TS) to enable effective exploration and exploitation. Correspondingly, we develop a new TS regret analysis framework for general rewards, which relates the regret to the total variation distance between the surrogate model and the true reward distribution. Furthermore, with a truncated Gibbs sampling procedure, our method is computationally scalable, incurring minimal additional memory and computational complexities compared to classical GP. Empirical results demonstrate state-of-the-art performance, particularly in settings with non-stationary, heavy-tailed, or other ill-conditioned rewards.</details> |
| **[BONSAI: Bayesian Optimization with Natural Simplicity and Interpretability](https://arxiv.org/abs/2602.07144v1)** | ⭐ 82/100 | 提出默认配置感知的贝叶斯优化方法 | 方法创新且理论完备，兼顾了优化性能与可解释性。 | <details><summary>展开</summary>Bayesian optimization (BO) is a popular technique for sample-efficient optimization of black-box functions. In many applications, the parameters being tuned come with a carefully engineered default configuration, and practitioners only want to deviate from this default when necessary. Standard BO, however, does not aim to minimize deviation from the default and, in practice, often pushes weakly relevant parameters to the boundary of the search space. This makes it difficult to distinguish between important and spurious changes and increases the burden of vetting recommendations when the optimization objective omits relevant operational considerations. We introduce BONSAI, a default-aware BO policy that prunes low-impact deviations from a default configuration while explicitly controlling the loss in acquisition value. BONSAI is compatible with a variety of acquisition functions, including expected improvement and upper confidence bound (GP-UCB). We theoretically bound the regret incurred by BONSAI, showing that, under certain conditions, it enjoys the same no-regret property as vanilla GP-UCB. Across many real-world applications, we empirically find that BONSAI substantially reduces the number of non-default parameters in recommended configurations while maintaining competitive optimization performance, with little effect on wall time.</details> |
| **[Supercharging Simulation-Based Inference for Bayesian Optimal Experimental Design](https://arxiv.org/abs/2602.06900v1)** | ⭐ 82/100 | 提出基于SBI的BOED新框架与优化策略 | 创新性强，方法论严谨，在基准测试中表现优异。 | <details><summary>展开</summary>Bayesian optimal experimental design (BOED) seeks to maximize the expected information gain (EIG) of experiments. This requires a likelihood estimate, which in many settings is intractable. Simulation-based inference (SBI) provides powerful tools for this regime. However, existing work explicitly connecting SBI and BOED is restricted to a single contrastive EIG bound. We show that the EIG admits multiple formulations which can directly leverage modern SBI density estimators, encompassing neural posterior, likelihood, and ratio estimation. Building on this perspective, we define a novel EIG estimator using neural likelihood estimation. Further, we identify optimization as a key bottleneck of gradient based EIG maximization and show that a simple multi-start parallel gradient ascent procedure can substantially improve reliability and performance. With these innovations, our SBI-based BOED methods are able to match or outperform by up to $22\%$ existing state-of-the-art approaches across standard BOED benchmarks.</details> |
| **[Principle-Evolvable Scientific Discovery via Uncertainty Minimization](https://arxiv.org/abs/2602.06448v1)** | ⭐ 82/100 | 提出PiEvo框架实现科学原理的演化与发现 | 创新性强，通过贝叶斯优化提升科学发现效率，实验严谨。 | <details><summary>展开</summary>Large Language Model (LLM)-based scientific agents have accelerated scientific discovery, yet they often suffer from significant inefficiencies due to adherence to fixed initial priors. Existing approaches predominantly operate within a static hypothesis space, which restricts the discovery of novel phenomena, resulting in computational waste when baseline theories fail. To address this, we propose shifting the focus from searching hypotheses to evolving the underlying scientific principles. We present PiEvo, a principle-evolvable framework that treats scientific discovery as Bayesian optimization over an expanding principle space. By integrating Information-Directed Hypothesis Selection via Gaussian Process and an anomaly-driven augmentation mechanism, PiEvo enables agents to autonomously refine their theoretical worldview. Evaluation across four benchmarks demonstrates that PiEvo (1) achieves an average solution quality of up to 90.81%~93.15%, representing a 29.7%~31.1% improvement over the state-of-the-art, (2) attains an 83.3% speedup in convergence step via significantly reduced sample complexity by optimizing the compact principle space, and (3) maintains robust performance across diverse scientific domains and LLM backbones.</details> |

