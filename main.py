import streamlit as st
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

# ১. প্রাথমিক সেটআপ
st.set_page_config(page_title="BaraQura V10 Engine", layout="wide")

# এপিআই কি এবং ডাটাবেস ইনিশিয়ালাইজেশন
GEMINI_API_KEY = "AIzaSyCe_E4nSKKNfky_9cgKQMLwMf5EdGJHpy0"
db = DBManager()
engine = BaraQuraEngine(db, GEMINI_API_KEY)

# --- সাইডবার মেনু ---
st.sidebar.title("🛡️ BaraQura Control Panel")
menu = st.sidebar.radio("নেভিগেশন", ["চ্যাট টেস্ট", "লিড ড্যাশবোর্ড", "এআই মেমোরি রিভিউ"])

# ২. চ্যাট টেস্ট সেকশন (Testing the Brain)
if menu == "চ্যাট টেস্ট":
    st.header("🤖 AI Chatbot Test")
    
    with st.form("chat_form"):
        user_id = st.text_input("User ID (e.g. facebook_123)", "test_user_01")
        user_name = st.text_input("User Name", "Shakibul Hasan")
        user_msg = st.text_area("Message")
        submit = st.form_submit_button("Send Message")

    if submit and user_msg:
        response = engine.generate_response(user_id, user_name, user_msg)
        st.info(f"**BaraQura AI:** {response}")
        st.success("রেসপন্স জেনারেট হয়েছে এবং মেমোরি আপডেট করা হয়েছে।")

# ৩. লিড ড্যাশবোর্ড (তোর আগের সেলস ট্র্যাকিং)
elif menu == "লিড ড্যাশবোর্ড":
    st.header("📈 Sales Leads & Scoring")
    db.cursor.execute("SELECT * FROM users ORDER BY score DESC")
    leads = db.cursor.fetchall()
    
    if leads:
        st.table(leads)
    else:
        st.warning("এখনো কোনো লিড জমা হয়নি।")

# ৪. এআই মেমোরি রিভিউ (The Learning Loop 🛡️)
elif menu == "এআই মেমোরি রিভিউ":
    st.header("🧠 AI Memory & Learning Control")
    st.write("এআই নতুন যা শিখেছে তা এখানে রিভিউ কর। তুই 'Approve' করলে তবেই সে অন্য কাস্টমারকে এটি বলবে।")
    
    db.cursor.execute("SELECT id, question, answer FROM brain_memory WHERE is_verified = 0")
    pending_items = db.cursor.fetchall()
    
    if not pending_items:
        st.balloons()
        st.success("সব পরিষ্কার! এআই নতুন কিছু শেখার অপেক্ষায় আছে।")
    
    for item in pending_items:
        with st.expander(f"প্রশ্ন: {item[1]}"):
            st.write(f"**এআই এর প্রস্তাবিত উত্তর:** {item[2]}")
            if st.button(f"Approve ID: {item[0]}", key=f"btn_{item[0]}"):
                db.cursor.execute("UPDATE brain_memory SET is_verified = 1 WHERE id = ?", (item[0],))
                db.conn.commit()
                st.success("এটি এখন মেমোরিতে সেভ হয়েছে!")
                st.rerun()

# ৫. ডাটাবেস কানেকশন ক্লোজ (সেফটি)
# db.close() # স্ট্রিমলিটে এটি লুপে না চালানোই ভালো
