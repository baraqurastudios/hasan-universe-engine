import streamlit as st
import requests
import base64
import datetime

# --- ১. কনফিগারেশন (আপনার টোকেন এবং রিপোজিটরি এখানে দিন) ---
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN_HERE" 
REPO_NAME = "BaraQuraStudios/master-engine"
FILE_PATH = "app.py"

# --- ২. কোর ফাংশনসমূহ (GitHub API Logic) ---

def get_github_data():
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers).json()
    return response

def update_github_file(new_content, sha, message):
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    encoded = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')
    data = {"message": message, "content": encoded, "sha": sha}
    res = requests.put(url, headers=headers, json=data)
    return res.status_code == 200

# --- ৩. ইউজার ইন্টারফেস সেটআপ ---
st.set_page_config(page_title="BaraQura Master Engine", layout="wide")

# ড্যাশবোর্ড হেডার
st.markdown("<h1 style='text-align: center; color: #00FFAA;'>💎 BaraQura Studios Master Engine</h1>", unsafe_allow_html=True)

# সাইডবার স্ট্যাটাস
st.sidebar.title("🧬 System Evolution")
st.sidebar.success("✅ v110.0: Unified Sync Active")
st.sidebar.info(f"📅 {datetime.datetime.now().strftime('%d %b, %Y')}")

# ৪. মেইন কন্ট্রোল ট্যাবসমূহ
tab1, tab2, tab3 = st.tabs(["🔮 Oracle Portal", "🛡️ Recovery Center", "📊 Studio Status"])

with tab1:
    st.subheader("🌀 The Oracle Update Portal")
    option = st.radio("আপডেটের ধরন নির্বাচন করুন:", 
                      ["Smart Inject (পুরনো কোডের নিচে যোগ হবে)", "Full Overwrite (পুরো ফাইল নতুন করে লিখবে)"])
    
    patch_code = st.text_area("জেমিনি থেকে পাওয়া কোডটি এখানে দিন...", height=300)
    
    if st.button("Execute System Update 🚀"):
        if patch_code and GITHUB_TOKEN != "YOUR_GITHUB_TOKEN_HERE":
            with st.spinner("GitHub-এর সাথে সিঙ্ক্রোনাইজ হচ্ছে..."):
                data = get_github_data()
                sha = data.get('sha')
                
                if not sha:
                    st.error("❌ ফাইল খুঁজে পাওয়া যায়নি। GitHub কনফিগারেশন চেক করুন।")
                else:
                    # পুরনো কন্টেন্ট ব্যাকআপ রাখা (Undo এর জন্য)
                    old_content = base64.b64decode(data['content']).decode('utf-8')
                    st.session_state['last_backup'] = old_content
                    
                    if option == "Smart Inject (পুরনো কোডের নিচে যোগ হবে)":
                        final_code = f"{old_content}\n\n# --- New Patch: {datetime.datetime.now()} ---\n{patch_code}"
                        msg = "Smart injection via Oracle"
                    else:
                        final_code = patch_code
                        msg = "Full file overwrite via Oracle"
                    
                    # আপডেট পুশ করা
                    if update_github_file(final_code, sha, msg):
                        st.balloons()
                        st.success("Alhamdulillah! সিস্টেম সাকসেসফুলি আপডেট হয়েছে।")
                    else:
                        st.error("আপডেট ব্যর্থ হয়েছে। টোকেন বা পারমিশন চেক করুন।")
        else:
            st.warning("দয়া করে কোড দিন এবং GitHub Token নিশ্চিত করুন।")

with tab2:
    st.subheader("⏪ Recovery / Undo Center")
    st.warning("সর্বশেষ আপডেটে কোনো সমস্যা হলে এখান থেকে আগের ভার্সনে ফিরে যান।")
    
    if st.button("Restore Previous Version ⏪"):
        if 'last_backup' in st.session_state:
            data = get_github_data()
            if update_github_file(st.session_state['last_backup'], data['sha'], "Undo last update"):
                st.success("সফলভাবে আগের ভার্সন রিস্টোর করা হয়েছে!")
            else:
                st.error("রিস্টোর ব্যর্থ হয়েছে।")
        else:
            st.info("বর্তমানে রিস্টোর করার মতো কোনো ব্যাকআপ সেশনে নেই।")

with tab3:
    st.subheader("📊 Studio Live Status")
    st.write(f"সর্বশেষ সিঙ্ক টাইম: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.metric(label="Engine Status", value="Active", delta="v110.0 Stable")
    st.info("আপনার ইঞ্জিন এখন GitHub-এর মাধ্যমে সরাসরি আপডেট গ্রহণ করতে সক্ষম।")

st.divider()
st.caption("BaraQura Studios | v110.0 Master Engine | Admin: Sakibul Hasan")
