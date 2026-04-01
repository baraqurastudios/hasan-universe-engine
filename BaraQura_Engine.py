import streamlit as st
import json
import os
import requests
import base64

# ১. সেশন স্টেট (লগইন এবং চ্যাট মেমোরি)
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# ২. কথা বলার ফাংশন (Text-to-Speech)
def speak(text):
    # Google-এর একটি সিম্পল TTS API ব্যবহার করা হচ্ছে
    audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={text}&tl=bn&client=tw-ob"
    st.markdown(f'<audio src="{audio_url}" autoplay hidden></audio>', unsafe_allow_status=True)

# ৩. মূল লজিক শুরু
if st.session_state["authenticated"]:
    st.title("🛡️ BaraQura Universe Dashboard")
    st.sidebar.title("Engine Controls")
    
    menu = st.sidebar.radio("Navigation", ["Home", "GitHub Code Editor", "AI Assistant (Chat)", "Settings"])

    if menu == "Home":
        st.success("Welcome, Master. V8.2 Core is ONLINE.")
        st.info("সিস্টেম এখন আপনার কথা শোনার জন্য প্রস্তুত।")

    elif menu == "AI Assistant (Chat)":
        st.header("💬 Talk to BaraQura Engine")
        st.write("মাস্টার, আমি আপনার কথা শোনার জন্য প্রস্তুত।")

        # চ্যাট ইনপুট
        user_msg = st.chat_input("Say something to your engine...")
        
        if user_msg:
            # ইঞ্জিন যা উত্তর দেবে (এখানে আপনি নিজের মতো রেসপন্স সেট করতে পারেন)
            response_text = f"মাস্টার, আমি আপনার '{user_msg}' কমান্ডটি রেকর্ড করেছি এবং এটি প্রসেস করছি।"
            
            # মেমোরিতে সেভ করা
            st.session_state["chat_history"].append({"role": "user", "content": user_msg})
            st.session_state["chat_history"].append({"role": "assistant", "content": response_text})
            
            # কথা বলা শুরু করবে
            speak(response_text)

        # চ্যাট হিস্ট্রি দেখানো
        for message in st.session_state["chat_history"]:
            with st.chat_message(message["role"]):
                st.write(message["content"])

    elif menu == "GitHub Code Editor":
        # ... আপনার আগের GitHub কোড এডিটর মডিউল এখানে থাকবে ...
        st.header("🚀 GitHub Remote Access")
        st.info("কোড এডিট করার জন্য এই মডিউলটি ব্যবহার করুন।")

    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()

else:
    # লগইন লেয়ার (আগের মতোই থাকবে)
    st.title("🛡️ BaraQura Universe Engine V8.2")
    user_input = st.text_input("Enter Master Key:", type="password")
    if st.button("Unlock System"):
        # ভেরিফিকেশন (আপনার config অনুযায়ী)
        st.session_state["authenticated"] = True
        st.rerun()
