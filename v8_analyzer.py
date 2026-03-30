import os
import glob

def check_coding_weakness():
    print("🔍 V8.1 Analyzing your Codebase...")
    print("-" * 40)
    
    files = glob.glob("*.py")
    weakness_found = []

    for file in files:
        with open(file, "r") as f:
            content = f.read()
            
            # ১. সিকিউরিটি চেক (টোকেন লিক হচ্ছে কি না)
            if "8712362120" in content and file != "tele_bridge.py":
                weakness_found.append(f"⚠️ Security Risk: Token exposed in {file}!")
            
            # ২. এরর হ্যান্ডলিং চেক (Try-Except আছে কি না)
            if "try:" not in content:
                weakness_found.append(f"⚠️ Stability Issue: No error handling in {file}.")

            # ৩. হার্ডকোডেড মাস্টার কি চেক
            if "MASTER_KEY =" in content and "os.getenv" not in content:
                weakness_found.append(f"⚠️ Hardcoding: Master Key should be in Environment Variables ({file}).")

    if not weakness_found:
        print("✅ কোডিং-এ কোনো বড় দুর্বলতা পাওয়া যায়নি। মাস্টার, আপনি প্রো-লেভেলে কাজ করছেন!")
    else:
        print("🚨 দুর্বলতা শনাক্ত হয়েছে:")
        for w in weakness_found:
            print(w)
            
    print("-" * 40)

if __name__ == "__main__":
    check_coding_weakness()
    
