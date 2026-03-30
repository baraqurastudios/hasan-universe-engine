import os
import json

# --- CORE CONFIGURATION ---
CORE_VERSION = "V8.1.0"
CONFIG_FILE = "character_bible.json"

def initialize_core():
    print(f"🌌 V8.1 Core: Version {CORE_VERSION} Initializing...")
    print("-" * 40)

    # ১. ক্যারেক্টার ডাটা লোড করা (আপনার বাইবেল থেকে)
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            core_data = json.load(f)
            master_name = core_data["characters"]["Hasan"]["name"] if "Hasan" in core_data["characters"] else "Master"
            print(f"✅ Connection Established: Greetings, {master_name}!")
    else:
        print("⚠️ Warning: Core Bible missing. Running in Generic Mode.")

    # ২. সিস্টেম স্টেট চেক
    print("📡 Engine Status: ONLINE")
    print("🛰️ Stealth Layer: ACTIVE")
    print("-" * 40)
    print("🤖 V8.1: মাস্টার, আপনার কোর ইঞ্জিন এখন সচল।")

if __name__ == "__main__":
    initialize_core()
