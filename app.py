import streamlit as st
import requests
import base64
import datetime

# --- ১. প্রাথমিক কনফিগারেশন ---
REPO_NAME = "BaraQuraStudios/master-engine"
FILE_PATH = "app.py"

# --- ২. কোর ফাংশনসমূহ ---

def get_github_data(token):
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers).json()
    return response

def update_github_file(token, new_content, sha, message):
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {token}"}
    encoded = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')
    data = {"message": message, "content": encoded, "sha": sha}
    res = requests.put(url, headers=headers, json=data)
    return res.status_code == 200

# --- ৩. ইউজার ইন্টারফেস ---
st.set_page_config(page_title="BaraQura Master Engine", layout="wide")

# ড্যাশবোর্ড হেডার
st.markdown("<h1 style='text-align: center; color: #00FFAA;'>💎 BaraQura Studios Master Engine</h1>", unsafe_allow_html=True)

# সাইডবারে টোকেন ম্যানেজমেন্ট (একবার দিলেই হবে)
st.sidebar.title("🔐 Master Access")
user_token = st.sidebar.text_input("GitHub Token:", type="password", help="আপনার GitHub Personal Access Token এখানে দিন।")
if user_token:
    st.sidebar.success("✅ Token Connected")
else:
    st.sidebar.warning("⚠️ Please enter Token")

st.sidebar.divider()
st.sidebar.title("🧬 System Evolution")
st.sidebar.info(f"📅 {datetime.datetime.now().strftime('%d %b, %Y')}")

# ৪. মেইন কন্ট্রোল ট্যাবসমূহ
tab1, tab2, tab3 = st.tabs(["🔮 Oracle Portal", "🛡️ Recovery Center", "📊 Studio Status"])

with tab1:
    st.subheader("🌀 The Oracle Update Portal")
    option = st.radio("আপডেটের ধরন নির্বাচন করুন:", 
                      ["Smart Inject (নিচে যোগ হবে)", "Full Overwrite (পুরো ফাইল আপডেট)"])
    
    patch_code = st.text_area("জেমিনি থেকে পাওয়া কোডটি এখানে দিন...", height=300, placeholder="নতুন সিস্টেমের কোড এখানে পেস্ট করুন...")
    
    if st.button("Execute System Update 🚀"):
        if not user_token:
            st.error("❌ টোকেন ছাড়া আপডেট সম্ভব নয়। সাইডবারে টোকেন দিন।")
        elif not patch_code:
            st.warning("⚠️ কোড এন্ট্রি করুন।")
        else:
            with st.spinner("GitHub-এর সাথে সিঙ্ক্রোনাইজ হচ্ছে..."):
                data = get_github_data(user_token)
                sha = data.get('sha')
                
                if not sha:
                    st.error("❌ রিপোজিটরি কানেকশন এরর। টোকেন বা পাথ চেক করুন।")
                else:
                    old_content = base64.b64decode(data['content']).decode('utf-8')
                    st.session_state['last_backup'] = old_content
                    
                    if option == "Smart Inject (নিচে যোগ হবে)":
                        final_code = f"{old_content}\n\n# --- New Patch: {datetime.datetime.now()} ---\n{patch_code}"
                        msg = "Smart injection via Oracle"
                    else:
                        final_code = patch_code
                        msg = "Full file overwrite via Oracle"
                    
                    if update_github_file(user_token, final_code, sha, msg):
                        st.balloons()
                        st.success("Alhamdulillah! সিস্টেম আপডেট সফল হয়েছে।")
                    else:
                        st.error("আপডেট ব্যর্থ হয়েছে। পারমিশন চেক করুন।")

with tab2:
    st.subheader("⏪ Recovery / Undo Center")
    if st.button("Restore Previous Version ⏪"):
        if 'last_backup' in st.session_state and user_token:
            data = get_github_data(user_token)
            if update_github_file(user_token, st.session_state['last_backup'], data['sha'], "Undo last update"):
                st.success("সফলভাবে রিস্টোর করা হয়েছে!")
            else:
                st.error("রিস্টোর ব্যর্থ হয়েছে।")
        else:
            st.info("ব্যাকআপ বা টোকেন পাওয়া যায়নি।")

with tab3:
    st.subheader("📊 Studio Live Status")
    st.metric(label="Engine Status", value="Active", delta="Smooth Edition")
    st.write(f"সর্বশেষ সিঙ্ক: {datetime.datetime.now().strftime('%H:%M:%S')}")

st.divider()
st.caption("BaraQura Studios | v110.0 Master Engine | Admin: Sakibul Hasan")
