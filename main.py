from story_gen import generate_story
from metadata_gen import generate_youtube_meta
from tele_bridge import send_v8_notification

def start_v8(topic):
    print(f"🚀 V8.1 Launching for: {topic}")
    generate_story(topic)
    generate_youtube_meta(topic)
    send_v8_notification(f"✅ মাস্টার, '{topic}' এর কাজ শেষ!")

if __name__ == "__main__":
    start_v8("Prophet Musa and the Red Sea")
  
