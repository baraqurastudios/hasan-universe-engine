import time


# -----------------------------
# 🧠 GLOBAL AUTONOMOUS AI OS
# -----------------------------
class AutonomousAIOSv40:

    def __init__(self, brain, cloud, governance):

        self.brain = brain
        self.cloud = cloud
        self.governance = governance

        self.running = True
        self.system_log = []

    # -----------------------------
    # ⚡ MAIN AUTONOMOUS LOOP
    # -----------------------------
    def run_cycle(self, incoming_signal):

        """
        incoming_signal example:
        {
            "type": "cpu_spike",
            "value": 0.8,
            "task": "optimize_system"
        }
        """

        # 1️⃣ CLOUD EXECUTION CONTEXT
        execution = self.cloud.execute(incoming_signal.get("task", "noop"))

        # 2️⃣ BRAIN ANALYSIS
        decision = self.brain.decide(incoming_signal)

        # 3️⃣ GOVERNANCE CHECK
        final_action = self.governance.resolve([decision])

        # 4️⃣ APPLY ACTION
        result = self._apply(final_action, execution)

        # 5️⃣ LOG EVERYTHING
        self.system_log.append({
            "signal": incoming_signal,
            "decision": decision,
            "final_action": final_action,
            "result": result
        })

        return result

    # -----------------------------
    # ⚙️ ACTION EXECUTOR
    # -----------------------------
    def _apply(self, action, execution):

        act = action.get("action", "NOOP")

        if act == "SCALE_UP":
            return self.cloud.execute("scale_up")

        if act == "LOCKDOWN":
            self.running = False
            return {"status": "SYSTEM_LOCKED"}

        return {
            "status": "NOOP",
            "execution": execution
        }

    # -----------------------------
    # 🔄 SELF-HEAL LOOP
    # -----------------------------
    def self_heal(self):

        last_logs = self.system_log[-5:]

        failures = [log for log in last_logs if "error" in str(log)]

        if len(failures) >= 2:
            return self.cloud.execute("restart_services")

        return {"status": "HEALTHY"}

    # -----------------------------
    # 📊 SYSTEM STATUS
    # -----------------------------
    def status(self):

        return {
            "running": self.running,
            "logs": len(self.system_log),
            "cloud": self.cloud.report(),
            "governance": self.governance.report()
        }