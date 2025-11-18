"""
restaurants.py

Restaurant Agent (mock)
- Simulates searching for restaurants and returns structured results.
- In a live system this would call a search API or RAG pipeline.
"""

import asyncio

# Mock dataset (in real project you'd call Google Search / Places / RAG)
MOCK_RESTAURANTS = [
    "Thipsamai Pad Thai",
    "Somtum Der",
    "Baan Khanitha",
    "After You Dessert Cafe",
    "ICONSIAM Food Court"
]


async def find_restaurants(query):
    """
    Simulate latency of web search and return a list of restaurants relevant to the query.
    """
    # Simulate network / compute delay
    await asyncio.sleep(0.3)
    # Very simple relevance heuristic: if 'caf' in query -> prefer cafes
    q = query.lower()
    if "cafe" in q or "caf" in q:
        return ["After You Dessert Cafe", "Roast Coffee & Eatery", "Gallery Drip Coffee"]
    # Otherwise return a slice of mock results
    return MOCK_RESTAURANTS
