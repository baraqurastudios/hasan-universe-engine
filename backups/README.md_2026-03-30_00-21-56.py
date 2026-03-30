import os

# আপনার আসল গিটহাব টোকেনটি এখানে একবার সেভ করে নিন
# যাতে বার বার টোকেন বক্সে লিখতে না হয়
MY_REAL_TOKEN = "আপনার_আসল_টোকেন_এখানে_দিন"

def v8_vocal_engine():
    # এটি আপনার ইনপুট পড়ার একটি অল্টারনেটিভ ওয়ে
    # আমরা এখন 'README.md' ফাইলের প্রথম লাইনটি ব্যবহার করব কথা বলার জন্য
    try:
        with open("README.md", "r") as f:
            lines = f.readlines()
            # প্রথম লাইনে যা লিখবেন সেটা হবে আপনার কমান্ড
            master_msg = lines[0].strip().lower() if lines else ""
    except:
        master_msg = ""

    print("🌌 V8.1 Oracle: Listening via README interface.")
    
    if "status" in master_msg:
        print("🤖 V8.1: ইঞ্জিন সচল। হার্টবিট চেক: স্বাভাবিক।")
    elif "fire" in master_msg:
        print("🚨 V8.1: Emergency Seal Initiated!")
    else:
        print("🤖 V8.1: মাস্টার, README.md ফাইলের প্রথম লাইনে আপনার প্রশ্ন লিখুন।")

if __name__ == "__main__":
    v8_vocal_engine()
