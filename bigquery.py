from google.cloud import bigquery

# Ruta al archivo de credenciales JSON (usa dobles barras o un prefijo "r")
json_path = r"C:\sqlite\prueba-442022-80101aedea85.json"

# Crear cliente especificando las credenciales
try:
    client = bigquery.Client.from_service_account_json(json_path)
    print("Conexión exitosa con BigQuery.")
except FileNotFoundError as e:
    print("No se encontró el archivo JSON:", e)
except Exception as e:
    print("Ocurrió un error al conectar con BigQuery:", e)
