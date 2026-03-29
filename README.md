import os

def trigger_v8_activation():
    # ১. সাইডবার থেকে ইনপুট পড়া (যা আপনি টাইপ করবেন)
    sidebar_input = os.getenv("GITHUB_ACCESS_TOKEN")

    # ২. সিস্টেমের ভেতর লুকিয়ে রাখা মাস্টার কি পড়া (এটি কোডে দৃশ্যমান নয়)
    # আপনি আপনার সিস্টেমের সেটিংস থেকে 'V8_MASTER_KEY' সেট করে রাখবেন
    REAL_MASTER_KEY = os.getenv("V8_MASTER_KEY")

    print("\n" + "="*40)
    print("🌌 V8.1 CORE SECURITY CHECK")
    print("="*40)

    # ৩. ভেরিফিকেশন লজিক
    if sidebar_input and sidebar_input == REAL_MASTER_KEY:
        print("\n✅ STATUS: AUTHORIZED")
        print("🔓 ACTION: UNFREEZING BLACK HOLE...")
        os.environ["V8_STATUS"] = "ACTIVE"
    else:
        print("\n🔴 STATUS: FROZEN")
        print("⚠️ Unauthorized Key or Empty Input. Access Denied.")
        os.environ["V8_STATUS"] = "LOCKED"

if __name__ == "__main__":
    trigger_v8_activation()
