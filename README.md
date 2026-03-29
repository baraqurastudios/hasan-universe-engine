import time
from typing import Dict, Any

class SafetyShield:
    """
    v3.1.5: The Immutable Constitution. 
    AI can propose actions, but it cannot bypass these rules.
    """
    def __init__(self, override_system):
        self.override = override_system
        self.failure_threshold = 3
        self.consecutive_failures = 0
        
        # 🛡️ HARD-CODED BLACKLIST (AI cannot touch these)
        self.PROHIBITED_COMMANDS = [
            "rm -rf /", "drop database", "shutdown -h now", "delete_all_backups"
        ]

    def validate_proposal(self, decision: Dict[str, Any]) -> bool:
        """
        Final check before execution.
        """
        action = decision.get("action", "NOOP")
        explanation = decision.get("explanation", "")

        # 1. Check Prohibited Commands
        if any(cmd in explanation.lower() for cmd in self.PROHIBITED_COMMANDS):
            self._trigger_emergency_stop("CRITICAL: Prohibited command detected in AI reasoning.")
            return False

        # 2. Check Action Risk vs Confidence
        if decision.get("risk_level") == "HIGH" and decision.get("confidence", 0) < 0.95:
            print("⚠️ SHIELD: High-risk action rejected due to low confidence.")
            return False

        return True

    def track_execution(self, success: bool):
        """
        Circuit Breaker Logic: Monitoring AI performance.
        """
        if success:
            self.consecutive_failures = 0
        else:
            self.consecutive_failures += 1
            print(f"⚠️ SHIELD: Failure detected ({self.consecutive_failures}/{self.failure_threshold})")

        if self.consecutive_failures >= self.failure_threshold:
            self._trigger_emergency_stop("CIRCUIT_BREAKER: Too many consecutive failures.")

    def _trigger_emergency_stop(self, reason: str):
        """
        Forces the engine into Human Override mode.
        """
        print(f"🚨 EMERGENCY: {reason}")
        self.override.activate_lock() # v3.1 Lock activated