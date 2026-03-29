# -----------------------------------------------
# 💓 v8.0 SMART HEARTBEAT MONITOR (EVENT-BASED)
# -----------------------------------------------
import time
import sys
import keyboard  # এটি ইনস্টল করতে হবে: pip install keyboard

class SmartHeartbeat:
    def __init__(self):
        self.last_verified_time = time.time()
        self.grace_period = 14400  # ৪ ঘণ্টা (সেকেন্ডে)
        self.kill_switch_key = "ctrl+shift+k"

    def request_validation(self, action_name):
        """গুরুত্বপূর্ণ কাজের সময় মাস্টারকে ভেরিফাই করবে"""
        print(f"\n⚠️ CRITICAL ACTION DETECTED: [{action_name}]")
        print(f"🔐 Master, please press '{self.kill_switch_key}' to authorize...")

        # পরবর্তী ৩০ সেকেন্ডের মধ্যে কি-প্রেস না করলে সিস্টেম শাটডাউন হবে
        start_wait = time.time()
        authorized = False
        
        while time.time() - start_wait < 30:
            if keyboard.is_pressed(self.kill_switch_key):
                authorized = True
                self.last_verified_time = time.time()
                print("✅ AUTHORIZED. Proceeding with action...")
                time.sleep(1) # বাটন রিলিজের জন্য সময়
                break
        
        if not authorized:
            self.emergency_shutdown()

    def emergency_shutdown(self):
        print("\n💀 VALIDATION FAILED. Master is not responding.")
        print("🚨 SHUTTING DOWN UNIVERSE ENGINE TO PROTECT REALITY...")
        sys.exit(1)

# ব্যবহারের নিয়ম:
# monitor = SmartHeartbeat()
# if action == "DELETE_DATABASE":
#     monitor.request_validation("Database Purge")