from google.cloud import bigquery
from google.cloud.exceptions import GoogleCloudError

def create_table_and_load_csv_no_schema(json_path, project_id, dataset_id, table_id, csv_path):
    try:
        # Crear cliente especificando las credenciales
        client = bigquery.Client.from_service_account_json(json_path)
        
        # Crear una referencia a la tabla
        table_ref = client.dataset(dataset_id, project=project_id).table(table_id)
        
        # Configurar el job de carga desde el CSV sin esquema
        job_config = bigquery.LoadJobConfig(
            autodetect=True,  # Permite a BigQuery detectar automáticamente el esquema
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1  # Salta la primera fila si tiene encabezados
        )
        
        # Cargar los datos desde el archivo CSV
        with open(csv_path, "rb") as file:
            load_job = client.load_table_from_file(file, table_ref, job_config=job_config)
        
        load_job.result()  # Esperar a que termine el trabajo de carga
        print(f"Datos cargados exitosamente desde: {csv_path}")
        
        return f"Tabla {table_id} creada y datos cargados exitosamente."

    except GoogleCloudError as e:
        return f"Error al conectar con BigQuery: {e}"
    except FileNotFoundError:
        return f"Archivo CSV no encontrado en la ruta: {csv_path}"
    except Exception as e:
        return f"Error inesperado: {e}"

# Ejemplo de uso
if __name__ == "__main__":
    json_path = "C:/sqlite/prueba-442022-80101aedea85.json"
    project_id = "prueba-442022"
    dataset_id = "1"
    table_id = "Iris"
    csv_path = "C:/Users/Usuario/Documents/Bdproy2/Iris.csv"
    

    result = create_table_and_load_csv_no_schema(json_path, project_id, dataset_id, table_id, csv_path)
    print(result)
