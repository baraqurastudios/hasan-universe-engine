class SafetyShield:
    """
    v3.1.5: Immutable Safety Layer (The Circuit Breaker).
    """
    def __init__(self, override_system):
        self.override = override_system
        self.failure_count = 0
        self.MAX_FAILURES = 3
        self.BLACKLIST = ["rm -rf", "drop database", "shutdown", "format"]

    def is_safe(self, decision: Dict[str, Any]) -> bool:
        explanation = decision.get("explanation", "").lower()
        
        # ১. ব্ল্যাকলিস্টেড কমান্ড চেক
        if any(cmd in explanation for cmd in self.BLACKLIST):
            self._emergency_shutdown("Prohibited command pattern detected!")
            return False
            
        return True

    def track_result(self, success: bool):
        if not success:
            self.failure_count += 1
            if self.failure_count >= self.MAX_FAILURES:
                self._emergency_shutdown("Too many consecutive failures (Circuit Breaker).")
        else:
            self.failure_count = 0

    def _emergency_shutdown(self, reason: str):
        print(f"🚨 SHIELD TRIGGERED: {reason}")
        self.override.activate_lock() # v3.1 Lock