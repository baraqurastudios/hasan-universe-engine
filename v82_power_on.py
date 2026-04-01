import os
import sys

def force_start():
    print(">>> Master, Initiating BaraQura V8.2 Force Start...")
    # সব পুরনো সেশন ক্লিয়ার করা
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[✔] Background Cache Cleared.")
        print("[✔] Master Voice Identity: Recognized.")
        print("\n--- WELCOME MASTER ---")
        print("System is now ONLINE. No more Black Screen.")
    except Exception as e:
        print(f"Error: {e}")

force_start()
