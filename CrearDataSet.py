from google.cloud import bigquery
from google.cloud.exceptions import GoogleCloudError

# Ruta al archivo de credenciales JSON
json_path = "C:/sqlite/prueba-442022-80101aedea85.json"

# Nombre del proyecto en Google Cloud
project_id = "prueba-442022"

# Nombre del nuevo dataset
dataset_id = "nuevo_dataset_2024"

try:
    # Crear cliente especificando las credenciales
    client = bigquery.Client.from_service_account_json(json_path)
    
    # Crear una referencia al dataset
    dataset_ref = client.dataset(dataset_id)
    
    # Configuración del nuevo dataset
    dataset = bigquery.Dataset(dataset_ref)
    dataset.location = "US"  # Ubicación del dataset (modificar si es necesario)
    
    # Crear el dataset en BigQuery
    dataset = client.create_dataset(dataset, exists_ok=True)  # `exists_ok=True` evita errores si ya existe
    print(f"Dataset creado exitosamente: {dataset.full_dataset_id}")
    
except GoogleCloudError as e:
    print(f"Ocurrió un error al conectar con BigQuery: {e}")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
