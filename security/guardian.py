import os
import hashlib
import hmac
from functools import wraps
from flask import request, abort

# তোমার সিক্রেট কি (এটি .env থেকে আসবে)
APP_SECRET = os.getenv("FB_APP_SECRET")

class Guardian:
    @staticmethod
    def verify_fb_signature(payload, signature):
        """ফেসবুক থেকে আসা রিকোয়েস্ট ভেরিফাই করে"""
        if not signature:
            return False
        
        # 'sha256=' অংশটি সরিয়ে ফেলা
        expected_sig = hmac.new(
            bytes(APP_SECRET, 'utf-8'),
            msg=payload,
            digestmod=hashlib.sha256
        ).hexdigest()
        
        return hmac.compare_digest(f"sha256={expected_sig}", signature)

    @staticmethod
    def security_check(f):
        """সব ইনকামিং রিকোয়েস্টের জন্য সিকিউরিটি ডেকোরেটর"""
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # ১. সিগনেচার চেক
            signature = request.headers.get('X-Hub-Signature-256')
            if not Guardian.verify_fb_signature(request.data, signature):
                # হ্যাকিং এটেম্পট হিসেবে ধরে নেওয়া হবে
                print("⚠️ [ALERT] Unauthorized request blocked by Guardian!")
                abort(403) # Access Forbidden
            
            return f(*args, **kwargs)
        return decorated_function
