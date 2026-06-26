from prediction_market_agent.data.base import StandardMarket
from prediction_market_agent.config import PROB_CRASH_THRESHOLD, ARB_SPREAD_THRESHOLD
# 手工映射：将相似事件的两个平台 id 关联起来
EVENT_MAP = {
    ("polymarket-demo-1", "kalshi-demo-2"): "US Election",
    ("polymarket-demo-2", "kalshi-demo-1"): "Crypto",
}
class SignalDetector:
    @staticmethod
    def detect(markets: list[StandardMarket]) -> list[dict]:
        signals = []
        # 1. 概率极值检测
        for m in markets:
            if m.probability < PROB_CRASH_THRESHOLD:
                signals.append({
                    "market_id": m.id,
                    "type": "probability_low",
                    "message": f"{m.title} 概率极低 ({m.probability:.1%})"
                })
            elif m.probability > (1 - PROB_CRASH_THRESHOLD):
                signals.append({
                    "market_id": m.id,
                    "type": "probability_high",
                    "message": f"{m.title} 概率极高 ({m.probability:.1%})"
                })
        # 2. 跨平台价差检测（基于映射）
        for (id1, id2), event_name in EVENT_MAP.items():
            m1 = next((m for m in markets if m.id == id1), None)
            m2 = next((m for m in markets if m.id == id2), None)
            if m1 and m2:
                diff = abs(m1.probability - m2.probability)
                if diff >= ARB_SPREAD_THRESHOLD:
                    signals.append({
                        "type": "arbitrage",
                        "message": f"{event_name} 跨平台价差 {diff:.1%} (Polymarket: {m1.probability:.1%}, Kalshi: {m2.probability:.1%})"
                    })
        return signals