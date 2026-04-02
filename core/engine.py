import os
import sys
import time
import json
import logging

class Engine:
    def __init__(self):
        # কনফিগারেশন ফাইল পাথ
        self.config_file = "v82_config.json"
        
        # সেশন ভিত্তিক ট্র্যাকিংয়ের জন্য (হ্যাং হওয়া রোধ করবে)
        self.failed_attempts = 0
        logging.info("BaraQura Engine V8.2 Initialized")

    def load_config(self):
        """v82_config.json ফাইল থেকে লেটেস্ট মাস্টার কি পড়ার ফাংশন"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    data = json.load(f)
                    # আপনার JSON ফাইলের security_layer থেকে কি নেওয়া হচ্ছে
                    return data.get("security_layer", {}).get("master_key_hash", "1234")
            return "1234" # ফাইল না থাকলে ডিফল্ট কি
        except Exception as e:
            logging.error(f"Config Load Error: {e}")
            return "1234"

    def process(self, master_key):
        """এটি আপনার Master Key চেক করবে এবং মেইন ইঞ্জিনের কাজ করবে"""
        
        # ১. ফাইল চেক লজিক
        if not os.path.exists(self.config_file):
            # যদি ভুলবশত ফাইলটি আগেই লকডাউনে রিনেম হয়ে থাকে
            if os.path.exists(".hidden_vault_locked"):
                return "🚨 সিস্টেম লকডাউন অবস্থায় আছে। মাস্টার কি কাজ করবে না।"
            
            logging.error("Security Breach: Config file missing!")
            return "🚨 ভুল: আপনার গোপন ফাইল (v82_config.json) খুঁজে পাওয়া যাচ্ছে না!"

        # ২. ডাইনামিক পাসওয়ার্ড চেক (JSON ফাইল থেকে আনা হচ্ছে)
        correct_key = self.load_config()
        
        if master_key == correct_key:
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
            # ফাইল রিনেম করে লুকিয়ে ফেলা
            if os.path.exists(self.config_file):
                os.rename(self.config_file, ".hidden_vault_locked")
            
            logging.critical("SYSTEM LOCKDOWN ACTIVATED")
            
            # আপনার সেই পাওয়ারফুল পিসি বন্ধ করার লজিক (ঐচ্ছিক)
            # এটি আনকমেন্ট করলে ৩ বার ভুল পাসওয়ার্ড দিলে পিসি অফ হয়ে যাবে
            # os.system("shutdown /s /t 60") 
            
            return "সিস্টেম লক করা হয়েছে এবং তথ্য লুকিয়ে ফেলা হয়েছে।"
        except Exception as e:
            logging.error(f"Lockdown failed: {e}")
            return "লকডাউন প্রক্রিয়া ব্যর্থ হয়েছে।"
