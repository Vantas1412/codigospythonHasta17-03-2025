from google.cloud import bigquery
from google.cloud.exceptions import GoogleCloudError

# Ruta al archivo de credenciales JSON
json_path = "C:/sqlite/prueba-442022-80101aedea85.json"

try:
    # Crear cliente especificando las credenciales
    client = bigquery.Client.from_service_account_json(json_path)

    # Ejecutar una consulta para verificar que la conexión es exitosa
    query = """
    SELECT idProd
    FROM `prueba-442022.enero2024.Anuncios` order by idProd
    """
    
    query_job = client.query(query)  # Ejecutar la consulta
    results = query_job.result()  # Esperar a que termine la consulta
    
    # Imprimir los resultados
    for row in results:
        print(f"Total de filas: {row.idProd}")

except GoogleCloudError as e:
    print(f"Ocurrió un error al conectar con BigQuery: {e}")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
