from collections import defaultdict
class ProbabilityTracker:
    def __init__(self):
        self.history = defaultdict(list)
    def update(self, market_id: str, probability: float):
        self.history[market_id].append(probability)
    def get_change(self, market_id: str, lookback: int = 5) -> float | None:
        prices = self.history.get(market_id, [])
        if len(prices) >= 2:
            return prices[-1] - prices[-lookback]
        return None
