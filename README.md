import asyncio
from core.models import Action

class ControlPlane:
    def __init__(self, observer, strategist, watchdog, executor, state):
        self.observer = observer
        self.strategist = strategist
        self.watchdog = watchdog
        self.executor = executor
        self.state = state

    async def run_cycle(self):
        # 1. Collect
        logs = await self.observer.collect_async()

        # 2. Analyze
        action = self.strategist.analyze(logs)

        if action.type == "NOOP":
            return "IDLE: No action needed."

        # 3. Safety Check
        if not self.watchdog.validate(action):
            return f"SAFETY_BLOCK: Action {action.type} denied."

        # 4. Execute
        result = await self.executor.execute(action)

        # 5. Update State
        self.state.update(action, result)

        return f"SUCCESS: {action.type} executed on {action.target}"