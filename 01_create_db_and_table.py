import sqlite3

# Connection with database "test.db" if exists, else, create it
conn = sqlite3.connect('test.db')

# drop table "suscriptores" if existe to prevent future errors
query = '''
DROP TABLE if exists suscriptores
'''
conn.execute(query)

# Create table "suscriptores"
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

# Searching table names in database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())

# Column names
query = cursor.execute("SELECT * From suscriptores")
cols = [column[0] for column in query.description]
print(cols)

# Select all columns from table "suscriptores"
cursor.execute("SELECT * FROM suscriptores")
print(cursor.fetchall())

# Close connection with database
conn.close()
