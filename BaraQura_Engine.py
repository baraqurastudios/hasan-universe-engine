import streamlit as st
import json
import os
import requests
import base64

# ১. সেশন স্টেট চেক
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# ২. কনফিগ ফাইল লোড
def load_config():
    config_file = "v82_config.json"
    if os.path.exists(config_file):
        try:
            with open(config_file, "r") as f:
                return json.load(f)
        except:
            return None
    return None

# ৩. মূল লজিক শুরু
if st.session_state["authenticated"]:
    # --- ড্যাশবোর্ড ইন্টারফেস ---
    st.title("🛡️ BaraQura Universe Dashboard")
    st.sidebar.title("Engine Controls")
    
    menu = st.sidebar.radio("Navigation", ["Home", "GitHub Code Editor", "Settings"])

    if menu == "Home":
        st.success("Welcome, Master. System is fully ONLINE.")
        st.info("আপনার ইঞ্জিনের মূল মডিউলগুলো এখান থেকে নিয়ন্ত্রণ করুন।")

    elif menu == "GitHub Code Editor":
        st.header("🚀 GitHub Remote Code Access")
        
        # GitHub ক্রেডেনশিয়াল (সুরক্ষার জন্য আপনি এটি ডিরেক্ট ইনপুট দিতে পারেন)
        repo = "baraqurastudios/hasan-universe-engine" # আপনার রিপোজিটরি
        token = st.text_input("Enter GitHub Personal Access Token:", type="password")
        file_path = st.text_input("Enter File Path (e.g., main.py):", value="main.py")

        if st.button("Fetch Code from GitHub"):
            if token:
                url = f"https://api.github.com/repos/{repo}/contents/{file_path}"
                headers = {"Authorization": f"token {token}"}
                response = requests.get(url, headers=headers)
                
                if response.status_code == 200:
                    data = response.json()
                    content = base64.b64decode(data["content"]).decode("utf-8")
                    st.session_state["github_content"] = content
                    st.session_state["file_sha"] = data["sha"]
                    st.success(f"Successfully fetched {file_path}")
                else:
                    st.error("Failed to fetch file. Check your Token or File Path.")
            else:
                st.warning("Please enter your GitHub Token.")

        # কোড এডিটর বক্স
        if "github_content" in st.session_state:
            new_code = st.text_area("Edit your code here:", value=st.session_state["github_content"], height=400)
            
            if st.button("Push Changes to GitHub"):
                url = f"https://api.github.com/repos/{repo}/contents/{file_path}"
                headers = {"Authorization": f"token {token}"}
                
                new_content_b64 = base64.b64encode(new_code.encode("utf-8")).decode("utf-8")
                payload = {
                    "message": f"Update {file_path} via BaraQura Engine",
                    "content": new_content_b64,
                    "sha": st.session_state["file_sha"]
                }
                
                put_response = requests.put(url, json=payload, headers=headers)
                if put_response.status_code == 200:
                    st.success("🔥 Code successfully pushed to GitHub!")
                    del st.session_state["github_content"]
                else:
                    st.error(f"Error pushing code: {put_response.json().get('message')}")

    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()

else:
    # --- পাসওয়ার্ড প্রোটেকশন লেয়ার ---
    st.title("🛡️ BaraQura Universe Engine V8.2")
    config_data = load_config()
    if config_data:
        master_key = config_data["security_layer"]["master_key_hash"]
        user_input = st.text_input("Enter Master Key:", type="password")
        if st.button("Unlock System"):
            if user_input == master_key:
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("⚠️ Invalid Master Key!")
