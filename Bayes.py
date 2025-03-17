import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Datos simulados
data = {
    "idCampaña": [1, 2, 3, 4, 5],
    "Categoría": ["Electrónica", "Deportes", "Ropa", "Electrónica", "Hogar"],
    "Costo": [200, 150, 100, 250, 120],
    "Clicks": [500, 400, 200, 800, 350],
    "Conversiones": [50, 30, 10, 80, 40],
    "Segmento": ["Joven", "Adulto", "Joven", "Joven", "Adulto"],
    "Región": ["Urbano", "Urbano", "Rural", "Urbano", "Rural"],
    "Dispositivo": ["Móvil", "Web", "Móvil", "Móvil", "Web"],
}

df = pd.DataFrame(data)

# 1. Calcular la tasa de conversión y definir la distribución a priori
df["CTR"] = df["Conversiones"] / df["Clicks"]
df["NoConversiones"] = df["Clicks"] - df["Conversiones"]

# Definir parámetros a priori de la distribución Beta (ejemplo: α = 1, β = 1)
alpha_prior = 1
beta_prior = 1

# Actualizar las distribuciones Beta con los datos de conversiones
df["Alpha"] = alpha_prior + df["Conversiones"]
df["Beta"] = beta_prior + df["NoConversiones"]

# 2. Visualización de las distribuciones a posteriori para cada campaña
x = np.linspace(0, 1, 100)
for i, row in df.iterrows():
    dist = beta(row["Alpha"], row["Beta"])
    plt.plot(x, dist.pdf(x), label=f"Campaña {row['idCampaña']}")

plt.title("Distribución a posteriori de la tasa de conversión por campaña")
plt.xlabel("Tasa de conversión")
plt.ylabel("Densidad de probabilidad")
plt.legend()
plt.show()

# 3. Simulación Monte Carlo para inferencia
n_simulations = 10000
simulated_results = {}

for i, row in df.iterrows():
    dist = beta(row["Alpha"], row["Beta"])
    simulated_conversions = dist.rvs(size=n_simulations)
    simulated_results[row["idCampaña"]] = simulated_conversions.mean()

# 4. Cálculo del ROI esperado
ingreso_por_conversion = 10
roi = {}

for i, row in df.iterrows():
    expected_conversions = simulated_results[row["idCampaña"]]
    expected_revenue = expected_conversions * ingreso_por_conversion
    roi[row["idCampaña"]] = expected_revenue - row["Costo"]

# Mostrar resultados de ROI
print("ROI esperado por campaña:")
for campana, valor_roi in roi.items():
    print(f"Campaña {campana}: ROI = {valor_roi:.2f}")

# Recomendación: Seleccionar la campaña con mayor ROI
mejor_campana = max(roi, key=roi.get)
print(f"\nLa campaña con el mejor ROI es la campaña {mejor_campana}.")
