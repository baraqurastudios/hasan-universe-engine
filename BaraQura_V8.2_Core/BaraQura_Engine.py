import os
import sys
import json

class BlackHoleSecurity:
    def __init__(self, config_path="v82_config.json"):
        # যদি ফাইলটি ফোল্ডারের ভেতরে থাকে, তবে সঠিক পথটি নিশ্চিত করা
        self.config_path = config_path
        self.failed_attempts = 0
        self.max_attempts = 3
        self.config_data = None

        # ১. কনফিগ ফাইল লোড করা
        try:
            with open(self.config_path, "r") as f:
                self.config_data = json.load(f)
        except Exception as e:
            print(f"● Vault Missing! Access Denied. Error: {e}")
            sys.exit()

    def verify_access(self):
        # ২. সরাসরি JSON থেকে মাস্টার কি নিয়ে আসা
        master_key = self.config_data["security_layer"]["master_key_hash"]
        
        while self.failed_attempts < self.max_attempts:
            user_input = input("Enter Master Key: ")
            
            if user_input == master_key:
                print("🔓 Access Granted. Welcome, Operator.")
                return True
            else:
                self.failed_attempts += 1
                remaining = self.max_attempts - self.failed_attempts
                print(f"⚠️ Invalid Key! {remaining} attempts left.")
        
        # ৩ বার ভুল হলে লকডাউন ট্রিগার হবে
        self.trigger_lockdown()

    def trigger_lockdown(self):
        print("● Black Hole Activated! Protecting Data...")
        # সিস্টেম শাটডাউন না করে আমরা আপাতত প্রসেসটি বন্ধ রাখছি নিরাপত্তার জন্য
        print("SYSTEM LOCKED. RESTART REQUIRED.")
        sys.exit()

# --- Execution ---
if __name__ == "__main__":
    # আমরা নিশ্চিত করছি ফাইলটি একই ডিরেক্টরিতে আছে
    guardian = BlackHoleSecurity("v82_config.json")
    guardian.verify_access()
