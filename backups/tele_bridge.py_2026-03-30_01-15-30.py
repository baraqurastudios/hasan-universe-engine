import os
import requests

# --- V8.1 TELEGRAM CONFIGURATION ---
BOT_TOKEN = "8712362120:AAEXy7KsOlacCgRf00UUSEYhgwRXee4IbRQ"
# আপনার চ্যাট আইডি বের করার জন্য প্রথমে টেলিগ্রামে আপনার বোটকে একটি মেসেজ দিন
CHAT_ID = "" 

def send_v8_notification(message):
    """সিস্টেমের যে কোনো আপডেট সরাসরি আপনার ফোনে পাঠাবে"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID, 
        "text": f"🚀 V8.1 Alert\n------------------\n{message}"
    }
    try:
        response = requests.post(url, data=payload)
        return response.json()
    except Exception as e:
        print(f"❌ Telegram Error: {e}")
        return None

if __name__ == "__main__":
    # প্রথম কানেকশন টেস্ট
    print("🛰️ V8.1 Engine: Attempting to connect with Master via Telegram...")
    # মনে রাখবেন: চ্যাট আইডি না থাকলে মেসেজ ফোনে যাবে না, শুধু টার্মিনালে দেখাবে।
    test_status = send_v8_notification("মাস্টার, আপনার V8.1 ইঞ্জিন এখন টেলিগ্রামের সাথে যুক্ত।")
    if test_status:
        print("✅ Connection Active!")
      
