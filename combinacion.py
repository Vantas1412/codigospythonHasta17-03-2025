def generar_serie(n):
    serie = []
    a, b = 1, 1  # Valores iniciales de Fibonacci
    for i in range(1, n + 1):
        serie.append(i)  # Número natural
        serie.append(a)  # Número de Fibonacci
        a, b = b, a + b  # Avanzar en la serie de Fibonacci
    return serie

# Ejemplo: Generar los primeros 10 pares (20 números en total)
n = 10
print(*generar_serie(n))
