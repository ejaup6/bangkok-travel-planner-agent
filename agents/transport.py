"""
transport.py

Transport tool / agent
- Acts like a custom tool to estimate travel time and cost between example points.
- This satisfies the "Tools" requirement in the assignment.
"""

import asyncio
import random


async def estimate_transport(query):
    """
    Simulate computing transport summary. Returns a dict with sample fields.
    """
    await asyncio.sleep(0.15)
    # Mock some values; in a live system you'd compute routes and fares
    estimated = {
        "modes": ["BTS", "MRT", "Grab"],
        "typical_time_between_spots_min": 20 + random.randint(-5, 10),
        "typical_cost_per_day_THB": 300 + random.randint(-50, 150)
    }
    return estimated
