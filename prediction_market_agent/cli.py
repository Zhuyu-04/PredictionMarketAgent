import asyncio
import sys
from prediction_market_agent.data.polymarket import PolymarketDataSource
from prediction_market_agent.data.kalshi import KalshiDataSource
from prediction_market_agent.data.pipeline import DataPipeline
from prediction_market_agent.analysis.filters import MarketFilter
from prediction_market_agent.analysis.signals import SignalDetector
from prediction_market_agent.analysis.trackers import ProbabilityTracker
from prediction_market_agent.agent.llm_agent import LLMAgent
async def run_pipeline():
    print("🔮 PredictionMarketAgent - 启动数据管道...")
    polymarket = PolymarketDataSource()
    kalshi = KalshiDataSource()
    pipeline = DataPipeline([polymarket, kalshi])
    markets = await pipeline.collect()
    print(f"✅ 采集到 {len(markets)} 个市场")
    filtered = MarketFilter.filter(markets)
    print(f"🔍 筛选后剩余 {len(filtered)} 个高价值标的")
    signals = SignalDetector.detect(filtered)
    if signals:
        print(f"🚨 检测到 {len(signals)} 个信号:")
        for sig in signals[:5]:
            print(f"   - {sig['type']}: {sig['message']}")
    tracker = ProbabilityTracker()
    print("\n📈 概率变化追踪:")
    for market in filtered:
        tracker.update(market.id, market.probability)
        change = tracker.get_change(market.id)
        if change is not None:
            print(f"   {market.title}: {change:+.2%} (最新 vs 前5次记录)")
        else:
            print(f"   {market.title}: 首次记录，当前概率 {market.probability:.1%}")
    agent = LLMAgent()
    for market in filtered[:3]:
        result = await agent.analyze(market, signals)
        print(f"\n🤖 Agent 判断 [{market.title}]:")
        print(f"   建议: {result['action']} | 置信度: {result['confidence']}")
        print(f"   理由: {result['reasoning']}")
def run_demo():
    print("=" * 50)
    print("🔮 PredictionMarketAgent Demo")
    print("=" * 50)
    print("✅ 框架结构正常，数据管道就绪")
    print("💡 使用 'run' 参数启动实时分析 (需要安装依赖)")
    print("示例: python -m prediction_market_agent.cli run")
async def main():
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        await run_pipeline()
    else:
        run_demo()
if __name__ == "__main__":
    asyncio.run(main())
