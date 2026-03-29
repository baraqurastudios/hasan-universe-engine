import os
import time
import threading
import tkinter as tk
import sys

# --- CONFIGURATION ---
LOCK_LIMIT = 60    # ১ মিনিট = ৬০ সেকেন্ড (ফাইল লক হওয়ার জন্য)
FREEZE_LIMIT = 180 # ৩ মিনিট (১+২) = ১৮০ সেকেন্ড (সব পাওয়ার হারানোর জন্য)
LAST_ACTIVITY_TIME = time.time()
FILES_TO_MANAGE = ["v81_engine.py", "github_handler.py", "admin_panel.py"]
MASTER_KEY = os.getenv("V8_MASTER_KEY")

class AdvancedBlackHole:
    def __init__(self, root):
        self.root = root
        self.root.title("V8.1 Advanced Control")
        self.root.geometry("400x600")
        self.root.configure(bg="#1a1a1a") # ডার্ক মোড
        self.is_active = False
        self.is_frozen = False

        # Status Display
        self.status_label = tk.Label(root, text="SYSTEM: 🔴 FROZEN", font=("Helvetica", 16, "bold"), fg="red", bg="#1a1a1a")
        self.status_label.pack(pady=20)

        # Timer Display
        self.timer_label = tk.Label(root, text="Next Event: --:--", font=("Courier", 12), fg="#00ff00", bg="#1a1a1a")
        self.timer_label.pack()

        # Input Section
        tk.Label(root, text="Enter Master Key:", fg="white", bg="#1a1a1a").pack(pady=10)
        self.key_entry = tk.Entry(root, show="*", font=("Helvetica", 12), bg="#333", fg="white", insertbackground="white")
        self.key_entry.pack(pady=5)
        self.key_entry.bind("<Key>", self.reset_timer)

        # Buttons
        self.activate_btn = tk.Button(root, text="ACTIVATE SYSTEM", command=self.activate_system, bg="#2ecc71", fg="white", width=20, relief="flat")
        self.activate_btn.pack(pady=20)

        self.lock_btn = tk.Button(root, text="MANUAL LOCK", command=self.lock_system, bg="#e67e22", fg="white", width=20, relief="flat")
        self.lock_btn.pack(pady=5)

        # AI Visibility
        tk.Label(root, text="AI Knowledge Base (Visible Files):", fg="white", bg="#1a1a1a").pack(pady=15)
        self.file_list = tk.Listbox(root, height=6, width=40, bg="#222", fg="#00ff00", borderwidth=0)
        self.file_list.pack(pady=5)
        
        self.update_ai_view()
        
        # ব্যাকগ্রাউন্ড প্রহরী চালু
        threading.Thread(target=self.monitor_logic, daemon=True).start()

    def reset_timer(self, event=None):
        global LAST_ACTIVITY_TIME
        if not self.is_frozen:
            LAST_ACTIVITY_TIME = time.time()

    def activate_system(self):
        if self.key_entry.get() == MASTER_KEY:
            self.is_active = True
            self.is_frozen = False
            self.status_label.config(text="SYSTEM: 🟢 ACTIVE", fg="#2ecc71")
            
            # ফাইল রিভাইভ করা
            vault_files = [f for f in os.listdir(".") if f.endswith(".vault")]
            for v_file in vault_files:
                original = v_file.lstrip('.').replace(".vault", "")
                if os.path.exists(v_file): os.rename(v_file, original)
            
            if os.path.exists(".master_lock"): os.remove(".master_lock")
            self.update_ai_view()
            self.reset_timer()
        else:
            self.status_label.config(text="SYSTEM: ❌ DENIED", fg="red")

    def lock_system(self):
        """১ম স্টেজ: ফাইল ব্ল্যাক হোলে পাঠানো"""
        self.is_active = False
        self.status_label.config(text="SYSTEM: 🟡 LOCKED", fg="#e67e22")
        for filename in FILES_TO_MANAGE:
            if os.path.exists(filename):
                os.rename(filename, f".{filename}.vault")
        
        with open(".master_lock", "w") as f: f.write("LOCKED")
        self.update_ai_view()

    def freeze_system(self):
        """২য় স্টেজ: পাওয়ার অফ এবং টোটাল ফ্রিজ"""
        self.is_frozen = True
        self.is_active = False
        self.status_label.config(text="SYSTEM: ❄️ TOTAL FREEZE", fg="#3498db")
        self.timer_label.config(text="ALL POWER LOST", fg="red")
        print("❄️ CRITICAL: System is now in Total Freeze mode. Shutting down...")
        time.sleep(2)
        self.root.destroy() # ড্যাশবোর্ড বন্ধ হয়ে যাবে
        sys.exit() # প্রোগ্রাম পুরোপুরি বন্ধ

    def update_ai_view(self):
        self.file_list.delete(0, tk.END)
        for f in os.listdir("."):
            if "V8" not in f.upper() and not f.startswith(".") and ".vault" not in f:
                self.file_list.insert(tk.END, f)

    def monitor_logic(self):
        while True:
            elapsed = time.time() - LAST_ACTIVITY_TIME
            
            if self.is_active:
                # ১ম স্টেজের জন্য কাউন্টডাউন
                remaining_lock = max(0, LOCK_LIMIT - int(elapsed))
                mins, secs = divmod(remaining_lock, 60)
                self.timer_label.config(text=f"Auto-Lock in: {mins:02d}:{secs:02d}", fg="#00ff00")
                
                if elapsed >= LOCK_LIMIT:
                    self.lock_system()
            
            elif not self.is_active and not self.is_frozen:
                # ২য় স্টেজের জন্য কাউন্টডাউন (লক হওয়ার পর)
                remaining_freeze = max(0, FREEZE_LIMIT - int(elapsed))
                mins, secs = divmod(remaining_freeze, 60)
                self.timer_label.config(text=f"Total Freeze in: {mins:02d}:{secs:02d}", fg="red")
                
                if elapsed >= FREEZE_LIMIT:
                    self.freeze_system()
            
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedBlackHole(root)
    root.mainloop()
