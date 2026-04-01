import streamlit as st
import os
import sys
import logging
from datetime import datetime

# --- ১. সিস্টেম পাথ সেটআপ (যাতে ফোল্ডারগুলো থেকে ইমপোর্ট কাজ করে) ---
folders = ['security', 'core', 'database', 'interface', 'config']
for folder in folders:
    folder_path = os.path.join(os.getcwd(), folder)
    if folder_path not in sys.path:
        sys.path.append(folder_path)

# --- ২. লগিং সিস্টেম সেটআপ ---
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename='logs/system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

# --- ৩. মডিউল ইমপোর্ট ---
try:
    from core.engine import Engine
    from database.db_manager import DatabaseManager
    from security.guardian import SecurityManager
    from interface.worker import Interface
    logging.info("All modules imported successfully")
except Exception as e:
    logging.error(f"Import Error: {e}")
    st.error(f"❌ Module Import Failed: {e}")

# --- ৪. Streamlit UI কনফিগারেশন ---
st.set_page_config(
    page_title="BaraQura Engine V8.2",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ BaraQura Engine V8.2")
st.info("System initialized with professional architecture")

# --- ৫. সিস্টেম ইনিশিয়ালাইজেশন ---
try:
    security = SecurityManager()
    db = DatabaseManager()
    core = Engine()
    ui = Interface()
    logging.info("System modules initialized successfully")
except Exception as e:
    logging.error(f"Initialization Error: {e}")
    st.error(f"❌ System initialization failed: {e}")
    st.stop()

# --- ৬. ইউজার ইনপুট ও প্রসেসিং ---
user_input = st.text_input("Enter your input:")

if st.button("Run Engine"):
    try:
        if not user_input:
            st.warning("⚠️ Please enter input!")
            st.stop()

        # Security check
        if not security.validate(user_input):
            st.error("🚫 Access Denied!")
            logging.warning(f"Blocked unsafe input: {user_input}")
            st.stop()

        # Process
        result = core.process(user_input)

        # Save to Database
        db.save(result)

        # Output
        st.success("✅ Result:")
        st.write(result)
        logging.info("Execution successful")

    except Exception as e:
        logging.error(f"Runtime Error: {e}")
        st.error(f"❌ Something went wrong: {e}")
