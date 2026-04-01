import streamlit as st
import logging

# Proper imports (IMPORTANT)
from core.engine import Engine
from database.db_manager import DatabaseManager
from security.guardian import SecurityManager
from interface.worker import Interface

# -------------------------
# Logging Setup
# -------------------------
logging.basicConfig(
    filename='logs/system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# -------------------------
# Streamlit UI Config
# -------------------------
st.set_page_config(
    page_title="BaraQura Engine V8.2",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ BaraQura Engine V8.2")
st.info("System initialized with professional architecture")

# -------------------------
# Initialize System
# -------------------------
try:
    security = SecurityManager()
    db = DatabaseManager()
    core = Engine()
    ui = Interface()

    logging.info("System modules initialized successfully")

except Exception as e:
    logging.error(f"Initialization Error: {e}")
    st.error("❌ System initialization failed!")
    st.stop()

# -------------------------
# User Input Section
# -------------------------
user_input = st.text_input("Enter your input:")

if st.button("Run Engine"):
    try:
        if not user_input:
            st.warning("⚠️ Please enter input!")
            st.stop()

        # Security check
        if not security.validate(user_input):
            st.error("🚫 Access Denied!")
            logging.warning("Blocked unsafe input")
            st.stop()

        # Process
        result = core.process(user_input)

        # Save
        db.save(result)

        # Output
        st.success("✅ Result:")
        st.write(result)

        logging.info("Execution successful")

    except Exception as e:
        logging.error(f"Runtime Error: {e}")
        st.error("❌ Something went wrong!")
