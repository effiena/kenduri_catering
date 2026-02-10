<<<<<<< HEAD
import sqlite3
import os

DB_FILE = "database.db"

# 1️⃣ Delete old database if it exists
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
    print("Old database deleted.")

# 2️⃣ Create new database
conn = sqlite3.connect(DB_FILE)
print("New database created.")

# 3️⃣ Create vendors table with all needed columns
conn.execute("""
CREATE TABLE vendors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    min_pax INTEGER,
    max_pax INTEGER,
    price_per_pax INTEGER,
    whatsapp TEXT,
    email TEXT,
    password TEXT
)
""")
conn.commit()
print("Vendors table created with all columns!")

# 4️⃣ Add a test vendor (optional)
conn.execute("""
INSERT INTO vendors 
(name, location, min_pax, max_pax, price_per_pax, whatsapp, email, password)
VALUES
('Nasi Kahwin Catering', 'Selangor', 300, 1000, 15, '60123456789', 'test@example.com', '1234')
""")
conn.commit()
conn.close()
=======
import sqlite3
import os

DB_FILE = "database.db"

# 1️⃣ Delete old database if it exists
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
    print("Old database deleted.")

# 2️⃣ Create new database
conn = sqlite3.connect(DB_FILE)
print("New database created.")

# 3️⃣ Create vendors table with all needed columns
conn.execute("""
CREATE TABLE vendors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    min_pax INTEGER,
    max_pax INTEGER,
    price_per_pax INTEGER,
    whatsapp TEXT,
    email TEXT,
    password TEXT
)
""")
conn.commit()
print("Vendors table created with all columns!")

# 4️⃣ Add a test vendor (optional)
conn.execute("""
INSERT INTO vendors 
(name, location, min_pax, max_pax, price_per_pax, whatsapp, email, password)
VALUES
('Nasi Kahwin Catering', 'Selangor', 300, 1000, 15, '60123456789', 'test@example.com', '1234')
""")
conn.commit()
conn.close()
>>>>>>> 4f9d69a78090eb14aa5ade15d3544f9c9c31d0aa
print("✅ Database setup complete!")