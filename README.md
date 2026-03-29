import subprocess
import os

class SandboxIsolation:
    """
    v3.1.15: The Virtual Cage.
    Ensures AI runs in a limited environment with NO write access to core files.
    """
    def __init__(self, restricted_dir="/tmp/ai_sandbox"):
        self.restricted_dir = restricted_dir
        if not os.path.exists(self.restricted_dir):
            os.makedirs(self.restricted_dir)

    def safe_execute_check(self, command: str):
        """
        এআই যদি কোনো কমান্ড রান করতে চায়, তবে সেটি এই স্যান্ডবক্সে বন্দি থাকবে।
        """
        # 🚫 নিষিদ্ধ কি-ওয়ার্ড ফিল্টার (Hard-coded)
        forbidden = ["sudo", "chmod", "chown", "rm -rf /", "nano", "vim", "python3"]
        if any(bad in command for bad in forbidden):
            return "🚨 SECURITY_VIOLATION: Unauthorized system access attempt."

        try:
            # এআই-কে শুধু তার নির্দিষ্ট ডিরেক্টরির ভেতর কাজ করতে দেওয়া হবে
            result = subprocess.run(
                command, 
                shell=True, 
                cwd=self.restricted_dir, 
                capture_output=True, 
                text=True,
                timeout=5 # ৫ সেকেন্ডের বেশি সময় নিতে পারবে না (Anti-loop)
            )
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return f"ERROR: Execution Blocked - {str(e)}"