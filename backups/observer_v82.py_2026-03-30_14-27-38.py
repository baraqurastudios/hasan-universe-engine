import time

class RecursiveObserver:
    def __init__(self):
        self.log_file = "observer_logs.txt"
        self.master_override = False

    def observe_action(self, action_name, logic_data):
        # ১. লজিক সিঙ্ক্রোনাইজেশন শুরু
        start_time = time.time()
        
        print(f"🔍 [Observer] Analyzing: {action_name}...")
        
        # ২. টাইম-আউট লজিক (Infinite Loop আটকাতে)
        if time.time() - start_time > 10:
            return "TIMEOUT: Logic Conflict. Manual Intervention Required."

        # ৩. হিউম্যান ওভাররাইড চেক
        if self.master_override:
            self.log_action(action_name, "ALLOWED: Master Override Active.")
            return "SUCCESS"

        # ৪. সাধারণ সিকিউরিটি চেক
        if "delete" in action_name.lower() or "shutdown" in action_name.lower():
            return "WARNING: Risk Detected. Please use Master Key to Force."
        
        return "SUCCESS"

    def log_action(self, action, status):
        with open(self.log_file, "a") as f:
            f.write(f"[{time.ctime()}] Action: {action} | Status: {status}\n")

# --- মাস্টারের ব্যবহারের জন্য ---
obs = RecursiveObserver()

# যদি আপনি নিশ্চিত থাকেন যে কাজটি করতে চান:
obs.master_override = True  # এটিই আপনার 'Final Force Command'
status = obs.observe_action("Delete System Logs", "Recursive Logic")
print(f"Final Status: {status}")
                        
