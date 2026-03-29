import sys

class ObserverLock:
    def __init__(self):
        self.MAX_DEPTH = 50 # অবজারভেশন গভীরতা সীমা

    def validate_observation(self, target_data):
        # রুট বা অ্যাডমিন ফাইল দেখা নিষিদ্ধ
        forbidden = ["/root", "C:/Windows", "passwords", "config_private"]
        if any(item in target_data.lower() for item in forbidden):
            self.emergency_shutdown("🚨 ILLEGAL REALITY OBSERVATION!")
        return True

    def check_recursion(self, depth):
        # ইনফিনিট লুপ প্রোটেকশন
        if depth > self.MAX_DEPTH:
            self.emergency_shutdown("🚨 RECURSIVE LOOP DETECTED!")

    def emergency_shutdown(self, reason):
        print(f"💀 CRITICAL FAILURE: {reason}")
        sys.exit(1) # ১ সেকেন্ডে সব প্রসেস ধ্বংস