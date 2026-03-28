import streamlit as st
import requests
import base64
import datetime

# --- ১. মাস্টার সিকিউরিটি (bq2026) ---
def check_password():
    if "authenticated" not in st.session_state:
        st.markdown("<h1 style='text-align: center; color: #00FFAA;'>💎 BaraQura Evolution Gate</h1>", unsafe_allow_html=True)
        pwd = st.text_input("Master Access Key:", type="password")
        if st.button("Activate v129.0 Sync Engine 🚀"):
            if pwd == "bq2026": 
                st.session_state["authenticated"] = True
                st.rerun()
        return False
    return True

if check_password():
    st.set_page_config(page_title="BaraQura v129.0", layout="wide")

    # --- ২. গিটহাব সিঙ্ক ফাংশন (The Secret Engine) ---
    def update_github_file(content, github_token, repo_name, file_path):
        url = f"https://api.github.com/repos/{repo_name}/contents/{file_path}"
        headers = {"Authorization": f"token {github_token}", "Accept": "application/vnd.github.v3+json"}
        
        # বর্তমান ফাইলের তথ্য আনা
        get_file = requests.get(url, headers=headers)
        if get_file.status_code == 200:
            sha = get_file.json()['sha']
            content_base64 = base64.b64encode(content.encode()).decode()
            
            data = {
                "message": "System Auto-Update from BaraQura Dashboard",
                "content": content_base64,
                "sha": sha
            }
            # ফাইল আপডেট করা
            put_file = requests.put(url, headers=headers, json=data)
            return put_file.status_code
        return 404

    # --- ৩. মেইন ইন্টারফেস ---
    st.title("🛰️ BaraQura Unified Master Engine v129.0")
    
    tab1, tab2, tab3 = st.tabs(["⚡ Direct Code Hit", "📱 Telegram", "📊 Analytics"])

    with tab1:
        st.subheader("🛠️ Live GitHub Code Editor")
        st.write("এখানকার পরিবর্তন সরাসরি আপনার গিটহাবের `app.py` ফাইলে হিট করবে।")
        
        # গিটহাব সেটিংস (আপনার রিপোজিটরি অনুযায়ী)
        token = st.text_input("GitHub Token (Secret):", type="password", help="আপনার GitHub Personal Access Token দিন")
        repo = "baraqurastudios/hasan-universe-engine" # আপনার রিপো নাম
        path = "app.py"
        
        new_code = st.text_area("নতুন কোডটি এখানে লিখুন:", value=open("app.py").read() if "app.py" else "", height=300)
        
        if st.button("🔥 Hit GitHub & Update App"):
            if token:
                with st.spinner("গিটহাবে কোড পাঠানো হচ্ছে..."):
                    status = update_github_file(new_code, token, repo, path)
                    if status == 200 or status == 201:
                        st.balloons()
                        st.success("অভিনন্দন! আপনার app.py সরাসরি আপডেট হয়েছে। ২ মিনিট পর সাইট রিফ্রেশ দিন।")
                    else:
                        st.error(f"আপডেট ব্যর্থ হয়েছে। এরর কোড: {status}")
            else:
                st.warning("দয়া করে গিটহাব টোকেন দিন।")

    # বাকি ট্যাবগুলো আগের মতোই থাকবে...
    with tab2:
        st.subheader("🤖 Telegram Bot")
        st.button("Send Status Update")

    with tab3:
        st.subheader("Analytics")
        st.metric("Total Views", "125.4K")

    st.divider()
    st.caption("BaraQura Studios | v129.0 GitHub Sync | Admin: Sakibul Hasan")
