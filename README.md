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

## 2026-06-09

## Bayesian optimization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[$α$-PFN: Fast Entropy Search via In-Context Learning](https://arxiv.org/abs/2606.07134v1)** | ⭐ 74/100 | 使用PFN实现贝叶斯优化中熵搜索采集函数的快速近似。 | 通过两阶段摊销策略将复杂的蒙特卡洛估计转化为单次前向传播，大幅提速。 | <details><summary>展开</summary>Information-theoretic acquisition functions such as Entropy Search (ES) offer a principled exploration-exploitation framework for Bayesian optimization (BO). However, their practical implementation relies on complicated and slow approximations, i.e., a Monte Carlo estimation of the information gain. This complexity can introduce numerical errors and requires specialized, hand-crafted implementations. We propose a two-stage amortization strategy that learns to approximate entropy search-based acquisition functions using Prior-data Fitted Networks (PFNs) in a single forward pass. A first PFN is trained to be conditioned on information about the optima; second, the $α$-PFN is trained to predict the expected information gain by training on information gains measured with the first PFN. The $α$-PFN offers a flexible learned approximation, which replaces the complex heuristic approximations with a single forward pass per candidate, enabling rapid and extensible acquisition evaluation. Empirically, our approach is competitive with state-of-the-art entropy search implementations on synthetic and real-world benchmarks, while accelerating the different entropy search variants across all our experiments, with speed ups over 50x. Source code: https://github.com/automl/AlphaPFN.</details> |
| **[SEMIKHORN: Globally balanced affinities for mmWave Localization in MU mMIMO systems](https://arxiv.org/abs/2606.06640v1)** | ⭐ 73/100 | 提出基于t-SNEkhorn的半监督信道图谱框架，实现高精度毫米波定位。 | 创新性地引入双随机相似度度量，结合贝叶斯优化，在低标签率下表现优异。 | <details><summary>展开</summary>This work conceives SEMIKHORN, a semisupervised channel charting (CC) framework for mmWave localization, which leverages t-SNEkhorn, a doubly stochastic variant of t-distributed Stochastic Neighbor Embedding (t-SNE) that utilizes entropic optimal transport to construct pairwise similarities. Unlike standard t-SNE, which normalizes affinities independently for each data point, t-SNEkhorn generates globally balanced similarities ensuring consistent neighborhood representation. We consider wireless networks with distributed base stations (BSs) equipped with multiple antennas, where each BS constructs a local dissimilarity matrix from the channel state information (CSI). These local dissimilarity matrices are then fused to obtain a single global dissimilarity matrix, which is processed through manifold learning to embed users onto a geometric map. The performance is evaluated in a simulated outdoor environment, and Bayesian optimization is employed on the framework hyperparameters to minimize the mean localization error (MLE). Experimental results demonstrate that the proposed framework achieves an MLE of 6.86% in a circular vicinity of radius 100m, requiring less than 15% of labeled CSI samples.</details> |

