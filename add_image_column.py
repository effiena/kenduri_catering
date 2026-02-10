<<<<<<< HEAD
import sqlite3

# Connect to your database
conn = sqlite3.connect("database.db")

try:
    # Try to add the 'image' column to the vendors table
    conn.execute("ALTER TABLE vendors ADD COLUMN image TEXT")
    print("✅ 'image' column added successfully!")
except sqlite3.OperationalError:
    # This error happens if the column already exists
    print("⚠ 'image' column already exists!")

# Save changes and close connection
conn.commit()
=======
import sqlite3

# Connect to your database
conn = sqlite3.connect("database.db")

try:
    # Try to add the 'image' column to the vendors table
    conn.execute("ALTER TABLE vendors ADD COLUMN image TEXT")
    print("✅ 'image' column added successfully!")
except sqlite3.OperationalError:
    # This error happens if the column already exists
    print("⚠ 'image' column already exists!")

# Save changes and close connection
conn.commit()
>>>>>>> 4f9d69a78090eb14aa5ade15d3544f9c9c31d0aa
conn.close()