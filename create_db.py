import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""
CREATE TABLE vendors (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
location TEXT,
min_pax INTEGER,
max_pax INTEGER,
price_per_pax INTEGER,
whatsapp TEXT
)
""")

conn.commit()
conn.close()
