import requests
import time
import sys

# ==============================
# CONFIGURATION
# ==============================
# আপনার জেনারেট করা লেটেস্ট টোকেনটি এখানে বসাবেন
TELEGRAM_TOKEN = "8712362120:AAEopZQcsqZCHbNDck2suTxPGoSdBYeCYRg"
BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

def send_message(chat_id, text):
    """টেলিগ্রামে মেসেজ পাঠানোর ফাংশন"""
    try:
        url = f"{BASE_URL}/sendMessage"
        # Markdown ব্যবহার করা হয়েছে যেন টেক্সট বোল্ড এবং সুন্দর দেখায়
        payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"❌ মেসেজ পাঠানো যায়নি: {e}")

def get_updates(offset=None):
    """টেলিগ্রাম থেকে নতুন মেসেজ চেক করার ফাংশন"""
    params = {"timeout": 30, "offset": offset}
    try:
        response = requests.get(f"{BASE_URL}/getUpdates", params=params, timeout=35)
        return response.json()
    except Exception as e:
        print(f"📡 সংযোগ সমস্যা (ইন্টারনেট চেক করুন): {e}")
        return None

# -------------------------
# SCRIPT GENERATOR (PRO VER.)
# -------------------------
def generate_script(topic):
    """ইসলামিক স্টোরিটেলিং এবং অডিও বুকের জন্য স্ক্রিপ্ট ফরম্যাট"""
    return f"""
💠 **BARAQURA ISLAMIC PRODUCTION** 💠
━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 **বিষয়:** {topic}
🎭 **ক্যারেক্টার:** হাসান, লিজা এবং শাকিব

--- 🎙️ **AUDIO BOOK / STORY MODULE** ---
🔊 **Narrator:** আসসালামু আলাইকুম। আজ আমাদের আলোচনার বিষয় {topic}...
📝 **Script:** (এখানে এআই বিস্তারিত গল্পটি জেনারেট করবে)

--- 🖼️ **AI IMAGE PROMPTS** ---
🎨 **Prompt:** Cinematic 3D Islamic animation style, {topic} theme, 8k resolution.

--- 📜 **APPROVAL STATUS** ---
✅ এই স্ক্রিপ্টটি কি ফাইনাল? 
👉 এপ্রুভ করতে লিখুন: **APPROVE**
👉 রিজেক্ট করতে লিখুন: **REJECT**
━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# -------------------------
# BOT CORE ENGINE
# -------------------------
def run_engine():
    offset = None
    print("🚀 BaraQura Engine v127.1 ইজ রানিং...")
    print("🔔 টেলিগ্রাম থেকে কমান্ডের জন্য অপেক্ষা করছি (যেমন: /story দানশীলতা)...")

    while True:
        data = get_updates(offset)
        
        # ডাটা না থাকলে বা এরর হলে ২ সেকেন্ড অপেক্ষা করে আবার চেষ্টা করবে
        if not data or "result" not in data:
            time.sleep(2)
            continue

        for update in data.get("result", []):
            offset = update["update_id"] + 1
            message = update.get("message", {})
            text = message.get("text", "")
            chat_id = message.get("chat", {}).get("id")

            if not text:
                continue

            # COMMAND: /STORY
            if text.startswith("/story"):
                topic = text.replace("/story", "").strip()
                if not topic:
                    send_message(chat_id, "⚠️ দয়া করে একটি বিষয় লিখুন।\nউদাহরণ: `/story ধৈর্য`")
                    continue

                send_message(chat_id, "🧠 **AI Autopilot** আপনার স্ক্রিপ্ট তৈরি করছে...")
                script = generate_script(topic)
                send_message(chat_id, script)

            # APPROVAL SYSTEM
            elif text.upper() == "APPROVE":
                send_message(chat_id, "✅ **Approved!** অডিও বুক এবং ভিডিওর কাজ প্রসেসিং হচ্ছে...")
                # এখানে আমরা পরবর্তীতে ভয়েস সিস্টেম অ্যাড করবো
                
            elif text.upper() == "REJECT":
                send_message(chat_id, "❌ **Rejected.** নতুন কোনো বিষয় দিয়ে চেষ্টা করুন।")

        time.sleep(1)

if __name__ == "__main__":
    try:
        run_engine()
    except KeyboardInterrupt:
        print("\n🛑 ইঞ্জিনটি মালিক দ্বারা বন্ধ করা হয়েছে।")
        sys.exit()