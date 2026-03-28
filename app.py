import streamlit as st
import requests
import base64
import datetime

# --- ১. মাস্টার কনফিগারেশন (GitHub Details) ---
# আপনার সঠিক ইউজারনেম এবং রিপোজিটরি নাম এখানে দিন
REPO_NAME = "BaraQuraStudios/master-engine" 
FILE_PATH = "app.py" 

# --- ২. কোর ফাংশনসমূহ (GitHub API Logic) ---
def get_github_data(token):
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json(), True
    else:
        return response.json().get('message', 'Unknown Error'), False

def update_github_file(token, new_content, sha, message):
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {token}"}
    encoded = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')
    data = {"message": message, "content": encoded, "sha": sha}
    res = requests.put(url, headers=headers, json=data)
    return res.status_code == 200

# --- ৩. সিস্টেম স্টেট ও কনফিগারেশন ---
st.set_page_config(page_title="BaraQura OS", layout="wide")

if "system_logs" not in st.session_state:
    st.session_state.system_logs = []

if "modules" not in st.session_state:
    st.session_state.modules = {
        "core": True,
        "animation_engine": False,
        "auto_update": True, # এখন এটি সক্রিয়
        "ai_brain": False
    }

# --- ৪. ইউজার ইন্টারফেস (Header & Sidebar) ---
st.markdown("<h1 style='text-align: center; color: #00FFAA;'>🚀 BaraQura Studios Master Engine</h1>", unsafe_allow_html=True)

st.sidebar.title("🔐 Master Access")
user_token = st.sidebar.text_input("GitHub Token:", type="password", placeholder="Enter PAT...")
if user_token:
    st.sidebar.success("✅ Token Connected")
else:
    st.sidebar.warning("⚠️ Token Required")

st.sidebar.divider()
st.sidebar.title("🧬 System Core")
st.sidebar.success("Version: v1.0 (Foundation)")
st.sidebar.info(f"📅 {datetime.datetime.now().strftime('%d %b %Y')}")

# --- ৫. মেইন কন্ট্রোল সেন্টার (Tabs) ---
tab1, tab2, tab3 = st.tabs(["🔮 Oracle Portal", "⚡ Command Console", "📜 System Logs"])

with tab1:
    st.subheader("🌀 The Oracle Update Portal")
    mode = st.radio("Update Mode:", ["Smart Inject (Append)", "Full Overwrite"])
    patch_code = st.text_area("Paste code from Gemini...", height=250)
    
    if st.button("Execute System Update 🚀"):
        if not user_token:
            st.error("❌ সাইডবারে টোকেন দিন!")
        elif not patch_code:
            st.warning("⚠️ কোড পেস্ট করুন।")
        else:
            with st.spinner("GitHub-এর সাথে সিঙ্ক হচ্ছে..."):
                data, success = get_github_data(user_token)
                if success:
                    sha = data.get('sha')
                    old_content = base64.b64decode(data['content']).decode('utf-8')
                    st.session_state['last_backup'] = old_content
                    
                    if mode == "Smart Inject (Append)":
                        final_code = f"{old_content}\n\n# --- Patch: {datetime.datetime.now()} ---\n{patch_code}"
                    else:
                        final_code = patch_code
                    
                    if update_github_file(user_token, final_code, sha, "OS v1 Update"):
                        st.balloons()
                        st.success("Alhamdulillah! System Updated Successfully.")
                    else:
                        st.error("❌ Update failed. Check token permissions.")
                else:
                    st.error(f"❌ Connection Error: {data}")

with tab2:
    st.subheader("⚡ Command Console")
    command = st.text_input("Enter Command (e.g. /status, /modules)")
    
    if st.button("Run Command"):
        if command == "/status":
            res = {"system": "active", "version": "v1.0", "sync": "online"}
        elif command == "/modules":
            res = st.session_state.modules
        else:
            res = {"error": "unknown command"}
        st.json(res)
        st.session_state.system_logs.append(f"{datetime.datetime.now().strftime('%H:%M:%S')} - {command}: {res}")

with tab3:
    st.subheader("📜 Recent Activity")
    for log in st.session_state.system_logs[-10:]:
        st.code(log)

st.divider()
st.caption("BaraQura Studios | v1.0 Master Engine | Admin: Sakibul Hasan")
