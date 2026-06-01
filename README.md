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

## 2026-06-02

## Bayesian optimization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Spectral Anatomy of Quantum Gaussian Process Kernels](https://arxiv.org/abs/2605.30952v1)** | ⭐ 88/100 | 揭示量子高斯过程核的谱熵统一诊断框架 | 理论严谨且实验验证充分，统一了量子核性能瓶颈。 | <details><summary>展开</summary>Two recent results have reshaped quantum Gaussian processes (QGPs). On the one hand, \citet{lowe2025assessing} rule out the exponential speedups claimed by HHL-based QGP regression in the typical, well-conditioned regime; on the other, an independent line of work shows that highly expressive quantum kernels suffer posterior pathologies that break Bayesian optimization. We show that these seemingly unrelated phenomena are governed by the same quantity: the normalized spectral entropy $S(K)/\log n$ of the kernel Gram matrix. We prove a Cauchy--Schwarz tail bound on Nyström approximation error, a finite-sample variance-contraction identity in terms of Bach's degrees of freedom $d_σ(K)$, and a characterization of the \emph{target-dependent} optimal entropy via the intrinsic dimension of the target in the kernel eigenbasis. Empirically, the diagnostic is kernel-agnostic: hardware-efficient, matchgate, IQP \emph{and} RBF/Matérn/RFF/deep-kernel families all collapse onto identical $S/\log n$ curves on dequantization, ECE, and variance-contraction panels. The NLL sweet spot lives at high entropy for smooth targets and at low entropy for band-limited quantum-data targets. The diagnostic transfers from simulator to IBM Heron hardware with median absolute error $3.2\%$ and mean $5.2\%$ in $S/\log n$ across $24$ configurations at $n_q = 4$, with matchgate and IQP within $5\%$ mean and a single HE configuration returning a $30\%$ outlier that drops to $0.5\%$ on rerun (attributed to calibration drift); the same diagnostic transfers to a second Heron backend (mean error $2.7\%$) and to a $n_q = 6$ scale-up on the original backend (mean error $1.7\%$). No error mitigation is applied throughout.</details> |
| **[Best-Arm Identification-Based Trust Region Selection for Bayesian Optimization on Multimodal Functions](https://arxiv.org/abs/2605.31050v1)** | ⭐ 78/100 | 提出BAI引导的贝叶斯优化框架 | 结合多臂老虎机与信赖域，理论与实验支撑扎实 | <details><summary>展开</summary>Gaussian process-based Bayesian optimization (BO) is a popular approach for expensive black-box optimization, but its performance often degrades on complex multimodal or high-dimensional problems. Trust region-based BO mitigates this issue by focusing on local regions, and recent studies suggest that selecting an effective region can be formulated as a multi-armed bandit problem. We propose a trajectory-aware framework that integrates best-arm identification (BAI) with trust region-based BO to efficiently solve multimodal optimization problems. Our method extrapolates the optimization trajectories of multiple locally initialized optimizers to predict their final performance and progressively eliminates suboptimal candidates via BAI. We theoretically show that the proposed BAI-guided BO converges faster to the global optimum than conventional BO under mild assumptions, and demonstrate its effectiveness through extensive experiments on synthetic and real-world benchmarks.</details> |

