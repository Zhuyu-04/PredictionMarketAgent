import asyncio
import sys
from prediction_market_agent.data.polymarket import PolymarketDataSource
from prediction_market_agent.data.kalshi import KalshiDataSource
from prediction_market_agent.data.pipeline import DataPipeline
from prediction_market_agent.analysis.filters import MarketFilter
from prediction_market_agent.analysis.signals import SignalDetector
from prediction_market_agent.agent.llm_agent import MockLLMAgent
async def run_pipeline():
    print("🔮 PredictionMarketAgent - 启动数据管道...")
    # 初始化数据源
    polymarket = PolymarketDataSource()
    kalshi = KalshiDataSource()
    pipeline = DataPipeline([polymarket, kalshi])
    # 采集数据
    markets = await pipeline.collect()
    print(f"✅ 采集到 {len(markets)} 个市场")
    # 过滤
    filtered = MarketFilter.filter(markets)
    print(f"🔍 筛选后剩余 {len(filtered)} 个高价值标的")
    # 检测信号
    signals = SignalDetector.detect(filtered)
    if signals:
        print(f"🚨 检测到 {len(signals)} 个信号:")
        for sig in signals[:5]:
            print(f"   - {sig['type']}: {sig['message']}")
    # Agent 分析
    agent = MockLLMAgent()
    for market in filtered[:3]:   # 只分析前3个作为演示
        result = agent.analyze(market, signals)
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