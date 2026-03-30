import os

fail_count = 0

def security_watchdog(input_key, actual_key):
    global fail_count
    if input_key != actual_key:
        fail_count += 1
        if fail_count >= 3:
            print("⚠️ SECURITY BREACH! Self-Destructing sensitive data...")
            if os.path.exists("token.enc"): os.remove("token.enc")
            if os.path.exists("v8_master.key"): os.remove("v8_master.key")
            return "🔥 Data Erased for Security."
    return "✅ Access Granted."
  
