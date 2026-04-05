import streamlit as st
import os
import time

# ১. সেশন সেটআপ (একদম সিম্পল)
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- ২. সিকিউরিটি চেক ---
if not st.session_state.authenticated:
    st.title("🛡️ BaraQura Universe Access")
    
    curr = st.session_state.step
    st.info(f"Step {curr} of 3")

    # ফর্মের ঝামেলা এড়িয়ে সরাসরি ইনপুট
    if curr < 3:
        key_in = st.text_input("Leader Key", type="password", key=f"lk_{curr}")
        tok_in = st.text_input("Special Token", type="password", key=f"st_{curr}")
    else:
        key_in = st.text_input("Strong Key", type="password", key="sk_final")
        tok_in = st.text_input("Special Token", type="password", key="st_final")

    if st.button("Verify & Proceed"):
        # ইনপুট ক্লিন করা
        k = key_in.strip()
        t = tok_in.strip()

        if curr < 3:
            if k == "V8_UNIVERSE_GOD_2026" and t == "Meem":
                st.session_state.step += 1
                st.rerun()
            else:
                st.error("ভুল হয়েছে! বানান চেক কর।")
        else:
            if k == "Meem#8.10" and t == "Meem":
                st.session_state.authenticated = True
                st.balloons()
                st.rerun()
            else:
                st.error("Strong Key মেলেনি!")
    st.stop()

# --- ৩. মেইন ড্যাশবোর্ড ---
st.success("স্বাগতম মাস্টার! আপনি এখন ইউনিভার্সে আছেন।")
if st.button("Logout"):
    st.session_state.authenticated = False
    st.session_state.step = 1
    st.rerun()
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
