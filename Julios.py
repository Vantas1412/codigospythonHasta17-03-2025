import julius

# Configurar la API (necesitarás tu API key de julius.ai)
julius.api_key = 'tu_api_key'

# Ejemplo de datos en tuplas
datos = [
    (1, 100, 'producto_a', '2024-01-01'),
    (2, 150, 'producto_b', '2024-01-02'),
    (3, 200, 'producto_a', '2024-01-03')
]

# Enviar datos a Julius para análisis
respuesta = julius.analyze(
    data=datos,
    analysis_type='predictive',
    target_variable='ventas'
)

# Obtener predicciones
print(respuesta.predictions)
