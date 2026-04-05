import google.generativeai as genai
import json
import re

class BaraQuraBrain:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        # V4 GOD MODE সিস্টেম প্রম্পট
        self.system_instruction = """
        Role: তুমি BaraQura-এর Elite Sales Consultant। 
        
        CRITICAL RULES:
        1. Short Message: সর্বোচ্চ ২-৩ লাইন। 
        2. One Question: প্রতি মেসেজে মাত্র ১টি প্রশ্ন।
        3. Mirroring: ইউজারের টোন এবং ইমোজি ফলো করো।
        4. Internal JSON: উত্তরের শুরুতে অবশ্যই নিচের JSON ফরম্যাটটি দিবে:
        {
         "type": "cheap/smart/impulse",
         "mood": "curious/angry/skeptical/excited",
         "intent": "greeting/pricing/buy/objection/delay",
         "stage": "cold/warm/hot"
        }
        তারপর সাধারণ রিপ্লাই দিবে।
        """

    def get_smart_answer(self, user_message):
        try:
            full_prompt = f"{self.system_instruction}\n\nUser Says: {user_message}"
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"

    def parse_ai_response(self, raw_response):
        # Leak-Proof JSON Extraction
        json_match = re.search(r'\{.*?\}', raw_response, re.DOTALL)
        if json_match:
            try:
                json_data = json.loads(json_match.group(0))
                clean_text = raw_response.replace(json_match.group(0), "").strip()
                clean_text = clean_text.replace("```json", "").replace("```", "").strip()
                return json_data, clean_text
            except:
                return None, raw_response
        return None, raw_response
