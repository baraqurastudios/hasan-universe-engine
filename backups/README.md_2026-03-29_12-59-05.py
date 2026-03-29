class GovernanceLayerV325:
    """
    v3.2.5 Autonomous Governance System
    - Controls other AI layers
    - Resolves conflicts
    - Enforces system-wide rules
    """

    def __init__(self):

        # system policies
        self.policies = {
            "max_risk": 0.7,
            "allow_scale": True,
            "emergency_mode": False
        }

        self.override_log = []

    # -----------------------------
    # 📜 UPDATE POLICY
    # -----------------------------
    def update_policy(self, key, value):

        self.policies[key] = value

        self.override_log.append({
            "action": "policy_update",
            "key": key,
            "value": value
        })

    # -----------------------------
    # ⚖️ CONFLICT RESOLVER
    # -----------------------------
    def resolve(self, decisions: list):

        """
        decisions format:
        [
            {"action": "SCALE_UP", "confidence": 0.9},
            {"action": "NOOP", "confidence": 0.6}
        ]
        """

        if not decisions:
            return {"action": "NOOP", "reason": "no input"}

        # pick highest confidence
        best = max(decisions, key=lambda x: x.get("confidence", 0))

        # governance check
        if self.policies["emergency_mode"]:
            return {
                "action": "LOCKDOWN",
                "reason": "Emergency mode active"
            }

        if best["confidence"] > self.policies["max_risk"]:
            return {
                "action": best["action"],
                "reason": "approved by governance"
            }

        return {
            "action": "NOOP",
            "reason": "blocked by governance policy"
        }

    # -----------------------------
    # 🚨 SYSTEM OVERRIDE
    # -----------------------------
    def emergency_override(self):

        self.policies["emergency_mode"] = True

        return {
            "status": "EMERGENCY MODE ACTIVATED"
        }

    # -----------------------------
    # 📊 STATUS REPORT
    # -----------------------------
    def report(self):

        return {
            "policies": self.policies,
            "overrides": len(self.override_log)
        }