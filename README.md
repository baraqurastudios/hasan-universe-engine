class HumanOverride:
    def __init__(self):
        self.is_locked = False

    def activate_lock(self):
        self.is_locked = True
        return "🔒 ENGINE_LOCKED: Autonomous cycle suspended by Admin."

    def release_lock(self):
        self.is_locked = False
        return "🔓 ENGINE_UNLOCKED: Resuming autonomy."