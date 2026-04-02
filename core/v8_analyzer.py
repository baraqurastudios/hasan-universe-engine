import os
import time

# এটি ব্লক করা আইপি-র তালিকা ধরে রাখবে
BANNED_IPS = []

def black_hole_trap(ip):
    """হ্যাকারের জন্য তৈরি করা নকল ড্যাশবোর্ড (Decoy)"""
    print(f"\n[!] Critical Alert: Permanent Block Applied to IP: {ip}")
    print("--- REDIRECTING TO SECURE TERMINAL ---")
    time.sleep(2)
    
    # এটি হ্যাকারকে একটি অন্তহীন লুপে আটকে রাখবে
    while True:
        print("\n[Admin-Console]:$ Loading sensitive_data_v8.db...", flush=True)
        time.sleep(3)
        print("[Admin-Console]:$ Error 403: Connection unstable. Retrying...", flush=True)
        time.sleep(5)
        print("[Admin-Console]:$ Initializing remote wipe... [0%]", flush=True)
        time.sleep(2)
        # হ্যাকার মনে করবে সে কিছু করছে, কিন্তু আসলে সে এখানেই আটকে থাকবে।

def v8_sentinel_scan(user_ip="127.0.0.1", attempts=0):
    """Old Scanner Logic + New Trap Logic"""
    
    # যদি ৩ বারের বেশি ভুল চেষ্টা হয়
    if attempts >= 3:
        if user_ip not in BANNED_IPS:
            BANNED_IPS.append(user_ip)
        black_hole_trap(user_ip)
        return False

    # আপনার পুরানো কোড (Old Code)
    print(f"🔍 V8.1 Sentinel: Scanning for vulnerabilities... (Source: {user_ip})")
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print(f"✅ Scanned {len(files)} files. System secure.")
    return True

# ফাইলটি সরাসরি চালালে এটি কাজ করবে (টেস্ট করার জন্য)
if __name__ == "__main__":
    # আমরা এখানে টেস্ট করার জন্য ৩টি ভুল অ্যাটেম্পট দেখাচ্ছি
    v8_sentinel_scan(user_ip="192.168.1.100", attempts=3)
