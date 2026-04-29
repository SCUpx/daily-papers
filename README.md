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

## 2026-04-30

## Bayesian optimization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[DiMEx: Breaking the Cold Start Barrier in Data-Free Model Extraction via Latent Diffusion Priors](https://arxiv.org/abs/2601.01688v2)** | ⭐ 84/100 | 利用扩散模型解决模型窃取冷启动难题 | 创新性引入扩散先验，实验严谨且防御有效 | <details><summary>展开</summary>Model stealing attacks pose an existential threat to Machine Learning as a Service (MLaaS), allowing adversaries to replicate proprietary models for a fraction of their training cost. While Data-Free Model Extraction (DFME) has emerged as a stealthy vector, it remains fundamentally constrained by the "Cold Start" problem: GAN-based adversaries waste thousands of queries converging from random noise to meaningful data. We propose DiMEx, a framework that weaponizes the rich semantic priors of pre-trained Latent Diffusion Models to bypass this initialization barrier entirely. By employing Random Embedding Bayesian Optimization (REMBO) within the generator's latent space, DiMEx synthesizes high-fidelity queries immediately, achieving 52.1 percent agreement on SVHN with just 2,000 queries - outperforming state-of-the-art GAN baselines by over 16 percent. To counter this highly semantic threat, we introduce the Hybrid Stateful Ensemble (HSE) defense, which identifies the unique "optimization trajectory" of latent-space attacks. Our results demonstrate that while DiMEx evades static distribution detectors, HSE exploits this temporal signature to suppress attack success rates to 21.6 percent with negligible latency.</details> |
| **[A Finite Time Analysis of Thompson Sampling for Bayesian Optimization with Preferential Feedback](https://arxiv.org/abs/2604.25025v1)** | ⭐ 82/100 | 提出偏好反馈下的贝叶斯优化汤普森采样算法 | 理论分析严谨，方法创新，在偏好反馈领域具有较高实用价值。 | <details><summary>展开</summary>Preference feedback, in the form of pairwise comparisons rather than scalar scores, has seen increasing use in applications such as human-, laboratory-, and expert-in-the-loop design, as well as scientific discovery. We propose a Thompson Sampling (TS) approach to Bayesian optimization with preferential feedback that models comparisons using a monotone link on latent utility differences and leverages the dueling kernel induced by a base kernel. We provide a finite-time analysis showing that the performance of the proposed method matches that of standard TS for conventional Bayesian optimization with scalar feedback. The analysis exploits the anchor invariance of TS for challenger selection and introduces a double-TS pairing variant. We also demonstrate the performance of the method on both synthetic and real-world examples.</details> |
| **[Bayesian Optimization for Mixed-Variable Problems in the Natural Sciences](https://arxiv.org/abs/2604.07416v1)** | ⭐ 82/100 | 提出处理混合变量问题的贝叶斯优化框架 | 方法创新且实用，实验设计严谨，逻辑清晰。 | <details><summary>展开</summary>Optimizing expensive black-box objectives over mixed search spaces is a common challenge across the natural sciences. Bayesian optimization (BO) offers sample-efficient strategies through probabilistic surrogate models and acquisition functions. However, its effectiveness diminishes in mixed or high-cardinality discrete spaces, where gradients are unavailable and optimizing the acquisition function becomes computationally demanding. In this work, we generalize the probabilistic reparameterization (PR) approach of Daulton et al. to handle non-equidistant discrete variables, enabling gradient-based optimization in fully mixed-variable settings with Gaussian process (GP) surrogates. With real-world scientific optimization tasks in mind, we conduct systematic benchmarks on synthetic and experimental objectives to obtain an optimized kernel formulations and demonstrate the robustness of our generalized PR method. We additionally show that, when combined with a modified BO workflow, our approach can efficiently optimize highly discontinuous and discretized objective landscapes. This work establishes a practical BO framework for addressing fully mixed optimization problems in the natural sciences, and is particularly well suited to autonomous laboratory settings where noise, discretization, and limited data are inherent.</details> |
| **[AgentOpt v0.1 Technical Report: Client-Side Optimization for LLM-Based Agent](https://arxiv.org/abs/2604.06296v2)** | ⭐ 82/100 | 提出AgentOpt框架优化客户端智能体模型选择 | 填补客户端优化空白，方法论严谨且应用价值高 | <details><summary>展开</summary>AI agents are increasingly deployed in real-world applications, including systems such as Manus, OpenClaw, and coding agents. Existing research has primarily focused on server-side efficiency, proposing methods such as caching, speculative execution, traffic scheduling, and load balancing to reduce the cost of serving agentic workloads. However, as users increasingly construct agents by composing local tools, remote APIs, and diverse models, an equally important optimization problem arises on the client side. Client-side optimization asks how developers should allocate the resources available to them, including model choice, local tools, and API budget across pipeline stages, subject to application-specific quality, cost, and latency constraints. Because these objectives depend on the task and deployment setting, they cannot be determined by server-side systems alone. We introduce AgentOpt, the first framework-agnostic Python package for client-side agent optimization. We first study model selection, a high-impact optimization lever in multi-step agent pipelines. Given a pipeline and a small evaluation set, the goal is to find the most cost-effective assignment of models to pipeline roles. This problem is consequential in practice: at matched accuracy, the cost gap between the best and worst model combinations can reach 13-32x in our experiments. To efficiently explore the exponentially growing combination space, AgentOpt implements ten search algorithms, including UCB-E, UCB-E with Low-Rank Factorization, Arm Elimination, Epsilon-LUCB, Threshold Successive Elimination, and Bayesian Optimization. Across four benchmarks, UCB-E recovers near-optimal accuracy while reducing evaluation budget by 62-76\% relative to brute-force search. Code and benchmark results available at https://agentoptimizer.github.io/agentopt/.</details> |
| **[Automatic Configuration of LLM Post-Training Pipelines](https://arxiv.org/abs/2603.18773v1)** | ⭐ 82/100 | 提出AutoPipe框架优化LLM后训练配置 | 方法创新且高效，实验验证充分，实用价值高。 | <details><summary>展开</summary>LLM post-training pipelines that combine supervised fine-tuning and reinforcement learning are difficult to configure under realistic compute budgets: the configuration space is high-dimensional and heterogeneous, stages are strongly coupled, and each end-to-end evaluation is expensive. We propose AutoPipe, a budget-aware two-stage framework for configuration selection in LLM post-training. Offline, AutoPipe learns a dataset-conditioned learning-to-rank surrogate from historical runs, capturing within-dataset preferences and providing transferable guidance toward promising regions of the configuration space. Online, for a new dataset, AutoPipe uses the offline guidance to steer Bayesian optimization and models dataset-specific deviations with a Gaussian-process residual surrogate. To reduce evaluation cost, each trial is early-stopped and scored by a learned predictor that maps early training signals to a low-cost proxy for final post-training performance. Experiments on biomedical reasoning tasks show that AutoPipe consistently outperforms offline-only baselines and achieves comparable performance with the strongest online HPO baselines while using less than 10\% of their computational cost.</details> |

## EHL

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Electrohydrodynamic lubrication theory](https://arxiv.org/abs/2604.25350v1)** | ⭐ 78/100 | 建立带电圆柱近壁运动的电流体润滑模型 | 理论框架严谨，结合了静电学与流体力学，具有较高学术价值。 | <details><summary>展开</summary>The free motion of charged colloids within ionic solutions and in the vicinity of charged boundaries, is a phenomenon that occurs in various natural, biological and industrial settings. Here, we develop an electrohydrodynamic lubrication theoretical framework, in order to characterize such a motion in the case of an infinite rigid cylinder near a rigid wall. Combining hydrodynamic lubrication theory, Debye-H\''uckel electrostatics, and Nernst-Planck electrokinetics, we derive the three coupled equations of motion for the normal, longitudinal and rotational degrees of freedom of the cylinder, which are then investigated numerically and through asymptotic analysis. Our results reveal complex behaviours, beyond existing asymptotic electroviscous-lift expressions, and extend the classical Faxen-Brenner-like mobility matrix when surface charges and dissolved ions are incorporated.</details> |

