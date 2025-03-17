from google.cloud import bigquery
from google.cloud.exceptions import GoogleCloudError

# Ruta al archivo de credenciales JSON
json_path = "C:/sqlite/prueba-442022-80101aedea85.json"
csv_file_path = "C:/Users/Usuario/Documents/Bdproy2/Iris.csv"  # Ruta al archivo CSV

try:
    # Crear cliente especificando las credenciales
    client = bigquery.Client.from_service_account_json(json_path)

    # Definir el dataset y la tabla de destino
    project_id = 'prueba-442022'
    dataset_id = '1'  # Nombre del dataset
    table_id = f"{project_id}.{dataset_id}.nueva_tabla"  # Nombre completo de la tabla (proyecto.dataset.tabla)

    # Configuración del trabajo de carga de datos
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,  # Omitir la primera fila si contiene encabezados
        autodetect=True,  # Detectar el esquema automáticamente
    )

    # Abrir el archivo CSV y cargar los datos en la tabla
    with open(csv_file_path, "rb") as source_file:
        load_job = client.load_table_from_file(
            source_file,
            table_id,
            job_config=job_config
        )  # Cargar los datos desde el archivo CSV

    # Esperar a que el trabajo de carga termine
    load_job.result()

    # Verificar que los datos se cargaron correctamente
    table = client.get_table(table_id)
    print(f"Datos cargados con éxito en la tabla {table_id}. Total de filas: {table.num_rows}")

except GoogleCloudError as e:
    print(f"Ocurrió un error al conectar con BigQuery: {e}")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
