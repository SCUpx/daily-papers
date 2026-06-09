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

## 2026-06-10

## Bayesian optimization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Improving Bayesian Optimization via Training-Aware Conditional Diffusion Models](https://arxiv.org/abs/2606.08438v1)** | ⭐ 82/100 | 提出基于扩散模型的贝叶斯优化方法 | 创新性强，理论严谨，实验效果显著，具有较高学术价值。 | <details><summary>展开</summary>Bayesian optimization (BO) is a widely used approach for black-box optimization that uses a Gaussian process (GP) as a surrogate and guides sequential evaluations via an acquisition function, with the ultimate goal of locating the global optimum $\mathbf{x}^{\star}$. To align with this goal, information-based acquisition functions such as Predictive Entropy Search (PES) model $\mathbf{x}^{\star}$ as a random variable and reduce the entropy of its distribution, but approximating this distribution via traditional GP posterior sampling is computationally expensive. To address this limitation, we leverage Conditional Diffusion Models (CDMs) to efficiently approximate the distribution of $\mathbf{x}^{\star}$ and develop BO-inherent training strategies for CDMs. Motivated by the structural properties of the CDM-learned distribution, we further develop an acquisition strategy termed Diffusion-based Mode Seeking (DMS) to guide the sequential evaluation. We establish a sub-optimality guarantee for the CDM-learned distribution and demonstrate through extensive experiments that DMS outperforms standard BO baselines.</details> |
| **[Boundary Variance Inflation Causes Acquisition Bias in Gaussian Processes](https://arxiv.org/abs/2606.07561v1)** | ⭐ 82/100 | 揭示高斯过程边界方差膨胀及其对采集函数的影响 | 深入分析了边界效应的几何机制，并提出了有效的诊断方法。 | <details><summary>展开</summary>Gaussian processes with stationary kernels on bounded domains exhibit inflated posterior variance near the boundary. Despite being a long-recognized artifact in geostatistics and a source of over-exploration in Bayesian optimization, the causes and effects of boundary-induced acquisition bias are underexplored. We trace the root cause to a simple geometric mechanism: the truncation of the kernel correlation neighborhood at the domain boundary creates an observation-independent distortion that worsens with dimensionality. We show how this distortion manifests across three acquisition classes: variance maximization concentrates selections at the corners, whereas negative integrated posterior variance and expected predictive information gain move selections inward to axis-aligned interior shells. These patterns arise without reference to any objective function, meaning that acquisition behavior can be dominated by kernel geometry rather than the desired task-specific uncertainty. To quantify this, we introduce a function-free selection-profile diagnostic for arbitrary acquisitions, kernels, and bounded-domain geometries.</details> |
| **[In-Context Learning for Latent Space Bayesian Optimization](https://arxiv.org/abs/2606.09664v1)** | ⭐ 78/100 | 提出LSBO专用上下文学习模型 | 通过预训练适配解决LSBO分布失配，方法创新且实验扎实。 | <details><summary>展开</summary>Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO creates a distinctive mismatch: the induced map from latent code to objective value differs markedly from the regression tasks used to train current in-context models. We address this mismatch by complementing the pretraining stage of tabular foundation model surrogates with synthetic optimization tasks defined on the latent space of a molecular VAE. The continued-pretraining objective features a regularizer that anchors the model to the original checkpoint, preserving its broad regression prior while avoiding overspecialization to the adaptation tasks. On held-out molecular optimization benchmarks, the resulting model achieves strong performance, supporting the relevance of LSBO-specific adaptation for in-context surrogates.</details> |
| **[Bayesian Optimization of a Multi-Product Chemical Reactor Using Composite Models and Partial Physics Knowledge](https://arxiv.org/abs/2606.08611v1)** | ⭐ 78/100 | 融合物理约束的贝叶斯优化方法 | 通过复合模型与物理残差提升了化工过程优化的效率与安全性 | <details><summary>展开</summary>We study data-driven real-time economic optimization of a multi-product chemical reactor when no reliable first-principles model is available beyond a steady-state energy balance. Instead of learning the economic objective directly as a black-box function, we use a composite formulation in which Gaussian process (GP) models predict physically meaningful outputs, including product concentrations and reactor temperature, while profit is computed analytically from these predictions together with raw-material, product, and utility prices. This preserves the structure of the economic objective, makes it parametric in changing prices without needing retraining, and allows candidate operating points to be checked against the available energy balance through a physics residual. The GPs also provide predictive uncertainty, which is exploited in a Bayesian optimization (BO) framework both for data-efficient exploration and for conservative enforcement of the reactor temperature constraint through an upper confidence bound. The acquisition function additionally penalizes large energy-balance mismatch obtained by substituting the GP-predicted outputs and candidate inputs into the available steady-state energy balance. The approach is demonstrated on a benchmark simulation of a non-isothermal multi-product reactor. Relative to a trust-region safe BO implementation, the proposed method achieves better simulated economic performance within the available iteration budget. Relative to a purely data-driven BO approach that does not use the available physics information, it avoids reactor temperature constraint violations.</details> |

## Mixed lubrication

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Quantitative measurement of fluid inertial effects in confined Brownian motion](https://arxiv.org/abs/2606.09193v1)** | ⭐ 82/100 | 揭示受限布朗运动中惯性效应的物理机制 | 结合实验与模拟，严谨解析了受限流体惯性力贡献 | <details><summary>展开</summary>The hydrodynamic response of Brownian particles in liquids is fundamentally altered by inertial forces arising from unsteady momentum transport in the surrounding fluid. These forces are of two distinct types\,: the added mass and the history effect. While both are well understood in bulk and weakly-confined geometries, under deterministic driving, their respective behaviours under strong confinement and thermal fluctuations remain scarcely addressed, unclear and often entangled together. The goal of the present study is thus to fill this fundamental gap. The behaviours of the two distinct inertial contributions are quantitatively investigated in the vicinity of a flat, rigid wall, using a combination of broadrange thermal colloidal-probe atomic-force-microscopy experiments, advanced numerical simulations and theory. The separation of the added-mass and history-force contributions is achieved through their different frequency-scaling signatures within the measured high-resolution thermal spectra. Our results establish a complete picture of Brownian motion at interfaces, in the lubrication regime, with direct relevance to nanofluidics and interfacial biophysics.</details> |

