import sqlite3
from datetime import datetime

class DBManager:
    def __init__(self, db_name="baraqura_v10.db"):
        # check_same_thread=False দেওয়া হয়েছে যাতে Streamlit Cloud-এ এরর না দেয়
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # টেবিল স্ট্রাকচার (তোর metadata এবং intent ট্র্যাকিং সহ)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                name TEXT,
                phone TEXT UNIQUE,
                status TEXT DEFAULT 'Cold',
                score INTEGER DEFAULT 0,
                last_intent TEXT,
                updated_at TIMESTAMP
            )
        ''')
        self.conn.commit()

    def get_user(self, user_id):
        # ডাটাবেস থেকে ইউজারের বর্তমান অবস্থা জানা
        self.cursor.execute("SELECT score, status FROM users WHERE user_id = ?", (user_id,))
        row = self.cursor.fetchone()
        if row:
            return {'score': row[0], 'status': row[1]}
        # ডাটা না থাকলে ডিফল্ট (যাতে engine.py ক্র্যাশ না করে)
        return {'score': 0, 'status': 'Cold'}

    def save_lead(self, user_id, name, phone, score=100, status="Hot"):
        """ফোন নম্বর পাওয়া গেলে সরাসরি হট লিড হিসেবে সেভ বা আপডেট করা"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.cursor.execute('''
                INSERT INTO users (user_id, name, phone, score, status, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(user_id) DO UPDATE SET
                    phone=excluded.phone,
                    score=excluded.score,
                    status=excluded.status,
                    updated_at=excluded.updated_at
            ''', (user_id, name, phone, score, status, now))
        except sqlite3.IntegrityError:
            # যদি ফোন নম্বর অন্য কোনো আইডির সাথে অলরেডি থাকে
            self.cursor.execute('''
                UPDATE users SET score=?, status=?, updated_at=?
                WHERE phone=?
            ''', (score, status, now, phone))
        self.conn.commit()

    def update_user_score(self, user_id, score, status, intent="unknown"):
        """ইউজারের স্কোর এবং ইনটেন্ট আপডেট করা (New Logic)"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # INSERT OR REPLACE লজিক যাতে নতুন ইউজার হলেও ক্র্যাশ না করে
        self.cursor.execute('''
            INSERT INTO users (user_id, score, status, last_intent, updated_at)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET 
                score=excluded.score, 
                status=excluded.status, 
                last_intent=excluded.last_intent,
                updated_at=excluded.updated_at
        ''', (user_id, score, status, intent, now))
        self.conn.commit()

    def close(self):
        self.conn.close()
