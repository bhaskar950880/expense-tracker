import sqlite3

# database create / connect
conn = sqlite3.connect("expenses.db")

# table create
conn.execute("""
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    note TEXT,
    date TEXT
)
""")

conn.commit()
conn.close()

print("Database aur table create ho gaya")
