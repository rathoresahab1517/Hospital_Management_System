
import sqlite3
import os
from datetime import datetime
# # from werkzeug.security import generate_password_hash, check_password_hash
DPATH = os.path.join(os.path.dirname(__file__), 'database.db')
def get_db():
    conn = sqlite3.connect(DPATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            name TEXT NOT NULL,
            phone TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS patient (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL UNIQUE REFERENCES user(id),
            gender TEXT,
            blood_group TEXT,
            date_of_birth DATE,
            address TEXT,
            emergency_contact TEXT
        );
        CREATE TABLE IF NOT EXISTS doctor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL UNIQUE REFERENCES user(id),
            specialization TEXT,
            license_number TEXT,
            qualification TEXT,
            experience_years INTEGER,
            consultation_fee REAL,
            available_days TEXT,
            available_time_start TEXT,
            available_time_end TEXT
        );
    ''')
    conn.commit()
    conn.close()
if __name__ == '__main__':
    init_db()
    print("Database tables created successfully.")