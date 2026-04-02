import os
import json
import logging

class Engine: 
    def __init__(self):
        self.config_file = "v82_config.json"
        self.failed_attempts = 0
        self.black_hole_active = False 
        logging.info("BaraQura Engine V8.2 (Black Hole Ready) Initialized")

    def load_config(self):
        """v82_config.json থেকে মাস্টার কি পড়ার ফাংশন"""
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
        """মাস্টার কি যাচাই এবং ব্ল্যাক হোল প্রোটোকল রান করা"""
        
        # ১. ব্ল্যাক হোল চেক
        if os.path.exists(".black_hole_vault") or os.path.exists(".hidden_vault_locked"):
            self.black_hole_active = True
            return "🌌 [BLACK HOLE ACTIVATED]: সিস্টেমটি মহাকাশের অন্ধকারে হারিয়ে গেছে। উদ্ধার অসম্ভব।"

        correct_key = self.load_config()
        
        # ২. পাসওয়ার্ড যাচাই
        if master_key == correct_key:
            self.failed_attempts = 0
            logging.info("Master Access Granted 🟢")
            return "🔓 স্বাগতম মাস্টার! BaraQura সিস্টেম এখন অনলাইন।"
        
        else:
            self.failed_attempts += 1
            remaining = 4 - self.failed_attempts 

            if self.failed_attempts == 3:
                return "⚠️ শেষ সতর্কবার্তা! পরের বার ভুল হলে ব্ল্যাক হোল সিকিউরিটি ট্রিগার হবে।"

            if self.failed_attempts >= 4:
                self.trigger_black_hole()
                return "🚨 ৪ নম্বর বার ভুল! সিস্টেম এখন 'Black Hole Security'-র অধীনে।"
            
            return f"❌ ভুল চাবি! আপনার চেষ্টা বাকি আছে: {remaining} বার"

    def trigger_black_hole(self):
        """ফাইল রিনেম এবং লকডাউন ফাইল তৈরি করা"""
        try:
            if os.path.exists(self.config_file):
                os.rename(self.config_file, ".black_hole_vault")
                # একটি গোপন লক ফাইল তৈরি করা যাতে রিস্টার্ট দিলেও কাজ না করে
                with open(".hidden_vault_locked", "w") as f:
                    f.write("SYSTEM_SEIZED")
                logging.critical("🌌 BLACK HOLE SECURITY TRIGGERED!")
        except Exception as e:
            logging.error(f"Black Hole Activation failed: {e}")
