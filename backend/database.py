import sqlite3

conn = sqlite3.connect('database/smarthire.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS jds (
    id INTEGER PRIMARY KEY,
    summary TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY,
    name TEXT,
    cv_text TEXT
)
''')

conn.commit()
conn.close()