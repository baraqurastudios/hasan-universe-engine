# ==========================================
# 🧬 BaraQura OS: Unified Master Engine v6.5
# 📅 Date: 28 Mar, 2026 | Mode: Backup & Rollback
# ==========================================

import streamlit as st
import requests
import base64
import datetime

# --- ১. রিপোজিটরি কনফিগারেশন ---
U, R, F = "baraqurastudios", "hasan-universe-engine", "app.py"

st.set_page_config(page_title="BaraQura Master Engine", layout="wide", page_icon="🛡️")

# --- ২. সাইডবার: মাস্টার এক্সেস ---
st.sidebar.title("🔐 Master Control")
user_token = st.sidebar.text_input("GitHub Access Token:", type="password", key="auth_v65")

# --- ৩. কোর ইঞ্জিন (GitHub API) ---
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

# --- ৪. মেইন ইন্টারফেস ---
st.title("🛰️ BaraQura Unified Master Engine")

if user_token:
    # কানেকশন স্ট্যাটাস চেক
    file_data, status = call_github("GET", F, token=user_token)
    
    if status == 200:
        st.sidebar.success(f"✅ Connected to {R}")
        
        tab1, tab2 = st.tabs(["🌀 Oracle Update", "⏪ Rollback System"])

        # --- ট্যাব ১: ওড়াকল আপডেট (Auto Backup সহ) ---
        with tab1:
            st.subheader("The Oracle Update Portal")
            patch_code = st.text_area("নতুন কোড এখানে দিন...", height=350, key="patch_v65")

            if st.button("Execute System Update 🚀", key="update_btn_v65"):
                if not patch_code:
                    st.warning("⚠️ ইনজেক্ট করার জন্য কোনো কোড পাওয়া যায়নি।")
                else:
                    with st.spinner("🔄 সিঙ্ক্রোনাইজ হচ্ছে..."):
                        # ১. অটো ব্যাকআপ লজিক (ভুল হলে আগের ফাইল রক্ষা পাবে)
                        try:
                            old_content = base64.b64decode(file_data['content']).decode('utf-8')
                            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                            backup_path = f"backups/app_backup_{timestamp}.py"

                            backup_payload = {
                                "message": f"🔐 Auto Backup: {timestamp}",
                                "content": base64.b64encode(old_content.encode()).decode()
                            }
                            call_github("PUT", backup_path, data=backup_payload, token=user_token)
                        except Exception as e:
                            st.warning(f"⚠️ Backup failed: {e}")

                        # ২. সিনট্যাক্স চেক এবং আপডেট
                        try:
                            compile(patch_code, "<string>", "exec")
                            
                            update_payload = {
                                "message": f"Oracle Sync: {datetime.datetime.now().strftime('%H:%M')}",
                                "content": base64.b64encode(patch_code.encode()).decode(),
                                "sha": file_data['sha']
                            }
                            _, put_status = call_github("PUT", F, data=update_payload, token=user_token)

                            if put_status == 200:
                                st.balloons()
                                st.success("✅ সিস্টেম আপডেট হয়েছে (Backup Safe)।")
                                st.info("🔄 পরিবর্তন দেখতে অ্যাপটি রিফ্রেশ করুন।")
                            else:
                                st.error(f"❌ পুশ এরর: {put_status}")
                        except Exception as e:
                            st.error(f"❌ সিনট্যাক্স ভুল: {e}")

        # --- ট্যাব ২: রোলব্যাক সিস্টেম (Restore Backup) ---
        with tab2:
            st.subheader("Restore from Backup 🛡️")
            backups_list, b_status = call_github("GET", "backups", token=user_token)

            if b_status == 200 and isinstance(backups_list, list) and backups_list:
                # শুধু .py ফাইলগুলো ফিল্টার করা
                backup_files = [item['name'] for item in backups_list if item['name'].endswith(".py")]
                selected_backup = st.selectbox("📂 Select Backup File", backup_files[::-1], key="backup_select")

                if st.button("Restore Selected Backup ⏪"):
                    with st.spinner("🔄 Restoring..."):
                        # ব্যাকআপ কন্টেন্ট রিট্রিভ করা
                        b_file_data, _ = call_github("GET", f"backups/{selected_backup}", token=user_token)
                        if 'content' in b_file_data:
                            b_content = base64.b64decode(b_file_data['content']).decode('utf-8')
                            
                            # বর্তমান ফাইলের SHA রিট্রিভ করা
                            current_f, _ = call_github("GET", F, token=user_token)
                            
                            restore_payload = {
                                "message": f"Rollback to: {selected_backup}",
                                "content": base64.b64encode(b_content.encode()).decode(),
                                "sha": current_f['sha']
                            }
                            _, r_status = call_github("PUT", F, data=restore_payload, token=user_token)

                            if r_status == 200:
                                st.success(f"✅ Restored from {selected_backup}")
                                st.info("🔄 Refresh app to see changes.")
                            else:
                                st.error(f"❌ Restore failed. Status: {r_status}")
            else:
                st.info("No backups found in 'backups/' folder.")

    else:
        st.sidebar.error(f"❌ কানেকশন এরর: {status}")
else:
    st.warning("🔒 Please enter GitHub token first.")
