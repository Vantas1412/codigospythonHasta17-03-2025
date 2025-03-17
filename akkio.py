import requests

# URL base de la API de Akkio
api_url = "https://api.akkio.com/v1/"

# Tu clave de API de Akkio
api_key = "your_api_key"

# Ruta al archivo CSV en tu ordenador
file_path = 'path/to/your/dataset.csv'

# Abrir el archivo y enviarlo a la API de Akkio
with open(file_path, 'rb') as file:
    files = {'file': file}
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    # Solicitar la carga del archivo a Akkio
    response = requests.post(f"{api_url}datasets/upload", files=files, headers=headers)

# Verificar la respuesta de la API
if response.status_code == 200:
    print("Dataset cargado exitosamente:", response.json())
else:
    print("Error al cargar el dataset:", response.status_code, response.text)
