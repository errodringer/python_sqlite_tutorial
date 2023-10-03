import sqlite3

# Connection with database "test.db"
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Filter "edad" greater than 25
data_filter_date_gr = """
SELECT * FROM suscriptores WHERE edad > 25
"""
data_filter = cursor.execute(data_filter_date_gr).fetchall()
print(data_filter)

# Filter "edad" greater than 25
data_filter_date_le = """
SELECT * FROM suscriptores WHERE edad < 25
"""
data_filter = cursor.execute(data_filter_date_le).fetchall()
print(data_filter)

# sort data by "fecha" column
query = """
SELECT * FROM suscriptores ORDER BY fecha DESC
"""
data_ordered = cursor.execute(query).fetchall()
print(data_ordered)

# limit 1 row
query = """
SELECT * FROM suscriptores LIMIT 1
"""
data_limit = cursor.execute(query).fetchall()
print(data_limit)

conn.close()
