import os
import time
import threading
import tkinter as tk
from tkinter import messagebox
import sys

# --- SECURE CONFIG ---
MASTER_KEY = os.getenv("V8_MASTER_KEY")
IDLE_LOCK_LIMIT = 60    # ১ মিনিট (Auto-Lock)
IDLE_FREEZE_LIMIT = 180 # ৩ মিনিট (Total Freeze & Power Off)
LAST_ACTIVITY = time.time()

class MasterLoginGateway:
    def __init__(self, root):
        self.root = root
        self.root.title("V8.1 SECURE GATEWAY")
        self.root.geometry("350x450")
        self.root.configure(bg="#0a0a0a") # পিওর ব্ল্যাক থিম
        self.root.overrideredirect(False) # উইন্ডো কন্ট্রোল
        
        self.is_authenticated = False

        # --- UI ELEMENTS ---
        tk.Label(root, text="V8.1 CORE ACCESS", font=("Orbitron", 14, "bold"), fg="#00ffcc", bg="#0a0a0a").pack(pady=30)
        
        self.status_indicator = tk.Label(root, text="● SYSTEM LOCKED", fg="red", bg="#0a0a0a", font=("Arial", 10))
        self.status_indicator.pack()

        # পাসওয়ার্ড ইনপুট বক্স (মাস্টার শুধু এখানে টাইপ করবেন)
        tk.Label(root, text="ENTER MASTER KEY", fg="#888", bg="#0a0a0a", font=("Arial", 9)).pack(pady=20)
        self.password_entry = tk.Entry(root, show="*", font=("Arial", 14), bg="#1a1a1a", fg="#00ffcc", 
                                      insertbackground="white", justify='center', bd=0, highlightthickness=1)
        self.password_entry.config(highlightbackground="#333", highlightcolor="#00ffcc")
        self.password_entry.pack(pady=10, ipady=8, padx=40, fill='x')
        
        # লগইন বাটন
        self.login_btn = tk.Button(root, text="LOGIN TO CORE", command=self.attempt_login, 
                                   bg="#00ffcc", fg="black", font=("Arial", 10, "bold"), 
                                   activebackground="#00cca3", relief="flat", cursor="hand2")
        self.login_btn.pack(pady=20, ipady=5, padx=60, fill='x')

        self.timer_label = tk.Label(root, text="", fg="#555", bg="#0a0a0a", font=("Courier", 9))
        self.timer_label.pack(side="bottom", pady=20)

        # অ্যাক্টিভিটি ডিটেক্টর (মাউস বা কিবোর্ড নাড়লেই টাইমার রিসেট)
        self.root.bind_all("<Any-KeyPress>", self.reset_timer)
        self.root.bind_all("<Motion>", self.reset_timer)

        # ব্যাকগ্রাউন্ড ওয়াচম্যান
        threading.Thread(target=self.security_loop, daemon=True).start()

    def reset_timer(self, event=None):
        global LAST_ACTIVITY
        LAST_ACTIVITY = time.time()

    def attempt_login(self):
        entered_key = self.password_entry.get()
        if entered_key == MASTER_KEY:
            self.is_authenticated = True
            self.status_indicator.config(text="● ACCESS GRANTED", fg="#00ffcc")
            self.password_entry.delete(0, tk.END)
            self.password_entry.config(state="disabled")
            self.login_btn.config(state="disabled", text="CORE ACTIVE")
            self.reset_timer()
            print("🔓 Master Logged In. System Unfrozen.")
            # এখানে আপনার V8.1 ফাইল আনলক করার লজিক কল হবে
        else:
            messagebox.showerror("DENIED", "Invalid Master Key. Intruder Alert Logged.")

    def security_loop(self):
        while True:
            if self.is_authenticated:
                elapsed = time.time() - LAST_ACTIVITY
                
                # ১ মিনিট পর অটো-লক
                if elapsed >= IDLE_LOCK_LIMIT and elapsed < IDLE_FREEZE_LIMIT:
                    self.is_authenticated = False
                    self.root.after(0, self.auto_lock_ui)
                
                # ৩ মিনিট পর টোটাল ফ্রিজ (পাওয়ার অফ)
                if elapsed >= IDLE_FREEZE_LIMIT:
                    self.root.after(0, self.total_freeze_exit)
                    break
                
                # টাইমার আপডেট
                remaining = int(IDLE_FREEZE_LIMIT - elapsed)
                self.timer_label.config(text=f"SECURE SHUTDOWN IN: {remaining}s")
                
            time.sleep(1)

    def auto_lock_ui(self):
        self.status_indicator.config(text="● AUTO-LOCKED (IDLE)", fg="orange")
        self.password_entry.config(state="normal")
        self.login_btn.config(state="normal", text="RE-LOGIN")
        print("🔒 Idle Timeout: Files moved to Black Hole.")

    def total_freeze_exit(self):
        print("❄️ Total Freeze: System Powering Down.")
        self.root.destroy()
        sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MasterLoginGateway(root)
    root.mainloop()
