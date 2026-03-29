import json
import time

class AuditLogger:
    """
    v3.1 Core: Every decision is recorded for traceability.
    """

    def __init__(self, memory):
        self.memory = memory

    def log_decision(self, decision, status, result):
        entry = {
            "timestamp": time.time(),
            "decision": decision,
            "status": status,
            "result": result
        }

        self.memory.push_history(entry)

    def get_logs(self):
        return self.memory.get("incident_history") or []