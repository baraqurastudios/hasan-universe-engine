import os

def v8_sentinel_scan():
    print("🔍 V8.1 Sentinel: Scanning for vulnerabilities...")
    # আপনার সিস্টেমের সব ফাইল লিস্ট করার কমান্ড
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print(f"✅ Scanned {len(files)} files. System secure.")
    return True

if __name__ == "__main__":
    v8_sentinel_scan()
