import os
import json

class Engine: 
    def __init__(self):
        self.config_path = os.path.join("config", "v82_config.json")
        self.failed_attempts = 0

    def load_config(self):
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r') as f:
                    data = json.load(f)
                    # ডাটা থেকে সরাসরি স্ট্রিং নেওয়া হচ্ছে এবং স্পেস রিমুভ করা হচ্ছে
                    key = data.get("security_layer", {}).get("master_key_hash", "")
                    return str(key).strip()
            return "1234"
        except:
            return "1234"

    def process(self, master_key):
        vault_path = os.path.join("config", ".black_hole_vault")
        if os.path.exists(vault_path) or os.path.exists(".hidden_vault_locked"):
            return "🌌 [BLACK HOLE ACTIVATED]: সিস্টেম লকড।"

        correct_key = self.load_config()
        
        # পাসওয়ার্ড তুলনা করার সময় অতিরিক্ত সতর্কতা
        if str(master_key).strip() == correct_key:
            self.failed_attempts = 0
            return "🔓 স্বাগতম মাস্টার! BaraQura সিস্টেম অনলাইন।"
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= 4:
                self.trigger_black_hole()
                return "🚨 ৪ বার ভুল! Black Hole Security সক্রিয়।"
            return f"❌ ভুল চাবি! আপনার চেষ্টা বাকি আছে: {4 - self.failed_attempts} বার"

    def trigger_black_hole(self):
        try:
            if os.path.exists(self.config_path):
                os.rename(self.config_path, os.path.join("config", ".black_hole_vault"))
                with open(".hidden_vault_locked", "w") as f: f.write("LOCKED")
        except: pass
