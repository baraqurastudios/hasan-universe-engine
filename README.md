import requests
import time
import sys

# ==============================
# CONFIGURATION
# ==============================
# আপনার সর্বশেষ টোকেনটি এখানে বসান
TELEGRAM_TOKEN = "8712362120:AAEopZQcsqZCHbNDck2suTxPGoSdBYeCYRg"
BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

def send_message(chat_id, text):
    try:
        url = f"{BASE_URL}/sendMessage"
        payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
        requests.post(url, json=payload)
    except Exception as e:
        print(f"❌ Error sending message: {e}")

def get_updates(offset=None):
    params = {"timeout": 30, "offset": offset}
    try:
        response = requests.get(f"{BASE_URL}/getUpdates", params=params)
        return response.json()
    except Exception as e:
        print(f"📡 Connection error: {e}")
        return {}

# -------------------------
# MULTI-CONTENT SCRIPT GENERATOR
# -------------------------
def generate_script(topic):
    return f"""
💠 **BARAQURA ISLAMIC HUB - PRODUCTION** 💠
━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 **বিষয়:** {topic}
🎭 **ক্যারেক্টার:** হাসান, লিজা এবং শাকিব

--- 🎙️ **AUDIO BOOK / STORY MODULE** ---
🔊 **Narrator:** আসসালামু আলাইকুম। আজ আমাদের আলোচনার বিষয় {topic}...
📝 **Script:** (ভবিষ্যতে এখানে এআই সম্পূর্ণ গল্পটি লিখবে)

--- 🖼️ **AI IMAGE PROMPTS** ---
🎨 **Prompt:** Cinematic 3D style, {topic} theme, emotional lighting, 8k.

--- 📜 **STATUS** ---
✅ এই স্ক্রিপ্টটি কি ফাইনাল? 
[Reply: APPROVE or REJECT]
━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# -------------------------
# MAIN BOT ENGINE
# -------------------------
def run_engine():
    offset = None
    print("🚀 BaraQura Engine v127.0 is LIVE...")
    print("🔔 Waiting for commands in Telegram...")

    while True:
        data = get_updates(offset)
        
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
                    send_message(chat_id, "⚠️ দয়া করে একটি বিষয় লিখুন। যেমন: `/story দানশীলতা`")
                    continue

                send_message(chat_id, "🧠 **AI Autopilot** ইজ জেনারেটিং স্ক্রিপ্ট...")
                script = generate_script(topic)
                send_message(chat_id, script)

            # APPROVAL SYSTEM
            elif text.upper() == "APPROVE":
                send_message(chat_id, "✅ **Approved!** অডিও বুক এবং ভিডিও পাইপলাইন শুরু হচ্ছে...")
                # এখানে আমরা Phase 2-এর ভয়েস কোড যুক্ত করব
                
            elif text.upper() == "REJECT":
                send_message(chat_id, "❌ **Rejected.** নতুন টপিক দিন অথবা পুনরায় চেষ্টা করুন।")

        time.sleep(1)

if __name__ == "__main__":
    try:
        run_engine()
    except KeyboardInterrupt:
        print("\n🛑 Engine stopped by Owner.")
        sys.exit()