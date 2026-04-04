import re

class BaraQuraEngine:
    def __init__(self):
        # বেসিক কিউয়ার্ড লজিক (ভবিষ্যতে এখানে AI মডেল যুক্ত হবে)
        self.greetings = ['hi', 'hello', 'hey', 'সালাম', 'আদাব']
        self.order_keywords = ['দাম', 'প্রাইস', 'price', 'কত', 'order', 'অর্ডার']

    def generate_response(self, user_message, user_name):
        msg = user_message.lower()
        
        # ১. ফোন নম্বর ডিটেকশন (Regex)
        phone_pattern = r'(?:\+88|88)?(01[3-9]\d{8})'
        phone_match = re.search(phone_pattern, msg)
        
        if phone_match:
            phone = phone_match.group(1)
            return f"ধন্যবাদ {user_name}! আমি আপনার ফোন নম্বর ({phone}) পেয়েছি। আমাদের প্রতিনিধি দ্রুত যোগাযোগ করবে।"

        # ২. অর্ডার বা দাম জানতে চাইলে
        if any(word in msg for word in self.order_keywords):
            return f"জি {user_name}, আপনি কি আমাদের প্রোডাক্টের দাম জানতে চাচ্ছেন? অনুগ্রহ করে আপনার ফোন নম্বরটি দিন, আমি বিস্তারিত পাঠিয়ে দিচ্ছি।"

        # ৩. সাধারণ গ্রিটিংস
        if any(word in msg for word in self.greetings):
            return f"হ্যালো {user_name}! আমি BaraQura V8.10। আপনাকে কীভাবে সাহায্য করতে পারি?"

        # ৪. ডিফল্ট উত্তর (Fallback)
        return f"দুঃখিত {user_name}, আমি ঠিক বুঝতে পারিনি। আপনি কি অর্ডার করতে চান?"

# ইঞ্জিনটি ইনিশিয়ালাইজ করা
engine = BaraQuraEngine()
