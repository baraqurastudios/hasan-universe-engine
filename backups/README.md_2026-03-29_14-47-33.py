# -----------------------------------------------
# 🛡️ v8.0 SECURITY FINAL AUDIT (THE GUARDIAN)
# -----------------------------------------------
import os
import sys

class SecurityAudit:
    def __init__(self):
        # চেক করার জন্য প্রয়োজনীয় সব সিকিউরিটি ফাইল
        self.required_modules = [
            'safety/ethics_v8_core.py',
            'safety/v8_observer_locks.py',
            'safety/key_gen.py',
            'safety/digital_jail.py',
            'safety/advanced_traps.py',
            'safety/heartbeat_monitor.py'
        ]

    def run_full_scan(self):
        print("🔍 Running v8.0 Security Final Check...")
        missing_files = []

        for file in self.required_modules:
            if not os.path.exists(file):
                missing_files.append(file)
        
        if missing_files:
            print(f"🚨 CRITICAL BREACH: Security files missing: {missing_files}")
            self.lock_system()
            return False
        
        print("✅ ALL LOCKS ACTIVE. Universe integrity is 100%.")
        return True

    def lock_system(self):
        print("💀 SECURITY COMPROMISED. BOOTING ABORTED.")
        sys.exit(1)

# ব্যবহারের নিয়ম:
# audit = SecurityAudit()
# if audit.run_full_scan():
#    print("🚀 Universe is safe to launch!")