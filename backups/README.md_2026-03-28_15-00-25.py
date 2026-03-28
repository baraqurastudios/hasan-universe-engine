# ==========================================
# 🧠 BaraQura OS v1.5 – GOD MODE MODULE
# Features:
# 🧠 AI Auto Debugging
# 🔍 AI Code Review
# 📊 Usage Analytics
# 🧩 Plugin Marketplace
# ==========================================

import os
import json
import openai
import datetime

st.divider()
st.header("🧠 GOD MODE AI SYSTEM")

openai.api_key = os.getenv("OPENAI_API_KEY")

# ==========================================
# 🧠 1. AI AUTO DEBUGGING
# ==========================================
st.subheader("🧠 AI Auto Debugger")

def ai_debug(code):
    try:
        res = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Fix bugs and return clean Python code only."},
                {"role": "user", "content": code}
            ],
            temperature=0.2
        )
        return res['choices'][0]['message']['content']
    except Exception as e:
        return f"# Debug Error: {e}"

if st.button("🛠️ Auto Fix Code"):
    if new_code_input:
        fixed_code = ai_debug(new_code_input)
        st.session_state['fixed_code'] = fixed_code
        st.success("✅ Code Fixed!")

if 'fixed_code' in st.session_state:
    st.text_area("🧪 Fixed Code", st.session_state['fixed_code'], height=250)

    if st.button("Use Fixed Code"):
        new_code_input = st.session_state['fixed_code']
        st.success("✅ Applied!")


# ==========================================
# 🔍 2. AI CODE REVIEW
# ==========================================
st.subheader("🔍 AI Code Review")

def ai_review(code):
    try:
        res = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Review this code. Give issues and improvements."},
                {"role": "user", "content": code}
            ],
            temperature=0.3
        )
        return res['choices'][0]['message']['content']
    except Exception as e:
        return f"Review Error: {e}"

if st.button("🔎 Run Code Review"):
    if new_code_input:
        review = ai_review(new_code_input)
        st.session_state['review'] = review

if 'review' in st.session_state:
    st.text_area("📋 Review Report", st.session_state['review'], height=250)


# ==========================================
# 📊 3. USAGE ANALYTICS
# ==========================================
st.subheader("📊 Usage Analytics")

if 'analytics' not in st.session_state:
    st.session_state['analytics'] = {
        "updates": 0,
        "ai_used": 0,
        "debug_runs": 0
    }

# counters
if st.button("Simulate Update"):
    st.session_state['analytics']['updates'] += 1

if st.button("Simulate AI Use"):
    st.session_state['analytics']['ai_used'] += 1

if st.button("Simulate Debug"):
    st.session_state['analytics']['debug_runs'] += 1

st.json(st.session_state['analytics'])


# ==========================================
# 🧩 4. PLUGIN MARKETPLACE
# ==========================================
st.subheader("🧩 Plugin Marketplace")

PLUGINS = {
    "Formatter": "Auto format Python code",
    "Security Scan": "Basic vulnerability check",
    "Comment Generator": "Add comments to code"
}

selected_plugin = st.selectbox("Choose Plugin", list(PLUGINS.keys()))
st.info(PLUGINS[selected_plugin])

def run_plugin(name, code):
    if name == "Formatter":
        return code.strip()
    elif name == "Security Scan":
        if "eval(" in code:
            return "⚠️ Warning: eval() detected!"
        return "✅ No major issues"
    elif name == "Comment Generator":
        return "# Auto-commented\n" + code
    return code

if st.button("Run Plugin ⚙️"):
    if new_code_input:
        result = run_plugin(selected_plugin, new_code_input)
        st.session_state['plugin_result'] = result

if 'plugin_result' in st.session_state:
    st.text_area("🔌 Plugin Output", st.session_state['plugin_result'], height=200)