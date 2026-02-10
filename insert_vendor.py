import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""
INSERT INTO vendors 
(name, location, min_pax, max_pax, price_per_pax, whatsapp)
VALUES
('Nasi Kahwin Catering', 'Selangor', 300, 1000, 15, '60123456789')
""")

conn.commit()
conn.close()

print("Vendor added!")