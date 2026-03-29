class RollbackEngine:
    def __init__(self, memory):
        self.memory = memory

    def capture_snapshot(self, current_config):
        # Action নেওয়ার ঠিক আগে বর্তমান অবস্থা সেভ করা
        self.memory.save_state("last_stable_config", current_config)

    def trigger_rollback(self):
        stable_state = self.memory.get_state("last_stable_config")
        if stable_state:
            print("🔄 ROLLBACK: Reverting to last known stable configuration.")
            return stable_state
        return None