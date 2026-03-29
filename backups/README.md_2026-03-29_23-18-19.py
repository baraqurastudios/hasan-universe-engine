import os
import time
import sys

# --- CONFIGURATION ---
LOCK_LIMIT = 60    # ১ মিনিট (Stage 1)
FREEZE_LIMIT = 180 # ৩ মিনিট (Stage 2)
FILES_TO_HIDE = ["v81_engine.py", "admin_panel.py", "github_handler.py"]

def emergency_seal():
    # সাইডবার থেকে ইনপুট পড়া
    user_input = os.getenv("GITHUB_ACCESS_TOKEN")
    REAL_MASTER_KEY = os.getenv("V8_MASTER_KEY")

    print("\n" + "!"*45)
    print("🔥 V8.1 CORE SECURITY ENGINE: MONITORING...")
    print("!"*45)

    # ১. ইমার্জেন্সি সিল চেক (The "FIRE" Command)
    if user_input == "FIRE":
        print("\n🚨 [CRITICAL: EMERGENCY SEAL ACTIVATED]")
        print("💥 ACTION: TOTAL BLACK HOLE TRIGGERED!")
        
        # সাথে সাথে সব ফাইল লুকিয়ে ফেলা
        for filename in FILES_TO_MANAGE:
            if os.path.exists(filename):
                os.rename(filename, f".{filename}.vault")
        
        print("🌑 ALL FILES BURIED. SHUTTING DOWN NOW...")
        time.sleep(1)
        sys.exit() # সিস্টেমের পাওয়ার পুরোপুরি কাট-অফ

    # ২. নরমাল লগইন চেক
    elif user_input == REAL_MASTER_KEY:
        print("\n✅ [STATUS: AUTHORIZED]")
        # (এখানে আপনার সেই ১ ও ৩ মিনিটের টাইমার লজিক কাজ করবে...)
        print("⏱️ System is Live. Watch out for the 1-min Idle Lock.")
        
    else:
        print("\n🔴 [STATUS: FROZEN]")
        print("⚠️ Master, enter KEY or type 'FIRE' for Emergency Seal.")

if __name__ == "__main__":
    emergency_seal()
