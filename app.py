import streamlit as st
import requests
import base64
import datetime
import os

# --- ১. মাস্টার সিকিউরিটি ও কনফিগারেশন ---
# সিকিউরিটি ফিক্স: Streamlit Secrets বা Environment Variable ব্যবহার করুন
GITHUB_TOKEN = st.secrets.get("GITHUB_TOKEN") or os.getenv("GITHUB_TOKEN")
REPO_NAME = "BaraQuraStudios/master-engine"

# --- ২. কোর ইঞ্জিন (GitHub Logic) ---
def github_request(method, path, data=None, token=None):
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/{path}"
    headers = {"Authorization": f"token {token or GITHUB_TOKEN}"}
    if method == "GET":
        res = requests.get(url, headers=headers)
    else:
        res = requests.put(url, headers=headers, json=data)
    return res.json(), res.status_code

# --- ৩. ইউজার ইন্টারফেস সেটআপ ---
st.set_page_config(page_title="BaraQura OS Pro", layout="wide")
st.markdown("<h1 style='text-align: center; color: #00FFAA;'>🚀 BaraQura OS v1.2 Pro</h1>", unsafe_allow_html=True)

# --- ৪. সাইডবার (Security & Config) ---
st.sidebar.title("🔐 Master Access")
if not GITHUB_TOKEN:
    user_token = st.sidebar.text_input("Manual Token (Backup):", type="password")
else:
    user_token = GITHUB_TOKEN
    st.sidebar.success("✅ Secure Token Loaded")

st.sidebar.divider()
target_file = st.sidebar.text_input("📁 Target File Path", value="app.py")

# --- ৫. মেইন ড্যাশবোর্ড (Tabs) ---
tab1, tab2, tab3, tab4 = st.tabs(["🔮 AI Oracle", "⏪ Rollback", "⚡ Console", "📜 Logs"])

# --- ট্যাব ১: AI Oracle ---
with tab1:
    st.subheader("🌀 The Oracle Update Portal")
    mode = st.radio("Update Mode:", ["Smart Inject (Append)", "Full Overwrite"], horizontal=True)
    patch_code = st.text_area("Paste Code or AI Generated Script...", height=300)
    
    if st.button("Execute System Update 🚀"):
        if not user_token:
            st.error("❌ Token missing! Please set GITHUB_TOKEN in Secrets.")
        else:
            with st.spinner("Syncing with GitHub..."):
                data, status = github_request("GET", target_file, token=user_token)
                if status == 200:
                    sha = data['sha']
                    old_content = base64.b64decode(data['content']).decode('utf-8')
                    st.session_state['last_stable_code'] = old_content
                    
                    if mode == "Smart Inject (Append)":
                        final_code = f"{old_content}\n\n# --- Patch: {datetime.datetime.now()} ---\n{patch_code}"
                    else:
                        final_code = patch_code
                    
                    update_data = {
                        "message": f"Update {target_file}",
                        "content": base64.b64encode(final_code.encode()).decode(),
                        "sha": sha
                    }
                    _, up_status = github_request("PUT", target_file, data=update_data, token=user_token)
                    
                    if up_status == 200:
                        st.balloons()
                        st.success(f"Alhamdulillah! {target_file} updated.")
                    else:
                        st.error("Update failed. Check permissions.")
                else:
                    st.error("File not found or connection error.")

# --- ট্যাব ২: Rollback System ---
with tab2:
    st.subheader("⏪ System Rollback (Undo)")
    if 'last_stable_code' in st.session_state:
        if st.button("Restore Last Stable Version 🛡️"):
            data, _ = github_request("GET", target_file, token=user_token)
            update_data = {
                "message": "Rollback to stable",
                "content": base64.b64encode(st.session_state['last_stable_code'].encode()).decode(),
                "sha": data['sha']
            }
            _, res_status = github_request("PUT", target_file, data=update_data, token=user_token)
            if res_status == 200:
                st.success("System Restored!")
                st.rerun()
    else:
        st.info("No backup found in current session.")

# --- ট্যাব ৩: Command Console ---
with tab3:
    st.subheader("⚡ Command Console")
    cmd = st.text_input("Enter Command")
    if st.button("Run"):
        if cmd == "/status":
            st.json({"file": target_file, "token_status": "Loaded"})
        else:
            st.error("Unknown Command")

# --- ট্যাব ৪: Logs (ইন্ডেন্টেশন এরর এখানেই ছিল, ফিক্স করা হয়েছে) ---
with tab4:
    st.subheader("📜 System Logs")
    if "system_logs" not in st.session_state:
        st.session_state.system_logs = []
    
    if st.button("Clear Logs"):
        st.session_state.system_logs = []
    
    for log in st.session_state.system_logs:
        st.code(log)

st.divider()
st.caption("BaraQura OS v1.2 Pro | Secure Framework | Sakibul Hasan")
st.divider()
st.caption("BaraQura Studios | v1.0 Master Engine | Admin: Sakibul Hasan")
