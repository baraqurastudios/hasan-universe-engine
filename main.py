import streamlit as st
import os
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

# ১. সিস্টেম ইনিশিয়াল (তোর পুরনো database_sync লজিককেও সম্মান জানানো হয়েছে)
@st.cache_resource
def init_baraqura():
    # এখানে v10 ডাটাবেস ম্যানেজার ব্যবহার করা হচ্ছে
    db = DBManager()
    engine = BaraQuraEngine(db)
    return db, engine

db, engine = init_baraqura()

# ২. Streamlit UI (এটি না থাকলে ক্লাউডে লোড হবে না)
st.set_page_config(page_title="BaraQura Universe", page_icon="🛡️")
st.title("🛡️ BaraQura V10 Universe Engine")
st.info("System Status: Online | Security: Maximum")

# ৩. সেশন স্টেট (চ্যাট মনে রাখার জন্য)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ৪. চ্যাট ডিসপ্লে
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# ৫. ইউজার ইনপুট (তোর সেই লোকাল main.py এর লজিক এখন ক্লাউডে)
if user_input := st.chat_input("Ask BaraQura..."):
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # ইঞ্জিন দিয়ে প্রসেস করা
    # সিমুলেশন আইডি: test_user_fb_001
    response = engine.generate_response("test_user_fb_001", "MD Hasan Ali", user_input)
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

    # সাইডবারে তোর ডাটাবেস স্কোর দেখানো (যেটা আগে print হতো)
    status = db.get_user("test_user_fb_001")
    with st.sidebar:
        st.title("📊 Lead Monitoring")
        st.metric("Lead Status", status['status'])
        st.metric("Interest Score", status['score'])
