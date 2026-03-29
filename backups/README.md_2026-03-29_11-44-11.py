# core/engine.py (v2.1 Upgrade)
import asyncio

class ControlPlane:
    async def run_cycle(self):
        # Async monitoring and analysis
        logs = await self.observer.collect_async() 
        decision_json = self.strategist.analyze(logs)
        
        if not decision_json:
            return "IDLE_STATE"

        action_data = json.loads(decision_json)
        
        # v2.1: Advanced Safety Check
        if self.watchdog.is_safe(action_data):
            result = await self.executor.execute_async(action_data)
            self.state_manager.update_after_action(action_data, result)
            return result
        
        return "SAFETY_BLOCK"