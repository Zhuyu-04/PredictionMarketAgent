import json
from prediction_market_agent.data.base import StandardMarket
from prediction_market_agent.config import OPENAI_API_KEY
try:
    from openai import AsyncOpenAI
except ImportError:
    AsyncOpenAI = None
class LLMAgent:
    def __init__(self):
        if OPENAI_API_KEY and OPENAI_API_KEY != "sk-your-key-here" and AsyncOpenAI is not None:
            try:
                self.client = AsyncOpenAI(api_key=OPENAI_API_KEY)
            except Exception:
                self.client = None
        else:
            self.client = None
    async def analyze(self, market: StandardMarket, signals: list[dict]) -> dict:
        if self.client is None:
            return self._fallback(market, signals)
        signals_text = "\n".join([f"- {s['type']}: {s.get('message', '')}" for s in signals]) if signals else "无异常信号"
        prompt = f"""你是一位专业的预测市场分析师。
请基于以下市场信息和分析信号，给出你的交易判断。
## 市场信息
- 标的: {market.title}
- 当前概率: {market.probability:.1%}
- 24h成交量: ${market.volume_24h:,.0f}
- 价差: {market.spread:.1%}
- 数据源: {market.source}
## 分析信号
{signals_text}
## 任务
1. 评估该标的的风险/回报
2. 判断当前概率是否被高估或低估
3. 给出交易建议 (BUY/SELL/HOLD)
4. 提供置信度评分 (0-1)
5. 用 JSON 格式输出，包括 action, confidence, reasoning, risk_factors, time_horizon
请严格按照 JSON 格式回复，不要包含任何其他文字。"""
        try:
            response = await self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=500,
            )
            content = response.choices[0].message.content
            content = content.strip()
            if content.startswith("```json"):
                content = content[7:]
            if content.endswith("```"):
                content = content[:-3]
            return json.loads(content)
        except Exception as e:
            print(f"LLM 调用失败: {e}，降级为模拟")
            return self._fallback(market, signals)
    def _fallback(self, market, signals):
        action = "HOLD" if signals else "BUY"
        return {
            "market": market.title,
            "action": action,
            "confidence": 0.65,
            "reasoning": "基于模拟数据分析（无 LLM）",
            "risk_factors": [],
            "time_horizon": "short"
        }
