import streamlit as st
import os
import sys

# সরাসরি পাথ সেটআপ (যাতে এরর না হয়)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'core'))
sys.path.append(os.path.join(BASE_DIR, 'security'))

# মডিউল লোড করার নিরাপদ পদ্ধতি
try:
    from engine import Engine
    from guardian import SecurityManager
except Exception as e:
    st.error(f"মডিউল লোড এরর: {e}")
    st.stop()

# সেশন স্টেট
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

st.set_page_config(page_title="BaraQura V8.2", layout="wide")

if not st.session_state.authenticated:
    st.title("🤖 BaraQura V8.2")
    user_key = st.text_input("Enter Master Key:", type="password")
    
    if st.button("🚀 Login"):
        guardian = SecurityManager()
        engine = Engine()
        
        if guardian.validate(user_key):
            result = engine.process(user_key)
            if "🔓" in result:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error(result)
        else:
            st.error("🚫 Access Denied!")

else:
    st.success("🔓 স্বাগতম মাস্টার!")
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()
