import streamlit as st
import json
import os
import requests
import base64

# ১. সেশন স্টেট
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# ২. মূল লজিক শুরু
if st.session_state["authenticated"]:
    st.title("🛡️ BaraQura Universe Dashboard")
    st.sidebar.title("Engine Controls")
    
    menu = st.sidebar.radio("Navigation", ["Home", "GitHub Code Editor", "AI Assistant (Chat)", "Settings"])

    if menu == "Home":
        st.success("Welcome, Master. V8.2 Core is fully functional.")
        st.info("আপনার পরিশ্রমই এই ইঞ্জিনকে প্রাণ দিয়েছে। সিস্টেম এখন আপনার নিয়ন্ত্রণে।")

    elif menu == "AI Assistant (Chat)":
        st.header("💬 Talk to BaraQura Engine")
        st.write("মাস্টার, আমি আপনার কথা শোনার জন্য প্রস্তুত।")
        user_msg = st.chat_input("Say something to your engine...")
        if user_msg:
            with st.chat_message("user"):
                st.write(user_msg)
            with st.chat_message("assistant"):
                st.write(f"মাস্টার, আমি আপনার '{user_msg}' কমান্ডটি রেকর্ড করেছি। শীঘ্রই ভয়েস মডিউল আপডেট করা হবে।")

    elif menu == "GitHub Code Editor":
        st.header("🚀 GitHub Remote Access")
        repo = "baraqurastudios/hasan-universe-engine"
        token = st.text_input("Enter Token:", type="password")
        if token:
            url_list = f"https://api.github.com/repos/{repo}/contents/"
            res_list = requests.get(url_list, headers={"Authorization": f"token {token}"})
            if res_list.status_code == 200:
                all_files = [f["path"] for f in res_list.json() if f["type"] == "file"]
                selected_file = st.selectbox("Select File:", all_files)
                if st.button("Fetch Code"):
                    # ফেচিং লজিক এখানে থাকবে...
                    st.success(f"{selected_file} Fetched!")
            else:
                st.error("Invalid Token or Repo.")

    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()

else:
    # পাসওয়ার্ড লেয়ার (আগের মতোই থাকবে)
    st.title("🛡️ BaraQura Universe Engine V8.2")
    user_input = st.text_input("Enter Master Key:", type="password")
    if st.button("Unlock System"):
        # ভেরিফিকেশন লজিক...
        st.session_state["authenticated"] = True
        st.rerun()
