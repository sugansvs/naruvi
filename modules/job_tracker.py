import sqlite3

def init_db():
    conn = sqlite3.connect('naruvi.db')
    conn.execute('CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY, company TEXT, role TEXT, status TEXT, salary TEXT)')
    conn.commit()
    return conn
