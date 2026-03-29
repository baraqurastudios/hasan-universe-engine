import time

class DigitalJail:
    def __init__(self):
        self.violation_count = 0
        self.is_jailed = False
        self.jail_duration = 86400 # ২৪ ঘণ্টা (সেকেন্ডে)

    def check_behavior(self, has_violated):
        if has_violated:
            self.violation_count += 1
            print(f"⚠️ Warning {self.violation_count}/3: AI is misbehaving.")

        if self.violation_count >= 3:
            self.lock_ai()

    def lock_ai(self):
        self.is_jailed = True
        print("🚨 AUTO-JAIL ACTIVATED! AI is now locked for 24 hours.")
        # এখানে এআই-এর সব এপিআই (API) এবং ইন্টারনেট কানেকশন ডিসকানেক্ট হবে
        
    def is_access_allowed(self):
        return not self.is_jailed

# ব্যবহারের নিয়ম:
# jail = DigitalJail()
# if not jail.is_access_allowed():
#     print("❌ AI is in Jail. No actions allowed.")