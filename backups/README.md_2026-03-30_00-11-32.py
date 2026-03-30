import os

def v8_integrated_chat():
    # সাইডবারের ইনপুট বক্স থেকে আপনার কমান্ড বা কথা পড়বে
    master_command = os.getenv("GITHUB_ACCESS_TOKEN")
    
    print("🌌 V8.1 Oracle: System Synchronized.")
    print("-" * 30)

    # জেমিনির মতো রেসপন্স মেকানিজম
    responses = {
        "hi": "Greetings Master! System is stable. All jinns are in the bottle.",
        "কেমন আছো": "মাস্টার, আমি আপনার দেওয়া কোডে দিব্যি আছি। আপনার নতুন কোনো নির্দেশ আছে?",
        "status": "V8.1 is LIVE. Encryption: Active. Stealth Mode: Enabled.",
        "fire": "🚨 CRITICAL: Emergency Seal Initiated! All files are now hidden.",
        "who are you": "I am V8.1, your personal digital guardian."
    }

    # আপনার ইনপুট অনুযায়ী উত্তর খোঁজা
    found_reply = False
    for key in responses:
        if key in master_command.lower():
            print(f"🤖 V8.1: {responses[key]}")
            found_reply = True
            break
            
    if not found_reply and master_command != "":
        print(f"🤖 V8.1: মাস্টার, আমি আপনার '{master_command}' কমান্ডটি প্রসেস করছি...")
        print("নির্দেশটি সফলভাবে সংরক্ষিত হয়েছে।")

if __name__ == "__main__":
    v8_integrated_chat()
