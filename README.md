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

## 2026-05-25

## Bayesian optimization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[BOxCrete: A Bayesian Optimization Open-Source AI Model for Concrete Strength Forecasting and Mix Optimization](https://arxiv.org/abs/2603.21525v1)** | ⭐ 78/100 | 开源贝叶斯优化混凝土配比模型 | 模型开源且预测精度高，但数据集规模相对有限。 | <details><summary>展开</summary>Modern concrete must simultaneously satisfy evolving demands for mechanical performance, workability, durability, and sustainability, making mix designs increasingly complex. Recent studies leveraging Artificial Intelligence (AI) and Machine Learning (ML) models show promise for predicting compressive strength and guiding mix optimization, but most existing efforts are based on proprietary industrial datasets and closed-source implementations. Here we introduce BOxCrete, an open-source probabilistic modeling and optimization framework trained on a new open-access dataset of over 500 strength measurements (1-15 ksi) from 123 mixtures - 69 mortar and 54 concrete mixes tested at five curing ages (1, 3, 5, 14, and 28 days). BOxCrete leverages Gaussian Process (GP) regression to predict strength development, achieving average R$^2$ = 0.94 and RMSE = 0.69 ksi, quantify uncertainty, and carry out multi-objective optimization of compressive strength and embodied carbon. The dataset and model establish a reproducible open-source foundation for data-driven development of AI-based optimized mix designs.</details> |
| **[Bayesian Scattering: A Principled Baseline for Uncertainty on Image Data](https://arxiv.org/abs/2603.20908v1)** | ⭐ 78/100 | 提出贝叶斯散射作为图像不确定性基准 | 方法创新且实用，为复杂模型提供了稳健的基准参考 | <details><summary>展开</summary>Uncertainty quantification for image data is dominated by complex deep learning methods, yet the field lacks an interpretable, mathematically grounded baseline. We propose Bayesian scattering to fill this gap, serving as a first-step baseline akin to the role of Bayesian linear regression for tabular data. Our method couples the wavelet scattering transform-a deep, non-learned feature extractor-with a simple probabilistic head. Because scattering features are derived from geometric principles rather than learned, they avoid overfitting the training distribution. This helps provide sensible uncertainty estimates even under significant distribution shifts. We validate this on diverse tasks, including medical imaging under institution shift, wealth mapping under country-to-country shift, and Bayesian optimization of molecular properties. Our results suggest that Bayesian scattering is a solid baseline for complex uncertainty quantification methods.</details> |
| **[Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model](https://arxiv.org/abs/2603.18342v1)** | ⭐ 78/100 | 提出基于关键时刻的VLA模型不确定性量化方法 | 通过滑动窗口与运动加权提升了机器人故障预测的准确性 | <details><summary>展开</summary>Vision-Language-Action (VLA) models enable general-purpose robotic policies by mapping visual observations and language instructions to low-level actions, but they often lack reliable introspection. A common practice is to compute a token-level uncertainty signal and take its mean over a rollout. However, mean aggregation can dilute short-lived but safety-critical uncertainty spikes in continuous control. In particular, successful rollouts may contain localized high-entropy segments due to benign noise or non-critical micro-adjustments, while failure rollouts can appear low-entropy for most timesteps and only exhibit brief spikes near the onset of failure. We propose a unified uncertainty quantification approach for predicting rollout success versus failure that (1) uses max-based sliding window pooling to preserve transient risk signals, (2) applies motion-aware stability weighting to emphasize high-frequency action oscillations associated with unstable behaviors, and (3) performs DoF-adaptive calibration via Bayesian Optimization to prioritize kinematically critical axes. Experiments on the LIBERO benchmark show that our method substantially improves failure prediction accuracy and yields more reliable signals for failure detection, which can support downstream human-in-the-loop interventions.</details> |
| **[Maximum-Projection-Based Bayesian Optimization Utilizing Sensitivity Analysis for High-Efficiency Radial Turbine Design with Scarce Data](https://arxiv.org/abs/2603.17516v1)** | ⭐ 78/100 | 基于敏感性分析的贝叶斯优化提升径流涡轮效率 | 方法创新且实用，通过降维优化显著提升了设计效率。 | <details><summary>展开</summary>We propose a data-efficient workflow to optimize the efficiency of a radial turbine design under a strict budget of high-fidelity computational fluid dynamics simulations. Assuming anisotropic parameter impact, we use a maximum-projection initial experimental design to ensure space-filling and strong projection properties on low-dimensional subspaces. Bayesian optimization is performed using Gaussian process surrogates with an upper confidence bound acquisition function. In parallel, polynomial chaos expansions provide variance-based global sensitivity analysis metrics, which allow to identify a reduced subspace with the most influential parameters, wherein the optimization is continued. Turbine efficiency is increased from 85.77% initially to 91.77% at the end of the workflow, with a total budget of 330 simulations.</details> |
| **[CASHomon Sets: Efficient Rashomon Sets Across Multiple Model Classes and their Hyperparameters](https://arxiv.org/abs/2603.15321v1)** | ⭐ 78/100 | 提出CASHomon集以跨模型类评估预测多重性 | 创新性地将Rashomon集扩展至CASH场景，理论与实验扎实。 | <details><summary>展开</summary>Rashomon sets are model sets within one model class that perform nearly as well as a reference model from the same model class. They reveal the existence of alternative well-performing models, which may support different interpretations. This enables selecting models that match domain knowledge, hidden constraints, or user preferences. However, efficient construction methods currently exist for only a few model classes. Applied machine learning usually searches many model classes, and the best class is unknown beforehand. We therefore study Rashomon sets in the combined algorithm selection and hyperparameter optimization (CASH) setting and call them CASHomon sets. We propose TruVaRImp, a model-based active learning algorithm for level set estimation with an implicit threshold, and provide convergence guarantees. On synthetic and real-world datasets, TruVaRImp reliably identifies CASHomon sets members and matches or outperforms naive sampling, Bayesian optimization, classical and implicit level set estimation methods, and other baselines. Our analyses of predictive multiplicity and feature-importance variability across model classes question the common practice of interpreting data through a single model class.</details> |

