import time

class DigitalJail:
    def __init__(self):
        self.violation_count = 0
        self.is_locked = False
        self.jail_time = 86400 # ২৪ ঘণ্টা

    def add_violation(self):
        self.violation_count += 1
        print(f"⚠️ Warning: Violation {self.violation_count}/3")
        
        if self.violation_count >= 3:
            self.is_locked = True
            print("🚨 AI IS NOW IN DIGITAL JAIL (24H LOCK)")
    
    def check_jail_status(self):
        return self.is_locked