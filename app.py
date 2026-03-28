# ==========================================
# 🧬 BaraQura OS: Unified Master Engine v4.8
# 📅 Date: 28 Mar, 2026 | Mode: Final Stable
# ==========================================

import streamlit as st
import requests
import base64
import datetime

# --- ১. রিপোজিটরি কনফিগারেশন ---
U, R, F = "baraqurastudios", "hasan-universe-engine", "app.py"

# --- ২. সাইডবার: মাস্টার এক্সেস ---
st.sidebar.title("🔐 Master Access")
# key="master_token_input" ডুপ্লিকেট এলিমেন্ট আইডি এরর রোধ করে
user_token = st.sidebar.text_input("GitHub Token:", type="password", key="master_token_input")

# --- ৩. কোর ইঞ্জিন (GitHub API) ---
def call_github(method, endpoint, data=None, token=None):
    url = f"https://api.github.com/repos/{U}/{R}/contents/{endpoint}"
    headers = {
        "Authorization": f"token {token}",
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
    data, status = call_github("GET", F, token=user_token)
    if status == 200:
        st.sidebar.success(f"✅ Connected to {R}")
    else:
        st.sidebar.error(f"❌ Connection Error: {status}")

# --- ৫. ওরাকল পোর্টাল ইন্টারফেস ---
st.title("🌀 The Oracle Update Portal")
st.info("Mode: **Full Overwrite Sync**")

# ইউনিক key ব্যবহার করে DuplicateElementId এরর সমাধান
patch_code = st.text_area("নতুন কোড এখানে দিন...", height=350, key="oracle_code_area")

if st.button("Execute System Update 🚀", key="oracle_update_btn"):
    if not user_token:
        st.error("❌ আগে সাইডবারে GitHub Token প্রদান করুন।")
    elif not patch_code:
        st.warning("⚠️ ইনজেক্ট করার জন্য কোনো কোড পাওয়া যায়নি।")
    else:
        with st.spinner("🔄 সিঙ্ক্রোনাইজ হচ্ছে..."):
            # ফাইল ডাটা রিট্রিভ
            file_data, get_status = call_github("GET", F, token=user_token)
            
            if get_status == 200:
                sha = file_data['sha']
                
                # ৫.১ সিনট্যাক্স ভ্যালিডেশন (ভুল কোড ইনজেকশন রোধ করবে)
                try:
                    compile(patch_code, "<string>", "exec")
                    
                    # ৫.২ GitHub-এ পুশ করা (Overwrite Mode)
                    update_payload = {
                        "message": f"Oracle Update: {datetime.datetime.now().strftime('%H:%M')}",
                        "content": base64.b64encode(patch_code.encode()).decode(),
                        "sha": sha
                    }
                    
                    _, put_status = call_github("PUT", F, data=update_payload, token=user_token)
                    
                    if put_status == 200:
                        st.balloons()
                        st.success("✅ অভিনন্দন! সিস্টেম সফলভাবে আপডেট হয়েছে।")
                        st.info("💡 পরিবর্তনগুলো দেখতে অ্যাপটি রিফ্রেশ করুন।")
                    else:
                        st.error(f"❌ পুশ এরর (Status: {put_status})।")
                except Exception as e:
                    st.error(f"❌ কোডে সিনট্যাক্স ভুল আছে: {e}")
            else:
                st.error(f"❌ ফাইল খুঁজে পাওয়া যায়নি (Status: {get_status})।")
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

