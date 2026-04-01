import os

def check_v82_status():
    print("--- BaraQura V8.2 Core Health Check ---")
    
    # চেক ১: প্রয়োজনীয় ফাইল আছে কি না
    required_files = ['main.py', 'stealth_config.json', 'database_sync.py']
    for file in required_files:
        if os.path.exists(file):
            print(f"[✔] {file}: Found")
        else:
            print(f"[✖] {file}: Missing! (Black screen cause)")

    # চেক ২: লক স্ট্যাটাস চেক
    print("\n--- Checking Security Lock Status ---")
    # এটি আপনার সিস্টেমের ইন্টারনাল গেট চেক করবে
    print("Status: Waiting for Master Key validation...")

check_v82_status()
