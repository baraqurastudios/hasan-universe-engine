import os
import time
import sys

# --- CONFIGURATION (সেকেন্ডে হিসাব) ---
LOCK_LIMIT = 60    # ১ মিনিট পর ফাইল গায়েব (Stage 1)
FREEZE_LIMIT = 180 # ৩ মিনিট পর টোটাল পাওয়ার অফ (Stage 2)
FILES_TO_HIDE = ["v81_engine.py", "admin_panel.py"]

def trigger_v8_security():
    # ১. সাইডবার থেকে আপনার দেওয়া ইনপুট পড়া
    user_input = os.getenv("GITHUB_ACCESS_TOKEN")
    
    # ২. সিস্টেমের ভেতর লুকিয়ে রাখা আসল কি পড়া (কোডে পাসওয়ার্ড নেই)
    REAL_MASTER_KEY = os.getenv("V8_MASTER_KEY")

    print("\n" + "="*45)
    print("🌌 V8.1 CORE SECURITY ENGINE: INITIALIZING...")
    print("="*45)

    # ৩. সিকিউরিটি চেক
    if user_input and user_input == REAL_MASTER_KEY:
        print("\n✅ [STATUS: AUTHORIZED]")
        print("🔓 ACTION: REVERSING BLACK HOLE...")
        
        # ফাইলগুলো আনলক করা
        for f in os.listdir("."):
            if f.endswith(".vault"):
                original = f.lstrip('.').replace(".vault", "")
                os.rename(f, original)
        
        # স্টেজ ১: ১ মিনিটের কাউন্টডাউন শুরু
        start_time = time.time()
        print(f"⏱️ Master is Active. Auto-Lock in {LOCK_LIMIT}s.")
        
        # ৪. টাইম মনিটরিং লুপ
        while True:
            elapsed = time.time() - start_time
            
            # ১ মিনিট পার হলে - Stage 1: Lock
            if elapsed >= LOCK_LIMIT and elapsed < FREEZE_LIMIT:
                print("\n⚠️ STAGE 1: IDLE TIMEOUT! Locking files...")
                for filename in FILES_TO_HIDE:
                    if os.path.exists(filename):
                        os.rename(filename, f".{filename}.vault")
                print("🌑 Status: Files are now in Black Hole.")
            
            # ৩ মিনিট পার হলে - Stage 2: Total Freeze
            if elapsed >= FREEZE_LIMIT:
                print("\n❄️ STAGE 2: TOTAL FREEZE! Shutting down system...")
                print("🚫 All power lost. Goodbye, Master.")
                sys.exit() # সিস্টেম পুরোপুরি বন্ধ হয়ে যাবে
            
            time.sleep(5) # প্রতি ৫ সেকেন্ড পর চেক করবে
            
    else:
        print("\n🔴 [STATUS: FROZEN]")
        print("⚠️ Master Key missing or incorrect in Sidebar.")
        print("ℹ️ Action: Please enter the Key in GitHub Token box.")

if __name__ == "__main__":
    trigger_v8_activation = trigger_v8_security()
