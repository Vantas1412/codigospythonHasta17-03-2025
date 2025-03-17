from googleapiclient import discovery
from google.oauth2 import service_account

# Ruta al archivo de credenciales JSON
json_path = "C:/sqlite/prueba-442022-80101aedea85.json"

# Nombre del proyecto y dataset en Google Cloud
project_id = "prueba-442022"
dataset_id = "2"  # ID de tu dataset en BigQuery

# Correo de la cuenta de servicio
member = 'serviceAccount:aaron-py@prueba-442022.iam.gserviceaccount.com'

# Rol a asignar (por ejemplo, roles/bigquery.dataOwner)
role = 'roles/bigquery.dataOwner'

# Cargar credenciales de servicio
credentials = service_account.Credentials.from_service_account_file(
    json_path, scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

# Crear el cliente para la API de BigQuery
service = discovery.build('bigquery', 'v2', credentials=credentials)

# Obtener la política IAM actual del dataset
policy = service.datasets().getIamPolicy(
    projectId=project_id,
    datasetId=dataset_id
).execute()

# Verificar si el rol ya existe para el miembro
binding = next((b for b in policy['bindings'] if b['role'] == role), None)
if binding is None:
    binding = {'role': role, 'members': []}
    policy['bindings'].append(binding)

# Agregar el miembro al rol correspondiente
binding['members'].append(member)

# Aplicar la nueva política IAM al dataset
service.datasets().setIamPolicy(
    projectId=project_id,
    datasetId=dataset_id,
    body={'policy': policy}
).execute()

print(f"Rol {role} asignado a {member} sobre el dataset {dataset_id}.")
