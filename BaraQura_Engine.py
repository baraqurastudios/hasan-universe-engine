import streamlit as st
import requests
import base64

# ১. কথা বলার ফাংশন (Text-to-Speech)
def speak(text):
    audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={text}&tl=bn&client=tw-ob"
    st.markdown(f'<audio src="{audio_url}" autoplay hidden></audio>', unsafe_allow_html=True)

# ২. AI এর বুদ্ধি বাড়ানোর ফাংশন (Free AI API logic)
def get_ai_response(user_input):
    # এখানে আমরা একটি ফ্রি এআই ইন্টারফেস ব্যবহার করছি যা আপনার কথার উত্তর দেবে
    try:
        # এটি একটি উদাহরণ, আপনি চাইলে এখানে আপনার Gemini API Key বসাতে পারেন
        response = requests.get(f"https://api.simsimi.net/v2/?text={user_input}&lc=bn")
        if response.status_code == 200:
            return response.json()['success']
    except:
        return "মাস্টার, আমার সার্ভারে সংযোগ পেতে সমস্যা হচ্ছে। তবে আমি আপনার কথা শুনতে পাচ্ছি।"
    return "মাস্টার, আমি বিষয়টি নিয়ে ভাবছি।"

# ৩. ড্যাশবোর্ড ইন্টারফেস
if "authenticated" in st.session_state and st.session_state["authenticated"]:
    st.title("🛡️ BaraQura Universe Dashboard")
    
    menu = st.sidebar.radio("Navigation", ["Home", "GitHub Code Editor", "AI Assistant (Chat)"])

    if menu == "AI Assistant (Chat)":
        st.header("💬 Talk to BaraQura Brain")
        
        if "chat_history" not in st.session_state:
            st.session_state["chat_history"] = []

        user_msg = st.chat_input("আমার সাথে কথা বলুন, মাস্টার...")

        if user_msg:
            # ইঞ্জিন এখন চিন্তা করবে (AI Logic)
            with st.spinner("Thinking..."):
                ai_reply = get_ai_response(user_msg)
            
            # মেমোরিতে রাখা
            st.session_state["chat_history"].append({"role": "user", "content": user_msg})
            st.session_state["chat_history"].append({"role": "assistant", "content": ai_reply})
            
            # কথা বলা (Audio)
            speak(ai_reply)

        # চ্যাট প্রদর্শন
        for message in st.session_state["chat_history"]:
            with st.chat_message(message["role"]):
                st.write(message["content"])

# ৪. লগইন লেয়ার (আগের মতো)
else:
    st.title("🛡️ BaraQura Universe Engine V8.2")
    # ... আপনার পাসওয়ার্ড লজিক ...
    if st.button("Unlock"):
        st.session_state["authenticated"] = True
        st.rerun()
