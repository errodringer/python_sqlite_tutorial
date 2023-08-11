import sqlite3

conn = sqlite3.connect('test.db')

conn.execute("INSERT INTO suscriptores (ID,nombre,edad,descripcion,fecha) "
             "VALUES (1, 'Paco', 30, 'Nacio en el mundo', 2023-04-20)")
conn.execute("INSERT INTO suscriptores (ID,nombre,edad,descripcion,fecha) "
             "VALUES (2, 'Ricardo', 20, 'Nacio en Marte', 2023-04-21)")

conn.commit()

cursor = conn.cursor()

cursor.execute("SELECT * FROM suscriptores")
table_content = cursor.fetchall()
print(table_content)
print(table_content[0][1])

conn.close()
