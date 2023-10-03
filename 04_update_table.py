import sqlite3

# Connection with database "test.db"
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Set age to 31 when ID is 1
update_table = """
UPDATE suscriptores SET edad = 31 WHERE ID = 1
"""
# watch results
conn.execute(update_table)
cursor.execute("SELECT * FROM suscriptores")
table_content = cursor.fetchall()
print(table_content)

# Drop row which "fecha" is 1998
drop_row = """
DELETE FROM suscriptores WHERE fecha = '1998'
"""
# watch results
conn.execute(drop_row)
cursor.execute("SELECT * FROM suscriptores")
table_content = cursor.fetchall()
print(table_content)

conn.close()
