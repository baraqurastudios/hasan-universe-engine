import os
import json
from tele_bridge import send_v8_notification # টেলিগ্রাম কানেক্ট করা হলো

MASTER_KEY = "V8_UNIVERSE_GOD_2026"

def activate_guardian():
    INPUT_KEY = os.getenv("GITHUB_ACCESS_TOKEN")
    
    if INPUT_KEY == MASTER_KEY:
        print("✅ Identity Confirmed.")
        if os.path.exists(".hidden_bible.v8"):
            os.rename(".hidden_bible.v8", "character_bible.json")
            send_v8_notification("মাস্টার, আপনি লগইন করেছেন। ফাইল আনলক করা হয়েছে।")
    else:
        # অনুপ্রবেশকারী ধরলে ফোনে মেসেজ যাবে
        send_v8_notification("🚨 সাবধান! কেউ আপনার সিস্টেমে ভুল টোকেন দিয়ে ঢোকার চেষ্টা করছে!")
        
        if os.path.exists("character_bible.json"):
            os.rename("character_bible.json", ".hidden_bible.v8")
            print("🔒 System Locked & Hidden.")

if __name__ == "__main__":
    activate_guardian()
