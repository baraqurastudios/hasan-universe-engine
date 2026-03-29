import requests

def explain_error(status, api_key):
    # Precise prompt for high quality output
    prompt = f"""
    System Status Data: {status}
    Task: Explain the issues in simple, professional Bengali. 
    Provide a step-by-step fix recommendation for the developer.
    """

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a senior system architect explaining bugs to a developer in Bengali."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3 # Consistency বজায় রাখার জন্য
    }

    try:
        r = requests.post(url, headers=headers, json=data, timeout=15)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"AI Explanation layer failed: {str(e)[:100]}"