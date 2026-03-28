import streamlit as st
import requests
import base64

# --- ১. মাস্টার সিকিউরিটি ---
def check_password():
    if "authenticated" not in st.session_state:
        st.markdown("<h1 style='text-align: center; color: #00FFAA;'>💎 BaraQura Evolution Gate</h1>", unsafe_allow_html=True)
        pwd = st.text_input("Master Access Key:", type="password")
        if st.button("Activate v129.1 Sync Engine 🚀"):
            if pwd == "bq2026": 
                st.session_state["authenticated"] = True
                st.rerun()
        return False
    return True

if check_password():
    st.set_page_config(page_title="BaraQura v129.1", layout="wide")

    # --- ২. গিটহাব সিঙ্ক ফাংশন ---
    def update_github_file(content, github_token, repo_name, file_path):
        url = f"https://api.github.com/repos/{repo_name}/contents/{file_path}"
        headers = {"Authorization": f"token {github_token}", "Accept": "application/vnd.github.v3+json"}
        get_file = requests.get(url, headers=headers)
        if get_file.status_code == 200:
            sha = get_file.json()['sha']
            content_base64 = base64.b64encode(content.encode()).decode()
            data = {"message": "System Update", "content": content_base64, "sha": sha}
            put_file = requests.put(url, headers=headers, json=data)
            return put_file.status_code
        return get_file.status_code

    st.title("🛰️ BaraQura Unified Master Engine v129.1")
    
    tab1, tab2 = st.tabs(["⚡ Direct Code Hit", "📊 Dashboard"])

    with tab1:
        st.subheader("🛠️ Master Code Editor")
        
        # এখানে এখন ৩টি বক্সই পাবেন
        github_token = st.text_input("১. GitHub Token:", type="password", placeholder="আপনার গিটহাব টোকেন এখানে দিন")
        repo_name = st.text_input("২. Repo Name:", value="baraqurastudios/hasan-universe-engine", placeholder="username/repository-name")
        
        new_code = st.text_area("৩. নতুন কোড (app.py):", height=300, placeholder="নতুন কোডটি এখানে পেস্ট করুন...")
        
        if st.button("🔥 Hit GitHub & Update"):
            if github_token and repo_name and new_code:
                with st.spinner("গিটহাবে সিঙ্ক হচ্ছে..."):
                    status = update_github_file(new_code, github_token, repo_name, "app.py")
                    if status in [200, 201]:
                        st.balloons()
                        st.success("সফলভাবে আপডেট হয়েছে! ২ মিনিট পর অ্যাপটি রিস্টার্ট হবে।")
                    else:
                        st.error(f"ব্যর্থ হয়েছে! এরর কোড: {status}. আপনার টোকেন বা রিপো নেম চেক করুন।")
            else:
                st.warning("সবগুলো বক্স পূরণ করুন।")

    with tab2:
        st.write("আপনার ড্যাশবোর্ড এখন লাইভ।")

    st.divider()
    st.caption("BaraQura Studios | v129.1 | Admin: Sakibul Hasan")
