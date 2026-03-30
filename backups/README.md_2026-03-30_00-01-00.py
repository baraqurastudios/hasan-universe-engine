import os
import sys

# --- CONFIGURATION ---
MASTER_NAME = "Master"
ASSISTANT_NAME = "V8.1 Oracle"

def v8_chat_engine():
    # সাইডবার থেকে ইনপুট নিয়ে চেক করবে মাস্টার কি কি না
    user_action = os.getenv("GITHUB_ACCESS_TOKEN")
    REAL_MASTER_KEY = "V8_UNIVERSE_GOD_2026"

    print(f"\n🌌 {ASSISTANT_NAME}: System Initialized.")
    
    if user_action == REAL_MASTER_KEY:
        print(f"✅ Access Granted. Greetings, {MASTER_NAME}!")
        print("-" * 40)
        
        # এখানে আপনি আপনার কথা বা প্রশ্ন ইনপুট দেবেন (Console Input)
        # যেহেতু এটি একটি ওয়েব এডিটর, আমরা নিচের বক্সটি চ্যাটের জন্য ব্যবহার করব
        print(f"🤖 {ASSISTANT_NAME}: আমি আপনার জন্য এখন কী করতে পারি?")
        print("নির্দেশ দিন (যেমন: 'লক করো', 'ফাইল দেখাও', বা সাধারণ কথা)")
        print("-" * 40)
        
        # চ্যাট ইন্টারফেস লজিক
        while True:
            chat_input = input(f"👤 {MASTER_NAME}: ").strip().lower()
            
            if chat_input in ["hi", "hello", "কেমন আছো"]:
                print(f"🤖 {ASSISTANT_NAME}: আমি চমৎকার আছি মাস্টার! আপনার সিস্টেমের সব জিন এখন শান্ত অবস্থায় আছে।")
            
            elif chat_input in ["lock", "বন্ধ করো", "fire"]:
                print(f"🚨 {ASSISTANT_NAME}: কমান্ড গৃহীত। সব ফাইল ব্ল্যাক হোলে পাঠিয়ে দিচ্ছি...")
                # এখানে আপনার লক করার ফাংশন কল হবে
                break
                
            elif "কে তুমি" in chat_input or "who are you" in chat_input:
                print(f"🤖 {ASSISTANT_NAME}: আমি V8.1, আপনার ডিজিটাল জিনের বোতলের পাহারাদার।")
                
            elif chat_input == "exit":
                print(f"🤖 {ASSISTANT_NAME}: বিদায় মাস্টার! সাবধানে থাকবেন।")
                break
            
            else:
                print(f"🤖 {ASSISTANT_NAME}: আমি আপনার কথা বুঝতে পারছি। আমি কি আপনার কোনো ফাইল এডিট করে দেব?")

    else:
        print("🔴 STATUS: FROZEN. Enter Master Key to talk to me.")

if __name__ == "__main__":
    v8_chat_engine()
