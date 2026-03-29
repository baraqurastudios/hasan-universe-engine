class Watchdog:
    def __init__(self):
        self.history = {}

    def validate(self, action: Action) -> bool:
        # Risk-based blocking
        if action.risk == "HIGH":
            print(f"🚫 BLOCKED: High-risk action '{action.type}' requires manual approval.")
            return False

        # Loop detection logic
        key = f"{action.type}_{action.target}"
        self.history[key] = self.history.get(key, 0) + 1

        if self.history[key] > 3:
            print(f"🚨 ALERT: Loop detected for {key}! Execution halted.")
            return False

        return True