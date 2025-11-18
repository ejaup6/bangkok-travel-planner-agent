"""
shopping.py

Shopping Agent (mock)
- Returns shopping venue suggestions for Bangkok.
"""

import asyncio

MOCK_SHOPS = [
    "ICONSIAM",
    "Siam Center",
    "Terminal 21",
    "Chatuchak Weekend Market",
    "MBK Center"
]


async def find_shopping_spots(query):
    await asyncio.sleep(0.25)
    q = query.lower()
    if "market" in q or "night market" in q:
        return ["Chatuchak Weekend Market", "Jodd Fairs Night Market", "Talad Rot Fai Srinakarin"]
    return MOCK_SHOPS
