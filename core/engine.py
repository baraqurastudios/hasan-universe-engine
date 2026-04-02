import os
import sys
import time
import logging

class Engine:
    def __init__(self):
        # কনফিগারেশন ফাইল পাথ
        self.config_file = "v82_config.json"
        
        # সেশন ভিত্তিক ট্র্যাকিংয়ের জন্য (হ্যাং হওয়া রোধ করবে)
        self.failed_attempts = 0
        logging.info("BaraQura Engine V8.2 Initialized")

    def process(self, master_key):
        """এটি আপনার Master Key চেক করবে এবং মেইন ইঞ্জিনের কাজ করবে"""
        
        # ১. ফাইল চেক লজিক
        if not os.path.exists(self.config_file):
            # যদি ভুলবশত ফাইলটি আগেই লকডাউনে রিনেম হয়ে থাকে
            if os.path.exists(".hidden_vault_locked"):
                return "🚨 সিস্টেম লকডাউন অবস্থায় আছে। মাস্টার কি কাজ করবে না।"
            
            logging.error("Security Breach: Config file missing!")
            return "🚨 ভুল: আপনার গোপন ফাইল (v82_config.json) খুঁজে পাওয়া যাচ্ছে না!"

        # ২. পাসওয়ার্ড চেক (লজিক: '1234')
        if master_key == "1234":
            self.failed_attempts = 0 # সফল হলে রিসেট হবে
            logging.info("Master Access Granted")
            return "🔓 স্বাগতম মাস্টার! BaraQura সিস্টেম এখন অনলাইন এবং আপনার সেবায় প্রস্তুত।"
        
        else:
            self.failed_attempts += 1
            remaining = 3 - self.failed_attempts
            logging.warning(f"Failed Attempt: {self.failed_attempts}")

            if self.failed_attempts >= 3:
                # সরাসরি sys.exit না করে আগে ফাইল হাইড করবে
                lockdown_status = self.lockdown()
                return f"🚨 বিপদ! ৩ বার ভুল করা হয়েছে। {lockdown_status}"
            
            return f"❌ ভুল চাবি! চেষ্টা বাকি: {remaining}"

    def lockdown(self):
        """আপনার অরিজিনাল লকডাউন এবং শাটডাউন লজিক - Streamlit Safe Version"""
        try:
            # ফাইল রিনেম করে লুকিয়ে ফেলা
            if os.path.exists(self.config_file):
                os.rename(self.config_file, ".hidden_vault_locked")
            
            logging.critical("SYSTEM LOCKDOWN ACTIVATED")
            
            # পিসি বন্ধ করার কমান্ড (বিনা প্রয়োজনে যাতে পিসি বন্ধ না হয় তাই এটি অপশনাল রাখা ভালো)
            # আপনি চাইলে নিচের লাইনটি আনকমেন্ট করতে পারেন
            # os.system("shutdown /s /t 60") # ১ মিনিট সময় দিবে
            
            return "সিস্টেম লক করা হয়েছে এবং তথ্য লুকিয়ে ফেলা হয়েছে।"
        except Exception as e:
            logging.error(f"Lockdown failed: {e}")
            return "লকডাউন প্রক্রিয়া ব্যর্থ হয়েছে।"
