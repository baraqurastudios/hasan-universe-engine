import streamlit as st
import os
import sys

# পাথ সেটআপ
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
for folder in ['core', 'security']:
    if os.path.join(BASE_DIR, folder) not in sys.path:
        sys.path.insert(0, os.path.join(BASE_DIR, folder))

from engine import Engine
from guardian import SecurityManager

st.set_page_config(page_title="BaraQura V8.2", layout="wide")
st.title("🤖 BaraQura V8.2: The Omni-Intelligence")

if 'initialized' not in st.session_state:
    st.session_state.security = SecurityManager()
    st.session_state.core = Engine()
    st.session_state.initialized = True

user_input = st.text_input("Enter Master Command / Key:", type="password")

if st.button("🚀 Run Command"):
    if st.session_state.security.validate(user_input):
        result = st.session_state.core.process(user_input)
        st.write(result)
        if "🔓" in result: st.success("✅ Access Granted")
    else:
        st.error("🚫 Access Denied!")
