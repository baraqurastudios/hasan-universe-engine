import sqlite3

def init_v8_memory():
    # ডাটাবেস কানেকশন এবং টেবিল তৈরি
    conn = sqlite3.connect('v8_memory.db')
    cursor = conn.cursor()
    
    # মাস্টার সেটিংস এবং ইউজার প্রেফারেন্স টেবিল
    cursor.execute('''CREATE TABLE IF NOT EXISTS master_data 
                      (key TEXT PRIMARY KEY, value TEXT)''')
    
    # সিস্টেম লগ এবং ইন্টেলিজেন্স মেমোরি টেবিল
    cursor.execute('''CREATE TABLE IF NOT EXISTS intelligence_log 
                      (timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, 
                       event TEXT, status TEXT)''')
    
    conn.commit()
    conn.close()
    return "🗄️ V8.2 Database Initialized: Memory Sync Active."

def save_to_memory(key, value):
    conn = sqlite3.connect('v8_memory.db')
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO master_data (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()
    return f"💾 Saved: {key} -> {value}"

def retrieve_memory(key):
    conn = sqlite3.connect('v8_memory.db')
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM master_data WHERE key=?", (key,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "🔍 No Data Found."

# মডিউল চালু করা
if __name__ == "__main__":
    print(init_v8_memory())
    # উদাহরণ: আপনার নাম বা কোনো বিশেষ কমান্ড সেভ করা
    print(save_to_memory("Master_Name", "Master V8"))
    print(save_to_memory("Security_Level", "Maximum"))
  
