import sqlite3
from datetime import datetime

class DBManager:
    def __init__(self, db_name="baraqura_v10.db"):
        # Streamlit-এ থ্রেড সেফ রাখার জন্য check_same_thread=False
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # ১. ইউজার প্রোফাইল ও লিড ট্র্যাকিং (Price Integrity কলামসহ)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                name TEXT,
                phone TEXT UNIQUE,
                status TEXT DEFAULT 'Cold',
                score INTEGER DEFAULT 0,
                offered_price INTEGER DEFAULT NULL,
                last_offer_time TIMESTAMP,
                last_intent TEXT,
                follow_count INTEGER DEFAULT 0,
                updated_at TIMESTAMP
            )
        ''')

        # ২. এআই মেমোরি টেবিল
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS brain_memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT UNIQUE,
                answer TEXT,
                is_verified INTEGER DEFAULT 0, 
                created_at TIMESTAMP
            )
        ''')
        self.conn.commit()

    # --- Pricing & Integrity Methods ---
    
    def get_offered_price(self, user_id):
        """ইউজারকে আগে কোনো দাম বলা হয়েছে কি না তা চেক করা"""
        self.cursor.execute("SELECT offered_price FROM users WHERE user_id = ?", (user_id,))
        row = self.cursor.fetchone()
        return row[0] if row else None

    def save_offered_price(self, user_id, price):
        """নতুন অফার করা দাম সেভ করা"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute('''
            UPDATE users SET offered_price = ?, last_offer_time = ?, updated_at = ?
            WHERE user_id = ?
        ''', (price, now, now, user_id))
        self.conn.commit()

    # --- Score & Status Updates ---

    def update_score(self, user_id, points):
        """ইউজারের স্কোর বাড়ানো (ইঞ্জিন থেকে কল হবে)"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute('''
            UPDATE users SET score = score + ?, updated_at = ?
            WHERE user_id = ?
        ''', (points, now, user_id))
        self.conn.commit()

    def increment_followup(self, user_id):
        """অটো ফলো-আপ কাউন্ট ট্র্যাকিং"""
        self.cursor.execute("UPDATE users SET follow_count = follow_count + 1 WHERE user_id = ?", (user_id,))
        self.conn.commit()

    # --- Existing Methods (Cleaned) ---

    def get_user(self, user_id):
        self.cursor.execute("SELECT score, status FROM users WHERE user_id = ?", (user_id,))
        row = self.cursor.fetchone()
        return {'score': row[0], 'status': row[1]} if row else {'score': 0, 'status': 'Cold'}

    def save_pending_memory(self, question, answer):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT OR IGNORE INTO brain_memory (question, answer, created_at) VALUES (?, ?, ?)", 
                           (question, answer, now))
        self.conn.commit()

    def close(self):
        self.conn.close()
