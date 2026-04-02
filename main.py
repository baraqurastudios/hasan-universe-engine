import streamlit as st
import os
import sys
import json

# --- ১. পাথ কনফিগারেশন ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# ফোল্ডারগুলো পাথে যুক্ত করা যাতে ইমপোর্ট এরর না হয়
for folder in ['core', 'security']:
    folder_path = os.path.join(BASE_DIR, folder)
    if folder_path not in sys.path:
        sys.path.insert(0, folder_path)

# --- ২. মডিউল ইমপোর্ট ---
try:
    from engine import Engine
    from guardian import SecurityManager
except ImportError:
    # ব্যাকআপ ইমপোর্ট লজিক
    from core.engine import Engine
    from security.guardian import SecurityManager

# --- ৩. সেশন স্টেট ইনিশিয়ালাইজেশন ---
# এটি ব্ল্যাক স্ক্রিন প্রতিরোধের জন্য সবচেয়ে গুরুত্বপূর্ণ অংশ
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if 'core_initialized' not in st.session_state:
    st.session_state.core = Engine()
    st.session_state.security = SecurityManager()
    st.session_state.core_initialized = True

# --- ৪. ইউজার ইন্টারফেস ---
st.set_page_config(page_title="BaraQura V8.2", layout="wide")

# যদি ইউজার লগইন করা না থাকে
if not st.session_state.authenticated:
    st.title("🤖 BaraQura V8.2: Omni-Intelligence")
    st.markdown("---")
    
    # ইনপুট ফিল্ড
    user_key = st.text_input("Enter Master Command / Key:", type="password", key="login_key")
    
    if st.button("🚀 Run Command"):
        if st.session_state.security.validate(user_key):
            result = st.session_state.core.process(user_key)
            
            if "🔓" in result:
                st.session_state.authenticated = True
                st.rerun() # সেশন স্ট্যাটাস আপডেট করে পেজ রিফ্রেশ করবে
            else:
                st.error(result)
        else:
            st.error("🚫 Access Denied!")

# ৫. মেইন ড্যাশবোর্ড (লগইন করার পর যা দেখাবে)
else:
    st.success("🔓 স্বাগতম মাস্টার! BaraQura সিস্টেম এখন অনলাইন।")
    
    # ড্যাশবোর্ড ডাটা লোড করা
    try:
        config_path = os.path.join(BASE_DIR, "config", "v82_config.json")
        with open(config_path, 'r') as f:
            config_data = json.load(f)
        
        # আপনার empire_assets ডাটা দেখানো
        st.subheader("📊 Empire Dashboard")
        col1, col2 = st.columns(2)
        col1.metric("Total Profit", f"${config_data['empire_assets']['total_profit']}")
        col2.metric("Active Nodes", config_data['empire_assets']['active_nodes'])
        
        st.markdown("---")
        if st.button("🔴 Logout"):
            st.session_state.authenticated = False
            st.rerun()
            
    except Exception as e:
        st.error(f"Error loading dashboard: {e}")
