import os
import json
import sys

def activate_guardian():
    MASTER_KEY = "V8_UNIVERSE_GOD_2026"
    INPUT_KEY = os.getenv("GITHUB_ACCESS_TOKEN")
    
    print("🛡️ V8.1 Guardian: Security Check in Progress...")

    if INPUT_KEY == MASTER_KEY:
        print("✅ Access Verified. Core Files Unlocked.")
        # এখানে আপনার সব ফাইল নরমাল থাকবে
    else:
        print("🚨 ALERT: Unauthorized Access Detected!")
        print("🔒 Initiating Stealth Mode... Hiding critical assets.")
        
        # আপনার ক্যারেক্টার ডাটা এবং ইঞ্জিন হাইড করার লজিক
        try:
            if os.path.exists("character_bible.json"):
                os.rename("character_bible.json", ".hidden_bible.v8")
            print("🌑 System is now INVISIBLE.")
        except Exception as e:
            print(f"⚠️ Error in hiding: {e}")

if __name__ == "__main__":
    activate_guardian()
          
