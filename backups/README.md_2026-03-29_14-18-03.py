# -----------------------------------------------
# 🗝️ v8.0 UNIVERSE MASTER LAUNCHER (SECURED)
# -----------------------------------------------
import sys
from safety.key_gen import KeyGenerator
from safety.ethics_v8_core import EthicsV8
from dashboard.god_mode import app

def start_engine():
    key_system = KeyGenerator()
    
    print("🔒 v8.0 Universe Engine is LOCKED.")
    input_pass = input("🔑 Enter Master Key to Initialize Reality: ")

    # ১. চাবিকাঠি যাচাই (Key Verification)
    if key_system.verify_master(input_pass):
        session_id = key_system.get_session_token()
        print(f"✅ ACCESS GRANTED. Session Token: {session_id}")
        print("🌌 Booting v8.0 Observer God Layer...")
        
        # ২. এথিক্স এবং নিরাপত্তা লোড করা
        ethics = EthicsV8(master_key=session_id)
        print("🛡️ Ethics & Observer Locks: ACTIVE")

        # ৩. ড্যাশবোর্ড চালু করা
        print("🌐 Dashboard: http://localhost:8080")
        app.run(port=8080, debug=False)
    
    else:
        print("🚨 CRITICAL ERROR: UNAUTHORIZED ACCESS ATTEMPT!")
        print("💀 SYSTEM SELF-DESTRUCTING... GOODBYE.")
        sys.exit(1)

if __name__ == "__main__":
    start_engine()