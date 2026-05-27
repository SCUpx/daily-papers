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

## 2026-05-28

## Bayesian optimization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Joint Parameter and State-Space Bayesian Optimization: Using Process Expertise to Accelerate Manufacturing Optimization](https://arxiv.org/abs/2602.17679v2)** | ⭐ 76/100 | 提出结合专家知识与POGPN的JPSS框架，加速多阶段制造优化。 | 结合专家知识优化高维多阶段过程，实验充分且对比显著，具有较强实用性。 | <details><summary>展开</summary>Bayesian optimization (BO) is a powerful method for optimizing black-box manufacturing processes, but its performance is often limited when dealing with high-dimensional multi-stage systems, where we can observe intermediate outputs. Standard BO models the process as a black box and ignores the intermediate observations and the underlying process structure. Partially Observable Gaussian Process Networks (POGPN) model the process as a Directed Acyclic Graph (DAG). However, using intermediate observations is challenging when the observations are high-dimensional state-space time series. Process-expert knowledge can be used to extract low-dimensional latent features from the high-dimensional state-space data. We propose POGPN-JPSS, a framework that combines POGPN with Joint Parameter and State-Space (JPSS) modeling to use intermediate extracted information. We demonstrate the effectiveness of POGPN-JPSS on a challenging, high-dimensional simulation of a multi-stage bioethanol production process. Our results show that POGPN-JPSS significantly outperforms state-of-the-art methods by achieving the desired performance threshold twice as fast and with greater reliability. The fast optimization directly translates to substantial savings in time and resources. This highlights the importance of combining expert knowledge with structured probabilistic models for rapid process maturation.</details> |
| **[Combining Quasiparticle Self-Consistent $GW$ and Machine-Learned DFT+$U$ in Search of Half-Metallic Heuslers](https://arxiv.org/abs/2602.20621v1)** | ⭐ 74/100 | 结合QPGW与贝叶斯优化DFT+U方法研究半金属赫斯勒合金 | 采用贝叶斯优化提升DFT+U精度，对比多种计算方法，对自旋电子学材料筛选有参考价值。 | <details><summary>展开</summary>Half-metallic Heusler compounds are of significant interest for spintronics. For device fabrication, compounds that can be epitaxially grown on III-V semiconductors are particularly attractive. We present a first-principles investigation of four Co-based and two Ni-based Heusler compounds that are lattice-matched to InAs. The results of density functional theory (DFT) using semi-local and hybrid functionals are compared to quasiparticle self-consistent $GW$ (QPGW). We also consider DFT with machine-learned Hubbard $U$ corrections [npj Computational Materials 6, 180 (2020)] with a new Bayesian optimization (BO) objective function to determine the $U$ values that yield the closest agreement with the QPGW band structure and magnetic moments. We find that DFT+U(BO) can adequately reproduce the key QPGW features in most cases. Our results reveal a strong method dependence of the degree of spin polarization at the Fermi level and, in some cases, even the dominant spin channel (majority or minority). Of the materials studied here, Co$_2$TiSn and Co$_2$ZrAl are the most likely to be half-metals, and Co$_2$MnIn is likely to be a near-half-metal.</details> |
| **[Extending Multi-Source Bayesian Optimization With Causality Principles](https://arxiv.org/abs/2602.14791v1)** | ⭐ 74/100 | 提出MSCBO算法，将因果推断与多源贝叶斯优化结合以提升效率。 | 融合因果关系与多源信息，在降维和降低成本方面有显著改进，实验设计较为扎实。 | <details><summary>展开</summary>Multi-Source Bayesian Optimization (MSBO) serves as a variant of the traditional Bayesian Optimization (BO) framework applicable to situations involving optimization of an objective black-box function over multiple information sources such as simulations, surrogate models, or real-world experiments. However, traditional MSBO assumes the input variables of the objective function to be independent and identically distributed, limiting its effectiveness in scenarios where causal information is available and interventions can be performed, such as clinical trials or policy-making. In the single-source domain, Causal Bayesian Optimization (CBO) extends standard BO with the principles of causality, enabling better modeling of variable dependencies. This leads to more accurate optimization, improved decision-making, and more efficient use of low-cost information sources. In this article, we propose a principled integration of the MSBO and CBO methodologies in the multi-source domain, leveraging the strengths of both to enhance optimization efficiency and reduce computational complexity in higher-dimensional problems. We present the theoretical foundations of both Causal and Multi-Source Bayesian Optimization, and demonstrate how their synergy informs our Multi-Source Causal Bayesian Optimization (MSCBO) algorithm. We compare the performance of MSCBO against its foundational counterparts for both synthetic and real-world datasets with varying levels of noise, highlighting the robustness and applicability of MSCBO. Based on our findings, we conclude that integrating MSBO with the causality principles of CBO facilitates dimensionality reduction and lowers operational costs, ultimately improving convergence speed, performance, and scalability.</details> |
| **[High-lift Wing Separation Control via Bayesian Optimization and Deep Reinforcement Learning](https://arxiv.org/abs/2605.11981v1)** | ⭐ 72/100 | 利用BO与DRL对高升力翼型进行主动流动控制优化研究。 | 采用高精度LES模拟，对比了BO与DRL在复杂流动控制中的效能差异。 | <details><summary>展开</summary>This study investigates active flow control (AFC) of a 30P30N high-lift wing at a Reynolds number Re$_c$ = 450,000 and angle of attack $α$ = 23$^\circ$ using wallresolved large-eddy simulations (LES). Two optimization strategies are explored: open-loop Bayesian optimization (BO) and closed-loop deep reinforcement learning (DRL), both targeting the mitigation of stall and the improvement of aerodynamic efficiency via synthetic jets on the slat, main, and flap elements. The uncontrolled configuration was validated against literature data, confirming the reliability of the LES setup. The BO framework successfully identified steady jet velocities that increased efficiency by +10.9% through a -9.7% drag reduction while maintaining lift. In contrast, the DRL agent, despite leveraging instantaneous flow information from distributed sensors, achieved only minor improvements in lift and drag, with negligible efficiency gain. Training analysis indicated that the penalty-dominated reward constrained exploration. These results highlight the need for carefully designed rewards and computational acceleration strategies in DRL-based flow control at high Reynolds numbers.</details> |
| **[Optimizing Orbital Parameters of Satellites for a Global Quantum Network](https://arxiv.org/abs/2603.02480v1)** | ⭐ 72/100 | 利用贝叶斯优化和遗传算法优化量子卫星网络轨道参数。 | 比较了两种优化框架在量子纠缠分发中的表现，方法严谨且具有实用价值。 | <details><summary>展开</summary>Due to fundamental limitations on terrestrial quantum links, satellites have received considerable attention for their potential as entanglement generation sources in a global quantum internet. In this work, we focus on the problem of designing a constellation of satellites for such a quantum network. We find satellite inclination angles and satellite cluster allocations to achieve maximal entanglement generation rates to fixed sets of globally distributed ground stations. Exploring two black-box optimization frameworks: a Bayesian Optimization (BO) approach and a Genetic Algorithm (GA) approach, we find comparable results, indicating their effectiveness for this optimization task. While GA and BO often perform remarkably similar, BO often converges more efficiently, while later growth noted in GAs is indicative of less susceptibility towards local maxima. In either case, they offer substantial improvements over naive approaches that maximize coverage with respect to ground station placement.</details> |

