import hashlib
import uuid
import psutil
import time

class SecureObserverV82:
    def __init__(self):
        # ১. আপনার পিসির ইউনিক আইডি (এটি অন্য পিসিতে মিলবে না)
        self.__authorized_hwid = str(uuid.getnode()) 
        
        # ২. মাস্টারের গোপন কী (SHA-256 হ্যাশ) - এখানে 'your_password' এর হ্যাশ দেওয়া আছে
        self.__master_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
        
        self.__is_locked = False
        self.__failed_attempts = 0

    def __verify_hardware(self):
        """Hardware ID চেক করে নিশ্চিত করা যে এটি মাস্টারের পিসি"""
        current_hwid = str(uuid.getnode())
        return current_hwid == self.__authorized_hwid

    def authenticate(self, input_key):
        """মাস্টার কি ভেরিফিকেশন"""
        if self.__failed_attempts >= 3:
            print("🚨 CRITICAL: Too many failed attempts. System Cooling Down...")
            time.sleep(10) # হ্যাকারকে স্লো করে দেওয়া
            
        input_hash = hashlib.sha256(input_key.encode()).hexdigest()
        
        if input_hash == self.__master_hash and self.__verify_hardware():
            self.__is_locked = False
            self.__failed_attempts = 0
            print("✅ Access Granted. Welcome, Master.")
            return True
        else:
            self.__failed_attempts += 1
            print(f"❌ ACCESS DENIED! Attempt: {self.__failed_attempts}")
            return False

    def observe_action(self, action):
        """কাজের নিরাপত্তা যাচাই"""
        if not self.__verify_hardware():
            return "ERR: ILLEGAL_HARDWARE_ACCESS (System Hijack Detected)"
        
        # পিসির হেলথ চেক
        cpu = psutil.cpu_percent()
        if cpu > 90:
            return "ERR: CPU_OVERLOAD (Possible Malware Attack)"
            
        return "SUCCESS"

# --- মেইন ইঞ্জিনের সাথে কানেকশন ---
obs = SecureObserverV82()
