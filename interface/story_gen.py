import json
import os
from tele_bridge import send_v8_notification

def load_character_data():
    """চরিত্রের ডাটা লোড করা"""
    try:
        with open("character_bible.json", "r") as f:
            return json.load(f)
    except:
        return None

def generate_story(topic):
    """গল্প তৈরি এবং টেলিগ্রামে পাঠানো"""
    data = load_character_data()
    if not data:
        return "❌ Error: Character Bible not found!"

    hero = data["characters"]["Hasan"]["name"] if "Hasan" in data["characters"] else "Hasan"
    goal = data["characters"]["Hasan"]["goal"]
    
    # গল্পের খসড়া (Draft)
    story_script = f"""
    🎬 V8.1 Script Draft
    --------------------
    Topic: {topic}
    Main Character: {hero}
    Goal: {goal}
    
    Script: একদিন {hero} বের হলো {topic} নিয়ে নতুন কিছু শিখতে। 
    তার মা লিজা তাকে বুদ্ধি দিয়ে সাহায্য করলেন। 
    শেষ পর্যন্ত {hero} তার লক্ষ্যে সফল হলো।
    """
    
    # টেলিগ্রামে পাঠানো
    send_v8_notification(story_script)
    return "✅ Story Sent to Master's Telegram!"

if __name__ == "__main__":
    # আপনি টেলিগ্রাম থেকে যে টপিকটি পাঠাতে চান তা এখানে দিন
    topic_request = "Prophet Musa and the Red Sea" 
    print(f"✍️ Generating story for: {topic_request}")
    status = generate_story(topic_request)
    print(status)
  
