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

## 2026-04-27

## Bayesian optimization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Information Theoretic Bayesian Optimization over the Probability Simplex](https://arxiv.org/abs/2603.09793v1)** | ⭐ 84/100 | 提出基于信息几何的概率单纯形贝叶斯优化算法 | 理论基础扎实，几何核函数设计创新，应用效果显著。 | <details><summary>展开</summary>Bayesian optimization is a data-efficient technique that has been shown to be extremely powerful to optimize expensive, black-box, and possibly noisy objective functions. Many applications involve optimizing probabilities and mixtures which naturally belong to the probability simplex, a constrained non-Euclidean domain defined by non-negative entries summing to one. This paper introduces $α$-GaBO, a novel family of Bayesian optimization algorithms over the probability simplex. Our approach is grounded in information geometry, a branch of Riemannian geometry which endows the simplex with a Riemannian metric and a class of connections. Based on information geometry theory, we construct Matérn kernels that reflect the geometry of the probability simplex, as well as a one-parameter family of geometric optimizers for the acquisition function. We validate our method on benchmark functions and on a variety of real-world applications including mixtures of components, mixtures of classifiers, and a robotic control task, showing its increased performance compared to constrained Euclidean approaches.</details> |
| **[Record-Remix-Replay: Hierarchical GPU Kernel Optimization using Evolutionary Search](https://arxiv.org/abs/2604.11109v1)** | ⭐ 82/100 | 提出R^3框架优化GPU内核性能 | 结合LLM与进化搜索，显著提升了GPU内核优化效率。 | <details><summary>展开</summary>As high-performance computing and AI workloads become increasingly dependent on GPUs, maintaining high performance across rapidly evolving hardware generations has become a major challenge. Developers often spend months tuning scientific applications to fully exploit new architectures, navigating a complex optimization space that spans algorithm design, source implementation, compiler flags and pass sequences, and kernel launch parameters. Existing approaches can effectively search parts of this space in isolation, such as launch configurations or compiler settings, but optimizing across the full space still requires substantial human expertise and iterative manual effort. In this paper, we present Record-Remix-Replay (R^3), a hierarchical optimization framework that combines LLM-driven evolutionary search, Bayesian optimization, and record-replay compilation techniques to efficiently explore GPU kernel optimizations from source-level implementation choices down to compiler pass ordering and runtime configuration. By making candidate evaluation fast and scalable, our approach enables practical end-to-end search over optimization dimensions that are typically treated separately. We show that Record-Remix-Replay can optimize full scientific applications better than traditional approaches over kernel parameters and compiler flags, while also being nearly an order of magnitude faster than modern evolutionary search approaches.</details> |
| **[Physics-informed automated surface reconstructing via low-energy electron diffraction based on Bayesian optimization](https://arxiv.org/abs/2604.04578v1)** | ⭐ 82/100 | 基于物理信息贝叶斯优化的LEED结构分析方法 | 将物理模型嵌入贝叶斯优化，显著提升了LEED反问题的求解效率与自动化水平。 | <details><summary>展开</summary>Low-energy electron diffraction (LEED) is a cornerstone technique for determining surface atomic structures[heldStructureDeterminationLowenergy2025], yet the quantitative analysis of electron diffraction intensity as a function of incident electron energy -- that is, LEED-\textit{I(V)} analysis -- remains a complex inverse problem. In this work, we tackle quantitative LEED-\textit{I(V)} analysis based on physics-informed Bayesian optimization (BO). By embedding multiple scattering LEED forward models directly into a trust-region BO loop, our approach simultaneously optimizes both structural and experimental parameters, adaptively adjusting trust regions for efficient exploration of complex non-convex parameter spaces without manual intervention. The robustness and scalability of the approach are demonstrated using the Ag(100)-(1$\time$1) and Fe\textsubscript{2}O\textsubscript{3}(1$\overline{1}$02)-(1$\time$1) surfaces as examples. Our work establishes a general framework for solving inverse problems in various characterization techniques, unlocking a physics-informed efficient, reproducible, and autonomous paradigm.</details> |
| **[Grey-Box Bayesian Optimization for ISAC in Fluid-Antenna Assisted Air-Ground Network](https://arxiv.org/abs/2604.02181v1)** | ⭐ 82/100 | 提出灰盒贝叶斯优化提升FAS-ISAC性能 | 结合物理模型与贝叶斯优化，有效解决高维动态优化问题。 | <details><summary>展开</summary>Fluid antenna systems (FAS) provide extra position agile spatial diversity for integrated sensing and communication (ISAC), by jointly optimizing the port selection and precoding. However, this optimization is challenging in air ground networks due to the intricate dual objective Pareto frontier, complex self-interference, and prohibitive channel state information overhead. To overcome these bottlenecks, this work proposes a novel grey box multi objective Bayesian optimization framework to address the joint design of discrete port selection and ISAC precoding. Unlike black box methods, this architecture explicitly leverages known physical system models to learn unknown channel constituents, dramatically reducing sample complexity. To navigate high dimensional combinatorial spaces, an adaptive trust region mechanism powered by expected hypervolume improvement (EHI) acquisition is implemented. Furthermore, the framework incorporates a spatio-temporal tracking strategy to handle the continuous mobility of users and targets, robustly capturing the drifting optimum in time varying environments. Simulations demonstrate that this framework achieves significantly faster convergence and discovers superior Pareto optimal configurations, validating its efficiency for dynamic real time FAS-ISAC deployments.</details> |
| **[Efficient and Principled Scientific Discovery through Bayesian Optimization: A Tutorial](https://arxiv.org/abs/2604.01328v3)** | ⭐ 82/100 | 介绍贝叶斯优化在科学发现中的应用框架 | 系统性阐述了BO方法论，对科研实验设计具有极高指导价值。 | <details><summary>展开</summary>Traditional scientific discovery relies on an iterative hypothesise-experiment-refine cycle that has driven progress for centuries, but its intuitive, ad-hoc implementation often wastes resources, yields inefficient designs, and misses critical insights. This tutorial presents Bayesian Optimisation (BO), a principled probability-driven framework that formalises and automates this core scientific cycle. BO uses surrogate models (e.g., Gaussian processes) to model empirical observations as evolving hypotheses, and acquisition functions to guide experiment selection, balancing exploitation of known knowledge and exploration of uncharted domains to eliminate guesswork and manual trial-and-error. We first frame scientific discovery as an optimisation problem, then unpack BO's core components, end-to-end workflows, and real-world efficacy via case studies in catalysis, materials science, organic synthesis, and molecule discovery. We also cover critical technical extensions for scientific applications, including batched experimentation, heteroscedasticity, contextual optimisation, and human-in-the-loop integration. Tailored for a broad audience, this tutorial bridges AI advances in BO with practical natural science applications, offering tiered content to empower cross-disciplinary researchers to design more efficient experiments and accelerate principled scientific discovery.</details> |

