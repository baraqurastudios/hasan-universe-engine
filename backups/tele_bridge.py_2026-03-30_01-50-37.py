import requests

# --- V8.1 TELEGRAM CONFIGURATION ---
BOT_TOKEN = "8712362120:AAEXy7KsOlacCgRf00UUSEYhgwRXee4IbRQ"
CHAT_ID = "6700361740" 

def send_v8_notification(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"🛰️ V8.1 Alert\n------------------\n{message}"}
    try:
        response = requests.post(url, data=payload)
        return response.json()
    except Exception as e:
        print(f"❌ Telegram Error: {e}")
        return None

if __name__ == "__main__":
    send_v8_notification("মাস্টার, আপনার সিস্টেম এখন পুরোপুরি অনলাইন!")
