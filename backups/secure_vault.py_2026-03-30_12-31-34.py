from cryptography.fernet import Fernet

# মাস্টার কী জেনারেট (এটি একবারই করবেন এবং লুকিয়ে রাখবেন)
def generate_master_key():
    key = Fernet.generate_key()
    with open("master.key", "wb") as key_file:
        key_file.write(key)
    return "🔑 Master Key Generated & Saved!"

# ডাটা এনক্রিপ্ট করা
def encrypt_token(token):
    with open("master.key", "rb") as key_file:
        key = key_file.read()
    f = Fernet(key)
    encrypted_token = f.encrypt(token.encode())
    with open("token.enc", "wb") as token_file:
        token_file.write(encrypted_token)
    return "🛡️ Token Locked Successfully!"
                       
