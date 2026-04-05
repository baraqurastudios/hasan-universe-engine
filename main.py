import streamlit as st
import os
import time
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

# ১. এনভায়রনমেন্ট লোড করা
load_dotenv()

# ডাটাবেস কানেকশন গ্লোবালি সেট করা
db = DBManager()

# --- ২. আল্ট্রা সিকিউরিটি (Black Hole + Rhythm + Case-Sensitive Meem) ---
def check_access():
    # ব্ল্যাক হোল/কিল সুইচ চেক
    if st.session_state.get('system_status') == "KILLED":
        st.error("⚠️ SYSTEM TERMINATED BY MASTER. ENGINE IS ABSORBED BY BLACK HOLE.")
        revive_key = st.text_input("Enter Emergency Master Key (Meen#8.10) to Revive", type="password")
        if st.button("Revive Engine"):
            if revive_key == "Meen#8.10":
                st.session_state.system_status = "ACTIVE"
                st.session_state.attempts = 0
                st.success("Engine Revived! Restarting...")
                st.rerun()
        st.stop()

    # সেশন স্টেট ট্র্যাকিং
    if 'attempts' not in st.session_state: st.session_state.attempts = 0
    if 'authenticated' not in st.session_state: st.session_state.authenticated = False
    if 'press_times' not in st.session_state: st.session_state.press_times = []

    if not st.session_state.get('authenticated', False):
        st.title("🛡️ BaraQura Universe Access")
        
        # ধাপ ১: রিদমিক ট্যাপ
        st.subheader("Step 1: Identity Rhythm")
        if st.button("🔴 TAP RHYTHM HERE"):
            st.session_state.press_times.append(time.time())
            st.toast(f"Input recorded")

        # ধাপ ২: অথরাইজেশন
        st.subheader("Step 2: Authorization")
        key_input = st.text_input(f"Enter Master Key (Attempts: {st.session_state.attempts}/3)", type="password")

        taps = st.session_state.press_times
        intervals = [taps[i] - taps[i-1] for i in range(1, len(taps))]
        
        rhythm_granted = False
        if len(taps) == 3: # মোবাইল ২-১
            if intervals[0] < 0.5 and intervals[1] > 1.0: rhythm_granted = True
        elif len(taps) == 6: # ল্যাপটপ ৩-২-১
            if all(i < 0.5 for i in intervals[:2]) and all(i > 1.0 for i in intervals[2:5]): rhythm_granted = True

        # মেম লজিক (সন্দেহ বা ৩ বার ভুলের পর)
        magic_word_needed = (len(taps) > 0 and not rhythm_granted) or st.session_state.attempts >= 3
        magic_input = ""
        if magic_word_needed:
            st.warning("⚠️ Identity Suspicion! Case-Sensitive Magic Word Required.")
            magic_input = st.text_input("Confirm Magic Word (Meem)", type="password")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Verify & Unlock Engine"):
                # হ্যাকার প্রোটেকশন
                if st.session_state.attempts >= 3:
                    if not rhythm_granted:
                        st.session_state.system_status = "KILLED"
                        st.rerun()
                
                # এক্সেস ভেরিফিকেশন
                if rhythm_granted and key_input == "Meen#8.10":
                    st.session_state.authenticated = True
                    st.rerun()
                elif key_input == "V8_UNIVERSE_GOD_2026":
                    if magic_word_needed:
                        if magic_input == "Meem":
                            st.session_state.authenticated = True
                            st.rerun()
                        else:
                            st.session_state.attempts += 1
                    else:
                        st.session_state.authenticated = True
                        st.rerun()
                else:
                    st.session_state.attempts += 1
                    st.session_state.press_times = []
        
        with col2:
            if st.button("💀 ACTIVATE KILL SWITCH"):
                if key_input in ["V8_UNIVERSE_GOD_2026", "Meen#8.10"]:
                    st.session_state.system_status = "KILLED"
                    st.rerun()
        st.stop()

check_access()

# --- ৩. মেইন ইঞ্জিন সেটআপ ---
st.set_page_config(page_title="BaraQura V10 Engine", layout="wide")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
engine = BaraQuraEngine(db, GEMINI_API_KEY)

st.sidebar.title("🛡️ BaraQura Control Panel")
menu = st.sidebar.radio("নেভিগেশন", ["চ্যাট টেস্ট", "লিড ড্যাশবোর্ড", "এআই মেমোরি রিভিউ"])

# ৪. ফিচার ইমপ্লিমেন্টেশন
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
