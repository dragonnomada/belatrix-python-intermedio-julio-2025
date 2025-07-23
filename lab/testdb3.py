import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

cursor.execute("""

SELECT id, titulo FROM test

""")

for id, titulo in cursor.fetchall():
    print(id, titulo)

connection.close()