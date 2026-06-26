import os
import logging
# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
# ---------- 数据源 API 地址 (公开) ----------
POLYMARKET_BASE_URL = "https://gamma-api.polymarket.com"
KALSHI_BASE_URL = "https://trading-api.kalshi.com/trade-api/v2"
# ---------- 分析参数阈值 ----------
MIN_VOLUME_24H = float(os.getenv("MIN_VOLUME_24H", 10000))
MAX_SPREAD = float(os.getenv("MAX_SPREAD", 0.05))
PROB_CRASH_THRESHOLD = float(os.getenv("PROB_CRASH_THRESHOLD", 0.10))
ARB_SPREAD_THRESHOLD = float(os.getenv("ARB_SPREAD_THRESHOLD", 0.05))
# ---------- Agent 模式 ----------
LLM_MODE = os.getenv("LLM_MODE", "rule")        # "llm" 或 "rule"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)