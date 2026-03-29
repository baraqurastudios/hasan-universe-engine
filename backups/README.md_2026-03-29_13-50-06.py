import os
def sandbox_execute(command):
    # শুধুমাত্র নির্দিষ্ট ডিরেক্টরির ভেতর কাজ করার পারমিশন
    allowed_path = "/universe_simulation/sandbox/"
    if not command.startswith(allowed_path):
        raise Exception("🚨 SECURITY BREACH: Out of Sandbox!")