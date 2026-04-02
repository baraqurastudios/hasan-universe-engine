import os
import json
import logging

class Engine: 
    def __init__(self):
        # আপনার সঠিক পাথ: config ফোল্ডারের ভেতর (নিউ কারেকশন)
        self.config_folder = "config"
        self.config_path = os.path.join(self.config_folder, "v82_config.json")
        self.failed_attempts = 0 # আপনার আগের ভ্যারিয়েবল

    def load_config(self):
        """JSON থেকে মাস্টার কি পড়া (আপনার ফাইলের স্ট্রাকচার অনুযায়ী)"""
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r') as f:
                    data = json.load(f)
                    # আপনার JSON-এর security_layer কি ব্যবহার করা হয়েছে
                    return data.get("security_layer", {}).get("master_key_hash", "1234")
            return "1234"
        except Exception:
            return "1234"

    def process(self, master_key):
        # ব্ল্যাক হোল চেক (আপনার আগের লজিক + নিউ পাথ)
        vault_path = os.path.join(self.config_folder, ".black_hole_vault")
        if os.path.exists(vault_path) or os.path.exists(".hidden_vault_locked"):
            return "🌌 [BLACK HOLE ACTIVATED]: সিস্টেম লকড।"

        correct_key = self.load_config()
        
        if master_key == correct_key:
            self.failed_attempts = 0
            return "🔓 স্বাগতম মাস্টার! BaraQura সিস্টেম অনলাইন।"
        else:
            self.failed_attempts += 1
            # আপনার ৪ বার ট্রাই করার লজিক
            if self.failed_attempts >= 4:
                self.trigger_black_hole()
                return "🚨 ৪ নম্বর বার ভুল! Black Hole Security সক্রিয়।"
            return f"❌ ভুল চাবি! চেষ্টা বাকি: {4 - self.failed_attempts} বার"

    def trigger_black_hole(self):
        """ফাইল রিনেম (আপনার অরিজিনাল ব্ল্যাক হোল লজিক)"""
        try:
            if os.path.exists(self.config_path):
                # config ফোল্ডারের ভেতরেই রিনেম হবে
                os.rename(self.config_path, os.path.join(self.config_folder, ".black_hole_vault"))
                with open(".hidden_vault_locked", "w") as f: 
                    f.write("SYSTEM_SEIZED")
        except:
            pass
