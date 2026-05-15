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

## 2026-05-16

## Bayesian optimization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Bayesian Model Merging](https://arxiv.org/abs/2605.12843v1)** | ⭐ 88/100 | 提出贝叶斯模型合并框架，实现高效多任务模型融合。 | 方法创新且实验扎实，在多任务合并领域表现优异。 | <details><summary>展开</summary>Model merging aims to combine multiple task-specific expert models into a single model without joint retraining, offering a practical alternative to multi-task learning when data access or computational budget is limited. Existing methods, however, face two key limitations: (1) they overlook the valuable inductive bias of strong anchor models and estimate the merged weights from scratch, and (2) they rely on a shared hyperparameter setting across different modules of the network, lacking a global optimization strategy. This paper introduces Bayesian Model Merging (BMM), a plug-and-play bi-level optimization framework, where the inner level formulates the model merging as an activation-based Bayesian regression under a strong prior induced by an anchor model, yielding an efficient closed-form solution; and the outer level leverages a Bayesian optimization procedure to search module-specific hyperparameters globally based on a small validation set. Furthermore, we reveal a key alignment between activation statistics and task vectors, enabling us to derive a data-free variant of BMM that estimates the Gram matrix for regression without any auxiliary data. Across extensive benchmarks, including up to 20-task merging in vision and 5-task merging in language, BMM consistently outperforms all plug-and-play anchor baselines (e.g., TA, WUDI-Merging, and TSV). In particular, on the ViT-L/14 benchmark for 8-task merging, a single merged model reaches 95.1, closely matching the average performance of eight task-specific experts (95.8).</details> |
| **[Kernel-based guarantees for nonlinear parametric models in Bayesian optimization](https://arxiv.org/abs/2605.13160v1)** | ⭐ 82/100 | 提出非线性参数模型的核方法理论框架 | 填补了非线性模型在贝叶斯优化中理论保证的空白 | <details><summary>展开</summary>Modern Bayesian optimization and adaptive sampling methods increasingly rely on nonlinear parametric models, yet theoretical guarantees for such models under adaptive data collection remain limited. Existing analyses largely focus on Gaussian processes, kernel machines, linear models, or linearized neural approximations, leaving a gap between theory and the nonlinear models used in practice. We develop a kernel based framework for analyzing regularized nonlinear parametric models trained on adaptively collected data. Our approach uses kernels over the parameter space to induce reproducing kernel Hilbert space structures over the corresponding model class, yielding confidence bounds for models trained with broad classes of regularized convex losses. We show how these bounds can support convergence guarantees for nonlinear acquisition and surrogate models, including randomized regularized policies that select points by maximizing a trained random model. These results provide a unified route to analyzing nonlinear parametric models in Bayesian optimization and related adaptive optimization settings.</details> |
| **[Empowering LLMs for Structure-Based Drug Design via Exploration-Augmented Latent Inference](https://arxiv.org/abs/2601.15333v2)** | ⭐ 82/100 | 提出ELILLM框架优化药物设计 | 方法创新且实验扎实，在药物发现领域具有应用潜力。 | <details><summary>展开</summary>Large Language Models (LLMs) possess strong representation and reasoning capabilities, but their application to structure-based drug design (SBDD) is limited by insufficient understanding of protein structures and unpredictable molecular generation. To address these challenges, we propose Exploration-Augmented Latent Inference for LLMs (ELILLM), a framework that reinterprets the LLM generation process as an encoding, latent space exploration, and decoding workflow. ELILLM explicitly explores portions of the design problem beyond the model's current knowledge while using a decoding module to handle familiar regions, generating chemically valid and synthetically reasonable molecules. In our implementation, Bayesian optimization guides the systematic exploration of latent embeddings, and a position-aware surrogate model efficiently predicts binding affinity distributions to inform the search. Knowledge-guided decoding further reduces randomness and effectively imposes chemical validity constraints. We demonstrate ELILLM on the CrossDocked2020 benchmark, showing strong controlled exploration and high binding affinity scores compared with seven baseline methods. These results demonstrate that ELILLM can effectively enhance LLMs capabilities for SBDD.</details> |
| **[Manifold Sampling via Entropy Maximization](https://arxiv.org/abs/2605.12338v1)** | ⭐ 78/100 | 提出MASEM算法解决多连通域流形采样问题 | 方法创新且理论完备，在机器人领域应用潜力大。 | <details><summary>展开</summary>Sampling from constrained distributions has a wide range of applications, including in Bayesian optimization and robotics. Prior work establishes convergence and feasibility guarantees for constrained sampling, but assumes that the feasible set is connected. However, in practice, the feasible set often decomposes into multiple disconnected components, which makes efficient sampling under constraints challenging. In this paper, we propose MAnifold Sampling via Entropy Maximization (MASEM) for sampling on a manifold with an unknown number of disconnected components, implicitly defined by smooth equality and inequality constraints. The presented method uses a resampling scheme to maximize the entropy of the empirical distribution based on k-nearest neighbor density estimation. We show that, in the mean field, MASEM decreases the KL-divergence between the empirical distribution and the maximum-entropy target exponentially in the number of resampling steps. We instantiate MASEM with multiple local samplers and demonstrate its versatility and efficiency on synthetic and robotics-based benchmarks. MASEM enables fast and scalable mixing across a range of constrained sampling problems, improving over alternatives by an order of magnitude in Sinkhorn distance with competitive runtime.</details> |
| **[Accelerating battery research with an AI interface between FINALES and Kadi4Mat](https://arxiv.org/abs/2605.00909v1)** | ⭐ 78/100 | 构建AI接口实现电池实验自动化优化 | 创新性整合多系统，方法严谨且具有工程应用价值 | <details><summary>展开</summary>The time-consuming formation process critically impacts the longevity of sodium-ion coin cells and End Of Life (EOL) performance. This study aims to optimize formation protocols for duration efficiency, targeting high-performance outcomes while minimizing the number of experiments to reduce resource consumption and accelerate discovery. Specifically, we consider two potentially competing objectives: minimizing formation time and maximizing EOL performance. Beyond this application focus, we also present a methodological contribution: a framework designed to enable interoperability between the FINALES and Kadi RDM ecosystems, which we employ to tackle our optimization problem. In this setup, the FINALES framework orchestrates experiment planning and execution on the POLiS MAP, while an active-learning agent implemented within Kadi4Mat guides experiment selection, using multi-objective batched Bayesian optimization to efficiently explore the parameter space. This interoperability enhancement enables coordinated, distributed collaboration across automated systems and human-operated workflows, bridging multiple research centers. Using this approach, we iteratively explore the trade-off between formation time and EOL performance and identify candidate solutions approximating the Pareto front. The resulting workflow demonstrates the capability of interoperable infrastructures to facilitate data-driven optimization in battery research, and establishes a transferable framework applicable to diverse materials science and engineering optimization tasks.</details> |

