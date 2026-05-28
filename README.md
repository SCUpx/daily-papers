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

## 2026-05-29

## Bayesian optimization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[A comparative study of transformer models and recurrent neural networks for path-dependent composite materials](https://arxiv.org/abs/2603.00092v1)** | ⭐ 78/100 | 对比Transformer与RNN在复合材料路径依赖建模中的性能 | 系统性对比了两种架构，实验设计严谨，结论对工程应用有参考价值。 | <details><summary>展开</summary>Accurate modeling of Short Fiber Reinforced Composites (SFRCs) remains computationally expensive for full-field simulations. Data-driven surrogate models using Artificial Neural Networks (ANNs) have been proposed as an efficient alternative to numerical modeling, where Recurrent Neural Networks (RNNs) are increasingly being used for path-dependent multiscale modeling by predicting the homogenized response of a Representative Volume Element (RVE). However, recently, transformer models have been developed and they offer scalability and efficient parallelization, yet have not been systematically compared with RNNs in this field. In this study, we perform a systematic comparison between RNNs and transformer models trained on sequences of homogenized response of SFRC RVEs. We study the effect on two types of hyperparameters, namely architectural hyperparameters (such as the number of GRU layers, hidden size, number of attention heads, and encoder blocks) and training hyperparameters (such as learning rate and batch size). Both sets of hyperparameters are tuned using Bayesian optimization. We then analyze scaling laws with respect to dataset size and inference accuracy in interpolation and extrapolation regimes. The results show that while transformer models remain competitive in terms of accuracy on large datasets, the RNNs demonstrate better accuracy on small datasets and show better extrapolation performance. Furthermore, under extrapolation, there is a clear difference, where the RNN remains accurate, while the transformer model performs poorly. On the other hand, the transformer model is 7 times faster at inference, requiring 0.5 ms per prediction compared to the 3.5 ms per prediction for the RNN model.</details> |
| **[A Bayesian Approach to Low-Discrepancy Subset Selection](https://arxiv.org/abs/2602.14607v1)** | ⭐ 78/100 | 提出基于贝叶斯优化的子集选择方法 | 证明了核差异子集选择的NP难性，方法创新且实用。 | <details><summary>展开</summary>Low-discrepancy designs play a central role in quasi-Monte Carlo methods and are increasingly influential in other domains such as machine learning, robotics and computer graphics, to name a few. In recent years, one such low-discrepancy construction method called subset selection has received a lot of attention. Given a large population, one optimally selects a small low-discrepancy subset with respect to a discrepancy-based objective. Versions of this problem are known to be NP-hard. In this text, we establish, for the first time, that the subset selection problem with respect to kernel discrepancies is also NP-hard. Motivated by this intractability, we propose a Bayesian Optimization procedure for the subset selection problem utilizing the recent notion of deep embedding kernels. We demonstrate the performance of the BO algorithm to minimize discrepancy measures and note that the framework is broadly applicable any design criteria.</details> |
| **[Weighted Wasserstein Barycenter of Gaussian Processes for exotic Bayesian Optimization tasks](https://arxiv.org/abs/2602.09181v1)** | ⭐ 78/100 | 提出W2BGP框架统一多种贝叶斯优化任务 | 创新性强，通过Wasserstein重心统一了多种BO变体，方法论严谨。 | <details><summary>展开</summary>Exploiting the analogy between Gaussian Distributions and Gaussian Processes' posterior, we present how the weighted Wasserstein Barycenter of Gaussian Processes (W2BGP) can be used to unify, under a common framework, different exotic Bayesian Optimization (BO) tasks. Specifically, collaborative/federated BO, (synchronous) batch BO, and multi-fidelity BO are considered in this paper. Our empirical analysis proves that each one of these tasks requires just an appropriate weighting schema for the W2BGP, while the entire framework remains untouched. Moreover, we demonstrate that the most well-known BO acquisition functions can be easily re-interpreted under the proposed framework and also enable a more computationally efficient way to deal with the computation of the Wasserstein Barycenter, compared with state-of-the-art methods from the Machine Learning literature. Finally, research perspectives branching from the proposed approach are presented.</details> |
| **[Sequential versus Manifold Bayesian Optimization under Realistic Experimental Time Constraints](https://arxiv.org/abs/2602.07753v1)** | ⭐ 78/100 | 提出考虑实验时间的贝叶斯优化评估框架 | 方法创新且实用，通过时间建模优化实验策略，严谨性高。 | <details><summary>展开</summary>Bayesian optimization (BO) is widely used for autonomous materials discovery, yet its classical sequential formulation is insufficient for design of experimental workflows that often combine parallel or batch synthesis with inherently serial characterization. Methods such as combinatorial spread libraries and printed libraries sample a defined low-D manifold in the chemical space of the system. Here, we introduce a time-aware framework for comparing sequential and manifold BO under experimentally realistic constraints. By explicitly modeling synthesis and characterization times, we define an effective experimental time metric that enables fair, time-normalized benchmarking of optimization strategies. Using numerical experiments in ternary and quaternary compositional spaces, we show that sequential BO remains optimal for short-term experiments or when batching provides no effective time advantage, whereas manifold BO becomes favorable once multiplexed synthesis enables faster accumulation of measurements. We identify a small set of physically interpretable parameters that govern the transition between these regimes. These results establish a general, experimentally grounded framework for selecting optimization strategies in self-driving laboratories and autonomous materials discovery workflows. The accompanying analysis code is publicly available at https://github.com/Slautin/2025_GP_BO_Manifolds.</details> |
| **[Selecting Hyperparameters for Tree-Boosting](https://arxiv.org/abs/2602.05786v1)** | ⭐ 78/100 | 实证对比树提升算法的超参数优化方法 | 通过大规模数据集对比评估了多种优化算法，结论实用且严谨。 | <details><summary>展开</summary>Tree-boosting is a widely used machine learning technique for tabular data. However, its out-of-sample accuracy is critically dependent on multiple hyperparameters. In this article, we empirically compare several popular methods for hyperparameter optimization for tree-boosting including random grid search, the tree-structured Parzen estimator (TPE), Gaussian-process-based Bayesian optimization (GP-BO), Hyperband, the sequential model-based algorithm configuration (SMAC) method, and deterministic full grid search using $59$ regression and classification data sets. We find that the SMAC method clearly outperforms all the other considered methods. We further observe that (i) a relatively large number of trials larger than $100$ is required for accurate tuning, (ii) using default values for hyperparameters yields very inaccurate models, (iii) all considered hyperparameters can have a material effect on the accuracy of tree-boosting, i.e., there is no small set of hyperparameters that is more important than others, and (iv) choosing the number of boosting iterations using early stopping yields more accurate results compared to including it in the search space for regression tasks.</details> |

