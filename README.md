import time
from datetime import datetime, timedelta

class AutoPilotController:
    def __init__(self, max_retries=3, window_minutes=10):
        self.max_retries = max_retries
        self.window_minutes = window_minutes
        # এরর হিস্টোরি স্টোর করবে: { error_name: [timestamp1, timestamp2] }
        self.error_history = {}

    def _clean_old_errors(self, error_name):
        """উইন্ডোর বাইরের পুরনো এররগুলো ডিলিট করবে।"""
        now = datetime.now()
        threshold = now - timedelta(minutes=self.window_minutes)
        if error_name in self.error_history:
            self.error_history[error_name] = [
                ts for ts in self.error_history[error_name] if ts > threshold
            ]

    def should_retry(self, error_name):
        self._clean_old_errors(error_name)
        
        if error_name not in self.error_history:
            self.error_history[error_name] = []
            
        # নতুন এরর টাইমস্ট্যাম্প যোগ করা
        self.error_history[error_name].append(datetime.now())
        
        current_count = len(self.error_history[error_name])
        if current_count <= self.max_retries:
            return True, current_count
        return False, current_count

    def activate_emergency_mode(self, error_name):
        print(f"\n🚨 [CRITICAL] EMERGENCY MODE ACTIVATED")
        print(f"🛑 Cause: '{error_name}' failed {self.max_retries} times in {self.window_minutes} min.")
        print(f"📡 Action: Autopilot DISENGAGED. Sending SOS to Admin...")
        # এখানে তোমার v1.3 এর Telegram Alert কল হবে

    def handle_incident(self, error_name):
        can_retry, count = self.should_retry(error_name)
        
        if can_retry:
            print(f"🔄 Attempting Auto-Fix ({count}/{self.max_retries}) for: {error_name}")
            return "healing"
        else:
            self.activate_emergency_mode(error_name)
            return "emergency_stop"