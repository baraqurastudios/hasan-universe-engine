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

# ২. কথা বলার ফাংশন (Text-to-Speech) - ফিক্সড ভার্সন
def speak(text):
    # Google TTS API ব্যবহার করে অডিও তৈরি
    audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={text}&tl=bn&client=tw-ob"
    # এখানে 'unsafe_allow_status' এর বদলে 'unsafe_allow_html' ব্যবহার করা হয়েছে
    st.markdown(f'<audio src="{audio_url}" autoplay hidden></audio>', unsafe_allow_html=True)

# ৩. মূল লজিক শুরু
if st.session_state["authenticated"]:
    st.title("🛡️ BaraQura Universe Dashboard")
    st.sidebar.title("Engine Controls")
    
    menu = st.sidebar.radio("Navigation", ["Home", "GitHub Code Editor", "AI Assistant (Chat)", "Settings"])

    if menu == "Home":
        st.success("Welcome, Master. V8.2 Core is ONLINE.")

    elif menu == "AI Assistant (Chat)":
        st.header("💬 Talk to BaraQura Engine")
        st.write("মাস্টার, আমি আপনার কথা শোনার জন্য প্রস্তুত।")

        user_msg = st.chat_input("Say something to your engine...")
        
        if user_msg:
            # ইঞ্জিন যা উত্তর দেবে
            response_text = f"মাস্টার, আমি আপনার '{user_msg}' কমান্ডটি পেয়েছি। আমি এটি নিয়ে কাজ করছি।"
            
            # মেমোরিতে সেভ
            st.session_state["chat_history"].append({"role": "user", "content": user_msg})
            st.session_state["chat_history"].append({"role": "assistant", "content": response_text})
            
            # কথা বলা শুরু করবে (অডিও প্লে হবে)
            speak(response_text)

        # চ্যাট হিস্ট্রি দেখানো
        for message in st.session_state["chat_history"]:
            with st.chat_message(message["role"]):
                st.write(message["content"])

    elif menu == "GitHub Code Editor":
        # আপনার রিপোজিটরি এবং টোকেন দিয়ে কোড এডিট করার আগের মডিউলটি এখানে অটোমেটিক কাজ করবে
        st.header("🚀 GitHub Remote Access")
        st.info("আপনার ফাইলগুলো এখান থেকে সরাসরি এডিট করুন।")

    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()

else:
    # লগইন লেয়ার
    st.title("🛡️ BaraQura Universe Engine V8.2")
    user_input = st.text_input("Enter Master Key:", type="password")
    if st.button("Unlock System"):
        st.session_state["authenticated"] = True
        st.rerun()
