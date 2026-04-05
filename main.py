import streamlit as st
import os
import time
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

# ১. কোর সেটআপ ও সেশন লোড
load_dotenv()
db = DBManager()

if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'auth_step' not in st.session_state: st.session_state.auth_step = 1
if 'system_status' not in st.session_state: st.session_state.system_status = "ACTIVE"
if 'start_time' not in st.session_state: st.session_state.start_time = time.time()

# --- ২. সিকিউরিটি গেটওয়ে (Fixed Logic) ---
def check_access():
    if not st.session_state.authenticated:
        st.title("🛡️ BaraQura Universe Access")
        
        # ব্ল্যাক হোল কন্ডিশন
        if st.session_state.system_status == "KILLED":
            st.error("🌌 SYSTEM ABSORBED BY BLACK HOLE.")
            st.stop()

        step = st.session_state.auth_step
        st.info(f"Verification Stage: {step} of 3")

        # ফরমের ভেতরে ইনপুট (যাতে ডাটা না হারায়)
        with st.form(key=f"auth_v10_step_{step}"):
            if step < 3:
                l_key = st.text_input("Enter Leader Key", type="password")
                s_tok = st.text_input("Enter Special Token", type="password")
            else:
                s_key = st.text_input("Enter Strong Key", type="password")
                s_tok = st.text_input("Enter Special Token", type="password")
            
            if st.form_submit_button("Verify & Proceed"):
                # বানান ও স্পেস চেক
                k_clean = l_key.strip() if step < 3 else s_key.strip()
                t_clean = s_tok.strip()

                valid = False
                if step < 3:
                    if k_clean == "V8_UNIVERSE_GOD_2026" and t_clean == "Meem":
                        valid = True
                else:
                    if k_clean == "Meem#8.10" and t_clean == "Meem":
                        valid = True

                if valid:
                    if step == 3:
                        st.session_state.authenticated = True
                        st.balloons()
                    else:
                        st.session_state.auth_step += 1
                    st.rerun()
                else:
                    st.error("Invalid Credentials! Check Spelling.")
        st.stop()

check_access()

# --- ৩. মেইন ইউনিভার্স ড্যাশবোর্ড (Old Features) ---
st.set_page_config(page_title="BaraQura V10 Full", layout="wide")
engine = BaraQuraEngine(db, os.getenv("GEMINI_API_KEY"))

# ড্যাশবোর্ড ক্যালকুলেশন
elapsed = int(time.time() - st.session_state.start_time)
mins, secs = divmod(elapsed, 60)
db.cursor.execute("SELECT COUNT(*) FROM users")
customer_count = db.cursor.fetchone()[0]

# সাইডবার মাস্টার কন্ট্রোল
st.sidebar.title("🛡️ Master Control Panel")
with st.sidebar.expander("📡 System Pulse", expanded=True):
    st.write(f"**Status:** {st.session_state.system_status}")
    st.write(f"**Active Time:** {mins}m {secs}s")
    st.write(f"**Leads:** {customer_count}")
    load_val = 5 + (customer_count * 2)
    st.write(f"**System Load:** {load_val}%")
    st.progress(min(load_val, 100))

if st.sidebar.button("Logout & Lock"):
    st.session_state.authenticated = False
    st.session_state.auth_step = 1
    st.rerun()

# মেইন ইন্টারফেস
menu = st.sidebar.radio("Navigation", ["🤖 AI Chat Test", "📊 Database", "💻 Console"])

if menu == "🤖 AI Chat Test":
    st.header("BaraQura Selling Machine")
    u_id = st.text_input("User ID", "guest_01")
    msg = st.text_area("Master Message")
    if st.button("Send to Engine"):
        res = engine.generate_response(u_id, "Master", msg)
        st.info(f"AI Response: {res}")

elif menu == "📊 Database":
    st.header("Lead Generation Logs")
    # ডাটাবেজ থেকে তথ্য দেখানোর কোড এখানে...
    st.write("Fetching records from BaraQura DB...")
