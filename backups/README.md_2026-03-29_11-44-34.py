from core.models import Action

class Strategist:
    def analyze(self, logs: str) -> Action:
        # v2.1: Simple reasoning for now, will inject LLM later
        if "timeout" in logs.lower():
            return Action(type="UPDATE_CONFIG", target="timeout", value=30, risk="LOW")
        
        if "500" in logs or "critical" in logs.lower():
            return Action(type="RESTART_SERVICE", target="web_server", risk="MEDIUM")

        return Action(type="NOOP")