class BaraQuraEngine:
    def __init__(self, strategist, watchdog, executor, audit, override, shield):
        self.strategist = strategist
        self.watchdog = watchdog
        self.executor = executor
        self.audit = audit
        self.override = override
        self.shield = shield # v3.1.5 Safety Shield

    async def run_cycle(self, logs):
        if self.override.is_locked:
            return "ENGINE_PAUSED"

        decision = self.strategist.analyze(logs)
        
        # 🛡️ NEW: Final Safety Shield Validation
        if not self.shield.validate_proposal(decision.__dict__):
            self.audit.record(decision, "SHIELD_REJECTED", "Immutable Rule Violation")
            return "HALTED_BY_SHIELD"

        # ⚙️ Normal Execution
        result = await self.executor.execute(decision.__dict__)
        
        # 📈 Track outcome for Circuit Breaker
        success = True if result and "ERROR" not in str(result).upper() else False
        self.shield.track_execution(success)

        self.audit.record(decision, "EXECUTED", result)
        return result