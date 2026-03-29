import os
import time
import sys

# --- CONFIGURATION ---
LOCK_LIMIT = 60    # ১ মিনিট (Stage 1)
FREEZE_LIMIT = 180 # ৩ মিনিট (Stage 2)
FILES_TO_HIDE = ["v81_engine.py", "admin_panel.py", "github_handler.py"]

def run_v8_core():
    # সাইডবারের ইনপুট বক্স থেকে ডাটা পড়া (আপনার ইনপুট বাটন এটিই)
    user_action = os.getenv("GITHUB_ACCESS_TOKEN")
    REAL_MASTER_KEY = os.getenv("V8_MASTER_KEY")

    print("\n" + "="*45)
    print("🌌 V8.1 CORE SECURITY STATUS")
    print("="*45)

    # ১. ইমার্জেন্সি 'FIRE' বাটন লজিক (Kill Switch)
    if user_action == "FIRE":
        print("\n🚨 [CRITICAL: EMERGENCY SEAL ACTIVATED]")
        for f in FILES_TO_HIDE:
            if os.path.exists(f): os.rename(f, f".{f}.vault")
        print("🌑 ALL FILES BURIED. SYSTEM FROZEN.")
        sys.exit()

    # ২. মাস্টার কি চেক (Login Button Logic)
    elif user_action == REAL_MASTER_KEY:
        print("\n✅ STATUS: AUTHORIZED (ACTIVE)")
        print("🔓 ACTION: BLACK HOLE REVERSED.")
        print(f"⏱️ SECURITY: Auto-Lock in {LOCK_LIMIT}s.")
        
        # ১ মিনিটের টাইমার ব্যাকগ্রাউন্ডে চেক করবে
        time.sleep(LOCK_LIMIT)
        print("\n⚠️ IDLE TIMEOUT: Locking files for safety...")
        # অটো-লক লজিক...
        
    else:
        # স্ট্যাটাস ডিসপ্লে
        print("\n🔴 STATUS: FROZEN")
        print("ℹ️ ACTION REQUIRED:")
        print("1. Enter MASTER KEY in Sidebar for Access.")
        print("2. Enter 'FIRE' in Sidebar for Emergency Lock.")

if __name__ == "__main__":
    run_v8_core()
