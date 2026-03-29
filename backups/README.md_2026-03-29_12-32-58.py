class ControlPlaneV31:
    """
    v3.1: Observable + Safe Execution Engine
    """

    def __init__(self, strategist, watchdog, executor, audit, override):
        self.strategist = strategist
        self.watchdog = watchdog
        self.executor = executor
        self.audit = audit
        self.override = override

    def run_cycle(self, logs):

        decision = self.strategist.analyze(logs)

        # 🛡️ Human override check
        if self.override.is_locked():
            return "BLOCKED: SYSTEM LOCKED BY HUMAN"

        # 🛡️ Safety check
        if not self.watchdog.validate(decision):
            self.audit.log_decision(decision, "BLOCKED", None)
            return "BLOCKED_BY_SAFETY"

        # ⚙️ Execute
        result = self.executor.execute(decision)

        # 📊 Audit EVERYTHING
        self.audit.log_decision(decision, "EXECUTED", result)

        return {
            "decision": decision,
            "result": result
        }