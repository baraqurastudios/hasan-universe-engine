import sqlite3
from datetime import datetime

class DBManager:
    def __init__(self, db_name="baraqura_v10.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
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
        self.cursor.execute("SELECT score, status FROM users WHERE user_id = ?", (user_id,))
        row = self.cursor.fetchone()
        if row:
            return {'score': row[0], 'status': row[1]}
        return {'score': 0, 'status': 'Cold'}

    def save_lead(self, user_id, name, phone, score=100, status="Hot"):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.cursor.execute('''
                INSERT INTO users (user_id, name, phone, score, status, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (user_id, name, phone, score, status, now))
        except sqlite3.IntegrityError:
            self.cursor.execute('''
                UPDATE users SET score=?, status=?, updated_at=?
                WHERE phone=?
            ''', (score, status, now, phone))
        self.conn.commit()

    def update_user_score(self, user_id, score, status, intent):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
