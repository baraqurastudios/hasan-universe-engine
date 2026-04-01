import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# ১. কনফিগারেশন এবং নিরাপত্তা (API Key লোড করা)
load_dotenv()
# আপনার .env ফাইলে GEMINI_API_KEY=আপনার_কী লিখে রাখুন
# অথবা সরাসরি নিচে বসাতে পারেন (তবে এটি কম নিরাপদ)
API_KEY = os.getenv("GEMINI_API_KEY") 

if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("API Key পাওয়া যায়নি! দয়া করে .env ফাইলে এটি সেট করুন।")

# ২. কথা বলার ফাংশন (Text-to-Speech)
def speak(text):
    # গুগল টিটিএস ব্যবহার করে বাংলা অডিও জেনারেট
    audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={text}&tl=bn&client=tw-ob"
    st.markdown(f'<audio src="{audio_url}" autoplay hidden></audio>', unsafe_allow_html=True)

# ৩. Gemini AI থেকে উত্তর নেওয়ার ফাংশন
def get_gemini_response(user_input):
    try:
        # জেমিনি মডেলকে ইনপুট পাঠানো
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"মাস্টার, জেমিনি ইঞ্জিনে সমস্যা হচ্ছে: {str(e)}"

# ৪. লগইন লেয়ার (Master Key সিস্টেম)
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.title("🛡️ BaraQura Universe Engine V8.2")
    st.subheader("Login to Access Master Dashboard")
    
    # মাস্টার কী ইনপুট (Password mode)
    master_key = st.text_input("Enter Master Key:", type="password")
    
    if st.button("Unlock"):
        # এখানে আপনার নিজের পছন্দমতো পাসওয়ার্ড সেট করুন
        if master_key == "BaraQura@2026": 
            st.session_state["authenticated"] = True
            st.success("Access Granted, Master!")
            st.rerun()
        else:
            st.error("Invalid Master Key! Access Denied.")

# ৫. ড্যাশবোর্ড ইন্টারফেস (লগইন সফল হলে)
else:
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio("Go to", ["Home", "GitHub Code Editor", "AI Assistant (Chat)"])
    
    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()

    if menu == "AI Assistant (Chat)":
        st.title("🛡️ BaraQura Universe Dashboard")
        st.header("💬 Talk to BaraQura Brain (Gemini Powered)")
        
        if "chat_history" not in st.session_state:
            st.session_state["chat_history"] = []

        # চ্যাট ইনপুট
        user_msg = st.chat_input("আমার সাথে কথা বলুন, মাস্টার...")

        if user_msg:
            with st.spinner("BaraQura Brain is thinking..."):
                # Gemini থেকে উত্তর আনা
                ai_reply = get_gemini_response(user_msg)
            
            # হিস্টোরিতে সেভ করা
            st.session_state["chat_history"].append({"role": "user", "content": user_msg})
            st.session_state["chat_history"].append({"role": "assistant", "content": ai_reply})
            
            # অডিও ফিডব্যাক
            speak(ai_reply)

        # চ্যাট মেসেজগুলো দেখানো
        for message in st.session_state["chat_history"]:
            with st.chat_message(message["role"]):
                st.write(message["content"])

    elif menu == "Home":
        st.title("Welcome to BaraQura Universe")
        st.write("আপনার সিস্টেম এখন জেমিনি এআই দ্বারা পরিচালিত হচ্ছে।")

    elif menu == "GitHub Code Editor":
        st.title("GitHub Code Editor")
        st.write("এখানে আপনার গিটহাব ইন্টিগ্রেশন কোড যোগ করুন।")
