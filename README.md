class HumanOverride:
    """
    v3.1 Core: Manual control switch (production safety).
    """

    def __init__(self):
        self.locked = False

    def lock_system(self):
        self.locked = True
        return "🔒 SYSTEM LOCKED (Human Override Activated)"

    def unlock_system(self):
        self.locked = False
        return "🔓 SYSTEM UNLOCKED"

    def is_locked(self):
        return self.locked