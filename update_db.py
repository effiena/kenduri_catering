import sqlite3

# connect to your database
conn = sqlite3.connect("database.db")

# add email and password columns to vendors table
conn.execute("ALTER TABLE vendors ADD COLUMN email TEXT")
conn.execute("ALTER TABLE vendors ADD COLUMN password TEXT")

conn.commit()
conn.close()

print("✅ Database updated with email and password fields!")