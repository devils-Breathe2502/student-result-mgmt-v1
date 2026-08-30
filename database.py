import sqlite3

DB_NAME = "results.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no TEXT NOT NULL,
            marks1 INTEGER NOT NULL,
            marks2 INTEGER NOT NULL,
            marks3 INTEGER NOT NULL,
            total INTEGER NOT NULL,
            percentage REAL NOT NULL,
            grade TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_result(name, roll_no, marks1, marks2, marks3, total, percentage, grade):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO results (name, roll_no, marks1, marks2, marks3, total, percentage, grade)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, roll_no, marks1, marks2, marks3, total, percentage, grade))
    conn.commit()
    conn.close()

def get_all_results():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM results')
    rows = cursor.fetchall()
    conn.close()
    return rows
