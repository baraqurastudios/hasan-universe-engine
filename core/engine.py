import os
import sys
import time
import logging

class Engine:
    def __init__(self):
        # আপনার অরিজিনাল কনফিগারেশন
        self.config_file = "v82_config.json"
        self.failed_attempts = 0
        logging.info("BaraQura Engine V8.2 (Security Guardian) Initialized")

    def process(self, master_key):
        """এটি আপনার Master Key চেক করবে এবং মেইন ইঞ্জিনের কাজ করবে"""
        
        # ১. ফাইল চেক লজিক
        if not os.path.exists(self.config_file):
            logging.error("Security Breach: Config file missing!")
            return "🚨 ভুল: আপনার গোপন ফাইলটি খুঁজে পাওয়া যাচ্ছে না!"

        # ২. পাসওয়ার্ড চেক (আপনার লজিক অনুযায়ী '1234')
        if master_key == "1234":
            logging.info("Master Access Granted")
            return "🔓 স্বাগতম মাস্টার! BaraQura সিস্টেম এখন অনলাইন এবং আপনার সেবায় প্রস্তুত।"
        
        else:
            self.failed_attempts += 1
            remaining = 3 - self.failed_attempts
            logging.warning(f"Failed Attempt: {self.failed_attempts}")

            if self.failed_attempts >= 3:
                self.lockdown() # আপনার সেই পাওয়ারফুল লকডাউন ফাংশন
                return "🚨 বিপদ! ৩ বার ভুল করা হয়েছে। সিস্টেম লক করা হচ্ছে..."
            
            return f"❌ ভুল চাবি! চেষ্টা বাকি: {remaining}"

    def lockdown(self):
        """আপনার অরিজিনাল লকডাউন এবং শাটডাউন লজিক"""
        try:
            # ফাইল রিনেম করে লুকিয়ে ফেলা
            if os.path.exists(self.config_file):
                os.rename(self.config_file, ".hidden_vault_locked")
            
            logging.critical("SYSTEM LOCKDOWN ACTIVATED")
            
            # পিসি বন্ধ করার কমান্ড (৫ সেকেন্ড সময়)
            time.sleep(2)
            os.system("shutdown /s /t 5")
            sys.exit()
        except Exception as e:
            logging.error(f"Lockdown failed: {e}")
