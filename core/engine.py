import os
import json
import logging

class Engine: # নিশ্চিত করুন এই নামটি 'Engine' ই আছে
    def __init__(self):
        self.config_file = "v82_config.json"
        self.failed_attempts = 0
        logging.info("BaraQura Engine V8.2 Initialized")

    def load_config(self):
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    data = json.load(f)
                    return data.get("security_layer", {}).get("master_key_hash", "1234")
            return "1234"
        except Exception as e:
            logging.error(f"Config Load Error: {e}")
            return "1234"

    def process(self, master_key):
        if not os.path.exists(self.config_file):
            if os.path.exists(".hidden_vault_locked"):
                return "🚨 সিস্টেম লকডাউন অবস্থায় আছে।"
            return "🚨 ভুল: v82_config.json খুঁজে পাওয়া যাচ্ছে না!"

        correct_key = self.load_config()
        
        if master_key == correct_key:
            self.failed_attempts = 0
            return "🔓 স্বাগতম মাস্টার! BaraQura সিস্টেম এখন অনলাইন।"
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= 3:
                self.lockdown()
                return "🚨 বিপদ! ৩ বার ভুল করা হয়েছে। সিস্টেম লক করা হয়েছে।"
            return f"❌ ভুল চাবি! চেষ্টা বাকি: {3 - self.failed_attempts}"

    def lockdown(self):
        try:
            if os.path.exists(self.config_file):
                os.rename(self.config_file, ".hidden_vault_locked")
            logging.critical("SYSTEM LOCKDOWN ACTIVATED")
        except Exception as e:
            logging.error(f"Lockdown failed: {e}")
