import os
import sys

# আপনার মাস্টার কি এখানে (উদাহরণস্বরূপ: V8_GOD_MODE)
# আপনি আপনার পছন্দের কি-টি এখানে লিখে দিন
MY_REAL_MASTER_KEY = "V8_UNIVERSE_GOD_2026" 

def v8_access_portal():
    print("\n" + "="*40)
    print("🌌 V8.1 MASTER ACCESS PORTAL")
    print("="*40)
    
    # এটিই আপনার সিকিউরিটি বক্স
    print("\n[!] Please input your Key below to UNLOCK the system.")
    
    try:
        # এখানে আপনি আপনার কি-টি টাইপ করবেন
        master_input = input("ENTER KEY: ")
        
        if master_input == MY_REAL_MASTER_KEY:
            print("\n✅ ACCESS GRANTED, MASTER!")
            print("⚡ System status: ACTIVE")
            print("🌑 Black Hole: REVERSED (Files are visible now)")
            
            # আপনার কাজের জন্য ১ মিনিটের টাইম-আউট শুরু
            print("\n⏱️ Auto-Lock Active: System will freeze in 60s of inactivity.")
        else:
            print("\n❌ ACCESS DENIED!")
            print("🚫 Security Status: LOCKED. Files remain in Black Hole.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    v8_access_portal()
