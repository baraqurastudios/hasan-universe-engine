import requests
import base64

# --- ১. আপনার GitHub কনফিগারেশন ---
# (এখানে আপনার টোকেন এবং রিপোজিটরির নাম দিন)
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN_HERE"  # আপনার GitHub সেটিংস থেকে জেনারেট করা টোকেন
REPO_NAME = "BaraQuraStudios/master-engine" # আপনার রিপোজিটরির নাম
FILE_PATH = "app.py" # যে ফাইলটি আপডেট করতে চান

def push_to_github(new_content, commit_message="Oracle System Update"):
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    # বর্তমান ফাইলের 'sha' সংগ্রহ করা (GitHub এ আপডেট দিতে এটি লাগে)
    current_file = requests.get(url, headers=headers).json()
    sha = current_file.get('sha')
    
    # নতুন কন্টেন্ট এনকোড করা
    encoded_content = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')
    
    data = {
        "message": commit_message,
        "content": encoded_content,
        "sha": sha
    }
    
    # GitHub-এ আপডেট পুশ করা
    response = requests.put(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return "✅ GitHub File Updated Successfully!"
    else:
        return f"❌ Error: {response.json()}"

# ব্যবহারকারীর নির্দেশ অনুযায়ী অটো-আপডেট ট্রিগার
# system_command = "Update Dashboard Name to 'BaraQura Master Engine'"
# push_to_github(new_code_from_gemini)
