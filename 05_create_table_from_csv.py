import sqlite3
import csv

# Connection with database "test.db"
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

archivo_csv = 'data/iris.csv'
nombre_tabla = 'iris'

query = f'''
DROP TABLE if exists {nombre_tabla}
'''
conn.execute(query)

with open(archivo_csv, 'r') as csvfile:
    # Leer el CSV y obtener los nombres de las columnas
    reader = csv.reader(csvfile)
    column_names = next(reader)

    # Crear la tabla en SQLite
    # print(f"CREATE TABLE IF NOT EXISTS {nombre_tabla} ({', '.join(column_names)});")
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {nombre_tabla} ({', '.join(column_names)});")
    # Insertar los datos en la tabla
    for row in reader:
        # print(f"INSERT INTO {nombre_tabla} VALUES ({', '.join('?' for _ in range(len(row)))})", row)
        cursor.execute(f"INSERT INTO {nombre_tabla} VALUES ({', '.join('?' for _ in range(len(row)))})", row)

# Confirmar la transacción y cerrar la conexión
conn.commit()

cursor.execute(f"SELECT * FROM {nombre_tabla} LIMIT 2")
table_content = cursor.fetchall()
print(table_content)

conn.close()
