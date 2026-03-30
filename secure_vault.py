from cryptography.fernet import Fernet

def setup_v8_encryption():
    # মাস্টার চাবি তৈরি (একবারই রান করবেন)
    master_key = Fernet.generate_key()
    with open("v8_master.key", "wb") as f:
        f.write(master_key)
    
    # আপনার টেলিগ্রাম টোকেন এখানে এনক্রিপ্ট করুন
    cipher = Fernet(master_key)
    encrypted_token = cipher.encrypt(b"YOUR_TELEGRAM_TOKEN_HERE")
    with open("token.enc", "wb") as f:
        f.write(encrypted_token)
    
    return "✅ AES-256 Encryption Set: Data Hidden!"

if __name__ == "__main__":
    print(setup_v8_encryption())
