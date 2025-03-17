def eliminarRepetidos(matriz):
    matriz_sin = []
    for fila in matriz:
        if fila not in matriz_sin:
            matriz_sin.append(fila)
    return matriz_sin

def generar_combinaciones(matriz_sin, matriz, n):
    def obtener_combinaciones(lista, k):
        if k == 0:
            return [[]]
        if not lista:
            return []
        return obtener_combinaciones(lista[1:], k - 1) + [ [lista[0]] + c for c in obtener_combinaciones(lista[1:], k - 1) ]
    
    elementos = sorted(set(elem for fila in matriz_sin for elem in fila))
    conteo_combinaciones = {}

    for k in range(2, n + 1):
        for fila in matriz:
            combinaciones = obtener_combinaciones(sorted(fila), k)
            for combinacion in combinaciones:
                tupla_comb = tuple(combinacion)
                if tupla_comb in conteo_combinaciones:
                    conteo_combinaciones[tupla_comb] += 1
                else:
                    conteo_combinaciones[tupla_comb] = 1
    
    return conteo_combinaciones

def leer_txt(nombre_archivo):
    matriz = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                matriz.append(list(map(str, linea.strip().split())))
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    return matriz

def merge_sort_lista(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izq = lista[:medio]
        der = lista[medio:]
        
        merge_sort_lista(izq)
        merge_sort_lista(der)
        
        i = j = k = 0
        while i < len(izq) and j < len(der):
            if izq[i][1] > der[j][1]:
                lista[k] = izq[i]
                i += 1
            else:
                lista[k] = der[j]
                j += 1
            k += 1

        while i < len(izq):
            lista[k] = izq[i]
            i += 1
            k += 1
        
        while j < len(der):
            lista[k] = der[j]
            j += 1
            k += 1

    


archivo_txt = "matriz.txt"
matriz = leer_txt(archivo_txt)
matriz_sin = eliminarRepetidos(matriz)
print(matriz_sin)
soporte= leer_txt("soporte.txt")

n = len(max(matriz_sin, key=len))  
conteo_combinaciones = generar_combinaciones(matriz_sin, matriz, n)


lista_combinaciones = list(conteo_combinaciones.items())
merge_sort_lista(lista_combinaciones)


