import sqlite3

conn = sqlite3.connect("database.db")
conn.row_factory = sqlite3.Row

vendors = conn.execute("SELECT * FROM vendors").fetchall()

for v in vendors:
    print(v["name"], v["location"], v["min_pax"], v["max_pax"])

conn.close()