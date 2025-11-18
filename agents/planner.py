"""
planner.py

Planner Agent (Orchestrator)
- Demonstrates sequential + parallel agent orchestration using asyncio.
- Calls restaurant/shopping/transport agents in parallel, composes an itinerary,
  and optionally writes user preferences to memory.

No external API keys are required. All search responses are mocked for demo.
"""

import asyncio
import json
from agents.restaurants import find_restaurants
from agents.shopping import find_shopping_spots
from agents.transport import estimate_transport
from agents.memory_service import MemoryService

# Memory file path (simple JSON storage)
MEMORY_FILE = "examples/sample_sessions.json"


class PlannerAgent:
    def __init__(self, memory_file=MEMORY_FILE):
        self.memory = MemoryService(memory_file)

    async def _gather_suggestions(self, query):
        """
        Call multiple sub-agents in parallel and return their results.
        """
        # Kick off parallel tasks
        tasks = [
            asyncio.create_task(find_restaurants(query)),
            asyncio.create_task(find_shopping_spots(query)),
            asyncio.create_task(estimate_transport(query))
        ]
        # Await all
        results = await asyncio.gather(*tasks)
        restaurants, shopping, transport = results
        return {
            "restaurants": restaurants,
            "shopping": shopping,
            "transport": transport
        }

    async def create_itinerary(self, user_id, query, days=2, budget=None, save_preferences=False):
        """
        Main entrypoint for planner.
        - Uses sequential logic: read memory -> gather info (parallel) -> compose -> (optionally) save memory
        """
        # 1) Read memory (sequential)
        prefs = self.memory.get_user_preferences(user_id)
        if prefs:
            # merge or prefer explicit query for demo; we include prefs for trace
            query_with_prefs = f"{query} Preferences: {prefs}"
        else:
            query_with_prefs = query

        # 2) Gather sub-agent suggestions in parallel
        suggestions = await self._gather_suggestions(query_with_prefs)

        # 3) Compose itinerary (simple heuristic)
        itinerary = self._compose_itinerary(suggestions, days, budget)

        # 4) Optionally save preferences
        if save_preferences:
            # For demo we save simple extracted prefs; in real app you'd parse user input
            self.memory.save_user_preferences(user_id, {"last_query": query, "preferred_days": days})

        # 5) Log a session entry for observability (append)
        self.memory.append_session_log(user_id, query, itinerary)

        return itinerary

    def _compose_itinerary(self, suggestions, days, budget):
        """
        Simple synthesizer that builds a day-by-day list using suggestions.
        This function demonstrates how a Planner agent composes different agent outputs.
        """
        restaurants = suggestions.get("restaurants", [])[:max(1, days+1)]
        shopping = suggestions.get("shopping", [])[:max(1, days+1)]
        transport = suggestions.get("transport", {})

        daily_plan = {}
        for d in range(1, days + 1):
            day = f"Day {d}"
            daily_plan[day] = []
            # simple alternating plan: morning shopping, lunch at restaurant, evening sightseeing
            if d-1 < len(shopping):
                daily_plan[day].append(f"Morning: {shopping[d-1]}")
            if d-1 < len(restaurants):
                daily_plan[day].append(f"Lunch: {restaurants[d-1]}")
            daily_plan[day].append(f"Evening: Explore local area / markets")
        result = {
            "trip_duration": f"{days} Days",
            "daily_plan": daily_plan,
            "transport_summary": transport,
            "estimated_budget": budget or "Not specified"
        }
        return result


# Quick local demo when run as script
if __name__ == "__main__":
    async def demo():
        planner = PlannerAgent()
        itinerary = await planner.create_itinerary(
            user_id="demo_user",
            query="3 days Bangkok, cafes, night markets, shopping",
            days=3,
            budget="12000 THB",
            save_preferences=True
        )
        print(json.dumps(itinerary, indent=2, ensure_ascii=False))

    asyncio.run(demo())
