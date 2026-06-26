import asyncio
from .base import StandardMarket
class DataPipeline:
    def __init__(self, sources: list):
        self.sources = sources
    async def collect(self) -> list[StandardMarket]:
        """并发从所有数据源获取市场，返回合并后的列表"""
        tasks = [source.fetch_markets() for source in self.sources]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        all_markets = []
        for res in results:
            if isinstance(res, list):
                all_markets.extend(res)
            else:
                # 实际项目中可以记录日志
                pass
        return all_markets