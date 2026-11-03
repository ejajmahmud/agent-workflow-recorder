"""Deterministic session event recording and offline replay player."""
import time
import json
from typing import List, Dict, Any, Optional


class WorkflowRecorder:
    def __init__(self, session_id: str):
        self.session_id = session_id
        self._events: List[Dict[str, Any]] = []

    def record_step(self, action_type: str, payload: Any) -> None:
        self._events.append({
            "step_index": len(self._events),
            "type": action_type,
            "payload": payload,
            "timestamp": time.time()
        })

    def export_recording(self) -> str:
        return json.dumps({
            "session_id": self.session_id,
            "total_steps": len(self._events),
            "events": self._events
        }, indent=2)

    @classmethod
    def replay(cls, recording_json: str) -> List[Dict[str, Any]]:
        data = json.loads(recording_json)
        return data.get("events", [])
