import time
from core.v8_analyzer import v8_sentinel_scan

# কনফিগারেশন
ADMIN_PASSWORD = "V8" # আপনি চাইলে এখানে আপনার পছন্দমতো পাসওয়ার্ড দিতে পারেন
MAX_ATTEMPTS = 3


def start_system():
    print("--- BaraQura Engine V8.3: The Omni-Intelligence ---")
    attempts = 0
    
    # এখানে আমরা একটি কাল্পনিক আইপি ধরে নিচ্ছি, 
    # সার্ভারে চালালে এটি ইউজারের আসল আইপি হবে।
    user_ip = "192.168.1.100" 

    while attempts < MAX_ATTEMPTS:
        password = input("🔑 Enter System Access Password: ")
        
        if password == ADMIN_PASSWORD:
            print("\n✅ Access Granted! Initializing System...")
            # আপনার পুরানো স্ক্যানার রান করবে
            v8_sentinel_scan(user_ip, attempts=0)
            return True
        else:
            attempts += 1
            print(f"❌ Wrong Password! Remaining attempts: {MAX_ATTEMPTS - attempts}")
            
            if attempts >= MAX_ATTEMPTS:
                print("\n🚨 Security Breach Detected! Activating Black Hole...")
                # এই কমান্ডটি সরাসরি আপনার core/v8_analyzer.py এর ট্র্যাপকে ট্রিগার করবে
                v8_sentinel_scan(user_ip, attempts=attempts)
                break

if __name__ == "__main__":
    start_system()
