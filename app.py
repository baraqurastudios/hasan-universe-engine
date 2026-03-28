import streamlit as st
import datetime

# ================================
# 🧬 BaraQura OS v1 - Core Framework
# ================================

st.set_page_config(page_title="BaraQura OS", layout="wide")

# --- SYSTEM STATE ---
if "system_logs" not in st.session_state:
    st.session_state.system_logs = []

if "modules" not in st.session_state:
    st.session_state.modules = {
        "core": True,
        "animation_engine": False,
        "auto_update": False,
        "ai_brain": False
    }

# --- HEADER ---
st.markdown("<h1 style='text-align: center; color: #00FFAA;'>🚀 BaraQura OS v1</h1>", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("🧬 System Core")
st.sidebar.success("Version: v1.0 (Foundation)")
st.sidebar.info(f"📅 {datetime.datetime.now().strftime('%d %b %Y')}")

# --- COMMAND SYSTEM ---
st.subheader("⚡ Command Console")

command = st.text_input("Enter Command")

def run_command(cmd):
    if cmd == "/status":
        return {"system": "active", "version": "v1.0"}
    
    elif cmd.startswith("/install"):
        module = cmd.replace("/install ", "")
        if module in st.session_state.modules:
            st.session_state.modules[module] = True
            return {"installed": module}
        else:
            return {"error": "module not found"}
    
    elif cmd == "/modules":
        return st.session_state.modules
    
    else:
        return {"error": "unknown command"}

if st.button("Run"):
    result = run_command(command)
    st.json(result)
    st.session_state.system_logs.append(str(result))

# --- MODULE STATUS ---
st.subheader("📦 Modules")
st.json(st.session_state.modules)

# --- SYSTEM LOGS ---
st.subheader("📜 Logs")
for log in st.session_state.system_logs[-5:]:
    st.write(log)

st.divider()
st.caption("BaraQura OS v1 | Ultra Framework Base")
