1# ==========================================
# 🧬 BaraQura OS: Unified Master Engine v6.0
# 📅 Date: 28 Mar, 2026 | Mode: Self-Healing
# ==========================================

import streamlit as st
import requests
import base64
import datetime

# --- ১. গ্লোবাল রিপোজিটরি কনফিগারেশন ---
U, R, F = "baraqurastudios", "hasan-universe-engine", "app.py"

st.set_page_config(page_title="BaraQura Master Engine", layout="wide", page_icon="🛰️")

# --- ২. সাইডবার: মাস্টার এক্সেস ---
st.sidebar.header("🔐 Master Control")
# ইউনিক key ব্যবহার করে DuplicateElementId এরর স্থায়ীভাবে ফিক্স করা হয়েছে
user_token = st.sidebar.text_input("GitHub Access Token:", type="password", key="master_auth_v6")

# --- ৩. কোর ইঞ্জিন (GitHub API Handler) ---
def call_github(method, endpoint, data=None, token=None):
    url = f"https://api.github.com/repos/{U}/{R}/contents/{endpoint}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    try:
        if method == "GET":
            res = requests.get(url, headers=headers, timeout=10)
        else:
            res = requests.put(url, headers=headers, json=data, timeout=10)
        return res.json(), res.status_code
    except Exception as e:
        return {"message": str(e)}, 500

# --- ৪. মেইন ফ্রেম লজিক ---
st.title("🛰️ BaraQura Unified Master Engine")

if user_token:
    # কানেকশন চেক
    with st.spinner("Checking Connection..."):
        file_data, status = call_github("GET", F, token=user_token)
    
    if status == 200:
        st.sidebar.success(f"✅ Connected: {R}")
        
        # ট্যাব সিস্টেম: আপডেট এবং স্ক্রিপ্ট ল্যাব
        tab1, tab2, tab3 = st.tabs(["🌀 Oracle Update", "📝 Story Lab", "📊 Analytics"])
        
        # ট্যাব ১: ওরাকল আপডেট পোর্টাল
        with tab1:
            st.subheader("The Oracle Update Portal")
            st.info("Update Mode: **Full Overwrite Sync (Safe)**")
            
            # নতুন কোড ইনপুট এলাকা
            patch_code = st.text_area("নতুন কোড এখানে দিন...", height=400, key="oracle_patch_area_v6", placeholder="Paste Python code here...")
            
            if st.button("Push System Update 🚀", key="execute_sync_v6"):
                if patch_code:
                    try:
                        # ৫.১ সিনট্যাক্স শিল্ড: ভুল কোড থাকলে এটি আপডেট আটকে দেবে
                        compile(patch_code, "<string>", "exec")
                        
                        sha = file_data['sha']
                        payload = {
                            "message": f"BaraQura OS Auto-Sync: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
                            "content": base64.b64encode(patch_code.encode()).decode(),
                            "sha": sha
                        }
                        
                        _, put_status = call_github("PUT", F, data=payload, token=user_token)
                        
                        if put_status == 200:
                            st.balloons()
                            st.success("✅ অভিনন্দন! সিস্টেম ক্লিনভাবে আপডেট হয়েছে।")
                            st.info("💡 পরিবর্তনগুলো কার্যকর করতে অ্যাপটি রিফ্রেশ দিন।")
                        else:
                            st.error(f"❌ পুশ এরর: {put_status}")
                    except Exception as e:
                        # সিনট্যাক্স এরর মেসেজ
                        st.error(f"❌ কোডে সিনট্যাক্স ভুল আছে! আপডেট বাতিল করা হয়েছে। \n\nError: {e}")
                else:
                    st.warning("⚠️ কোড বক্স খালি।")
        
        # ট্যাব ২: হাসান এনিমেশন স্ক্রিপ্ট (ইউজার সামারি অনুযায়ী)
        with tab2:
            st.subheader("📝 Script Production Lab")
            st.write("চরিত্র: **হাসান (৭ বছর)** | মা: **লিজা**")
            st.info("এখানে আপনার এনিমেশন সিরিজের স্টোরি এবং ভয়েস স্ক্রিপ্ট ম্যানেজ করা যাবে।")

        with tab3:
            st.subheader("Studio Analytics")
            st.metric("System Health", "Optimal", "100%")

    else:
        st.sidebar.error(f"❌ কানেকশন এরর: {status}। টোকেন বা রিপোজিটরি নাম চেক করুন।")
else:
    st.warning("🔒 অ্যাক্সেস পেতে সাইডবারে আপনার GitHub Token প্রদান করুন।")
