import os

def v8_intel_engine():
    # মাস্টার কী এবং আপনার ইনপুট রিড করা
    user_input = os.getenv("GITHUB_ACCESS_TOKEN", "").lower()
    
    print("🌌 V8.1 Oracle: Diagnostic Mode Active.")
    print("-" * 40)

    # ১. যদি আপনি ইঞ্জিনের সমস্যা নিয়ে কথা বলতে চান
    if "problem" in user_input or "issue" in user_input or "ভুল" in user_input:
        print("🤖 V8.1: মাস্টার, আমি ইঞ্জিনের লজিক চেক করছি...")
        
        # এখানে সে চেক করবে কোনো ফাইল মিসিং কি না
        critical_files = ["v81_engine.py", "bot.py"]
        missing_files = [f for f in critical_files if not os.path.exists(f)]
        
        if missing_files:
            print(f"⚠️ পাওয়া গেছে! এই ফাইলগুলো মিসিং: {missing_files}")
            print("পরামর্শ: ফাইলগুলো .vault থেকে বের করুন অথবা নতুন করে তৈরি করুন।")
        else:
            print("✅ কোডের স্ট্রাকচার ঠিক আছে। আপনি কি লাইব্রেরি এরর পাচ্ছেন?")
            print("পরামর্শ: 'pip install pyTelegramBotAPI' চেক করুন।")

    # ২. সাধারণ চ্যাট এবং কোডিং আলাপ
    elif "write code" in user_input or "কোড লেখো" in user_input:
        print("🤖 V8.1: আমি কোড লিখতে প্রস্তুত। আপনি কি নতুন কোনো সিকিউরিটি লেয়ার চান?")
        print("নির্দেশ দিন, আমি আপনার জন্য স্ক্রিপ্ট তৈরি করে দিচ্ছি।")

    # ৩. যদি কোনো ইনপুট না থাকে
    elif user_input == "status":
        print("🤖 V8.1: ইঞ্জিন সচল। হার্টবিট চেক: স্বাভাবিক।")

    else:
        print(f"🤖 V8.1: আমি আপনার বার্তা '{user_input}' পেয়েছি।")
        print("মাস্টার, ইঞ্জিনের সমস্যা বা নতুন কোড নিয়ে কিছু বলতে চাইলে এখানে লিখুন।")

if __name__ == "__main__":
    v8_intel_engine()
