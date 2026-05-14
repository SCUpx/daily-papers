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

## 2026-05-15

## Bayesian optimization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Maximizing Reliability with Bayesian Optimization](https://arxiv.org/abs/2602.02432v1)** | ⭐ 82/100 | 提出两种贝叶斯优化法以提升极小失效概率下的可靠性 | 方法创新且针对性强，在极低失效概率场景下表现优异 | <details><summary>展开</summary>Bayesian optimization (BO) is a popular, sample-efficient technique for expensive, black-box optimization. One such problem arising in manufacturing is that of maximizing the reliability, or equivalently minimizing the probability of a failure, of a design which is subject to random perturbations - a problem that can involve extremely rare failures ($P_\mathrm{fail} = 10^{-6}-10^{-8}$). In this work, we propose two BO methods based on Thompson sampling and knowledge gradient, the latter approximating the one-step Bayes-optimal policy for minimizing the logarithm of the failure probability. Both methods incorporate importance sampling to target extremely small failure probabilities. Empirical results show the proposed methods outperform existing methods in both extreme and non-extreme regimes.</details> |
| **[SMOG: Scalable Meta-Learning for Multi-Objective Bayesian Optimization](https://arxiv.org/abs/2601.22131v2)** | ⭐ 82/100 | 提出SMOG模型实现多目标贝叶斯优化的元学习 | 结合元学习与多目标优化，方法创新且实验扎实 | <details><summary>展开</summary>Multi-objective optimization aims to solve problems with competing objectives. Evaluating such problems is often slow or expensive, limiting the budget of evaluations. In many applications, historical data from related optimization tasks is available and can be leveraged via meta-learning to accelerate optimization. Bayesian optimization, as a promising technique for expensive black-box problems, has been extended independently to meta-learning and multi-objective optimization, but methods that simultaneously address both settings remain largely unexplored. We propose SMOG-a scalable and modular meta-learning model based on a multi-output Gaussian process-that explicitly learns correlations between objectives. SMOG builds a structured joint Gaussian process prior across meta- and target tasks and, after conditioning on metadata, yields a closed-form prior for the target task. This construction propagates metadata uncertainty into the target surrogate in a principled way. SMOG supports hierarchical, parallel training, achieving linear scaling with the number of meta-tasks. The resulting surrogate integrates seamlessly with standard multi-objective Bayesian optimization acquisition functions. We demonstrate that our method is consistently competitive, delivering strong data efficiency across representative benchmarks and applications.</details> |
| **[Beyond the Black Box: An Interpretable Machine Learning Framework for Predicting Electronic Structure Microdescriptors and Structure-Performance Relationships in Fe-based Catalytic Systems](https://arxiv.org/abs/2605.08994v1)** | ⭐ 78/100 | 基于可解释AI优化铁基催化剂设计 | 方法创新且实用，模型性能显著优于传统基准 | <details><summary>展开</summary>The current catalyst discovery and development pipeline for energy-intensive applications like methane conversion remains bottlenecked by expensive trial-and-error experimentation, irreproducible chemical intuition, and a lack of frameworks linking complex catalytic design spaces to performance. This work presents an interpretable machine learning framework that integrates SHAP-based feature importance analysis (Explainable AI) with tree-based ensembles (Random Forest and Bayesian-optimized CatBoost) to characterize Fe-zeolite and oxide-supported catalysts for the partial oxidation of methane (POM). Despite limited data, the framework decodes complex structure-performance relationships by identifying and ranking thermodynamic, structural, and geometric microdescriptors that influence the electronic band gap and govern macroscale performance metrics such as selectivity, activity, and stability. This work explicitly demonstrates that thermodynamic lattice stability and geometric factors are the primary drivers of electronic band gap (a critical proxy for redox reactivity) rather than bulk stoichiometry. Non-linear models achieve an R2 of 0.61 - 0.77, significantly outperforming traditional linear baselines (R2 = 0.32). This workflow provides both a light-weight generalizable methodology and a prioritized list of physical features for accelerated catalyst screening - and these features can subsequently be integrated into microkinetic and reaction engineering models to create digital twins of complex reactor systems and to enable predictive optimization in autonomous R&amp;D laboratories.</details> |
| **[SPADE: Faster Drug Discovery by Learning from Sparse Data](https://arxiv.org/abs/2605.05370v1)** | ⭐ 78/100 | 提出SPADE算法提升药物筛选效率与速度 | 算法在样本效率与计算速度上有显著提升，实验设计严谨 | <details><summary>展开</summary>Drug discovery seeks molecules (ligands) that bind strongly and selectively to a target protein. However, fewer than 5% of candidate ligands pass the bar for even the early stages of drug discovery. Furthermore, we want methods that work for novel proteins for which we have no prior data. Starting from scratch, we have to iteratively select and test candidate ligands such that we find enough ligands of the desired quality in as few tests as possible. Our proposed algorithm, named SPADE, introduces a novel approach to ligand selection that requires only 40 tests on average to find 10 high-quality ligands. In one-vs-one comparisons, SPADE outperforms deep learning and Bayesian optimization methods on more proteins, achieving median improvements of 7%-32% in sample efficiency. SPADE is also 10x faster than its closest competitor at scoring candidate drugs. Dataset and code is available at https://anonymous.4open.science/r/SPADE_Fast_Drug_Discovery_by_Learning_from_Sparse_Data-F028/README.md</details> |
| **[Physiologically Grounded Driver Behavior Classification: SHAP-Driven Elite Feature Selection and Hybrid Gradient Boosting for Multimodal Physiological Signals](https://arxiv.org/abs/2605.05120v1)** | ⭐ 78/100 | 多模态生理信号驾驶行为分类框架 | 方法严谨且特征选择有效，但未涉及所选类别领域。 | <details><summary>展开</summary>An interpretable and scalable framework for decoding driving behaviors from multimodal physiological signals is proposed in this study. We utilize multimodal physiological driving behavior large-scale dataset comprising synchronized electroencephalogram (EEG), electromyography (EMG), and galvanic skin response (GSR) signals. Our approach involves rigorous preprocessing followed by a domain-specific feature extraction pipeline targeting time-domain, frequency-domain, and derived physiological indices. To address high dimensionality, we employ SHAP-based elite feature selection, retaining the top 250 features to reduce computational overhead while preserving predictive power. Hyperparameter optimization for extreme gradient boosting (XGBoost) and light gradient boosting machine (LightGBM) models is conducted using Bayesian optimization via Optuna. Finally, a weighted soft-voting ensemble is constructed to leverage the complementary strengths of both gradient boosting frameworks. The results demonstrate that the proposed ensemble achieves a test accuracy of 80.91% and a macro-F1 score of 0.79, significantly outperforming single-modality baselines and traditional machine learning models. Ablation studies confirm an 8% performance gain over the best single modality (EEG), validating the necessity of multimodal fusion. SHAP analysis further validates the physiological plausibility of the model, revealing that the EEG contributes the majority of predictive weight, GSR and EMG features provide critical discriminatory signals for high-arousal and motor-intensive maneuvers.</details> |

