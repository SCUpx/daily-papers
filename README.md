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

## 2026-05-21

## Bayesian optimization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Automated Discovery of Metainterfaces with Tailored Friction Laws](https://arxiv.org/abs/2605.19555v1)** | ⭐ 85/100 | 自动化设计摩擦律新界面 | 新颖性高，方法扎实，实验验证充分，应用潜力大。 | <details><summary>展开</summary>Providing dry solid contacts with on-demand macroscale frictional behaviour remains a formidable challenge in tribology, haptics or robotics. Metainterfaces created from surfaces with engineered asperity-based topographies can achieve such friction control. However, only few friction behaviours were demonstrated because suitable topographies were identified based on human intuition. Here, we introduce a numerical-optimisation-based inverse design framework to automatically discover new metainterfaces satisfying specified relationships between friction and normal forces (friction law). To illustrate the framework's versatility, we first expand the range of achievable friction coefficients at a constant material pair; we next unlock power-law friction laws with arbitrary exponents between 2/3 and 1.35; we then achieve bilinear laws with a smaller slope in the second segment than in the first. We validate relevant cases experimentally. By enabling systematic exploration of large parameter spaces, not limited to topography but potentially incorporating the individual asperities' bulk material or surface physicochemistry, our automated framework offers design solutions for any physically possible friction law. It also provides new insights into the elusive relationship between local interfacial properties and macroscopic friction.</details> |
| **[Efficient Conditioning Why Pseudo Observation Batch Bayesian Optimization Works When It Does not](https://arxiv.org/abs/2605.18819v1)** | ⭐ 83/100 | 提出高效条件化理论解释批贝叶斯优化 | 理论新颖，实验充分，方法实用，论述清晰，得分较高 | <details><summary>展开</summary>Constant Liar (CL), Kriging Believer (KB), and fantasy models are widely used for batch selection in parallel Bayesian Optimization, yet a unified theory explaining their effectiveness and conditions under which they fail has been lacking. We identify efficient conditioning as the key surrogate property the ability to update predictions in closed form when data is augmented. We prove that Gaussian Processes satisfy this requirement, producing provably distinct batch points with separation of order l, and that this holds for any acquisition function monotonically non decreasing in posterior uncertainty (EI, UCB, PI), with qualitatively similar behavior for Thompson Sampling. We unify CL, KB, and fantasy models as instances of a single conditioning mechanism differing only in the lie value distribution, and draw quantitative connections to Local Penalization (LP) and qualitative connections to Determinantal Point Processes (DPPs). To disentangle model structure from optimizer randomness, we introduce the Structural Diversity Diagnostic (SDD), a reusable methodology for testing surrogate compatibility. Experiments on Hartmann6D, Ackley 8D, Levy10D, and SVM hyperparameter tuning validate all theoretical predictions: CL or KBs implicit penalty matches or outperforms explicit LP greedy conditioning achieves convergence on par with joint qEI efficient conditioning extends to Multiquadric RBF networks; and parametric surrogates produce degenerate batches even when fully retrained (random forests), while neural networks regain diversity only at 15x the wall clock cost of GP conditioning. Robustness is confirmed across multiple initial datasets and under observation noise.</details> |
| **[Curvature-aware Expected Free Energy as an Acquisition Function for Bayesian Optimization](https://arxiv.org/abs/2603.26339v1)** | ⭐ 83/100 | 提出曲率感知期望自由能用于贝叶斯优化 | 新颖性高，理论与实验均扎实，实用性强，但部分细节可更清晰 | <details><summary>展开</summary>We propose an Expected Free Energy-based acquisition function for Bayesian optimization to solve the joint learning and optimization problem, i.e., optimize and learn the underlying function simultaneously. We show that, under specific assumptions, Expected Free Energy reduces to Upper Confidence Bound, Lower Confidence Bound, and Expected Information Gain. We prove that Expected Free Energy has unbiased convergence guarantees for concave functions. Using the results from these derivations, we introduce a curvature-aware update law for Expected Free Energy and show its proof of concept using a system identification problem on a Van der Pol oscillator. Through rigorous simulation experiments, we show that our adaptive Expected Free Energy-based acquisition function outperforms state-of-the-art acquisition functions with the least final simple regret and error in learning the Gaussian process.</details> |
| **[Goal-Oriented Lower-Tail Calibration of Gaussian Processes for Bayesian Optimization](https://arxiv.org/abs/2605.20145v1)** | ⭐ 82/100 | 提出tcGP用于高斯过程低尾校准 | 新颖性高，方法有效，实验充分，但部分理论细节可更清晰 | <details><summary>展开</summary>Bayesian optimization (BO) selects evaluation points for expensive black-box objectives using Gaussian process (GP) predictive distributions. Kernel choice and hyperparameter selection can lead to miscalibrated predictive distributions and an inappropriate exploration-exploitation trade-off. For minimization, sampling criteria such as expected improvement (EI) depend on the predictive distribution below the current best value, so lower-tail miscalibration directly affects the sampling decision. This article studies goal-oriented calibration of GP predictive distributions below a low threshold $t$ in the noiseless setting, for standard GP models with hyperparameters selected by maximum likelihood. A framework for predictive reliability below $t$ is introduced, based on two notions of spatial calibration: occurrence calibration over the design space and thresholded $μ$-calibration on sublevel sets of the form $\{x\in\mathbb{X}, f(x)\le t\}$. Building on this framework, we propose tcGP, a post-hoc method that calibrates GP predictive distributions below~$t$, and we show that the resulting EI-based global optimization algorithm remains dense in the design space. Experiments on standard benchmarks show improved lower-tail calibration and BO performance relative to standard GP models and globally calibrated GP models.</details> |
| **[Agentic Discovery of Cryomicroneedle Formulations](https://arxiv.org/abs/2605.19677v1)** | ⭐ 82/100 | AI辅助冷冻微针配方发现 | 新颖性高，方法扎实，实用性强，表述清晰 | <details><summary>展开</summary>Cryomicroneedles offer a route to minimally invasive intradermal delivery of living cells, but their cryogenic formulations must reconcile cell protection with constraints on toxicity and device fabrication. Here we report an AI-assisted, closed-loop workflow for cryomicroneedle cryoprotectant discovery that combines literature curation, Gaussian-process surrogate modelling, Bayesian optimization, and sequential wet-lab validation. A curated dataset of 198 mesenchymal stem-cell cryopreservation formulations from 42 studies was converted into 21 ingredient features and used to train an uncertainty-aware literature prior. This model captured moderate structure in the literature data but failed prospectively, motivating iterative wet-lab correction. Across ten validation iterations and 106 wet-lab observations, the model progressively adapted to cryomicroneedle-specific outcomes: batch RMSE decreased from 41.21 to 6.86 percentage points, later-stage rank correlations became consistently positive, and the cumulative wet-lab predicted-versus-measured summary reached $R^2 = 0.942$. The best validated formulation achieved 95.15\% post-thaw viability with low DMSO, ectoin, ethylene glycol, and fetal bovine serum. However, high viability alone did not ensure intact cryomicroneedle formation, highlighting the need for future multi-objective optimization. These results demonstrate that agent-assisted computational infrastructure can make data-efficient formulation discovery more accessible to labs with minimal data expertise in-house. Project code is available at https://github.com/baitmeister/ML-for-CryoMN.</details> |

