import streamlit as st
import os
import time
from datetime import datetime
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

# ১. প্রাথমিক সেটআপ ও সেশন ম্যানেজমেন্ট
load_dotenv()
db = DBManager()

if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'step' not in st.session_state: st.session_state.step = 1
if 'start_time' not in st.session_state: st.session_state.start_time = time.time()
if 'system_status' not in st.session_state: st.session_state.system_status = "ACTIVE"
if 'sleep_until' not in st.session_state: st.session_state.sleep_until = 0
if 'wrong_attempts' not in st.session_state: st.session_state.wrong_attempts = 0

# --- ২. সিকিউরিটি গেটওয়ে লজিক (The Final Loop) ---
def check_access():
    # ক. স্লিপিং মোড (Hold System)
    if st.session_state.sleep_until > time.time():
        remaining = int(st.session_state.sleep_until - time.time())
        st.warning(f"💤 SYSTEM ON HOLD. Re-activating in {remaining} seconds...")
        st.stop()

    # খ. ব্ল্যাক হোল রিভাইভ (Recovery)
    if st.session_state.system_status == "KILLED":
        st.error("🌌 SYSTEM ABSORBED BY BLACK HOLE.")
        st.subheader("Recovery Console (Need 2/3 Correct Keys)")
        rk1 = st.text_input("Leader Key (Revive)", type="password", key="rk1")
        rk2 = st.text_input("Strong Key (Revive)", type="password", key="rk2")
        rk3 = st.text_input("Special Token (Revive)", type="password", key="rk3")
        
        if st.button("Attempt Revival"):
            correct = 0
            if rk1 == "V8_UNIVERSE_GOD_2026": correct += 1
            if rk2 == "Meem#8.10": correct += 1
            if rk3 == "Meem": correct += 1
            if correct >= 2:
                st.session_state.system_status = "ACTIVE"
                st.session_state.step = 1
                st.session_state.wrong_attempts = 0
                st.success("Engine Revived! Restarting...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Revival Failed. Try Again.")
        st.stop()

    # গ. ৩-স্টেপ ডাইনামিক সিকিউরিটি লুপ (Fixed)
    if not st.session_state.authenticated:
        st.title("🛡️ BaraQura Universe Access")
        
        if st.session_state.wrong_attempts >= 2:
            st.markdown("<h2 style='color:red; text-align:center;'>🚨 HACKER ALERT: UNAUTHORIZED ACCESS! 🚨</h2>", unsafe_allow_html=True)

        current_step = st.session_state.step
        st.info(f"Identity Verification: Step {current_step} of 3")

        # ফর্ম ব্যবহার করা হয়েছে যাতে সাবমিট করার আগে ডেটা না হারায়
        with st.form(key=f"auth_step_{current_step}"):
            if current_step < 3:
                l_key = st.text_input("Enter Leader Key", type="password")
                s_token = st.text_input("Enter Special Token", type="password")
                s_key = None
            else:
                s_key = st.text_input("Enter Strong Key", type="password")
                s_token = st.text_input("Enter Special Token", type="password")
                l_key = None
            
            submit = st.form_submit_button("Verify & Proceed")

            if submit:
                is_valid = False
                if current_step < 3:
                    if l_key == "V8_UNIVERSE_GOD_2026" and s_token == "Meem":
                        is_valid = True
                else: # Step 3
                    if s_key == "Meem#8.10" and s_token == "Meem":
                        is_valid = True

                if is_valid:
                    if current_step == 3:
                        st.session_state.authenticated = True
                        st.balloons()
                        st.success("Access Granted! Loading Universe...")
                        time.sleep(1.5)
                        st.rerun()
                    else:
                        st.session_state.step += 1
                        st.success(f"Step {current_step} Verified.")
                        time.sleep(1)
                        st.rerun()
                else:
                    st.session_state.wrong_attempts += 1
                    if st.session_state.wrong_attempts >= 3:
                        st.session_state.system_status = "KILLED"
                    st.error("Invalid Credentials! Try Again.")
                    time.sleep(1)
                    st.rerun()
        st.stop()

check_access()

# --- ৩. মেইন ড্যাশবোর্ড (অ্যাপ কন্টেন্ট) ---
st.set_page_config(page_title="BaraQura V10 Final", layout="wide")
engine = BaraQuraEngine(db, os.getenv("GEMINI_API_KEY"))

# ড্যাশবোর্ড ডেটা ক্যালকুলেশন
elapsed = int(time.time() - st.session_state.start_time)
mins, secs = divmod(elapsed, 60)
db.cursor.execute("SELECT COUNT(*) FROM users")
customer_count = db.cursor.fetchone()[0]

# --- সাইডবার মাস্টার কন্ট্রোল ---
st.sidebar.title("🛡️ BaraQura Command Center")

with st.sidebar.expander("📡 System Pulse & Status", expanded=True):
    st.write(f"**Status:** {st.session_state.system_status}")
    st.write(f"**Active Time:** {mins}m {secs}s")
    st.write(f"**Total Conversations:** {customer_count}")
    
    # লোড ব্রেকডাউন (Old logic + New scaling)
    load_val = 5 + (customer_count * 2)
    st.write(f"**System Load:** {load_val}%")
    st.progress(min(load_val, 100))
    st.caption(f"Breakdown: AI Core (5%) + Active Chats ({customer_count * 2}%)")

with st.sidebar.expander("🌙 Sleep Mode Setup"):
    s_mins = st.number_input("Set Hold Time (Mins)", min_value=1, value=5)
    if st.sidebar.button("Activate Sleep Mode"):
        st.session_state.sleep_until = time.time() + (s_mins * 60)
        st.rerun()

if st.sidebar.button("🚪 Logout & Exit", use_container_width=True):
    st.session_state.authenticated = False
    st.session_state.step = 1
    st.rerun()

menu = st.sidebar.radio("Navigation", ["🤖 চ্যাট টেস্ট", "📊 লিড ড্যাশবোর্ড", "💻 Developer Console"])

# ফিচার ইমপ্লিমেন্টেশন
if menu == "🤖 চ্যাট টেস্ট":
    st.header("BaraQura Selling Machine")
    u_id = st.text_input("Target User ID", "user_99")
    u_msg = st.text_area("Your Message")
    if st.button("Execute AI Response"):
        res = engine.generate_response(u_id, "Master", u_msg)
        st.info(f"AI: {res}")
        st.balloons()

elif menu == "💻 Developer Console":
    st.header("Universe Developer Console")
    # ডেভেলপার কনসোল লজিক এখানে থাকবে...
    st.write("File System: /core, /security, /database")
# --- ৩. মেইন অ্যাপ ড্যাশবোর্ড ---
st.set_page_config(page_title="BaraQura V10 Final", layout="wide")
engine = BaraQuraEngine(db, os.getenv("GEMINI_API_KEY"))

# সেশন টাইমার ও কাস্টমার কাউন্ট
elapsed_time = int(time.time() - st.session_state.start_time)
mins, secs = divmod(elapsed_time, 60)
db.cursor.execute("SELECT COUNT(*) FROM users")
customer_count = db.cursor.fetchone()[0]

st.sidebar.title("🛡️ BaraQura Control Panel")

with st.sidebar.expander("📡 System Pulse & Status", expanded=True):
    st.write(f"**Status:** {st.session_state.system_status}")
    st.write(f"**Active Time:** {mins}m {secs}s")
    st.write(f"**Conversations:** {customer_count}")
    base_load = 5 + (customer_count * 2)
    st.write(f"**System Load:** {base_load}%")
    st.progress(min(base_load, 100))

with st.sidebar.expander("🌙 Sleep Mode Setup"):
    sleep_mins = st.number_input("Minutes", min_value=1, value=5)
    if st.button("Activate Sleep"):
        st.session_state.sleep_until = time.time() + (sleep_mins * 60)
        st.rerun()

if st.sidebar.button("🚪 Logout & Exit", use_container_width=True):
    st.session_state.authenticated = False
    st.session_state.attempts = 0
    st.rerun()

menu = st.sidebar.radio("Navigation", ["🤖 চ্যাট টেস্ট", "📈 ড্যাশবোর্ড", "💻 Developer Console"])

# চ্যাট টেস্ট ও অন্যান্য ফিচার আগের মতোই থাকবে...
if menu == "🤖 চ্যাট টেস্ট":
    st.header("BaraQura AI Chat")
    u_id = st.text_input("User ID", "test_01")
    msg = st.text_area("Message")
    if st.button("Send"):
        res = engine.generate_response(u_id, "Master", msg)
        st.info(f"AI: {res}")
        st.balloons()
import streamlit as st
import os
import time
import random
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

# ১. এনভায়রনমেন্ট ও সেশন সেটআপ
load_dotenv()
db = DBManager()

# সেশন স্টেট ইনিশিয়ালাইজেশন
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'attempts' not in st.session_state: st.session_state.attempts = 0
if 'start_time' not in st.session_state: st.session_state.start_time = time.time()
if 'system_status' not in st.session_state: st.session_state.system_status = "ACTIVE"
if 'sleep_until' not in st.session_state: st.session_state.sleep_until = 0

# --- ২. আল্ট্রা সিকিউরিটি লজিক (The Loop & Black Hole) ---
def check_access():
    # ক. স্লিপিং মোড চেক
    current_time = time.time()
    if st.session_state.sleep_until > current_time:
        remaining = int(st.session_state.sleep_until - current_time)
        st.warning(f"💤 System is in SLEEP MODE. Re-activating in {remaining} seconds...")
        st.stop()

    # খ. ব্ল্যাক হোল ও রিভাইভ লজিক
    if st.session_state.system_status == "KILLED":
        st.error("🌌 SYSTEM ABSORBED BY BLACK HOLE.")
        st.subheader("Black Hole Recovery (Provide any 2 correct keys)")
        rk1 = st.text_input("Leader Key (Revive)", type="password", key="rev_lk")
        rk2 = st.text_input("Strong Key (Revive)", type="password", key="rev_sk")
        rk3 = st.text_input("Special Token (Revive)", type="password", key="rev_st")
        
        if st.button("Attempt Revival"):
            correct_count = 0
            if rk1 == "V8_UNIVERSE_GOD_2026": correct_count += 1
            if rk2 == "Meem#8.10": correct_count += 1
            if rk3 == "Meem": correct_count += 1
            
            if correct_count >= 2:
                st.session_state.system_status = "ACTIVE"
                st.session_state.attempts = 0
                st.success("Engine Revived! Restarting...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Revival Failed.")
        st.stop()

    # গ. ৩-স্টেপ সিকিউরিটি লুপ (Fixed Logics)
    if not st.session_state.authenticated:
        st.title("🛡️ BaraQura Universe Access")
        
        # হ্যাকার অ্যালার্ট
        if st.session_state.attempts >= 2:
            st.markdown("<h2 style='color:red; text-align:center;'>🚨 HACKER ALERT: UNAUTHORIZED ACCESS! 🚨</h2>", unsafe_allow_html=True)

        step = st.session_state.attempts + 1
        st.info(f"Identity Verification: Step {step} of 3")
        
        # স্টেপ অনুযায়ী ডাইনামিক বক্স
        if step == 1 or step == 2:
            l_key = st.text_input("Enter Leader Key", type="password", key=f"lk_{step}")
            s_token = st.text_input("Enter Special Token", type="password", key=f"st_{step}")
            s_key = None
        else: # Step 3
            s_key = st.text_input("Enter Strong Key", type="password", key="sk_3")
            s_token = st.text_input("Enter Special Token", type="password", key="st_3")
            l_key = None

        if st.button("Verify Identity"):
            is_valid = False
            # লজিক ভেরিফিকেশন
            if step < 3:
                if l_key == "V8_UNIVERSE_GOD_2026" and s_token == "Meem":
                    is_valid = True
            else: # Step 3 logic
                if s_key == "Meem#8.10" and s_token == "Meem":
                    is_valid = True

            if is_valid:
                if step == 3:
                    st.session_state.authenticated = True
                    st.balloons()
                    st.success("Access Granted! Loading Universe...")
                    time.sleep(1.5)
                    st.rerun()
                else:
                    st.session_state.attempts = step # ধাপ বাড়িয়ে দেওয়া
                    st.success(f"Step {step} Verified. Proceeding...")
                    time.sleep(1)
                    st.rerun()
            else:
                st.session_state.attempts += 1
                if st.session_state.attempts >= 3:
                    st.session_state.system_status = "KILLED"
                st.error("Invalid Credentials!")
                time.sleep(1)
                st.rerun()
        st.stop()

check_access()

# --- ৩. মেইন অ্যাপ ড্যাশবোর্ড ---
st.set_page_config(page_title="BaraQura V10 Final", layout="wide")
engine = BaraQuraEngine(db, os.getenv("GEMINI_API_KEY"))

# সেশন টাইমার ও কাস্টমার কাউন্ট
elapsed_time = int(time.time() - st.session_state.start_time)
mins, secs = divmod(elapsed_time, 60)
db.cursor.execute("SELECT COUNT(*) FROM users")
customer_count = db.cursor.fetchone()[0]

st.sidebar.title("🛡️ BaraQura Control Panel")

with st.sidebar.expander("📡 System Pulse & Status", expanded=True):
    st.write(f"**Status:** {st.session_state.system_status}")
    st.write(f"**Active Time:** {mins}m {secs}s")
    st.write(f"**Conversations:** {customer_count}")
    base_load = 5 + (customer_count * 2)
    st.write(f"**System Load:** {base_load}%")
    st.progress(min(base_load, 100))

with st.sidebar.expander("🌙 Sleep Mode Setup"):
    sleep_mins = st.number_input("Minutes", min_value=1, value=5)
    if st.button("Activate Sleep"):
        st.session_state.sleep_until = time.time() + (sleep_mins * 60)
        st.rerun()

if st.sidebar.button("🚪 Logout & Exit", use_container_width=True):
    st.session_state.authenticated = False
    st.session_state.attempts = 0
    st.rerun()

menu = st.sidebar.radio("Navigation", ["🤖 চ্যাট টেস্ট", "📈 ড্যাশবোর্ড", "💻 Developer Console"])

# চ্যাট টেস্ট ও অন্যান্য ফিচার আগের মতোই থাকবে...
if menu == "🤖 চ্যাট টেস্ট":
    st.header("BaraQura AI Chat")
    u_id = st.text_input("User ID", "test_01")
    msg = st.text_area("Message")
    if st.button("Send"):
        res = engine.generate_response(u_id, "Master", msg)
        st.info(f"AI: {res}")
        st.balloons()
    st.sidebar.title("🛡️ BaraQura Master Control")

with st.sidebar.expander("📡 System Pulse & Live Status", expanded=True):
    st.write(f"**Status:** {st.session_state.system_status}")
    st.write(f"**Active Time:** {mins}m {secs}s")
    st.write(f"**Conversations:** {customer_count}")
    base_load = 5 + (customer_count * 2)
    st.write(f"**System Load:** {base_load}%")
    st.progress(min(base_load, 100))

with st.sidebar.expander("🌙 Sleep Mode Setup"):
    sleep_mins = st.number_input("Sleep Time (Mins)", min_value=1, value=5)
    if st.button("Activate Sleep"):
        st.session_state.sleep_until = time.time() + (sleep_mins * 60)
        st.rerun()

menu = st.sidebar.radio("Navigation", ["🤖 চ্যাট টেস্ট", "📈 লিড ড্যাশবোর্ড", "💻 Developer Console"])

if st.sidebar.button("🚪 Logout & Exit", use_container_width=True):
    st.session_state.authenticated = False
    st.rerun()

# --- ৪. ফিচার ইমপ্লিমেন্টেশন ---
if menu == "🤖 চ্যাট টেস্ট":
    st.header("Selling Machine AI")
    user_id = st.text_input("User ID", "user_101")
    user_msg = st.text_area("Message")
    if st.button("Send Message"):
        response = engine.generate_response(user_id, "Master", user_msg)
        st.info(f"AI: {response}")
        st.balloons()

elif menu == "💻 Developer Console":
    st.header("Developer Console")
    all_files = [f for f in os.listdir(".") if f.endswith((".py", ".env"))]
    target_file = st.selectbox("Select File", all_files)
    if target_file:
        with open(target_file, "r") as f: content = f.read()
        edited = st.text_area("Edit Code", value=content, height=400)
        if st.button("💾 Save & Update"):
            try:
                compile(edited, target_file, 'exec')
                with open(target_file, "w") as f: f.write(edited)
                st.balloons()
                st.success("Successfully Updated!")
            except Exception as e:
                st.error(f"Syntax Error: {e}")
with st.sidebar.expander("📡 System Pulse & Live Status", expanded=True):
    st.write(f"**Status:** {st.session_state.system_status}")
    st.write(f"**Active Time:** {mins}m {secs}s")
    st.write(f"**Conversations:** {customer_count}")
    base_load = 5 + (customer_count * 2)
    st.write(f"**System Load:** {base_load}%")
    st.progress(min(base_load, 100))

with st.sidebar.expander("🌙 Sleep Mode Setup"):
    sleep_mins = st.number_input("Sleep Time (Mins)", min_value=1, value=5)
    if st.button("Activate Sleep"):
        st.session_state.sleep_until = time.time() + (sleep_mins * 60)
        st.rerun()

menu = st.sidebar.radio("Navigation", ["🤖 চ্যাট টেস্ট", "📈 লিড ড্যাশবোর্ড", "💻 Developer Console"])

if st.sidebar.button("🚪 Logout & Exit", use_container_width=True):
    st.session_state.authenticated = False
    st.rerun()

# --- ৪. ফিচার ইমপ্লিমেন্টেশন ---
if menu == "🤖 চ্যাট টেস্ট":
    st.header("Selling Machine AI")
    user_id = st.text_input("User ID", "user_101")
    user_msg = st.text_area("Message")
    if st.button("Send Message"):
        response = engine.generate_response(user_id, "Master", user_msg)
        st.info(f"AI: {response}")
        st.balloons()

elif menu == "💻 Developer Console":
    st.header("Developer Console")
    all_files = [f for f in os.listdir(".") if f.endswith((".py", ".env"))]
    target_file = st.selectbox("Select File", all_files)
    if target_file:
        with open(target_file, "r") as f: content = f.read()
        edited = st.text_area("Edit Code", value=content, height=400)
        if st.button("💾 Save & Update"):
            try:
                compile(edited, target_file, 'exec')
                with open(target_file, "w") as f: f.write(edited)
                st.balloons()
                st.success("Successfully Updated!")
            except Exception as e:
                st.error(f"Syntax Error: {e}")

# --- সাইডবার কন্ট্রোল সেন্টার ---
st.sidebar.title("🛡️ BaraQura Master Control")

with st.sidebar.expander("📡 System Pulse & Live Status", expanded=True):
    st.write(f"**Status:** {st.session_state.system_status}")
    st.write(f"**Active Time:** {mins}m {secs}s")
    st.write(f"**Conversations:** {customer_count}")
    
    # লোড ব্রেকডাউন
    base_load = 5 + (customer_count * 2)
    st.write(f"**System Load:** {base_load}%")
    st.progress(min(base_load, 100))
    st.caption(f"Breakdown: AI Brain (5%) + Active Chats ({customer_count * 2}%)")

with st.sidebar.expander("🌙 Sleep Mode Setup"):
    sleep_mins = st.number_input("Sleep Time (Mins)", min_value=1, value=5)
    if st.button("Activate Sleep"):
        st.session_state.sleep_until = time.time() + (sleep_mins * 60)
        st.rerun()

menu = st.sidebar.radio("Navigation", ["🤖 চ্যাট টেস্ট", "📈 লিড ড্যাশবোর্ড", "💻 Developer Console"])

if st.sidebar.button("🚪 Logout & Exit", use_container_width=True):
    st.session_state.authenticated = False
    st.rerun()

# --- ৪. ফিচার ইমপ্লিমেন্টেশন ---
if menu == "🤖 চ্যাট টেস্ট":
    st.header("Selling Machine AI")
    user_id = st.text_input("User ID", "user_101")
    user_msg = st.text_area("Message")
    if st.button("Send Message"):
        response = engine.generate_response(user_id, "Master", user_msg)
        st.info(f"AI: {response}")
        st.balloons()

elif menu == "💻 Developer Console":
    st.header("Developer Console")
    all_files = [f for f in os.listdir(".") if f.endswith((".py", ".env"))]
    target_file = st.selectbox("Select File", all_files)
    if target_file:
        with open(target_file, "r") as f: content = f.read()
        edited = st.text_area("Edit Code", value=content, height=400)
        if st.button("💾 Save & Update"):
            try:
                compile(edited, target_file, 'exec')
                with open(target_file, "w") as f: f.write(edited)
                st.balloons()
                st.success("Successfully Updated!")
            except Exception as e:
                st.error(f"Syntax Error: {e}")
mins, secs = divmod(elapsed_time, 60)

# কাস্টমার কাউন্ট
db.cursor.execute("SELECT COUNT(*) FROM users")
customer_count = db.cursor.fetchone()[0]

# --- সাইডবার কন্ট্রোল সেন্টার ---
st.sidebar.title("🛡️ BaraQura Master Control")

# সিস্টেম পালস ও লোড ব্রেকডাউন
with st.sidebar.expander("📡 System Pulse & Live Status", expanded=True):
    st.write(f"**Status:** {st.session_state.system_status}")
    st.write(f"**Active Time:** {mins}m {secs}s")
    st.write(f"**Total Conversations:** {customer_count}")
    
    # লোড ব্রেকডাউন
    base_load = 5 + (customer_count * 2) # কাস্টমার বাড়লে লোড বাড়বে
    st.write(f"**System Load:** {base_load}%")
    st.progress(min(base_load, 100))
    st.caption(f"Breakdown: AI Brain (5%) + Active Chats ({customer_count * 2}%)")
    
    if st.session_state.attempts >= 2:
        st.error("🚨 RED ALERT: UNKNOWN USER DETECTED!")

# স্লিপিং মোড সেটআপ
with st.sidebar.expander("🌙 Sleep Mode Setup"):
    sleep_mins = st.number_input("Set Sleep Time (Minutes)", min_value=1, value=5)
    if st.button("Activate Sleep Mode"):
        st.session_state.sleep_until = time.time() + (sleep_mins * 60)
        st.rerun()

menu = st.sidebar.radio("Navigation", ["🤖 চ্যাট টেস্ট", "📈 লিড ড্যাশবোর্ড", "💻 Developer Console"])

if st.sidebar.button("🚪 Logout & Exit", use_container_width=True):
    st.session_state.authenticated = False
    st.rerun()

# --- ৪. ফিচার ইমপ্লিমেন্টেশন ---
if menu == "🤖 চ্যাট টেস্ট":
    st.header("Selling Machine AI")
    user_id = st.text_input("User ID", "user_101")
    user_msg = st.text_area("Message")
    if st.button("Send Message"):
        response = engine.generate_response(user_id, "Master", user_msg)
        st.info(f"AI: {response}")
        st.balloons()

elif menu == "💻 Developer Console":
    st.header("Developer Console")
    all_files = [f for f in os.listdir(".") if f.endswith((".py", ".env"))]
    target_file = st.selectbox("Select File", all_files)
    if target_file:
        with open(target_file, "r") as f: content = f.read()
        edited = st.text_area("Edit Code", value=content, height=400)
        if st.button("💾 Save & Update"):
            try:
                compile(edited, target_file, 'exec') # ৫ নম্বর পয়েন্ট: ভুল কোড নিবে না
                with open(target_file, "w") as f: f.write(edited)
                st.balloons()
                st.success("Successfully Updated!")
            except Exception as e:
                st.error(f"Syntax Error: {e}")
            code_content = f.read()
        
        edited_code = st.text_area(f"Editing: {target_file}", value=code_content, height=500)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 Save & Update"):
                with open(target_file, "w", encoding="utf-8") as f:
                    f.write(edited_code)
                st.success("ফাইল আপডেট হয়েছে!")
                time.sleep(1)
                st.rerun()
        with col2:
            if st.button("🔍 Check Errors"):
                try:
                    compile(edited_code, target_file, 'exec')
                    st.success("কোড ঠিক আছে!")
                except Exception as e:
                    st.error(f"কোডে ভুল আছে: {e}")

# বাকি মেনুগুলো (লিড ড্যাশবোর্ড ও মেমোরি)
elif menu == "📈 লিড ড্যাশবোর্ড":
    st.header("📈 Sales Leads & Scoring")
    db.cursor.execute("SELECT * FROM users ORDER BY score DESC")
    leads = db.cursor.fetchall()
    if leads: st.table(leads)
    else: st.warning("ডেটা নেই।")

elif menu == "🧠 এআই মেমোরি":
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
