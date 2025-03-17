def eliminarRepetidos(matriz):
   
    matriz_sin = []
    for fila in matriz:
        if fila not in matriz_sin:
            matriz_sin.append(fila)
    return matriz_sin

def crearMatrizElementos(matriz_sin, matriz):
   
    elementos = sorted(set(elem for fila in matriz_sin for elem in fila))  # Elementos únicos ordenados
    matriz_cod = [list(elementos)]  # Primera fila con los elementos únicos

    for fila in matriz:
        cod = [1 if elem in fila else 0 for elem in elementos]  # Codificar presencia (1 o 0)
        matriz_cod.append(cod)

    return matriz_cod

def contarRepetidos(matriz_cod):
    
    vector_rep = [sum(fila) for fila in matriz_cod]
    return vector_rep

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

def merge(matriz, vector):
  
    if len(vector) > 1:
        medio = len(vector) // 2
        vector_izq, vector_der = vector[:medio], vector[medio:]
        matriz_izq, matriz_der = matriz[:medio], matriz[medio:]

        merge(matriz_izq, vector_izq)
        merge(matriz_der, vector_der)

        i = j = k = 0
        while i < len(vector_izq) and j < len(vector_der):
            if vector_izq[i] > vector_der[j]:  
                vector[k], matriz[k] = vector_izq[i], matriz_izq[i]
                i += 1
            else:
                vector[k], matriz[k] = vector_der[j], matriz_der[j]
                j += 1
            k += 1

        while i < len(vector_izq):
            vector[k], matriz[k] = vector_izq[i], matriz_izq[i]
            i += 1
            k += 1

        while j < len(vector_der):
            vector[k], matriz[k] = vector_der[j], matriz_der[j]
            j += 1
            k += 1

def suma_columnas(matriz_cod):
    
    return [sum(col) for col in zip(*matriz_cod)]

txt_file = "matriz.txt"  
matriz = leer_txt(txt_file)

matriz_sin = eliminarRepetidos(matriz)
matriz_cod = crearMatrizElementos(matriz_sin, matriz)
vector_rep = contarRepetidos(matriz_cod[1:])

print("Frecuencia antes de ordenar:")
for fila, elem in zip(matriz_cod[1:], vector_rep):
    print(fila, elem)

print("\nDespués de ordenar:")
merge(matriz_cod[1:], vector_rep)
for fila, elem in zip(matriz_cod[1:], vector_rep):
    print(fila, elem)
