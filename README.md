# Uniswap V3 数据获取与 LP 收益分析 - 1小时教学课程

> 课程目标：从链上数据获取到 LP 收益计算，完整梳理 Uniswap V3 的流动性模型

## 📋 课程大纲

| 页码 | 标题 | 时间 | 内容模块 |
|------|------|------|---------|
| 1 | 标题页 | 2min | 课程导入 |
| 2 | 课程安排 | 1min | 知识框架 |
| 3-4 | Uniswap V3 基础 | 8min | 概念讲解 + 图表 |
| 5-7 | 数据获取方法 | 12min | 链上数据 + Subgraph + 代码示例 |
| 8-10 | LP 仓位分析 | 10min | Position 结构 + 价格区间 + 代码演示 |
| 11-13 | 收益来源与计算 | 15min | 手续费、IL、净收益 + 公式 + 计算器 |
| 14-16 | 实战分析 | 10min | 真实数据案例 + 图表对比 |
| 17-18 | 总结 & 讨论 | 2min | 核心要点 + 思考题 |

**总时长**：60分钟

---

## 🎯 每页设计清单

### 第1页：标题页
- 大标题
- 讲师名字
- 日期
- 背景：Uniswap V3 Logo + AMM 示意图

### 第2页：课程安排
- 6个学习模块流���图
- 每个模块的时间分配
- 学习成果

### 第3页：Uniswap V3 是什么
- V2 vs V3 对比表
- 核心创新点说明
- 市场数据：TVL、交易量

### 第4页：关键概念图解
- Price Range 可视化图
- Tick 概念示意图
- Liquidity 浓度示意图

### 第5页：数据来源概览
- 数据来源分类图
- RPC vs Subgraph 对比
- 典型应用场景

### 第6页：链上数据获取代码
- Python 代码块：读取 pool slot0
- 实际输出数据样本
- 数据解释说明

### 第7页：Subgraph 数据查询
- GraphQL 查询代码
- 查询结果示例 JSON
- 数据字段说明

### 第8页：LP Position 结构
- Position NFT 信息表
- 关键字段说明
- 代码读取示例

### 第9页：价格区间与收益
- 价格范围对比表：不同区间的资本效率
- 可视化：价格在/超出区间的状态
- 数据表格：相同流动性下的收益差异

### 第10页：手续费收益计算
- 公式推导
- Python 计算代码
- 计算结果示例

### 第11页：无常损失（IL）讲解
- IL 公式
- IL 随价格变化的曲线图
- 实际案例对比

### 第12页：净收益计算
- 收益构成的堆积柱状图
- 公式汇总
- Excel / Python 计算器代码

### 第13页：实战案例 - 真实池子分析
- 选定池子：ETH/USDC 0.3%
- 实时数据展示
- Position 历史收益表格
- 图表对比

### 第14页：案例分析 - 手续费 vs IL
- 收益时间序列图
- 手续费积累曲线
- IL 成本曲线
- 净收益曲线

### 第15页：多个 Position 对比
- 不同价格区间的 Position 对比表
- 收益、IL、ROI 对比柱状图
- 结论：最优价格区间分析

### 第16页：Python 完整代码展示
- 数据获取 + 计算 + 可视化 脚本
- 代码注释详细
- 适合现场演示

### 第17页：总结
- 4个核心要点
- 关键公式汇总
- 下一步学习方向

### 第18页：讨论题
- 4个开放式思考题
- QA 环节

---

## 📁 文件结构

```text
uniswap-v3-lp-analysis-course/
├── README.md
├── slides/
│   ├── slide_01_title.md
│   ├── slide_02_agenda.md
│   ├── slide_03_basics.md
│   ├── slide_04_concepts.md
│   ├── slide_05_data_sources.md
│   ├── slide_06_fetch_onchain.md
│   ├── slide_07_subgraph.md
│   ├── slide_08_position.md
│   ├── slide_09_price_range.md
│   ├── slide_10_fees.md
│   ├── slide_11_impermanent_loss.md
│   ├── slide_12_net_profit.md
│   ├── slide_13_case_study_1.md
│   ├── slide_14_case_study_2.md
│   ├── slide_15_comparison.md
│   ├── slide_16_code_demo.md
│   ├── slide_17_summary.md
│   └── slide_18_discussion.md
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
│   ├── v2_vs_v3.png
│   ├── price_range.png
│   ├── tick_concept.png
│   ├── liquidity_distribution.png
│   ├── il_curve.png
│   ├── fee_accumulation.png
│   └── net_profit_comparison.png
├── requirements.txt
└── LICENSE
```

---

## 🚀 快速开始

### 环境配置
```bash
pip install -r requirements.txt
```

### 运行演示
```bash
python code/01_fetch_pool_data.py
python code/04_calculate_fees.py
python code/08_complete_analysis.py
```

---

## 📊 数据示例

### ETH/USDC 0.3% 池子
```text
池子地址: 0x8ad599c3A0ff1De082011EFDDc58f1908eb6e6D8
Token0: WETH
Token1: USDC
费用: 0.3%
TVL: $1.2B (示例)
交易量 (24h): $500M (示例)
```

### LP Position 示例
```text
Position ID: 123456
价格区间: [1800, 2200] USDC/ETH
初始投入: 1 ETH + 2000 USDC
流动性: 1000 liquidity units
手续费收入 (7天): 0.08 ETH + 150 USDC
无常损失: -4%
净收益: +2.5%
```

---

## 🎓 学习成果

完成本课程后，学生应该能够：
1. 理解 Uniswap V3 的核心机制和 V2 的差异
2. 使用 Python + ethers.js 获取链上 Uniswap 数据
3. 使用 Subgraph 进行历史数据查询
4. 计算 LP 的手续费收益、无常损失和净收益
5. 分析不同价格区间的风险收益特征
6. 用数据驱动的方法评估 LP 策略效果

---

## 💡 授课建议

### 时间分配
- 前15分钟：概念讲解（第1-4页）
- 中间30分钟：数据获取 + 收益计算（第5-12页）
- 后10分钟：实战案例 + 讨论（第13-18页）
- 机动5分钟：答疑、代码演示

### 现场演示工具
- Jupyter Notebook
- Dune Analytics
- Etherscan

### 互动方式
- 第9页：让学生预测不同价格区间的收益差异
- 第11页：让学生体验不同波动率下的 IL
- 第15页：让学生讨论“最优的价格区间是多少”

---

## 📚 扩展阅读

- Uniswap V3 官方文档
- Uniswap V3 数学原理
- The Graph Subgraph
- Dune Analytics

---

**最后更新**：2026-10-01  
**课程版本**：v1.0
