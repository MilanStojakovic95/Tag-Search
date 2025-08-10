import sqlite3
import os

DB_PATH = os.path.join("data", "library.db")

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT UNIQUE,
            name TEXT,
            extension TEXT,
            added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_video(path):
    name = os.path.basename(path)
    ext = os.path.splitext(name)[1].lower()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute(
            "INSERT OR IGNORE INTO videos (path, name, extension) VALUES (?, ?, ?)",
            (path, name, ext)
        )
        conn.commit()
    except Exception as e:
        print(f"DB insert error: {e}")
    conn.close()
