from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
@dataclass
class StandardMarket:
    """标准化预测市场数据"""
    id: str
    source: str               # "polymarket" 或 "kalshi"
    title: str
    description: str
    probability: float       # 0 ~ 1
    volume_24h: float        # 24小时成交量 (USD)
    liquidity: float         # 流动性
    spread: float            # 买卖价差
    category: str
    end_time: Optional[datetime] = None
    url: str = ""
    raw_data: dict = field(default_factory=dict)
class BaseDataSource:
    """数据源抽象基类"""
    async def fetch_markets(self, limit: int = 500) -> List[StandardMarket]:
        raise NotImplementedError