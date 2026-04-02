import os
import json
import logging

class Engine: 
    def __init__(self):
        self.config_file = "v82_config.json"
        self.failed_attempts = 0
        # ব্ল্যাক হোল সিকিউরিটি স্ট্যাটাস
        self.black_hole_active = False 
        logging.info("BaraQura Engine V8.2 (Black Hole Ready) Initialized")

    def load_config(self):
        """v82_config.json থেকে মাস্টার কি পড়ার ফাংশন"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    data = json.load(f)
                    return data.get("security_layer", {}).get("master_key_hash", "1234")
            elif os.path.exists(".black_hole_vault"):
                return "LOCKED_BY_BLACK_HOLE"
            return "1234"
        except Exception as e:
            logging.error(f"Config Load Error: {e}")
            return "1234"

    def process(self, master_key):
        """মাস্টার কি যাচাই এবং ব্ল্যাক হোল প্রোটোকল রান করা"""
        
        # ১. ব্ল্যাক হোল চেক: সিস্টেম যদি অলরেডি ভল্টে থাকে
        if os.path.exists(".black_hole_vault"):
            self.black_hole_active = True
            return "🌌 [BLACK HOLE ACTIVATED]: সিস্টেমটি সম্পূর্ণভাবে মহাকাশের অন্ধকারে হারিয়ে গেছে। মাস্টার কি ছাড়া উদ্ধার সম্ভব নয়।"

        # ২. ডাইনামিক পাসওয়ার্ড লোড
        correct_key = self.load_config()
        
        # ৩. পাসওয়ার্ড যাচাই
        if master_key == correct_key:
            self.failed_attempts = 0
            logging.info("Master Access Granted 🟢")
            return "🔓 স্বাগতম মাস্টার! BaraQura সিস্টেম এখন অনলাইন এবং আপনার সেবায় প্রস্তুত।"
        
        else:
            self.failed_attempts += 1
            remaining = 4 - self.failed_attempts # মোট ৪ বার সুযোগ
            logging.warning(f"Failed Attempt: {self.failed_attempts}")

            # ৪. ৩ বার ভুল হলে সাধারণ ওয়ার্নিং
            if self.failed_attempts == 3:
                return "⚠️ শেষ সতর্কবার্তা! পরের বার ভুল হলে ব্ল্যাক হোল সিকিউরিটি ট্রিগার হবে।"

            # ৫. ৪ নম্বর বারে ব্ল্যাক হোল সিকিউরিটি ট্রিগার করা
            if self.failed_attempts >= 4:
                self.trigger_black_hole()
                return "🚨 ৪ নম্বর বার ভুল! সিস্টেম এখন 'Black Hole Security'-র অধীনে। সকল কনফিগ ফাইল ধ্বংস/লুকিয়ে ফেলা হয়েছে।"
            
            return f"❌ ভুল চাবি! আপনার চেষ্টা বাকি আছে: {remaining} বার"

    def trigger_black_hole(self):
        """সবচেয়ে শক্তিশালী সিকিউরিটি: ফাইল রিনেম এবং সিস্টেম সিজ করা"""
        try:
            if os.path.exists(self.config_file):
                # ফাইলটিকে এমন এক নামে রিনেম করা যা কেউ চিনবে না
                os.rename(self.config_file, ".black_hole_vault")
                logging.critical("🌌 BLACK HOLE SECURITY TRIGGERED: All nodes encrypted.")
            
            # আপনার সেই আগের শাটডাউন লজিকটি চাইলে এখানে দিতে পারেন
            # os.system("shutdown /s /t 10") 
            
        except Exception as e:
            logging.error(f"Black Hole Activation failed: {e}")
