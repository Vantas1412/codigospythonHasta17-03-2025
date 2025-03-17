import psycopg2

# Parámetros de conexión
hostname = 'localhost'
dbname = 'postgres'
username = 'Aaron'
password = '1412'
port_id = 5432  # Puerto predeterminado de PostgreSQL

# Verificar la conexión
try:
    connection = psycopg2.connect(
        host=hostname,
        database=dbname,
        user=username,
        password=password,
        port=port_id
    )
    # Establecer la codificación a UTF-8
    connection.set_client_encoding('UTF8')
    print("Conexión exitosa a PostgreSQL")

except Exception as error:
    print(f"Ocurrió un error al conectar a PostgreSQL: {error}")

finally:
    # Cerrar la conexión si se creó
    if 'connection' in locals():
        connection.close()
        print("Conexión cerrada")
