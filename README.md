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

## 2026-05-12

## Bayesian optimization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[ADKO: Agentic Decentralized Knowledge Optimization](https://arxiv.org/abs/2605.07863v1)** | ⭐ 82/100 | 提出去中心化智能体知识优化框架 | 理论分析严谨，结合大模型与贝叶斯优化，创新性强。 | <details><summary>展开</summary>We present Agentic Decentralized Knowledge Optimization (ADKO), a framework for collaborative black-box optimization across autonomous agents that achieves sample efficiency, privacy preservation, heterogeneous-objective handling, and communication efficiency. Each agent maintains a private Gaussian Process (GP) surrogate trained on local data and communicates only through knowledge tokens-compact, lossy summaries containing directional signals, advantage scores, and optional language-model (LM) insights-without sharing raw data or model parameters. ADKO unifies GP-Upper Confidence Bound (GP-UCB), parallel Bayesian optimization, decentralized learning, and LM-guided discovery. We provide the first formal analysis of dual information loss: token compression, quantified via mutual-information-based fidelity, and LM approximation error, decomposed into bias and stochastic noise. Our main result shows cumulative regret decomposes into GP error, LM bias, LM noise, and compression loss, with necessary and sufficient conditions for sublinear regret. We also propose fidelity-aware token pruning to preserve high-information tokens under memory budget. Experiments on neural architecture search and scientific discovery validate the theory and show consistent improvements over strong baselines.</details> |
| **[When Losses Align: Gradient-Based Composite Loss Weighting for Efficient Pretraining](https://arxiv.org/abs/2605.07756v1)** | ⭐ 82/100 | 提出梯度对齐方法高效优化预训练损失权重 | 方法创新且显著降低了超参调优的计算开销 | <details><summary>展开</summary>Modern deep models are often pretrained on large-scale data with missing labels using composite objectives, where the relative weights of multiple loss terms act as hyperparameters. Tuning these weights with random search or Bayesian optimization is computationally expensive, as it requires many independent training runs. To address this, we propose a gradient-based bilevel method that learns pretraining loss weights online by aligning the composite pretraining gradient with a downstream objective. By exploiting the structure of the loss, the method avoids the multiple backward passes typically required by truncated backpropagation through the full model, reducing the overhead of hyperparameter tuning to approximately 30% above a single training run. We evaluate the approach on event-sequence modeling and self-supervised computer vision, where it matches or improves upon carefully tuned baselines while substantially reducing the cost of hyperparameter tuning compared to random or Bayesian search.</details> |
| **[Open-Ended Task Discovery via Bayesian Optimization](https://arxiv.org/abs/2605.07572v1)** | ⭐ 82/100 | 提出GSR框架实现开放式任务发现与优化 | 创新性引入任务生成机制，理论严谨且应用广泛。 | <details><summary>展开</summary>When applying Bayesian optimization (BO) to scientific workflow, a major yet often overlooked source of uncertainty is the task itself -- namely, what to optimize and how to evaluate it -- which can evolve as evidence accumulates. We introduce Generate-Select-Refine (GSR), a open-ended BO framework that alternates between task generation and task optimization. Starting from a user-provided seed task, GSR generates new tasks in a coarse-to-fine manner while a task-acquisition function schedules optimization. Asymptotically, it concentrates evaluations on the best task, incurring only logarithmic regret overhead relative to single-task BO. We apply GSR to new product development, chemical synthesis scaling, algorithm analysis, and patent repurposing, where it outperforms existing LLM-based optimizers.</details> |
| **[Curiosity is Knowledge: Self-Consistent Learning and No-Regret Optimization with Active Inference](https://arxiv.org/abs/2602.06029v1)** | ⭐ 82/100 | 揭示主动推理中好奇心与学习优化的理论联系 | 理论贡献显著，提供了主动推理的收敛性保证，严谨且具应用价值。 | <details><summary>展开</summary>Active inference (AIF) unifies exploration and exploitation by minimizing the Expected Free Energy (EFE), balancing epistemic value (information gain) and pragmatic value (task performance) through a curiosity coefficient. Yet it has been unclear when this balance yields both coherent learning and efficient decision-making: insufficient curiosity can drive myopic exploitation and prevent uncertainty resolution, while excessive curiosity can induce unnecessary exploration and regret. We establish the first theoretical guarantee for EFE-minimizing agents, showing that a single requirement--sufficient curiosity--simultaneously ensures self-consistent learning (Bayesian posterior consistency) and no-regret optimization (bounded cumulative regret). Our analysis characterizes how this mechanism depends on initial uncertainty, identifiability, and objective alignment, thereby connecting AIF to classical Bayesian experimental design and Bayesian optimization within one theoretical framework. We further translate these theories into practical design guidelines for tuning the epistemic-pragmatic trade-off in hybrid learning-optimization problems, validated through real-world experiments.</details> |
| **[Multi Objective Design Optimization of Non Pneumatic Passenger Car Tires Using Finite Element Modeling, Machine Learning, and Particle swarm Optimization and Bayesian Optimization Algorithms](https://arxiv.org/abs/2602.04277v1)** | ⭐ 82/100 | 提出非充气轮胎多目标优化框架 | 结合机器学习与优化算法，显著提升设计效率与性能。 | <details><summary>展开</summary>Non Pneumatic tires offer a promising alternative to pneumatic tires. However, their discontinuous spoke structures present challenges in stiffness tuning, durability, and high speed vibration. This study introduces an integrated generative design and machine learning driven framework to optimize UPTIS type spoke geometries for passenger vehicles. Upper and lower spoke profiles were parameterized using high order polynomial representations, enabling the creation of approximately 250 generative designs through PCHIP based geometric variation. Machine learning models like KRR for stiffness and XGBoost for durability and vibration achieved strong predictive accuracy, reducing the reliance on computationally intensive FEM simulations. Optimization using Particle Swarm Optimization and Bayesian Optimization further enabled extensive performance refinement. The resulting designs demonstrate 53% stiffness tunability, up to 50% durability improvement, and 43% reduction in vibration compared to the baseline. PSO provided fast, targeted convergence, while Bayesian Optimization effectively explored multi objective tradeoffs. Overall, the proposed framework enables systematic development of high performance, next generation UPTIS spoke structures.</details> |

