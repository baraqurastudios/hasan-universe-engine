import streamlit as st
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

# ১. সিস্টেম লেআউট এবং ক্যাশ (Cloud Performance এর জন্য)
@st.cache_resource
def load_v10_system():
    db = DBManager()
    engine = BaraQuraEngine(db)
    return db, engine

db, engine = load_v10_system()

# ২. টাইটেল এবং স্ট্যাটাস
st.set_page_config(page_title="BaraQura V10", layout="wide")
st.title("🛡️ BaraQura V10 Universe Engine")
st.sidebar.success("System: Online")

# ৩. চ্যাট হিস্ট্রি ম্যানেজমেন্ট
if "messages" not in st.session_state:
    st.session_state.messages = []

# ৪. চ্যাট মেসেজ দেখানো
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ৫. ইউজার ইনপুট বক্স
if prompt := st.chat_input("এআই এর সাথে কথা বলুন..."):
    # ইউজারের মেসেজ
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- গুরুত্বপূর্ণ পরিবর্তন এখানে ---
    # এখানে আমি তোর নাম "Md. Shakibul Hasan" সেট করে দিয়েছি
    user_id = "shakibul_001" 
    full_name = "Md. Shakibul Hasan" 

    # V10 ইঞ্জিনের বুদ্ধি ব্যবহার করে উত্তর তৈরি
    response = engine.generate_response(user_id, full_name, prompt)
    
    # এআই রিপ্লাই
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # সাইডবারে স্কোর মনিটরিং
    status = db.get_user(user_id)
    with st.sidebar:
        st.divider()
        st.subheader("📊 Live Lead Tracking")
        st.write(f"**User:** {full_name}")
        st.write(f"**Score:** {status['score']}")
        st.write(f"**Status:** {status['status']}")
