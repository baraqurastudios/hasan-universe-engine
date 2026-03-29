import hashlib
import os

class KeyGenerator:
    def __init__(self):
        # আপনার মাস্টার পাসওয়ার্ড (এটি পরিবর্তন করে নিজের মতো গোপন কোড দিন)
        self.__secret_master_pass = "V8_GOD_MODE_2026" 
        self.salt = "uNiVeRsE_v8_sAlT" # এনক্রিপশন আরও মজবুত করার জন্য

    def verify_master(self, input_pass):
        """পাসওয়ার্ড চেক করে এক্সেস দেয়"""
        hashed_input = hashlib.sha256((input_pass + self.salt).encode()).hexdigest()
        hashed_master = hashlib.sha256((self.__secret_master_pass + self.salt).encode()).hexdigest()
        
        return hashed_input == hashed_master

    def get_session_token(self):
        """প্রতিবার লগইন করলে একটি ইউনিক সেশন আইডি তৈরি করে"""
        return hashlib.md5(os.urandom(16)).hexdigest()