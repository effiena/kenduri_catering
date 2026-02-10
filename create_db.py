<<<<<<< HEAD
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
=======
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
>>>>>>> 4f9d69a78090eb14aa5ade15d3544f9c9c31d0aa
