import json
from tele_bridge import send_v8_notification

def generate_youtube_meta(topic):
    # গল্পের মূল বিষয়বস্তু অনুযায়ী মেটাডাটা তৈরি
    title = f"{topic} | হাসান সিরিজ - শিক্ষামূলক গল্প"
    description = f"""
    আসসালামু আলাইকুম! আজকের ভিডিওতে আমরা জানব {topic} সম্পর্কে। 
    এটি একটি শিক্ষামূলক গল্প যা ছোট-বড় সবার ভালো লাগবে।
    
    আমাদের চ্যানেলটি সাবস্ক্রাইব করে পাশেই থাকুন।
    #HasanSeries #BaraQuraStudios #EducationalStory #{topic.replace(' ', '')}
    """
    tags = f"{topic}, Hasan Series, Islamic Stories, Kids Education, BaraQura"
    
    full_meta = f"🎬 *YouTube Assets Ready*\n\n📌 *Title:* {title}\n\n📝 *Description:* {description}\n\n🏷️ *Tags:* {tags}"
    
    # টেলিগ্রামে পাঠানো
    send_v8_notification(full_meta)
    return "✅ YouTube Metadata sent to Telegram!"

if __name__ == "__main__":
    target_topic = "Prophet Musa and the Red Sea"
    print(generate_youtube_meta(target_topic))
