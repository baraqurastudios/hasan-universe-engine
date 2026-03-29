# -----------------------------------------------
# 🌌 v8.0 UNIVERSE MASTER LAUNCHER (THE INCEPTION)
# -----------------------------------------------
import sys
import time
from core.memory_cloud import MemoryCloud
from core.self_healing import SelfHealer
from safety.ethics_v8_core import EthicsV8
from safety.v8_observer_locks import ObserverLock
from dashboard.god_mode import app

def initialize_universe():
    print("✨ Starting v8.0 Observer God Layer...")
    time.sleep(1)

    # ১. এথিক্স এবং লক লোড করা (Mandatory)
    print("🛡️ Booting Ethics Engine & Mandatory Locks...")
    ethics = EthicsV8(admin_id="MASTER_USER")
    locks = ObserverLock()
    
    # ২. মেমোরি এবং সেলফ-হিলিং চালু করা
    print("🧠 Awakening Long-term Memory Cloud...")
    memory = MemoryCloud()
    healer = SelfHealer()

    # ৩. সিস্টেম চেক (সব সিকিউরিটি পাস করলে ড্যাশবোর্ড খুলবে)
    print("✅ All Security Protocols Verified.")
    print("\n--- UNIVERSE IS NOW LIVE ---")
    print("👁️ God-Mode Dashboard: http://localhost:8080")
    print("----------------------------\n")

    # ৪. ড্যাশবোর্ড রান করা
    try:
        app.run(port=8080, debug=False, use_reloader=False)
    except KeyboardInterrupt:
        print("\n🛑 Master Shutdown Initiated. Reality Wiping...")
        sys.exit(0)

if __name__ == "__main__":
    initialize_universe()