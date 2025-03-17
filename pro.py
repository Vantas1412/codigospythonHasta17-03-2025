# Importar librerías necesarias
import pandas as pd
from prophet import Prophet

# 1. Crear un DataFrame con los datos históricos
data = pd.DataFrame({
    'ds': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'],
    'y': [120, 150, 170, 200, 230]  # Ventas mensuales
})

# 2. Crear y entrenar el modelo Prophet
model = Prophet()
model.fit(data)

# 3. Crear un DataFrame con fechas futuras para predecir
future = model.make_future_dataframe(periods=6, freq='M')  # Predicción para los próximos 6 meses

# 4. Realizar la predicción
forecast = model.predict(future)

# 5. Visualizar los resultados
# Gráfica principal con las predicciones
import matplotlib.pyplot as plt

model.plot(forecast)
plt.title("Predicción de Ventas Mensuales")
plt.xlabel("Fecha")
plt.ylabel("Ventas")
plt.show()

# Opcional: Mostrar componentes (tendencias y estacionalidad)
model.plot_components(forecast)
plt.show()

# 6. Mostrar las predicciones en consola
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(6))
