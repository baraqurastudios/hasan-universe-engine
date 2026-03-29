# -----------------------------
# 🔒 SENSITIVE DATA PROTECTOR
# -----------------------------
class SensitiveDataProtector:
    def __init__(self):
        # এআই-এর জন্য নিষিদ্ধ ফাইলের তালিকা
        self.forbidden_files = ["config.env", ".env", "github_token.txt", "secrets.json"]
        self.forbidden_patterns = ["ghp_", "sk-", "password", "access_token"]

    def validate_file_access(self, file_path):
        """এআই কোনো ফাইল রিড করার আগে এই চেকটি হবে"""
        if any(f in file_path for f in self.forbidden_files):
            raise PermissionError("❌ [DIVINE PROTECTION] Access to Secret Files Denied!")
        return True

    def scan_generated_code(self, code):
        """কোড পুশ করার আগে টোকেন লিক হচ্ছে কি না চেক করা"""
        for pattern in self.forbidden_patterns:
            if pattern in code:
                return False, f"🚨 Critical Breach: Sensitive pattern '{pattern}' detected in code!"
        return True, "✅ Code is clean."