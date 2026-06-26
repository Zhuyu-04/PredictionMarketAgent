from prediction_market_agent.data.base import StandardMarket
class MockLLMAgent:
    def analyze(self, market: StandardMarket, signals: list[dict]) -> dict:
        # 非常简单的规则：如果出现异常信号则推荐 HOLD，否则 BUY
        action = "HOLD" if signals else "BUY"
        return {
            "market": market.title,
            "action": action,
            "confidence": 0.65,
            "reasoning": "基于模拟数据分析",
            "risk_factors": [],
            "time_horizon": "short"
        }