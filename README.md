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