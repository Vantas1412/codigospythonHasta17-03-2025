def generar_serie(n):
    serie = [1, 1, 1, 1, 1, 1]  # Valores iniciales dados
    
    for i in range(6, n):
        nuevo_valor = serie[i - 2] + serie[i - 3]
        serie.append(nuevo_valor)
    
    return serie

# Generar los primeros 30 términos
n = 30
print(generar_serie(n))
