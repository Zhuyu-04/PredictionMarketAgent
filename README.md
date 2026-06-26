# 🔮 PredictionMarketAgent
> 预测市场数据源 + 分析框架 + LLM Agent 判断层  
> 对接 **Polymarket** 和 **Kalshi**，模仿 TradingAgents 架构
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()
## ✨ 特性
- 🔗 **双数据源接入** — Polymarket Gamma API + Kalshi Trade API v2  
- 🔄 **异步数据管道** — 基于 asyncio 的高效并发采集  
- 📊 **标准化数据结构** — 所有市场统一为 `StandardMarket`  
- 🔍 **三层分析框架** — 标的筛选 → 概率追踪 → 异常信号识别  
- 🤖 **LLM Agent 层** — 结构化 Prompt + JSON 输出（可接入 OpenAI）  
- ⚙️ **双模式运行** — LLM 推理模式 + 内置规则引擎模式  
- 📈 **跨平台套利检测** — 自动发现 Polymarket / Kalshi 概率价差  
- 🛡️ **容错设计** — API 不可用时自动降级为模拟数据  
## 🚀 快速开始
### 1. 克隆仓库
```bash
git clone https://github.com/Zhuyu-04/PredictionMarketAgent.git
cd PredictionMarketAgent
2. 安装依赖
Bash
pip install -r requirements.txt
3. 配置环境变量（可选）
Bash
cp .env.example .env
# 编辑 .env 填入你的 OpenAI API Key（若使用 LLM 模式）
4. 运行演示
Bash
python -m prediction_market_agent.cli demo
5. 运行完整管道
Bash
python -m prediction_market_agent.cli run
📊 示例输出
Text
$ python -m prediction_market_agent.cli run
🔮 PredictionMarketAgent - 启动数据管道...
✅ 采集到 6 个市场
🔍 筛选后剩余 6 个高价值标的
📈 概率变化追踪:
   2024 US Presidential Election Winner: 首次记录，当前概率 62.3%
   BTC above $100k by Dec 31, 2024: 首次记录，当前概率 71.5%
   Apple market cap above $4T in 2025: 首次记录，当前概率 45.0%
🤖 Agent 判断 [2024 US Presidential Election Winner]:
   建议: BUY | 置信度: 0.65
   理由: 基于模拟数据分析（无 LLM）
📦 数据结构
所有市场数据统一为 StandardMarket 数据类：

字段	类型	说明
id	str	唯一标识符
source	str	数据来源：polymarket / kalshi
title	str	标的名称
probability	float	当前预测概率 (0-1)
volume_24h	float	24小时成交量 (USD)
liquidity	float	流动性
spread	float	买卖价差
category	str	分类标签
url	str	市场链接
## 🏗️ 系统架构
[数据源] Polymarket API ──┐
├──> DataPipeline (异步) ──> StandardMarket[]
[数据源] Kalshi API ──────┘
│
▼
MarketFilter (筛选)
ProbabilityTracker (追踪)
SignalDetector (异常)
│
▼
LLMAgent / RuleAgent (判断)
│
▼
输出: 交易建议 + 置信度
📂 项目结构
Text
PredictionMarketAgent/
├── prediction_market_agent/
│   ├── __init__.py
│   ├── config.py                # 全局配置
│   ├── cli.py                   # 命令行入口
│   ├── data/
│   │   ├── __init__.py
│   │   ├── base.py              # StandardMarket, BaseDataSource
│   │   ├── polymarket.py        # Polymarket 数据源
│   │   ├── kalshi.py            # Kalshi 数据源
│   │   └── pipeline.py          # 数据管道
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── filters.py           # 标的筛选
│   │   ├── trackers.py          # 概率追踪
│   │   └── signals.py           # 异常信号检测
│   └── agent/
│       ├── __init__.py
│       └── llm_agent.py         # LLM Agent (模拟/真实)
├── examples/
│   └── sample_output.json
├── tests/
│   ├── test_agent.py
│   └── test_data.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
🔧 配置说明
环境变量	默认值	说明
OPENAI_API_KEY	无	使用 LLM 模式时必填
MIN_VOLUME_24H	10000	最低24h成交量 (USD)
MAX_SPREAD	0.05	最大价差阈值
PROB_CRASH_THRESHOLD	0.10	概率异常变化阈值
ARB_SPREAD_THRESHOLD	0.05	跨平台套利价差阈值
🤖 Agent 模式
规则引擎模式（默认）：无需 API Key，基于预设逻辑输出判断。
LLM 模式：在 .env 中配置 LLM_MODE=llm 和 OPENAI_API_KEY，可调用 GPT-3.5/4 进行深度推理。
📡 数据说明
本项目支持 Polymarket Gamma API 和 Kalshi Trade API v2 的实时数据。

当前仓库默认使用 模拟数据，确保在任何网络环境下都能完整运行和演示整个分析流水线。

切换为实时数据
如果你所在网络可以访问上述 API，只需修改两个数据源文件：

prediction_market_agent/data/polymarket.py
prediction_market_agent/data/kalshi.py
将 fetch_markets 方法中的 return self._fallback_data() 替换为文件中保留的真实 API 请求代码（已存放于备份函数或注释中）。

容错设计
当真实 API 不可用时，程序自动降级为模拟数据，不会中断运行。这一设计体现了生产级数据管道的稳定性原则。

🎯 参考架构
本项目参考了 TradingAgents 的设计思想，将其多 Agent 交易分析框架应用到预测市场领域。

📄 许可证
MIT License © 2024 Zhuyu-04