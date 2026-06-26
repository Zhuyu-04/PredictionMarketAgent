from prediction_market_agent.data.base import StandardMarket
from prediction_market_agent.config import MIN_VOLUME_24H, MAX_SPREAD
class MarketFilter:
    @staticmethod
    def filter(markets: list[StandardMarket]) -> list[StandardMarket]:
        filtered = []
        for m in markets:
            if m.volume_24h >= MIN_VOLUME_24H and m.spread <= MAX_SPREAD:
                filtered.append(m)
        return filtered
