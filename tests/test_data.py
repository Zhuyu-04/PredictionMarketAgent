import pytest
from prediction_market_agent.data.polymarket import PolymarketDataSource
from prediction_market_agent.data.pipeline import DataPipeline
from prediction_market_agent.analysis.filters import MarketFilter
from prediction_market_agent.data.base import StandardMarket
@pytest.mark.asyncio
async def test_polymarket_fetch():
    source = PolymarketDataSource()
    markets = await source.fetch_markets()
    assert len(markets) > 0
@pytest.mark.asyncio
async def test_pipeline_collect():
    source1 = PolymarketDataSource()
    source2 = PolymarketDataSource()
    pipeline = DataPipeline([source1, source2])
    markets = await pipeline.collect()
    assert len(markets) > 0
def test_filter():
    m1 = StandardMarket(id="1", source="test", title="Test", description="", probability=0.5, volume_24h=20000, liquidity=1000, spread=0.02, category="test", url="")
    m2 = StandardMarket(id="2", source="test", title="Test", description="", probability=0.5, volume_24h=500, liquidity=1000, spread=0.02, category="test", url="")
    result = MarketFilter.filter([m1, m2])
    assert len(result) == 1
