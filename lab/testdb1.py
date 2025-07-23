import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS test (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL
)

""")

connection.commit()

connection.close()