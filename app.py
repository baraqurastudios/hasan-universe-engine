import streamlit as st
import requests
import base64
import datetime

# --- ১. কনফিগারেশন ---
U, R, F = "baraqurastudios", "hasan-universe-engine", "app.py"

st.set_page_config(page_title="BaraQura Master Engine", layout="wide")

# --- ২. সাইডবার এক্সেস ---
st.sidebar.title("🔐 Master Access")
user_token = st.sidebar.text_input("GitHub Token:", type="password", key="auth_token")

# --- ৩. কোর ফাংশন ---
def call_github(method, endpoint, data=None, token=None):
    url = f"https://api.github.com/repos/{U}/{R}/contents/{endpoint}"
    h = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    try:
        if method == "GET": res = requests.get(url, headers=h)
        else: res = requests.put(url, headers=h, json=data)
        return res.json(), res.status_code
    except: return None, 500

# --- ৪. মেইন ইন্টারফেস ---
st.title("🛰️ BaraQura Unified Master Engine")

if user_token:
    data, status = call_github("GET", F, token=user_token)
    if status == 200:
        st.sidebar.success("✅ Connected to GitHub")
        
        tab1, tab2 = st.tabs(["🌀 Oracle Update", "📝 Script Lab"])
        
        with tab1:
            st.subheader("The Oracle Update Portal")
            patch_code = st.text_area("নতুন কোড এখানে দিন...", height=300, key="patch_input")
            if st.button("Push Update 🚀"):
                if patch_code:
                    sha = data['sha']
                    payload = {
                        "message": f"Manual Fix: {datetime.datetime.now()}",
                        "content": base64.b64encode(patch_code.encode()).decode(),
                        "sha": sha
                    }
                    _, p_status = call_github("PUT", F, data=payload, token=user_token)
                    if p_status == 200:
                        st.success("✅ সিস্টেম আপডেট হয়েছে! অ্যাপটি রিফ্রেশ করুন।")
                        st.balloons()
                    else: st.error(f"Error: {p_status}")
        
        with tab2:
            st.info("হাসান এনিমেশন স্ক্রিপ্ট মডিউল এখানে আসবে।")
    else:
        st.sidebar.error(f"❌ কানেকশন এরর: {status}")
else:
    st.warning("দয়া করে সাইডবারে আপনার GitHub Token প্রদান করুন।")
    if not user_token:
        st.error("❌ আগে সাইডবারে GitHub Token প্রদান করুন।")
    elif not patch_code:
        st.warning("⚠️ কোড প্রদান করুন।")
    else:
        with st.spinner("🔄 সিঙ্ক্রোনাইজ হচ্ছে..."):
            file_data, get_status = call_github("GET", F, current_token=user_token)
            
            if get_status == 200:
                sha = file_data['sha']
                # ৫.১ ক্লিন রিডিং (Syntax Error এড়াতে)
                old_code = base64.b64decode(file_data['content']).decode('utf-8', errors='ignore')
                
                # ৫.২ স্মার্ট অ্যাপেন্ড লজিক
                final_code = old_code.rstrip() + f"\n\n# --- Oracle Patch: {datetime.datetime.now()} ---\n{patch_code}\n"
                
                # ৬. পুশ করা
                update_payload = {
                    "message": f"Fixed Syntax: {datetime.datetime.now().strftime('%H:%M')}",
                    "content": base64.b64encode(final_code.encode()).decode(),
                    "sha": sha
                }
                
                _, put_status = call_github("PUT", F, data=update_payload, current_token=user_token)
                
                if put_status == 200:
                    st.balloons()
                    st.success("✅ অভিনন্দন! আপনার সিস্টেম সফলভাবে আপডেট হয়েছে।")
                else:
                    st.error(f"❌ পুশ এরর (Status: {put_status})।")
            else:
                st.error(f"❌ ফাইল খুঁজে পাওয়া যায়নি।")

# --- Oracle Patch: 2026-03-28 08:33:43.142972 ---
# ==========================================
# 🧬 BaraQura OS: Unified Main Frame v3.8
# 📅 Date: 28 Mar, 2026 | Mode: Clean Recovery
# ==========================================

import streamlit as st
import requests
import base64
import datetime

# --- ১. রিপোজিটরি কনফিগারেশন ---
U = "baraqurastudios"
R = "hasan-universe-engine"
F = "app.py"

# --- ২. সাইডবার: মাস্টার এক্সেস ---
st.sidebar.title("🔐 Master Access")
user_token = st.sidebar.text_input("GitHub Token (BaraQuraSync):", type="password")

# --- ৩. কোর ইঞ্জিন (GitHub API) ---
def call_github(method, endpoint, data=None, current_token=None):
    url = f"https://api.github.com/repos/{U}/{R}/contents/{endpoint}"
    headers = {
        "Authorization": f"token {current_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    try:
        if method == "GET":
            res = requests.get(url, headers=headers)
        else:
            res = requests.put(url, headers=headers, json=data)
        return res.json(), res.status_code
    except Exception as e:
        return {"message": str(e)}, 500

# --- ৪. কানেকশন ও স্ট্যাটাস চেক ---
if user_token:
    data, status = call_github("GET", F, current_token=user_token)
    if status == 200:
        st.sidebar.success(f"✅ Connected to {R}")
    else:
        st.sidebar.error(f"❌ Connection Error: {status}")

# --- ৫. ওরাকল পোর্টাল ইন্টারফেস ---
st.title("🌀 The Oracle Update Portal")
st.info("Status: **Clean Recovery Mode Active**")

patch_code = st.text_area("নতুন কোড এখানে দিন...", height=250)

if st.button("Execute System Update 🚀"):
    if not user_token:
        st.error("❌ আগে সাইডবারে GitHub Token প্রদান করুন।")
    elif not patch_code:
        st.warning("⚠️ কোড প্রদান করুন।")
    else:
        with st.spinner("🔄 সিঙ্ক্রোনাইজ হচ্ছে..."):
            file_data, get_status = call_github("GET", F, current_token=user_token)
            
            if get_status == 200:
                sha = file_data['sha']
                # ৫.১ ক্লিন রিডিং (Syntax Error এড়াতে)
                old_code = base64.b64decode(file_data['content']).decode('utf-8', errors='ignore')
                
                # ৫.২ স্মার্ট অ্যাপেন্ড লজিক
                final_code = old_code.rstrip() + f"\n\n# --- Oracle Patch: {datetime.datetime.now()} ---\n{patch_code}\n"
                
                # ৬. পুশ করা
                update_payload = {
                    "message": f"Fixed Syntax: {datetime.datetime.now().strftime('%H:%M')}",
                    "content": base64.b64encode(final_code.encode()).decode(),
                    "sha": sha
                }
                
                _, put_status = call_github("PUT", F, data=update_payload, current_token=user_token)
                
                if put_status == 200:
                    st.balloons()
                    st.success("✅ অভিনন্দন! আপনার সিস্টেম সফলভাবে আপডেট হয়েছে।")
                else:
                    st.error(f"❌ পুশ এরর (Status: {put_status})।")
            else:
                st.error(f"❌ ফাইল খুঁজে পাওয়া যায়নি।")


Correction kore dau
