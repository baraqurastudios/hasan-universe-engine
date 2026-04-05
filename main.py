import streamlit as st
import os
import time
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

# ১. এনভায়রনমেন্ট ও ডাটাবেস লোড
load_dotenv()
db = DBManager()

# --- ২. আল্ট্রা সিকিউরিটি (Black Hole + Rhythm + Case-Sensitive Meem) ---
def check_access():
    if st.session_state.get('system_status') == "KILLED":
        st.error("🌌 SYSTEM ABSORBED BY BLACK HOLE.")
        revive_key = st.text_input("Enter Emergency Master Key (Meen#8.10) to Revive", type="password")
        if st.button("Revive Engine"):
            if revive_key == "Meen#8.10":
                st.session_state.system_status = "ACTIVE"
                st.session_state.attempts = 0
                st.rerun()
        st.stop()

    if 'attempts' not in st.session_state: st.session_state.attempts = 0
    if 'authenticated' not in st.session_state: st.session_state.authenticated = False
    if 'press_times' not in st.session_state: st.session_state.press_times = []

    if not st.session_state.get('authenticated', False):
        st.title("🛡️ BaraQura Universe Access")
        
        # রিদম ইনপুট
        if st.button("🔴 TAP RHYTHM HERE"):
            st.session_state.press_times.append(time.time())
            st.toast("Tap recorded")

        key_input = st.text_input(f"Master Key (Attempts: {st.session_state.attempts}/3)", type="password")

        # রিদম লজিক
        taps = st.session_state.press_times
        intervals = [taps[i] - taps[i-1] for i in range(1, len(taps))]
        rhythm_granted = False
        if len(taps) == 3: # Mobile 2-1
            if intervals[0] < 0.5 and intervals[1] > 1.0: rhythm_granted = True
        elif len(taps) == 6: # Laptop 3-2-1
            if all(i < 0.5 for i in intervals[:2]) and all(i > 1.0 for i in intervals[2:5]): rhythm_granted = True

        # ম্যাজিক ওয়ার্ড লজিক
        magic_needed = (len(taps) > 0 and not rhythm_granted) or st.session_state.attempts >= 3
        magic_input = st.text_input("Confirm Magic Word (Meem)", type="password") if magic_needed else ""

        if st.button("Verify & Unlock"):
            if st.session_state.attempts >= 3 and not rhythm_granted:
                st.session_state.system_status = "KILLED"
                st.rerun()
            
            if (rhythm_granted and key_input == "Meen#8.10") or (key_input == "V8_UNIVERSE_GOD_2026" and (not magic_needed or magic_input == "Meem")):
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.session_state.attempts += 1
                st.session_state.press_times = []
        st.stop()

check_access()

# --- ৩. মেইন অ্যাপ সেটআপ ---
st.set_page_config(page_title="BaraQura V10 Engine", layout="wide")
engine = BaraQuraEngine(db, os.getenv("GEMINI_API_KEY"))

st.sidebar.title("🛡️ BaraQura Control Panel")
menu = st.sidebar.radio("নেভিগেশন", ["🤖 চ্যাট টেস্ট", "📈 লিড ড্যাশবোর্ড", "🧠 এআই মেমোরি", "💻 Developer Console"])

# --- ৪. ফিচার ইমপ্লিমেন্টেশন ---

if menu == "🤖 চ্যাট টেস্ট":
    st.header("Selling Machine AI Test")
    user_id = st.text_input("User ID", "test_user_01")
    
    # অটো নাম লজিক
    db.cursor.execute("SELECT name FROM users WHERE user_id = ?", (user_id,))
    res = db.cursor.fetchone()
    auto_name = res[0] if res else "Customer"
    user_name = st.text_input("User Name", auto_name)

    user_msg = st.text_area("Message")
    if st.button("Send Message"):
        response = engine.generate_response(user_id, user_name, user_msg)
        st.info(f"**BaraQura AI:** {response}")
        # নতুন ইউজার হলে নাম সেভ করা
        if user_name != "Customer":
            db.cursor.execute("INSERT OR REPLACE INTO users (user_id, name) VALUES (?, ?)", (user_id, user_name))
            db.conn.commit()

elif menu == "💻 Developer Console":
    st.header("Developer Console: Live File Editor")
    
    # প্রজেক্টের সব ফাইল ড্রপডাউনে আনা
    all_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith((".py", ".env", ".txt")):
                all_files.append(os.path.join(root, file))
    
    target_file = st.selectbox("ফাইল সিলেক্ট কর:", all_files)
    
    if target_file:
        with open(target_file, "r", encoding="utf-8") as f:
            code_content = f.read()
        
        edited_code = st.text_area(f"Editing: {target_file}", value=code_content, height=500)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 Save & Update"):
                with open(target_file, "w", encoding="utf-8") as f:
                    f.write(edited_code)
                st.success("ফাইল আপডেট হয়েছে! সিস্টেম রিবুট হচ্ছে...")
                time.sleep(1)
                st.rerun()
        with col2:
            if st.button("🔍 Check Errors"):
                try:
                    compile(edited_code, target_file, 'exec')
                    st.success("কোড ঠিক আছে!")
                except Exception as e:
                    st.error(f"কোডে ভুল আছে: {e}")

# বাকি মেনুগুলো (লিড ড্যাশবোর্ড ও মেমোরি) তোর আগের মতোই থাকবে
if menu == "চ্যাট টেস্ট":
    st.header("🤖 AI Chatbot Test (The Selling Machine)")
    
    # ইউজার আইডি থেকে নাম অটো-ফেচিং লজিক
    user_id = st.text_input("User ID", "test_user_01")
    
    # ডাটাবেসে নাম খোঁজা
    db.cursor.execute("SELECT name FROM users WHERE user_id = ?", (user_id,))
    user_row = db.cursor.fetchone()
    auto_name = user_row[0] if user_row else "Customer"
    
    user_name = st.text_input("User Name", auto_name)

    with st.form("chat_form"):
        user_msg = st.text_area("Message")
        submit = st.form_submit_button("Send Message")

    if submit and user_msg:
        response = engine.generate_response(user_id, user_name, user_msg)
        st.info(f"**BaraQura AI:** {response}")
        st.success("রেসপন্স জেনারেট হয়েছে।")

elif menu == "লিড ড্যাশবোর্ড":
    st.header("📈 Sales Leads & Scoring")
    db.cursor.execute("SELECT * FROM users ORDER BY score DESC")
    leads = db.cursor.fetchall()
    if leads: st.table(leads)
    else: st.warning("ডেটা নেই।")

elif menu == "এআই মেমোরি রিভিউ":
    st.header("🧠 AI Learning Loop")
    db.cursor.execute("SELECT id, question, answer FROM brain_memory WHERE is_verified = 0")
    pending_items = db.cursor.fetchall()
    if not pending_items: st.success("সব ভেরিফাইড!")
    for item in pending_items:
        with st.expander(f"Q: {item[1]}"):
            st.write(f"Proposed A: {item[2]}")
            if st.button(f"Approve ID: {item[0]}", key=f"btn_{item[0]}"):
                db.cursor.execute("UPDATE brain_memory SET is_verified = 1 WHERE id = ?", (item[0],))
                db.conn.commit()
                st.rerun()
