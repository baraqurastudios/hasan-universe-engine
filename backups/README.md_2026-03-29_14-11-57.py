class ApprovalGateway:
    def __init__(self, admin_telegram_id):
        self.admin_id = admin_telegram_id

    def request_approval(self, content):
        print(f"📡 Sending Draft to Admin [{self.admin_id}]...")
        print(f"Draft: {content[:50]}...")
        
        # এখানে টেলিগ্রাম বটের মাধ্যমে আপনার ইনপুটের জন্য অপেক্ষা করবে
        user_input = input("Enter 'YES' to publish or 'NO' to discard: ")
        
        if user_input.upper() == "YES":
            return True # পাবলিশ করার পারমিশন পেল
        return False # ড্রাফট ডিলিট