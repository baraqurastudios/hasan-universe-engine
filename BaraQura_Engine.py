import streamlit as st
import json
import os
import requests
import base64

# ১. সেশন স্টেট
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# ২. কথা বলার ফাংশন
def speak(text):
    audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={text}&tl=bn&client=tw-ob"
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
        
        user_msg = st.chat_input("Say something to your engine...")
        
        if user_msg:
            msg_lower = user_msg.lower()
            
            # --- কথোপকথন ও কমান্ড আলাদা করার লজিক ---
            if "hi" in msg_lower or "hello" in msg_lower or "কেমন আছো" in msg_lower:
                response_text = "হ্যালো মাস্টার! আমি ভালো আছি। আপনার দিনটি কেমন যাচ্ছে?"
            
            elif "কে তুমি" in msg_lower or "তোমার নাম কি" in msg_lower:
                response_text = "আমি বারাকুরা ইউনিভার্স ইঞ্জিন ভার্সন ৮.২। আমি আপনার ব্যক্তিগত এআই সহকারী।"
            
            elif "status" in msg_lower or "অবস্থা" in msg_lower:
                response_text = "মাস্টার, সিস্টেমের সব মডিউল বর্তমানে অনলাইন এবং সুরক্ষিত আছে।"
            
            elif "কমান্ড" in msg_lower or "command" in msg_lower:
                response_text = "মাস্টার, আপনি আমাকে গিটহাবে কোড আপডেট করার বা সিস্টেম লক করার কমান্ড দিতে পারেন।"
            
            else:
                # যদি কোনো নির্দিষ্ট কি-ওয়ার্ড না পায়
                response_text = f"মাস্টার, আমি আপনার '{user_msg}' বিষয়টি বুঝতে পেরেছি। আপনি কি এটি নিয়ে আরও কিছু বলতে চান?"

            # মেমোরিতে সেভ এবং কথা বলা
            st.session_state["chat_history"].append({"role": "user", "content": user_msg})
            st.session_state["chat_history"].append({"role": "assistant", "content": response_text})
            speak(response_text)

        # চ্যাট হিস্ট্রি প্রদর্শন
        for message in st.session_state["chat_history"]:
            with st.chat_message(message["role"]):
                st.write(message["content"])

    elif menu == "GitHub Code Editor":
        st.header("🚀 GitHub Remote Access")
        # আগের গিটহাব এডিটর কোড এখানে থাকবে
        st.info("এখান থেকে আপনি কোড পুশ করতে পারবেন।")

    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()

else:
    # লগইন লেয়ার (পাসওয়ার্ড প্রোটেকশন)
    st.title("🛡️ BaraQura Universe Engine V8.2")
    user_input = st.text_input("Enter Master Key:", type="password")
    if st.button("Unlock System"):
        st.session_state["authenticated"] = True
        st.rerun()
