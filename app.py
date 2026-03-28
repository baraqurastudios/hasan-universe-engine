# ==========================================
# 🧬 BaraQura OS: AI-Powered Dev Engine v7.0
# 📅 Date: 28 Mar, 2026 | Mode: Advanced Dev OS
# ==========================================

import streamlit as st
import requests
import base64
import datetime
import difflib

# --- ১. গ্লোবাল কনফিগারেশন ---
U, R = "baraqurastudios", "hasan-universe-engine"
# ডিফল্ট ফাইল সেট করা হলো
if 'selected_file' not in st.session_state:
    st.session_state['selected_file'] = "app.py"

st.set_page_config(page_title="BaraQura AI Dev OS", layout="wide", page_icon="🧠")

# --- ২. সাইডবার: মাস্টার কন্ট্রোল ---
st.sidebar.title("🔐 Master Control")
user_token = st.sidebar.text_input("GitHub Access Token:", type="password", key="v7_token")

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
st.title("🛰️ BaraQura AI-Powered Dev OS")

if user_token:
    # ৪.১ ফাইল এক্সপ্লোরার (Multi-file Support)
    st.sidebar.subheader("📁 Repository Explorer")
    repo_files, repo_status = call_github("GET", "", token=user_token)
    
    if repo_status == 200 and isinstance(repo_files, list):
        file_list = [f['name'] for f in repo_files if f['type'] == 'file']
        st.session_state['selected_file'] = st.sidebar.selectbox("Select File to Edit", file_list)
        st.sidebar.success(f"📂 Active: {st.session_state['selected_file']}")
    
    # বর্তমান ফাইলের ডাটা রিট্রিভ
    current_f = st.session_state['selected_file']
    file_data, f_status = call_github("GET", current_f, token=user_token)

    if f_status == 200:
        old_code = base64.b64decode(file_data['content']).decode('utf-8', errors='ignore')
        
        # ট্যাব সিস্টেম
        tab1, tab2, tab3 = st.tabs(["🤖 AI & Oracle Editor", "🔍 Diff Viewer", "⏪ Rollback"])

        # --- ট্যাব ১: AI Generator & Editor ---
        with tab1:
            st.subheader("🤖 AI Code Generator")
            ai_prompt = st.text_input("আপনি কি তৈরি করতে চান? (Describe here)", placeholder="Example: Create a login function...")
            
            if st.button("Generate Code ✨", key="ai_gen"):
                # Placeholder AI Logic (ভবিষ্যতে Gemini/OpenAI API এখানে বসবে)
                generated = f"# AI Generated for: {ai_prompt}\n\ndef new_feature():\n    print('BaraQura System: {ai_prompt} Active')\n"
                st.session_state['ai_code'] = generated
            
            if 'ai_code' in st.session_state:
                st.code(st.session_state['ai_code'], language="python")
                if st.button("Use Generated Code ⬇️"):
                    st.session_state['patch_code'] = st.session_state['ai_code']

            st.divider()
            st.subheader("🌀 The Oracle Editor")
            # এডিটর বক্স
            final_patch = st.text_area("Final Code to Push", 
                                      value=st.session_state.get('patch_code', ""), 
                                      height=300, key="main_editor")

            if st.button("Execute Safe Update 🚀"):
                if final_patch:
                    try:
                        # সিনট্যাক্স শিল্ড
                        compile(final_patch, "<string>", "exec")
                        
                        # ১. অটো ব্যাকআপ
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                        b_path = f"backups/{current_f}_{timestamp}.py"
                        b_payload = {"message": f"Backup: {timestamp}", "content": base64.b64encode(old_code.encode()).decode()}
                        call_github("PUT", b_path, data=b_payload, token=user_token)

                        # ২. মেইন আপডেট
                        u_payload = {
                            "message": f"DevOS Update: {current_f}",
                            "content": base64.b64encode(final_patch.encode()).decode(),
                            "sha": file_data['sha']
                        }
                        _, put_s = call_github("PUT", current_f, data=u_payload, token=user_token)
                        
                        if put_s == 200:
                            st.balloons(); st.success("✅ Update & Backup Success!")
                        else: st.error(f"Error: {put_s}")
                    except Exception as e: st.error(f"❌ Syntax Error: {e}")

        # --- ট্যাব ২: Diff Viewer ---
        with tab2:
            st.subheader("🔍 Changes Comparison (Before vs After)")
            col_a, col_b = st.columns(2)
            with col_a: st.text_area("📜 Current Code", old_code, height=300, disabled=True)
            with col_b: st.text_area("✏️ New Changes", final_patch, height=300, disabled=True)
            
            if st.button("Compare Lines 🔍"):
                diff = difflib.unified_diff(old_code.splitlines(), final_patch.splitlines(), lineterm='')
                st.code("\n".join(diff), language="diff")

        # --- ট্যাব ৩: রোলব্যাক ---
        with tab3:
            st.subheader("⏪ Rollback System")
            backups, b_s = call_github("GET", "backups", token=user_token)
            if b_s == 200 and isinstance(backups, list):
                b_files = [i['name'] for i in backups if current_f in i['name']]
                sel_b = st.selectbox("Select Backup", b_files[::-1])
                if st.button("Restore Now"):
                    # রিস্টোর লজিক (v6.5 এর মতো)
                    b_data, _ = call_github("GET", f"backups/{sel_b}", token=user_token)
                    res_payload = {
                        "message": f"Restore: {sel_b}",
                        "content": b_data['content'],
                        "sha": file_data['sha']
                    }
                    call_github("PUT", current_f, data=res_payload, token=user_token)
                    st.success("✅ Restored!")
    else:
        st.error("File loading failed. Check Token or Repo.")
else:
    st.warning("🔐 Please enter GitHub token in the sidebar.")
