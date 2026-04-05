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

# ২. পেজ কনফিগারেশন
st.set_page_config(page_title="BaraQura V10", layout="wide")
st.title("🛡️ BaraQura V10 Universe Engine")

# --- গুরুত্বপূর্ণ পরিবর্তন: ইউজারের তথ্য লুপের বাইরে রাখা ---
user_id = "shakibul_v10_001" 
full_name = "Md. Shakibul Hasan" 

# ৩. সাইডবার স্ট্যাটাস (লাইভ আপডেট হবে)
with st.sidebar:
    st.success("System: Online")
    st.divider()
    st.subheader("📊 Live Lead Tracking")
    # ডাটাবেস থেকে রিয়েলটাইম ডাটা আনা
    current_status = db.get_user(user_id)
    if current_status:
        st.write(f"**User:** {full_name}")
        st.info(f"**Score:** {current_status['score']}")
        st.warning(f"**Status:** {current_status['status']}")
    else:
        st.write("No active lead detected.")

# ৪. চ্যাট হিস্ট্রি ম্যানেজমেন্ট
if "messages" not in st.session_state:
    st.session_state.messages = []

# ৫. চ্যাট মেসেজগুলো স্ক্রিনে দেখানো
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ৬. ইউজার ইনপুট বক্স
if prompt := st.chat_input("এআই এর সাথে কথা বলুন..."):
    # ইউজারের মেসেজ সেশনে সেভ করা
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # V10 ইঞ্জিনের মাধ্যমে রেসপন্স তৈরি (তোর পুরো নাম পাঠানো হচ্ছে)
    response = engine.generate_response(user_id, full_name, prompt)
    
    # এআই রিপ্লাই দেখানো এবং সেভ করা
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # পেজ রিফ্রেশ করা যাতে সাইডবার স্কোর সাথে সাথে আপডেট হয়
    st.rerun()
