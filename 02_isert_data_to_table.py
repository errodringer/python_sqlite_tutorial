import sqlite3

# Connection with database "test.db"
conn = sqlite3.connect('test.db')

# Create new column on table "suscriptores"
alter_table_query = """
ALTER TABLE suscriptores
ADD COLUMN numero INT
"""
conn.execute(alter_table_query)

# Add two rows (two subscribers)
conn.execute("INSERT INTO suscriptores (ID,nombre,edad,descripcion,fecha,numero) "
             "VALUES (1, 'Paco', 30, 'Nacio en el mundo', 2023-04-20, 3)")
conn.execute("INSERT INTO suscriptores (ID,nombre,edad,descripcion,fecha,numero) "
             "VALUES (2, 'Ricardo', 20, 'Nacio en Marte', 2023-04-21, 6)")

conn.commit()

cursor = conn.cursor()

cursor.execute("SELECT * FROM suscriptores")
table_content = cursor.fetchall()
print(table_content)
print(table_content[0][1])

for row in table_content:
    print(row)

conn.close()
