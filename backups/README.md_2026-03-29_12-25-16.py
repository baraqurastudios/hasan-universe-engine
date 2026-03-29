import asyncio
from core.models import Action

class ControlPlaneV22:
    def __init__(self, observer, strategist, watchdog, executor, memory, rollback, monitor):
        self.observer = observer
        self.strategist = strategist
        self.watchdog = watchdog
        self.executor = executor
        self.memory = memory
        self.rollback = rollback
        self.monitor = monitor

    async def run_cycle(self):
        # 1. State Awareness
        services = self.monitor.get_active_services()
        logs = await self.observer.collect_async()

        # 2. Decision Logic
        action = self.strategist.analyze(logs, services)
        if action.type == "NOOP": return "IDLE"

        # 3. Safety & Rollback Prep
        if self.watchdog.validate(action):
            self.rollback.capture_snapshot({"service": action.target, "status": "stable"})
            
            # 4. Persistence & Execution
            self.memory.push_incident({"action": action.type, "target": action.target})
            result = await self.executor.execute(action)
            
            if not result:
                return self.rollback.trigger_rollback()
            return "SUCCESS"
        
        return "BLOCKED"