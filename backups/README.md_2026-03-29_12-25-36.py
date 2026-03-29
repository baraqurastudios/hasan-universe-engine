import time

class AuditSystem:
    def __init__(self, memory):
        self.memory = memory

    def record(self, decision_obj, status, result):
        # v3.1: Storing full decision object with timestamp
        entry = {
            "timestamp": time.time(),
            "decision": decision_obj.__dict__,
            "status": status,
            "result": result
        }
        self.memory.push_history(entry)