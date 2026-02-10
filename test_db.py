<<<<<<< HEAD
import sqlite3

conn = sqlite3.connect("database.db")
conn.row_factory = sqlite3.Row

vendors = conn.execute("SELECT * FROM vendors").fetchall()

for v in vendors:
    print(v["name"], v["location"], v["min_pax"], v["max_pax"])

=======
import sqlite3

conn = sqlite3.connect("database.db")
conn.row_factory = sqlite3.Row

vendors = conn.execute("SELECT * FROM vendors").fetchall()

for v in vendors:
    print(v["name"], v["location"], v["min_pax"], v["max_pax"])

>>>>>>> 4f9d69a78090eb14aa5ade15d3544f9c9c31d0aa
conn.close()