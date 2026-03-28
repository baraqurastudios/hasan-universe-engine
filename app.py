import streamlit as st
import requests
import base64
import datetime

# --- ১. মাস্টার কনফিগারেশন (GitHub API) ---
# আপনার GitHub সেটিংস থেকে এই তথ্যগুলো আপডেট করে নিন
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN_HERE" 
REPO_NAME = "BaraQuraStudios/master-engine" # আপনার রিপোজিটরির সঠিক নাম
FILE_PATH = "app.py" 

# --- ২. GitHub রাইট ফাংশন (The Patch) ---
def sync_to_github(new_content, commit_msg="System Update via Oracle Portal"):
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    # বর্তমান ফাইলের SHA সংগ্রহ (GitHub ভার্সন কন্ট্রোলের জন্য প্রয়োজন)
    res = requests.get(url, headers=headers).json()
    sha = res.get('sha')
    
    if not sha:
        return "❌ Error: Could not find File SHA. Check Repo/Path."

    # কন্টেন্ট এনকোডিং
    encoded = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')
    
    payload = {
        "message": commit_msg,
        "content": encoded,
        "sha": sha
    }
    
    response = requests.put(url, headers=headers, json=payload)
    return response.status_code == 200

# --- ৩. ইউজার ইন্টারফেস (v110.0 Structure) ---
st.set_page_config(page_title="BaraQura Master Engine", layout="wide")

# ড্যাশবোর্ড হেডার (আপনার পছন্দমতো আপডেট করা হয়েছে)
st.markdown("<h1 style='text-align: center; color: #00FFAA;'>💎 BaraQura Studios Master Engine</h1>", unsafe_allow_html=True)
st.sidebar.title("🧬 System Evolution")
st.sidebar.success("✅ v110.0: GitHub Sync Active")

# ৪. ওরাকল পোর্টাল ও অটো-আপডেট ট্যাব
tab1, tab2 = st.tabs(["🔮 Oracle Portal", "📊 Studio Status"])

with tab1:
    st.subheader("🌀 The Oracle Update Portal")
    patch_code = st.text_area("নতুন কোড বা ফাইল কন্টেন্ট এখানে দিন...", height=300)
    
    if st.button("Push System Update to GitHub 🚀"):
        if patch_code and GITHUB_TOKEN != "YOUR_GITHUB_TOKEN_HERE":
            with st.spinner("GitHub-এ ফাইল রাইট হচ্ছে..."):
                success = sync_to_github(patch_code)
                if success:
                    st.balloons()
                    st.success("Alhamdulillah! GitHub ফাইল সাকসেসফুলি আপডেট হয়েছে।")
                else:
                    st.error("GitHub আপডেট ব্যর্থ হয়েছে। টোকেন বা পারমিশন চেক করুন।")
        else:
            st.warning("দয়া করে কোড দিন এবং আপনার GitHub Token কনফিগার করুন।")

with tab2:
    st.write(f"সর্বশেষ সিঙ্ক টাইম: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.info("আপনার স্ক্রিপ্ট এখন সরাসরি GitHub-এর সাথে কানেক্টেড।")

st.divider()
st.caption("BaraQura Studios | v110.0 Master Engine | Admin: Sakibul Hasan")
