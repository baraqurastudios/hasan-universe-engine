import sqlite3

def read_v8_memory():
    db_name = "v8_memory.db"
    
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("🔍 --- V8.2 MASTER DATA --- 🔍")
        cursor.execute("SELECT * FROM system_memory")
        memory_data = cursor.fetchall()
        for row in memory_data:
            print(f"📌 Key: {row[0]} | Value: {row[1]}")
            
        print("\n📜 --- V8.2 ACTIVITY LOGS --- 📜")
        cursor.execute("SELECT * FROM logs ORDER BY time DESC LIMIT 10") # শেষ ১০টি কাজ
        logs = cursor.fetchall()
        for log in logs:
            print(f"🕒 {log[0]} -> {log[1]}")
            
        conn.close()
    except sqlite3.OperationalError:
        print("⚠️ Error: Database file not found yet! Please run the Main Engine first.")

if __name__ == "__main__":
    read_v8_memory()
      
