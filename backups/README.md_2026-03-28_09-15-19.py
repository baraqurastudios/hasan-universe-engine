# ==========================================
# 🧬 BaraQura OS: Ultimate AI-Dev Edition v8.0
# 📅 Date: 28 Mar, 2026 | Mode: Full Production
# ==========================================

import streamlit as st
import requests
import base64
import datetime
import difflib
import os
try:
    import openai
except ImportError:
    st.error("Please add 'openai' to your requirements.txt")

# --- ১. গ্লোবাল কনফিগারেশন ---
U, R = "baraqurastudios", "hasan-universe-engine"
st.set_page_config(page_title="BaraQura AI Dev OS", layout="wide", page_icon="🚀")

# --- ২. রোল-বেসড এক্সেস কন্ট্রোল (RBAC) ---
st.sidebar.title("🔐 Master Control")
user_token = st.sidebar.text_input("Access Token:", type="password", key="v8_token")

# টোকেন ভ্যালিডেশন (Environment Variables থেকে অথবা ডিফল্ট)
ADMIN_KEY = os.getenv("ADMIN_TOKEN", "bq_admin_2026")
EDITOR_KEY = os.getenv("EDITOR_TOKEN", "bq_editor_2026")

user_role = "viewer"
if user_token == ADMIN_KEY:
    user_role = "admin"
elif user_token == EDITOR_KEY:
    user_role = "editor"

st.sidebar.info(f"👤 Role: **{user_role.upper()}**")

# --- ৩. কোর ইঞ্জিন (GitHub API Handler) ---
def call_github(method, endpoint, data=None, token=None):
    url = f"https://api.github.com/repos/{U}/{R}/contents/{endpoint}"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    try:
        if method == "GET":
            res = requests.get(url, headers=headers, timeout=15)
        else:
            res = requests.put(url, headers=headers, json=data, timeout=15)
        return res.json(), res.status_code
    except Exception as e:
        return {"message": str(e)}, 500

# --- ৪. মেইন ফ্রেম ---
st.title("🛰️ BaraQura AI-Dev Operating System")

if not user_token:
    st.warning("🔒 Please enter your Access Token to initialize the system.")
    st.stop()

if user_role == "viewer":
    st.warning("⚠️ You have Read-Only access. Contact Admin for Edit rights.")

# --- ৫. ফোল্ডার ও ফাইল নেভিগেশন ---
st.subheader("📂 Folder & File Explorer")
if 'current_path' not in st.session_state:
    st.session_state['current_path'] = ""

col_path, col_reset = st.columns([4, 1])
with col_path:
    path_input = st.text_input("Current Path", value=st.session_state['current_path'], key="path_box")
with col_reset:
    if st.button("Root 🏠"): 
        st.session_state['current_path'] = ""
        st.rerun()

files_data = call_github("GET", path_input, token=user_token)[0]
if isinstance(files_data, list):
    folders = [f['name'] for f in files_data if f['type'] == 'dir']
    files = [f['name'] for f in files_data if f['type'] == 'file']
    
    c1, c2 = st.columns(2)
    with c1:
        sel_folder = st.selectbox("📂 Folders", ["-- Select to Open --"] + folders)
        if sel_folder != "-- Select to Open --":
            st.session_state['current_path'] = f"{path_input}/{sel_folder}".strip("/")
            st.rerun()
    with c2:
        sel_file = st.selectbox("📄 Files", ["-- Select to Edit --"] + files)
        active_file = f"{path_input}/{sel_file}".strip("/") if sel_file != "-- Select to Edit --" else None

if active_file:
    st.success(f"📍 Active File: **{active_file}**")
    file_info, f_status = call_github("GET", active_file, token=user_token)
    
    if f_status == 200:
        old_code = base64.b64decode(file_info['content']).decode('utf-8', errors='ignore')
        
        tab_ai, tab_diff, tab_back = st.tabs(["🤖 AI & Oracle", "🔍 Diff Viewer", "⏪ Backups"])

        # --- ট্যাব ১: Real OpenAI & Editor ---
        with tab_ai:
            st.subheader("🤖 AI Code Generator (OpenAI)")
            openai.api_key = os.getenv("OPENAI_API_KEY") # Ensure this is set in Streamlit Secrets
            
            ai_prompt = st.text_input("Describe the feature or fix you need:")
            if st.button("Generate with AI 🚀") and ai_prompt:
                if not openai.api_key:
                    st.error("API Key missing! Set OPENAI_API_KEY in environment.")
                else:
                    with st.spinner("AI is thinking..."):
                        try:
                            response = openai.ChatCompletion.create(
                                model="gpt-4o-mini",
                                messages=[{"role": "user", "content": ai_prompt}]
                            )
                            st.session_state['ai_out'] = response['choices'][0]['message']['content']
                        except Exception as e: st.error(f"AI Error: {e}")
            
            if 'ai_out' in st.session_state:
                st.code(st.session_state['ai_out'], language="python")
                if st.button("Inject to Editor ⬇️"):
                    st.session_state['editor_input'] = st.session_state['ai_out']

            st.divider()
            new_code = st.text_area("Master Editor", value=st.session_state.get('editor_input', old_code), height=400)

            if user_role in ["admin", "editor"]:
                if st.button("Push System Update 🚀"):
                    # ১. ব্যাকআপ লজিক
                    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    b_path = f"backups/{sel_file}_{ts}.py"
                    call_github("PUT", b_path, data={"message":"Auto Backup","content":base64.b64encode(old_code.encode()).decode()}, token=user_token)
                    
                    # ২. আপডেট লজিক
                    u_payload = {"message": f"Update {sel_file}", "content": base64.b64encode(new_code.encode()).decode(), "sha": file_info['sha']}
                    res, s_code = call_github("PUT", active_file, data=u_payload, token=user_token)
                    if s_code == 200: st.balloons(); st.success("Update Successful!")
            else:
                st.warning("Permission Denied: Viewer role cannot push changes.")

        # --- ট্যাব ২: Diff Viewer ---
        with tab_diff:
            diff = difflib.unified_diff(old_code.splitlines(), new_code.splitlines(), lineterm='')
            st.code("\n".join(diff), language="diff")

        # --- ট্যাব ৩: রোলব্যাক ---
        with tab_back:
            if st.button("🚀 Deploy (Re-run)"): st.rerun()

    else: st.error("Could not load file content.")
