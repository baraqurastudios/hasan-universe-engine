import os

# আপনার সিক্রেট মাস্টার কি (এটিই আপনার পাসওয়ার্ড)
MY_SECRET_KEY = "V8_UNIVERSE_GOD_2026"

def trigger_v8_activation():
    # এটি আপনার বাম পাশের ওই ইনপুট বক্স থেকে ডাটা পড়বে
    sidebar_value = os.getenv("GITHUB_ACCESS_TOKEN")

    print("\n" + "="*40)
    print("🌌 V8.1 CORE ACTIVATION UNIT")
    print("="*40)

    if sidebar_value == MY_SECRET_KEY:
        # যদি বক্সের লেখা আর পাসওয়ার্ড মিলে যায়
        print("\n✅ STATUS: AUTHORIZED")
        print("🔓 ACTION: UNFREEZING BLACK HOLE...")
        print("⚡ ALL V8.1 CORE FILES ARE NOW LIVE.")
        
        # এখানে আসল আনলক লজিক ট্রিগার হবে
        os.environ["V8_STATUS"] = "ACTIVE"
    else:
        # যদি না মিলে
        print("\n🔴 STATUS: FROZEN")
        print("⚠️  Master, please put your KEY in the sidebar box first.")
        os.environ["V8_STATUS"] = "LOCKED"

if __name__ == "__main__":
    trigger_v8_activation()
