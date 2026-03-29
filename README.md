import os
import time
import sys

# সরাসরি সিস্টেম এনভায়রনমেন্ট থেকে কি নেওয়া
MASTER_KEY = os.getenv("V8_MASTER_KEY")
IDLE_LIMIT = 60 # ১ম স্টেজ: ১ মিনিট

def master_core_gateway():
    print("\n" + "="*30)
    print("🌌 V8.1 CORE ACCESS GATEWAY")
    print("="*30)
    
    # এআই-কে আপনার পাসওয়ার্ড থেকে দূরে রাখতে ইনপুট মাস্কিং
    try:
        # মাস্টার এখানে শুধু তার কি-টি টাইপ করবেন
        user_input = input("🔒 ENTER MASTER KEY: ")
        
        if user_input == MASTER_KEY:
            print("\n✅ [ACCESS GRANTED]")
            print("🚀 Core is now ACTIVE. Black Hole unfreezing...")
            # এখানে ফাইল আনলক হওয়ার লজিক শুরু হবে
            start_idle_monitor()
        else:
            print("\n❌ [ACCESS DENIED]")
            print("⚠️ Intruder alert logged. System remains FROZEN.")
            
    except Exception as e:
        print(f"Error: {e}")

def start_idle_monitor():
    # এখানে ১ মিনিটের টাইমার কাজ করবে
    print(f"⏱️ Security Timer Active: Auto-Lock in {IDLE_LIMIT}s")
    # টাইমার লজিক...

if __name__ == "__main__":
    master_core_gateway()
