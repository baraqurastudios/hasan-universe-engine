import streamlit as st
import os
import sys
import json
import time

# ১. পাথ কনফিগারেশন (core ফোল্ডারকে চেনানো)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'core'))

# ২. মডিউল ইমপোর্ট
try:
    from engine import Engine
except ImportError:
    st.error("Engine module not found in core folder!")

# ৩. পেজ সেটআপ
st.set_page_config(page_title="BaraQura V8.2 Dashboard", layout="wide")

# ৪. সেশন স্টেট (ডাটা মনে রাখার জন্য)
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'engine_active' not in st.session_state:
    st.session_state.engine_active = False

# --- ইন্টারফেস লজিক ---
if not st.session_state.authenticated:
    st.title("🤖 BaraQura V8.2: Terminal Access")
    master_key_input = st.text_input("Enter Master Key:", type="password")
    
    if st.button("🚀 Unlock System"):
        config_path = "config/v82_config.json"
        try:
            with open(config_path, 'r') as f:
                data = json.load(f)
                if master_key_input == data['security_layer']['master_key_hash']:
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Access Denied!")
        except Exception as e:
            st.error(f"Error: {e}")

else:
    # ড্যাশবোর্ড শুরু
    st.title("🔓 BaraQura System Online")
    
    # টপ ম্যাট্রিক্স (আপনার প্রফিট এবং নোড)
    try:
        with open("config/v82_config.json", 'r') as f:
            data = json.load(f)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Profit", f"${data['empire_assets']['total_profit']:,}")
        c2.metric("Active Nodes", data['empire_assets']['active_nodes'])
        c3.metric("System Status", "ACTIVE" if st.session_state.engine_active else "IDLE")
    except:
        pass

    st.markdown("---")

    # --- ইঞ্জিন কন্ট্রোল সেকশন ---
    col_cmd, col_log = st.columns([1, 2])

    with col_cmd:
        st.subheader("🕹️ Core Control")
        if st.button("⚡ POWER ON ENGINE", use_container_width=True):
            st.session_state.engine_active = True
            # লগ জেনারেট করা
            st.session_state.logs.append(">>> Initializing BaraQura Engine V8.2...")
            st.session_state.logs.append(">>> Security Handshake: COMPLETE")
            st.session_state.logs.append(">>> Loading Neural Assets...")
            st.session_state.logs.append(">>> System Status: ONLINE")
            
        if st.button("🛑 SHUTDOWN", use_container_width=True):
            st.session_state.engine_active = False
            st.session_state.logs.append(">>> Shutting down systems safely...")
            st.session_state.logs.append(">>> Engine Offline.")

    with col_log:
        st.subheader("📜 System Logs")
        # লগ বক্স (ডার্ক স্টাইল)
        log_text = "\n".join(st.session_state.logs[-10:]) # শেষ ১০টি লগ দেখাবে
        st.code(log_text if log_text else "Waiting for command...", language="bash")

    if st.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()
