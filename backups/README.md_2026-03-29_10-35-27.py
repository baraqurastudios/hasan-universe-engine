import requests
import json

class ReasoningEngine:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://api.openai.com/v1/chat/completions"

    def _build_system_prompt(self):
        return (
            "You are a Senior System Reliability Engineer (SRE). "
            "Your task is to analyze system logs and provide a root cause analysis "
            "and actionable fix recommendations in professional Bengali."
        )

    def analyze(self, log_report):
        """v1.4 এর রিপোর্ট থেকে রিজন বের করবে।"""
        prompt = f"Please analyze the following system report and explain why these issues occur and how to fix them:\n\n{log_report}"
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Temperature ০.৩ রাখা হয়েছে যাতে লজিক্যাল এবং ফিক্সড অ্যানসার পাওয়া যায়
        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": self._build_system_prompt()},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3
        }

        try:
            r = requests.post(self.endpoint, headers=headers, json=payload, timeout=20)
            r.raise_for_status()
            ai_response = r.json()["choices"][0]["message"]["content"]
            return ai_response
        except Exception as e:
            return f"Reasoning Engine Error: {str(e)[:100]}"

# v1.4 + v1.5 integration logic
def final_workflow(report_data, key):
    engine = ReasoningEngine(key)
    analysis = engine.analyze(report_data)
    
    final_output = f"--- 🧠 AI REASONING REPORT ---\n\n{analysis}"
    return final_output