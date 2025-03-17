import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(t, y) que representa la EDO
def f(t, y):
    return -2 * y

# Parámetros
y0 = 1  # Condición inicial
t0 = 0  # Tiempo inicial
tf = 5  # Tiempo final
h = 0.1  # Tamaño del paso

# Inicializar vectores para el tiempo y las soluciones
t_values = np.arange(t0, tf, h)
y_values = np.zeros(len(t_values))

# Condición inicial
y_values[0] = y0

# Método de Euler explícito
for n in range(1, len(t_values)):
    y_values[n] = y_values[n-1] + h * f(t_values[n-1], y_values[n-1])
    # Imprimir la solución en cada paso
    print(f"Paso {n}: t = {t_values[n]:.2f}, y = {y_values[n]:.4f}")

# Graficar la solución
plt.plot(t_values, y_values, label="Aproximación de Euler")
plt.xlabel('Tiempo (t)')
plt.ylabel('y(t)')
plt.title('Solución de la EDO con el Método de Euler')
plt.legend()
plt.grid(True)
plt.show()
