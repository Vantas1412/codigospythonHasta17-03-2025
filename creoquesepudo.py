from google.cloud import bigquery

# Inicializar el cliente de BigQuery
client = bigquery.Client(project="prueba-442022")

# Query para seleccionar datos de la tabla
query = """
SELECT id, nombre, email
FROM `prueba-442022.1.clientes`
"""

# Ejecutar la query
query_job = client.query(query)  # Ejecutar consulta
results = query_job.result()  # Esperar a que finalice y obtener resultados

# Imprimir resultados
print("Resultados de la tabla clientes:")
for row in results:
    print(f"ID: {row.id}, Nombre: {row.nombre}, Email: {row.email}")
