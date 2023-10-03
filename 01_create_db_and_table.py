import sqlite3

conn = sqlite3.connect('test.db')

# create empty table "suscriptores"
query = '''
DROP TABLE if exists suscriptores
'''
conn.execute(query)

query = '''
CREATE TABLE if not exists suscriptores
(ID         INT PRIMARY KEY NOT NULL,
nombre      TEXT            NOT NULL,
edad        INT             NOT NULL,
descripcion TEXT            NOT NULL,
fecha       TEXT            NOT NULL)
'''

conn.execute(query)

cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())

cursor.execute("SELECT * FROM suscriptores")
print(cursor.fetchall())


conn.close()
