import asyncio
import aiohttp
async def main():
    proxy = "http://127.0.0.1:7897"
    url = "https://gamma-api.polymarket.com/markets?limit=1"
    headers = {"User-Agent": "Mozilla/5.0"}
    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        try:
            async with session.get(url, headers=headers, proxy=proxy, timeout=15) as resp:
                print("状态码:", resp.status)
                print(await resp.text()[:300])
        except Exception as e:
            print("请求失败:", e)
asyncio.run(main())
