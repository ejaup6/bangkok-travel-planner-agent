"""
memory_service.py

Simple JSON-based Memory Service.
- Stores user preferences and session logs in a JSON file.
- This demonstrates Session & Memory without external DB.
"""

import json
import os
from datetime import datetime

DEFAULT_PATH = "examples/sample_sessions.json"


class MemoryService:
    def __init__(self, filepath=DEFAULT_PATH):
        self.filepath = filepath
        # Ensure file exists
        if not os.path.exists(os.path.dirname(self.filepath)) and os.path.dirname(self.filepath):
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump({"users": {}, "sessions": []}, f, ensure_ascii=False, indent=2)

    def _read(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def _write(self, data):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get_user_preferences(self, user_id):
        data = self._read()
        return data.get("users", {}).get(user_id)

    def save_user_preferences(self, user_id, prefs: dict):
        data = self._read()
        if "users" not in data:
            data["users"] = {}
        data["users"][user_id] = prefs
        self._write(data)

    def append_session_log(self, user_id, query, planner_output):
        data = self._read()
        entry = {
            "user_id": user_id,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "query": query,
            "planner_output": planner_output
        }
        if "sessions" not in data:
            data["sessions"] = []
        data["sessions"].append(entry)
        self._write(data)
