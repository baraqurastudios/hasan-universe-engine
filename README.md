import requests
import time

# সঠিক টোকেন আপডেট করা হয়েছে
TELEGRAM_TOKEN = "8712362120:AAEopZQcsqZCHbNDck2suTxPGoSdBYeCYRg"
BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

def send_message(chat_id, text):
    requests.post(f"{BASE_URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": text
    })

def get_updates(offset=None):
    params = {"timeout": 30, "offset": offset}
    try:
        return requests.get(f"{BASE_URL}/getUpdates", params=params).json()
    except Exception as e:
        print(f"Error fetching updates: {e}")
        return {}

# -------------------------
# ISLAMIC MULTI-CONTENT ENGINE
# -------------------------
def generate_script(topic):
    # f-string লজিক ফিক্স করা হয়েছে
    return f"""
📖 Islamic Story: Production Unit
💠 **BARAQURA ISLAMIC HUB** 💠
━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 **বিষয়:** {topic}
🛠️ **ফরম্যাট:** Audio Book & Visual Storytelling

--- 🎙️ **AUDIO BOOK MODULE** ---
[শান্ত এবং গম্ভীর ভয়েসওভার শুরু হবে]
🔊 **Narrator:** আসসালামু আলাইকুম। আজ আমরা শুনবো {topic}-এর এক অসামান্য অধ্যায়...
📝 **Script:** (এখানে গল্পের মূল কাহিনী থাকবে যা অডিও বুকের জন্য দীর্ঘ এবং বিস্তারিত হবে।)

--- 🖼️ **AI IMAGE GENERATION PROMPTS** ---
🎨 **Prompt 1:** Cinematic 3D animation style, an ancient desert city at sunset, 8k resolution, glowing golden light.
🎨 **Prompt 2:** A young boy (Hasan) listening to his mother (Liza), emotional lighting, warm cozy room, 3D character design.

--- 📜 **STORYTELLING STATUS** ---
✅ এই স্ক্রিপ্টটি কি Audio Book-এর জন্য ফাইনাল?
✅ ইমেজ প্রম্পটগুলো কি ঠিক আছে?

[REPLY: APPROVE OR REJECT]
"""

# -------------------------
# MAIN BOT LOOP
# -------------------------
def run_bot():
    offset = None
    print("🚀 BaraQura Bot is running...")

    while True:
        data = get_updates(offset)
        
        if not data or "result" not in data:
            time.sleep(1)
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
                    send_message(chat_id, "দয়া করে একটি টপিক দিন। যেমন: /story Patience")
                    continue

                script = generate_script(topic)
                send_message(chat_id, "🧠 Generating multi-content script...")
                send_message(chat_id, script)
                send_message(chat_id, "Reply: APPROVE or REJECT")

            elif text.upper() == "APPROVE":
                send_message(chat_id, "✅ Approved! Next pipeline (Phase 2) coming soon...")

            elif text.upper() == "REJECT":
                send_message(chat_id, "❌ Rejected. Send new topic with /story.")

        time.sleep(1)

# রান করার কমান্ড
if __name__ == "__main__":
    run_bot()
