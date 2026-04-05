import streamlit as st
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

# ১. সিস্টেম ইনিশিয়াল (Streamlit-এর জন্য অপ্টিমাইজড)
@st.cache_resource
def get_baraqura_system():
    # তোর ডাটাবেস এবং ইঞ্জিন কানেক্ট করা হচ্ছে
    db = DBManager()
    engine = BaraQuraEngine(db)
    return db, engine

db, engine = get_baraqura_system()

# ২. পেজ সেটআপ এবং স্টাইল
st.set_page_config(page_title="BaraQura V10", page_icon="🤖")
st.title("🤖 BaraQura V10 Sales Machine")
st.markdown("---")

# ৩. সেশন স্টেট (চ্যাট হিস্ট্রি ব্যাকআপ)
if "messages" not in st.session_state:
    st.session_state.messages = []

# ৪. ইউজারের প্রোফাইল (সিমুলেশন - ক্লাউড টেস্টের জন্য)
user_id = "cloud_tester_001"
raw_name = "MD Hasan Ali"

# ৫. চ্যাট হিস্ট্রি ডিসপ্লে করা
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ৬. ইউজার ইনপুট এবং ইঞ্জিনের কাজ
if user_input := st.chat_input("এআই এর সাথে কথা বলুন..."):
    # ইউজারের মেসেজ সেভ এবং শো করা
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # তোর ইঞ্জিন দিয়ে রেসপন্স জেনারেট করা (V10 Logic)
    response = engine.generate_response(user_id, raw_name, user_input)
    
    # এআই রেসপন্স শো করা
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # ৭. সাইডবারে রিয়েল-টাইম ডাটাবেস লগ (তোর রিকোয়ারমেন্ট অনুযায়ী)
    status = db.get_user(user_id)
    with st.sidebar:
        st.header("📊 Real-time Monitoring")
        st.success(f"User: {raw_name}")
        st.info(f"Current Score: {status['score']}")
        st.warning(f"Lead Status: {status['status']}")
        
        if st.button("Clear Chat"):
            st.session_state.messages = []
            st.rerun()
