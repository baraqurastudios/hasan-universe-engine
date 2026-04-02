import streamlit as st
import os
import sys
import logging
from datetime import datetime

# --- ১. পাথ সেটআপ ---
current_dir = os.path.dirname(os.path.abspath(__file__))
folders = ['security', 'core', 'database', 'interface', 'config']
for folder in folders:
    folder_path = os.path.join(current_dir, folder)
    if folder_path not in sys.path:
        sys.path.append(folder_path)

# --- ২. লগিং ---
if not os.path.exists('logs'): os.makedirs('logs')
logging.basicConfig(filename='logs/system.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# --- ৩. মডিউল ইমপোর্ট (সরাসরি পাথ থেকে) ---
try:
    from core.engine import Engine
    from database.db_manager import DatabaseManager
    from security.guardian import SecurityManager
    from interface.worker import Interface
except ImportError as e:
    # যদি সাধারণ ইমপোর্টে কাজ না হয়, তবে অল্টারনেটিভ পাথ ট্রাই করবে
    try:
        from engine import Engine
        from db_manager import DatabaseManager
        from guardian import SecurityManager
        from worker import Interface
    except Exception as inner_e:
        st.error(f"❌ Critical Module Missing: {e}")
        st.stop()

# --- ৪. UI কনফিগারেশন ---
st.set_page_config(page_title="BaraQura V8.2", page_icon="🤖", layout="wide")
st.title("🤖 BaraQura V8.2: The Omni-Intelligence") # টাইটেল পরিবর্তন করা হয়েছে
st.markdown("---")

# --- ৫. সেশন স্টেট ---
if 'initialized' not in st.session_state:
    try:
        st.session_state.security = SecurityManager()
        st.session_state.db = DatabaseManager()
        st.session_state.core = Engine()
        st.session_state.ui = Interface()
        st.session_state.initialized = True
    except Exception as e:
        st.error(f"❌ ইনিশিয়ালাইজেশন এরর: {e}")
        st.stop()

# --- ৬. ইন্টারফেস ---
with st.sidebar:
    st.header("⚙️ System Status")
    st.success("Core: Online")
    st.info(f"Time: {datetime.now().strftime('%H:%M:%S')}")

user_input = st.text_input("Enter Master Command / Key:", type="password")

if st.button("🚀 Run Command"):
    if not user_input:
        st.warning("⚠️ কি প্রদান করুন!")
    else:
        try:
            # সিকিউরিটি এবং প্রসেস রান করা
            # আপনার Guardian মডিউলের validate ফাংশনটি কাজ করবে
            if st.session_state.security.validate(user_input):
                with st.spinner("Processing..."):
                    # core_process না থাকলে process রান করবে
                    result = st.session_state.core.process(user_input)
                    st.session_state.db.save(result)
                    st.success("✅ Execution Successful")
                    st.write(result)
            else:
                st.error("🚫 Access Denied!")
        except Exception as e:
            st.error(f"❌ Runtime Error: {e}")
