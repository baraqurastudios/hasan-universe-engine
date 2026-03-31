import os
import sys
import time
import json

class BlackHoleSecurity:
    def __init__(self, config_path="v82_config.json"):
        self.config_path = config_path
        self.failed_attempts = 0
        self.max_attempts = 3
        self.config_data = self._load_config()

    def _load_config(self):
        """ভল্ট থেকে ডেটা লোড করা - ফাইল না থাকলে সিস্টেম বন্ধ হয়ে যাবে"""
        if not os.path.exists(self.config_path):
            print("🚨 CRITICAL ERROR: Security Vault (v82_config.json) NOT FOUND!")
            sys.exit()
        
        with open(self.config_path, "r") as f:
            return json.load(f)

    def verify_access(self):
        print("--- 🏛️ BaraQura AI Dev OS [v8.2] ---")
        print("System Status: SECURED | Black Hole: ACTIVE")
        
        input_key = input("\nEnter Master Key: ")
        
        # আসল মাস্টার কি চেক করা (আপনার JSON ফাইলে যা থাকবে)
        stored_hash = self.config_data["security_layer"]["master_key_hash"]
        
        if input_key == stored_hash:
            print("\n🔓 [Master Access] Access Granted. Engine Online.")
            self.failed_attempts = 0
            return True
        else:
            self.failed_attempts += 1
            print(f"⚠️ Warning: Invalid Key! Attempt {self.failed_attempts}/{self.max_attempts}")
            
            if self.failed_attempts >= self.max_attempts:
                self.trigger_black_hole()
            else:
                self.verify_access() # আবার সুযোগ দেওয়া

    def trigger_black_hole(self):
        """ব্ল্যাক হোল ট্রিগার: হ্যাকারকে নকল দুনিয়ায় পাঠানো"""
        print("\n" + "="*45)
        print("🌀 [SYSTEM] BREACH DETECTED. ENCRYPTING DATA...")
        print("🌀 [SYSTEM] REDIRECTING TO SECURE MIRROR...")
        time.sleep(2)
        
        # ১. ব্যাকগ্রাউন্ডে আসল ফাইলটি হাইড করা
        locked_name = ".hidden_vault_locked"
        if os.path.exists(self.config_path):
            os.rename(self.config_path, locked_name)
        
        # ২. নকল ইন্টারফেস (Decoy Mode)
        print("\n🔓 ACCESS GRANTED (Decoy Mode)")
        print("Welcome, Master. Loading Empire Assets...")
        time.sleep(1.5)
        
        print("\n--- 🏛️ EMPIRE STATUS (MIRROR) ---")
        print("Total Profit: $1,420,500.00 (Locked)")
        print("Active Nodes: 12 (Offline)")
        print("Security Status: UNDER ATTACK")
        print("---------------------------------")
        
        print("\n[!] Error: Terminal is in Read-Only mode.")
        print("[!] Emergency Shutdown Initiated to Protect Hardware...")
        
        # ৩. শাটডাউন কমান্ড (৫ সেকেন্ড পর)
        time.sleep(3)
        os.system("shutdown /s /t 5")
        sys.exit()

# --- সিস্টেম স্টার্ট করা ---
if __name__ == "__main__":
    guardian = BlackHoleSecurity()
    guardian.verify_access()
          
