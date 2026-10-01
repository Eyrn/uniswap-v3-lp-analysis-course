# Uniswap V3 LP 收益分析课程

> 从链上数据获取到 LP 收益计算的实战教学项目

## 项目简介

这是一个面向 Web3 / DeFi 研究与教学的 Python 项目，围绕 Uniswap V3 流动性池（LP）展开：

- 获取链上池子状态与价格数据
- 获取 Position / NFT 仓位数据
- 分析手续费收益、无常损失（Impermanent Loss）与净收益
- 结合可视化图表进行教学演示

该项目适合：

- 课程讲解
- 研究型分析脚本
- 个人学习与案例复现
- DeFi / AMM 相关内容教学

## 目录结构

```text
uniswap-v3-lp-analysis-course/
├── README.md
├── requirements.txt
├── LICENSE
├── code/
│   ├── 01_fetch_pool_data.py
│   ├── 02_fetch_position.py
│   ├── 03_subgraph_query.py
│   ├── 04_calculate_fees.py
│   ├── 05_calculate_il.py
│   ├── 06_net_profit.py
│   ├── 07_visualization.py
│   └── 08_complete_analysis.py
├── data/
│   ├── sample_pools.json
│   ├── sample_positions.json
│   └── sample_results.csv
├── images/
│   ├── v2_vs_v3.svg
│   ├── price_range.svg
│   └── il_curve.svg
├── slides/
│   ├── slide_01_title.md
│   ├── slide_02_agenda.md
│   └── slide_03_basics.md
└── ...
```

## 快速开始

### 1. 安装依赖

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
# 或 .venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 2. 运行示例脚本

```bash
python code/01_fetch_pool_data.py
python code/04_calculate_fees.py
python code/08_complete_analysis.py
```

### 3. 查看分析结果

示例数据位于 `data/` 目录，生成结果会输出到终端或 CSV 文件中。

## 学习路线

1. Uniswap V3 基础概念
2. 数据获取：RPC / Subgraph
3. Position 与价格区间分析
4. 手续费收益计算
5. 无常损失与净收益
6. 可视化与案例分析

## 课程主题

- 池子状态：slot0 / tick / liquidity
- Position：lower/upper price / fees / liquidity
- 收益来源：fee + price movement + operational cost
- 风险观测：IL 与市场波动率
- 策略评估：不同区间策略下的收益差异

## 关键脚本说明

### `code/01_fetch_pool_data.py`

读取示例池子数据，展示池子基础信息、价格与流动性状态。

### `code/02_fetch_position.py`

解析 Position 数据，展示区间、流动性与持仓结构。

### `code/03_subgraph_query.py`

提供 GraphQL 查询示例，用于获取 The Graph 中的历史池子与 Position 数据。

### `code/04_calculate_fees.py`

根据样例数据计算手续费收益，展示简单的累计公式。

### `code/05_calculate_il.py`

计算不同价格变化下的无常损失，帮助理解 LP 在极端波动中的风险。

### `code/06_net_profit.py`

将手续费收益与 IL 合并，评估净收益。

### `code/07_visualization.py`

生成收益曲线、IL 曲线，以及不同区间策略对比图。

### `code/08_complete_analysis.py`

整合各阶段脚本，提供完整的案例分析入口。

## 课程输出对象

- 适合 1 小时教学课程
- 便于现场演示
- 可扩展为更长的研究型分析项目

## 贡献方式

欢迎补充以下内容：

- 更完整的 Subgraph 查询
- 实际链上 RPC 接口脚本
- 更细的收益模型
- 自动化图表生成
- 更多教学案例与对比分析

## 许可证

本项目采用 MIT License。详情见 `LICENSE`。

## 更新说明

- 2026-10-01：初始化课程项目结构，并补充示例脚本、数据与可视化资源。

