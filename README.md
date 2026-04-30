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

## 2026-05-01

## Bayesian optimization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[A Tutorial Review of Bayesian Optimization with Gaussian Processes to Accelerate Stationary Point Searches](https://arxiv.org/abs/2603.10992v5)** | ⭐ 82/100 | 提出贝叶斯优化加速势能面搜索的统一框架 | 方法论严谨且具有通用性，对计算化学有重要价值 | <details><summary>展开</summary>Building local surrogates to accelerate stationary point searches on potential energy surfaces spans decades of effort. Done correctly, surrogates can reduce the number of expensive electronic structure evaluations by roughly an order of magnitude while preserving the accuracy of the underlying theory, with the gain depending on oracle cost, search distance, and the availability of analytical forces. We present a unified Bayesian optimization view of minimization, single-point saddle searches, and double-ended path searches: all three share one six-step surrogate loop and differ only in the inner optimization target and the acquisition criterion. The framework uses Gaussian process regression with derivative observations, inverse-distance kernels, and active learning, and we develop optional extensions for production use, including farthest-point sampling with the Earth Mover's Distance, MAP regularization, an adaptive trust radius, and random Fourier features for scaling. Accompanying pedagogical Rust code demonstrates that all three applications use the same Bayesian optimization loop, bridging the gap between theoretical formulation and practical execution.</details> |
| **[On Regret Bounds of Thompson Sampling for Bayesian Optimization](https://arxiv.org/abs/2603.09276v1)** | ⭐ 82/100 | 推导了GP-TS的遗憾界并优化了累积遗憾上界 | 理论贡献扎实，填补了GP-TS分析中的多项空白 | <details><summary>展开</summary>We study a widely used Bayesian optimization method, Gaussian process Thompson sampling (GP-TS), under the assumption that the objective function is a sample path from a GP. Compared with the GP upper confidence bound (GP-UCB) with established high-probability and expected regret bounds, most analyses of GP-TS have been limited to expected regret. Moreover, whether the recent analyses of GP-UCB for the lenient regret and the improved cumulative regret upper bound can be applied to GP-TS remains unclear. To fill these gaps, this paper shows several regret bounds: (i) a regret lower bound for GP-TS, which implies that GP-TS suffers from a polynomial dependence on $1/δ$ with probability $δ$, (ii) an upper bound of the second moment of cumulative regret, which directly suggests an improved regret upper bound on $δ$, (iii) expected lenient regret upper bounds, and (iv) an improved cumulative regret upper bound on the time horizon $T$. Along the way, we provide several useful lemmas, including a relaxation of the necessary condition from recent analysis to obtain improved regret upper bounds on $T$.</details> |
| **[Local Constrained Bayesian Optimization](https://arxiv.org/abs/2603.07965v1)** | ⭐ 82/100 | 提出LCBO解决高维约束贝叶斯优化难题 | 方法创新且理论完备，在高维约束问题上表现优异 | <details><summary>展开</summary>Bayesian optimization (BO) for high-dimensional constrained problems remains a significant challenge due to the curse of dimensionality. We propose Local Constrained Bayesian Optimization (LCBO), a novel framework tailored for such settings. Unlike trust-region methods that are prone to premature shrinking when confronting tight or complex constraints, LCBO leverages the differentiable landscape of constraint-penalized surrogates to alternate between rapid local descent and uncertainty-driven exploration. Theoretically, we prove that LCBO achieves a convergence rate for the Karush-Kuhn-Tucker (KKT) residual that depends polynomially on the dimension $d$ for common kernels under mild assumptions, offering a rigorous alternative to global BO where regret bounds typically scale exponentially. Extensive evaluations on high-dimensional benchmarks (up to 100D) demonstrate that LCBO consistently outperforms state-of-the-art baselines.</details> |
| **[Active Learning for Tractable and Reproducible Pulsed Laser Deposition](https://arxiv.org/abs/2603.05699v1)** | ⭐ 82/100 | 利用主动学习优化PLD薄膜生长 | 方法创新且实验扎实，有效提升了材料生长效率。 | <details><summary>展开</summary>This paper shows how data-driven machine learning approaches can improve growth control, reproducibility, and physical insight in the pulsed laser deposition (PLD) growth of correlated oxides. Despite well-known relationships between growth conditions and material properties, consistently producing high-quality films of complex materials like LaVO$_3$ remains difficult due to the highly non-equilibrium nature of PLD and the defects and competing phases that accumulate during growth. Here, we use an active learning framework based on Gaussian process Bayesian optimization that incorporates measured bulk and surface lattice properties along with impurity phase information to efficiently map the multidimensional growth space of LaVO$_3$ by PLD. By tuning the relative weighting of these properties, the model identifies an optimized region where phase-pure films of LaVO$_3$ exhibit two-dimensional surfaces, near-ideal lattice parameters, and minimal sub-band gap optical absorption. The trained model reveals clear competition among different defect formation mechanisms that are connected to unseen parameters like supersaturation and surface mobility, thus giving insight into the highly non-equilibrium process of PLD growth. Together, this demonstrates that property-guided machine learning can accelerate materials optimization while providing a new way to address fundamental growth mechanisms in PLD that enable understanding and utilization of quantum phenomena found in complex oxides.</details> |
| **[Advancing accelerator virtual beam diagnostics through latent evolution modeling: an integrated solution to forward, inverse, tuning, and UQ problems](https://arxiv.org/abs/2602.22618v1)** | ⭐ 82/100 | 提出LEM框架实现加速器束流诊断与优化 | 方法创新且应用广泛，逻辑清晰，具备高实用价值 | <details><summary>展开</summary>Virtual beam diagnostics relies on computationally intensive beam dynamics simulations where high-dimensional charged particle beams evolve through the accelerator. We propose Latent Evolution Model (LEM), a hybrid machine learning framework with an autoencoder that projects high-dimensional phase spaces into lower-dimensional representations, coupled with transformers to learn temporal dynamics in the latent space. This approach provides a common foundational framework addressing multiple interconnected challenges in beam diagnostics. For \textit{forward modeling}, a Conditional Variational Autoencoder (CVAE) encodes 15 unique projections of the 6D phase space into a latent representation, while a transformer predicts downstream latent states from upstream inputs. For \textit{inverse problems}, we address two distinct challenges: (a) predicting upstream phase spaces from downstream observations by utilizing the same CVAE architecture with transformers trained on reversed temporal sequences along with aleatoric uncertainty quantification, and (b) estimating RF settings from the latent space of the trained LEM using a dedicated dense neural network that maps latent representations to RF parameters. For \textit{tuning problems}, we leverage the trained LEM and RF estimator within a Bayesian optimization framework to determine optimal RF settings that minimize beam loss. This paper summarizes our recent efforts and demonstrates how this unified approach effectively addresses these traditionally separate challenges.</details> |

## Mixed lubrication

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Linear poroelastic response of thin permeable gel films](https://arxiv.org/abs/2604.26464v1)** | ⭐ 73/100 | 推导了薄层渗透性多孔弹性凝胶在点载荷下的力学响应函数。 | 建立了薄层凝胶的格林函数模型，对软物质力学和润滑研究具有理论价值。 | <details><summary>展开</summary>When a hydrophilic and deformable porous material is immersed in a bath, it may absorb the solvent and expand by several times its volume, thus forming a highly soft and porous hydrogel. A stress applied on the soft hydrogel surface deforms it and forces the absorbed solvent to move by flowing through the network of pores. This coupled phenomenon sets the framework of poroelasticity. Moreover, polymeric gels are often used in ultra-thin coatings to tune surface properties. Together with the characteristic poroelastic coupling, this thinness challenges the modelling of their response. In this article, we derive the point-force mechanical response of a thin, permeable and poroelastic layer bounded to a rigid substrate. We show that the gel surface is only deformed around the indentation point, within a radius on the order of the layer thickness. The obtained Green's function can be directly used to predict the space- and time-dependent surface deformation of the gel. Our findings are relevant for a broad range of applications, such as indentation experiments on swollen gels, thin membranes or soft and living systems, as well as lubrication problems involving a soft and porous wall, for instance in microfluidics.</details> |

