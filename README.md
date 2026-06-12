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

## 2026-06-13

## Bayesian optimization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Towards Provably Fair Machine Learning: Bayesian Approaches For Consistent and Transparent Predictions](https://arxiv.org/abs/2606.12615v1)** | ⭐ 82/100 | 提出贝叶斯公平分类器以实现子群预测一致性 | 方法创新且严谨，有效解决了机器学习公平性问题 | <details><summary>展开</summary>ML classifiers deployed in high-stakes domains produce predictions whose quality varies systematically across subgroups. For granular subgroups defined by intersections of multiple features, predictions are often inconsistent with the observed data: the model's outputs contradict the evidence available for that subgroup. This problem is exacerbated by regularisation, which improves aggregate performance by collapsing small subgroups into larger groups, disproportionately affecting demographic minorities. We define two requirements for consistent prediction: determinism (identical individuals receive identical predictions) and statistical consistency (we cannot reject, at significance level alpha, the hypothesis that the predictions for a subgroup were drawn from the Bayesian optimal target distribution inferred for that subgroup). From these requirements we derive the Fair Bayesian classifier, which enforces both across every group and subgroup simultaneously and abstains whenever no consistent deterministic prediction is possible. On three benchmark datasets (Adult, COMPAS, and Bank Marketing), standard classifiers produce statistically inconsistent predictions for a substantial proportion of subgroups. Our classifier achieves zero consistency error by construction while exceeding baseline accuracy and multicalibration on every dataset tested. Statistical consistency provides a principled foundation for prediction quality with direct implications for algorithmic fairness. Minority demographics are disproportionately concentrated in small subgroups, precisely where frequentist inference is least reliable; addressing this inference problem is therefore a necessary step toward fair ML. By enforcing Bayesian consistency at the finest resolution the data supports, the our classifier demonstrates that exhaustive subgroup fairness with principled abstention is achievable in practice.</details> |

