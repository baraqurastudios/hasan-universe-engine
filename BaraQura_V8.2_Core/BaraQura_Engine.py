import os
import sys
import json

class BlackHoleSecurity:
    def __init__(self, config_path="v82_config.json"):
        self.config_path = config_path
        self.failed_attempts = 0
        self.max_attempts = 3
        
        # ১. ভল্ট (JSON File) ওপেন করার কমান্ড
        try:
            with open(self.config_path, "r") as f:
                self.config_data = json.load(f)
        except:
            print("🚨 Vault Missing! Access Denied.")
            sys.exit()

    def verify_access(self):
        # ২. সরাসরি JSON ফাইল থেকে পাসওয়ার্ড নিয়ে আসা
        master_key = self.config_data["security_layer"]["master_key_hash"]
        user_input = input("Enter Master Key: ")
        
        if user_input == master_key:
            print("🔓 Access Granted. Welcome, Operator.")
            return True
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= self.max_attempts:
                self.trigger_lockdown()
            else:
                print(f"⚠️ Invalid Key! {self.failed_attempts}/{self.max_attempts}")
                self.verify_access()

    def trigger_lockdown(self):
        print("🌀 Black Hole Activated! Protecting Data...")
        # ফাইল হাইড (Rename) করা
        if os.path.exists(self.config_path):
            os.rename(self.config_path, ".hidden_vault_locked")
        
        print("💻 Shutting Down System...")
        os.system("shutdown /s /t 5")
        sys.exit()

# --- Execution ---
if __name__ == "__main__":
    guardian = BlackHoleSecurity()
    guardian.verify_access()
      
