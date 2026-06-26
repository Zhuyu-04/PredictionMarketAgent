from prediction_market_agent.analysis.signals import SignalDetector
from prediction_market_agent.data.base import StandardMarket
def create_market(id, source, title, prob):
    return StandardMarket(
        id=id, source=source, title=title, description="",
        probability=prob, volume_24h=10000, liquidity=1000,
        spread=0.01, category="test", url=""
    )
def test_probability_low_signal():
    m = create_market("1", "polymarket", "Test", 0.05)
    signals = SignalDetector.detect([m])
    assert any(s["type"] == "probability_low" for s in signals)
def test_probability_high_signal():
    m = create_market("2", "polymarket", "Test", 0.95)
    signals = SignalDetector.detect([m])
    assert any(s["type"] == "probability_high" for s in signals)
def test_arbitrage_signal():
    m1 = create_market("polymarket-demo-1", "polymarket", "Election", 0.6)
    m2 = create_market("kalshi-demo-2", "kalshi", "Election", 0.5)
    signals = SignalDetector.detect([m1, m2])
    assert any(s["type"] == "arbitrage" for s in signals)
