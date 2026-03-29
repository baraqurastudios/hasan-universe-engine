class StateManager:
    def __init__(self):
        self.current_state = {"last_action": None, "status": "BOOTING", "risk_score": 0}

    def update(self, action, result):
        self.current_state["last_action"] = action.type
        self.current_state["status"] = "HEALTHY" if result else "DEGRADED"
        print(f"📊 State Updated: {self.current_state}")