# ==============================
# BARAQURA VOICE ENGINE
# ==============================
class VoiceEngine:
    # আপনার স্টুডিওর জন্য এভেইলেবল ভয়েস লিস্ট
    VOICE_MODELS = {
        "Puck": {"type": "Child/Playful", "target": "Hasan (7y)"},
        "Kore": {"type": "Female/Warm", "target": "Mother (Liza)"},
        "Charon": {"type": "Male/Deep", "target": "Father (Shakib)"}
    }

    @staticmethod
    def assign_voice(character_name):
        """চরিত্র অনুযায়ী ভয়েস অটো-অ্যাসাইন করা"""
        if "Hasan" in character_name:
            return "Puck"
        elif "Liza" in character_name or "Mother" in character_name:
            return "Kore"
        elif "Shakib" in character_name or "Father" in character_name:
            return "Charon"
        return "Default_Narrator"

# ==============================
# UPDATED SCRIPT GENERATOR (WITH VOICE)
# ==============================
def generate_script_with_voice(topic=None):
    # আগের স্ক্রিপ্ট জেনারেটর ব্যবহার করে
    raw_script = ScriptGenerator.generate_script(topic)
    
    # ভয়েস ম্যাপিং করা
    raw_script["voice_mapping"] = {
        "Hasan": VoiceEngine.assign_voice("Hasan"),
        "Mother": VoiceEngine.assign_voice("Liza"),
        "Father": VoiceEngine.assign_voice("Shakib")
    }
    
    return raw_script

# ==============================
# API ROUTE FOR VOICE SELECTION
# ==============================
@API.route("/voice_config")
def api_voice_config(data, user):
    if not user:
        return {"error": "Unauthorized"}
    
    action = data.get("action", "list")
    if action == "list":
        return VoiceEngine.VOICE_MODELS
    
    return {"status": "Voice profile updated"}
