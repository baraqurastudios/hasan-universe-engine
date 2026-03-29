class BaraQuraEngine:
    def __init__(self, strategist, watchdog, executor, audit, override):
        self.strategist = strategist
        self.watchdog = watchdog
        self.executor = executor
        self.audit = audit
        self.override = override

    async def run_cycle(self, logs):
        # ১. হিউম্যান ওভাররাইড চেক (v3.1)
        if self.override.is_locked:
            return "STATUS_LOCKED"

        # ২. ডিসিশন মেকিং উইথ এক্সপ্লেনেশন (v3.1)
        decision = self.strategist.analyze(logs)

        # ৩. সেফটি গেট চেক (Watchdog)
        if not self.watchdog.validate(decision.__dict__):
            self.audit.record(decision, "BLOCKED", "Safety Policy Violation")
            return "ACTION_BLOCKED"

        # ৪. এক্সিকিউশন ও অডিট ট্রেইল (v3.1)
        result = await self.executor.execute(decision.__dict__)
        self.audit.record(decision, "EXECUTED", result)

        return result