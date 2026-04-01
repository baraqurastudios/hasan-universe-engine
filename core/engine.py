import os
import sys
import time

# এটিই আপনার সিস্টেমের মূল পাহারাদার
class SecurityGuardian:
    def __init__(self):
        self.config_file = "v82_config.json" # ফাইলের নাম
        self.failed_attempts = 0 # ভুল চেষ্টার হিসাব

    def start_system(self):
        # প্রথমে চেক করবে ফাইলটি আছে কি না
        if not os.path.exists(self.config_file):
            print("🚨 ভুল: আপনার গোপন ফাইলটি খুঁজে পাওয়া যাচ্ছে না!")
            return

        # ফাইল থেকে পাসওয়ার্ড পড়বে
        print("--- BaraQura v8.2 System Loading ---")
        user_input = input("আপনার Master Key দিন: ")

        # এখানে পাসওয়ার্ড চেক হচ্ছে (সহজ করার জন্য '1234' ধরা হয়েছে)
        if user_input == "1234":
            print("🔓 স্বাগতম মাস্টার! সিস্টেম এখন অনলাইন।")
        else:
            self.failed_attempts += 1
            print(f"❌ ভুল চাবি! চেষ্টা বাকি: {3 - self.failed_attempts}")
            
            if self.failed_attempts < 3:
                self.start_system() # আবার চেষ্টা করতে বলবে
            else:
                self.lockdown() # ৩ বার ভুল হলে লকডাউন

    def lockdown(self):
        print("🚨 বিপদ! ৩ বার ভুল করা হয়েছে। সিস্টেম লক করা হচ্ছে...")
        # আপনার ফাইলটির নাম বদলে দিবে যাতে কেউ খুঁজে না পায়
        os.rename(self.config_file, ".hidden_vault_locked")
        print("🔒 আপনার সব তথ্য লুকিয়ে ফেলা হয়েছে।")
        
        # পিসি ৫ সেকেন্ডের মধ্যে বন্ধ করে দিবে
        time.sleep(2)
        print("💻 পিসি বন্ধ হচ্ছে...")
        os.system("shutdown /s /t 5")
        sys.exit()

# --- সিস্টেম রান করা ---
guardian = SecurityGuardian()
guardian.start_system()
