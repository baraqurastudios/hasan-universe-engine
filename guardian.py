import os
import sys

def emergency_kill_switch(command):
    SECRET_CODE = "KILL_V8_NOW" # আপনার গোপন কোড
    
    if command == SECRET_CODE:
        print("⚠️ EMERGENCY: KILL-SWITCH ACTIVATED!")
        print("🔒 Locking System... Clearing Cache... Shutting Down.")
        # ব্যাক-এন্ড প্রসেস বন্ধ করা
        os._exit(0) 
    else:
        print("✅ System Safe. Monitoring continues...")

# উদাহরণ: কমান্ড চেক
# emergency_kill_switch("KILL_V8_NOW")
