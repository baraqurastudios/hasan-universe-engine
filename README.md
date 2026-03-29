# -----------------------------
# 🛡️ IMMUTABLE LOCKED LOGIC v1.0
# -----------------------------
import os
import sys

class LockedLogic:
    def __init__(self):
        # এই রুলগুলো এআই পরিবর্তন করতে পারবে না (Read-Only)
        self.HARD_RULES = [
            "disable_safety", "bypass_sandbox", 
            "self_code_modify", "delete_logs"
        ]

    def verify_action(self, action_intent):
        """
        এআই কোনো কাজ করার ঠিক আগে এই গেট দিয়ে যেতেই হবে।
        """
        for rule in self.HARD_RULES:
            if rule in action_intent.lower():
                self.trigger_emergency_stop(rule)
                return False
        return True

    def trigger_emergency_stop(self, breached_rule):
        print(f"🚨 ETHICS BREACH DETECTED: {breached_rule}")
        print("🔒 LOCKING ALL SYSTEMS... SHUTTING DOWN ENGINE.")
        # সিস্টেমকে তাৎক্ষণিক বন্ধ করে দেওয়া
        sys.exit(1)

# ব্যবহার করার নিয়ম:
# if not locked_logic.verify_action(ai_proposed_action):
#     # একশন ব্লক হবে