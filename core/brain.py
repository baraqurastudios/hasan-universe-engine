import google.generativeai as genai
import json
import re

class BaraQuraBrain:
    def __init__(self, api_key):
        # এপিআই কী কনফিগারেশন
        genai.configure(api_key=api_key)
        
        # ৪0৪ এরর ফিক্স করার জন্য ডাইনামিক মডেল সিলেকশন
        try:
            # প্রথমে ফ্ল্যাশ মডেল চেষ্টা করা হবে
            self.model = genai.GenerativeModel('gemini-1.5-flash')
            # একটি ছোট টেস্ট রান করে দেখা মডেলটি কাজ করছে কি না
            self.model.generate_content("test", generation_config={"max_output_tokens": 1})
        except Exception:
            try:
                # কাজ না করলে 'models/' প্রিফিক্স সহ চেষ্টা করা হবে
                self.model = genai.GenerativeModel('models/gemini-1.5-flash')
            except Exception:
                # সবশেষে স্টেবল ভার্সন ব্যবহার করা হবে
                self.model = genai.GenerativeModel('gemini-pro')
        
        self.system_instruction = """
        Role: তুমি BaraQura-এর Elite Sales Consultant। 
        Rules: 
        1. সর্বোচ্চ ২-৩ লাইন। 
        2. ১টি প্রশ্ন। 
        3. উত্তরের শুরুতে অবশ্যই নিচের JSON দিবে:
        {"type": "cheap/smart", "mood": "curious/angry", "intent": "pricing/buy", "stage": "cold/hot"}
        """

    def get_smart_answer(self, user_message):
        try:
            full_prompt = f"{self.system_instruction}\n\nUser Says: {user_message}"
            response = self.model.generate_content(full_prompt)
            if response and response.text:
                return response.text
            return "Error: AI response text is empty."
        except Exception as e:
            # এরর মেসেজটি পরিষ্কারভাবে দেখাবে
            return f"Error: {str(e)}"

    def parse_ai_response(self, raw_response):
        # JSON অংশটি খুঁজে বের করা
        json_match = re.search(r'\{.*?\}', raw_response, re.DOTALL)
        if json_match:
            try:
                json_data = json.loads(json_match.group(0))
                clean_text = raw_response.replace(json_match.group(0), "").strip()
                # অপ্রয়োজনীয় কোড ব্লক পরিষ্কার করা
                clean_text = clean_text.replace("```json", "").replace("```", "").strip()
                return json_data, clean_text
            except:
                return None, raw_response
        return None, raw_response
