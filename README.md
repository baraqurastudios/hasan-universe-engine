import requests
import time

# আপনার লেটেস্ট টোকেন এখানে বসান
TOKEN = "8712362120:AAEopZQcsqZCHbNDck2suTxPGoSdBYeCYRg"

def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    try:
        r = requests.get(url, params={"offset": offset, "timeout": 20})
        return r.json()
    except:
        return None

def send_msg(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

def run():
    offset = None
    print("🚀 BaraQura Bot is Starting...")
    while True:
        data = get_updates(offset)
        if data and data.get("result"):
            for update in data["result"]:
                offset = update["update_id"] + 1
                msg = update.get("message", {})
                chat_id = msg.get("chat", {}).get("id")
                text = msg.get("text", "")

                if text.startswith("/story"):
                    topic = text.replace("/story", "").strip()
                    send_msg(chat_id, f"✅ Topic Received: {topic}\n🧠 AI is creating your script...")
                elif text.upper() == "APPROVE":
                    send_msg(chat_id, "💎 Phase 2 Activated!")

        time.sleep(1)

if __name__ == "__main__":
    run()
Z