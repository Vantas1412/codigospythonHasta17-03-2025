import cx_Oracle

# Configura tus credenciales y conexión
username = 'PROYECTO'
password = '1412'
dsn = '127.0.0.1:1521/XE'  # Ajusta el DSN correctamente

# Conectar a la base de datos
try:
    connection = cx_Oracle.connect(username, password, dsn)
    print("Conexión exitosa a Oracle Database 10g")

    # Ejemplo de consulta
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM persona")
    for row in cursor:
        print(row)
    
except cx_Oracle.DatabaseError as e:
    print("Error al conectar:", e)

finally:
    # Asegúrate de cerrar el cursor y la conexión si fueron creados
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
