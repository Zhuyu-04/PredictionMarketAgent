import pytest
from prediction_market_agent.agent.llm_agent import LLMAgent
from prediction_market_agent.data.base import StandardMarket
@pytest.mark.asyncio
async def test_agent_fallback():
    agent = LLMAgent()
    market = StandardMarket(id="1", source="test", title="Test Market", description="", probability=0.6, volume_24h=10000, liquidity=500, spread=0.01, category="test", url="")
    result = await agent.analyze(market, [])
    assert "action" in result
    assert result["action"] in ["BUY", "SELL", "HOLD"]
