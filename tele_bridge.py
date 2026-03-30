import requests

# আপনার কনফিগারেশন
BOT_TOKEN = "8712362120:AAEXy7KsOlacCgRf00UUSEYhgwRXee4IbRQ"
CHAT_ID = "6700361740"

def test_v8_signal():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID, 
        "text": "🛰️ V8.1 LIVE TEST: মাস্টার, আপনার সিস্টেম এখন পুরোপুরি সচল!"
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Message Sent Successfully!")
    else:
        print(f"❌ Failed: {response.text}")

# রান করুন
test_v8_signal()
