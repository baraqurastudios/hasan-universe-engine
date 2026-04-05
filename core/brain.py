import google.generativeai as genai
import json
import re

class BaraQuraBrain:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
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
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"

    def parse_ai_response(self, raw_response):
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
