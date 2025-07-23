import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

cursor.execute("INSERT INTO test (titulo) VALUES (?)", ("Hola mundo 2",))

connection.commit()

connection.close()