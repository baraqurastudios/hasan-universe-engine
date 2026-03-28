import requests
import time

# =========================
# CONFIG
# =========================
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

OPENAI_API_KEY = "YOUR_API_KEY"

# =========================
# TELEGRAM SEND
# =========================
def send(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg})

# =========================
# GET LAST MESSAGE
# =========================
def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    return requests.get(url, params=params).json()

# =========================
# AI SCRIPT GENERATOR
# =========================
def generate_script(topic):
    prompt = f"""
    Write a powerful emotional Islamic story about: {topic}
    Style: short video (1 minute)
    Tone: emotional, inspiring
    """

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    res = requests.post("https://api.openai.com/v1/chat/completions",
                        headers=headers, json=data)

    return res.json()["choices"][0]["message"]["content"]

# =========================
# MAIN LOOP
# =========================
def run():
    last_update_id = None

    send("🚀 BaraQura AI System Started")

    while True:
        updates = get_updates(last_update_id)

        for u in updates.get("result", []):
            last_update_id = u["update_id"] + 1

            if "message" in u:
                text = u["message"]["text"]

                # USER COMMAND
                if text.startswith("/story"):
                    topic = text.replace("/story ", "")
                    
                    send("🧠 Generating script...")
                    script = generate_script(topic)

                    send(f"📜 Script:\n\n{script}")
                    send("✅ Reply 'approve' to continue or 'reject'")

                elif text.lower() == "approve":
                    send("🔥 Approved! Next step coming soon...")

                elif text.lower() == "reject":
                    send("❌ Rejected. Send new topic.")

        time.sleep(2)

# =========================
# START
# =========================
run()