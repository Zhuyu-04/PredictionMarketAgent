from prediction_market_agent.data.base import StandardMarket
from prediction_market_agent.config import PROB_CRASH_THRESHOLD, ARB_SPREAD_THRESHOLD
class SignalDetector:
    @staticmethod
    def detect(markets: list[StandardMarket]) -> list[dict]:
        signals = []
        # 简单示例：检查概率是否极端（实际应比较历史数据）
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
        # 跨平台价差检测（简单按标题匹配，仅演示）
        # 实际项目中需要更准确的映射
        by_title = {}
        for m in markets:
            by_title.setdefault(m.title, []).append(m)
        for title, group in by_title.items():
            if len(group) >= 2:
                probs = [m.probability for m in group]
                if max(probs) - min(probs) >= ARB_SPREAD_THRESHOLD:
                    signals.append({
                        "type": "arbitrage",
                        "message": f"{title} 跨平台价差 {max(probs)-min(probs):.1%}",
                    })
        return signals