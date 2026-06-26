import json
import os
from collections import defaultdict
HISTORY_FILE = "probability_history.json"
class ProbabilityTracker:
    def __init__(self):
        self.history = defaultdict(list)
        self.load()
    def update(self, market_id: str, probability: float):
        self.history[market_id].append(probability)
        self.save()
    def get_change(self, market_id: str, lookback: int = 5) -> float | None:
        prices = self.history.get(market_id, [])
        if len(prices) >= 2:
            # 修正：lookback 为 1 时，应返回最近一个价格的变化
            return prices[-1] - prices[-2]
        return None
    def save(self):
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, indent=2)
    def load(self):
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for k, v in data.items():
                    self.history[k] = v