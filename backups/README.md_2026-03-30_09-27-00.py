import os
import sys

# --- CONFIGURATION ---
ATTEMPT_LIMIT = 3
LOG_FILE = "security_log.v8"

def check_intruder():
    # মাস্টার কী এবং আপনার ইনপুট রিড করা (GitHub Access Token বক্স থেকে)
    user_input = os.getenv("GITHUB_ACCESS_TOKEN")
    REAL_MASTER_KEY = "V8_UNIVERSE_GOD_2026"

    # আগে কতবার ভুল হয়েছে তা চেক করা
    failed_attempts = 0
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            content = f.read()
            failed_attempts = int(content) if content.isdigit() else 0

    print("🛰️ V8.1 Sentinel: Scanning for unauthorized access...")

    # পাসওয়ার্ড চেক
    if user_input == REAL_MASTER_KEY:
        print("✅ Access Granted. Welcome back, Master.")
        # সফলভাবে লগইন করলে কাউন্টার ০ করে দেওয়া
        with open(LOG_FILE, "w") as f: f.write("0")
        
    elif user_input == "FIRE":
        print("🚨 EMERGENCY SEAL ACTIVATED BY MASTER.")
        # সব ফাইল লক করার ফাংশন এখানে কল হবে
        sys.exit()

    else:
        failed_attempts += 1
        print(f"⚠️ Warning: Invalid Key! Attempt {failed_attempts}/{ATTEMPT_LIMIT}")
        
        with open(LOG_FILE, "w") as f: f.write(str(failed_attempts))

        # যদি ৩ বার ভুল হয়
        if failed_attempts >= ATTEMPT_LIMIT:
            print("🚫 CRITICAL: Intruder Detected! Initiating Total Lockdown.")
            # এখানে আপনার সব ফাইল .vault হয়ে যাবে
            os.rename("v81_engine.py", ".v81_engine.py.vault")
            sys.exit()

if __name__ == "__main__":
    check_intruder()
