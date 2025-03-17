def eliminarRepetidos(matriz):
    matriz_sin = []
    for fila in matriz:
        if fila not in matriz_sin:
            matriz_sin.append(fila)
    return matriz_sin

def crearMatrizElementos(matriz_sin, matriz):
    elementos = sorted(set(elem for fila in matriz_sin for elem in fila))
    matriz_cod = [list(elementos)]
    for fila in matriz:
        cod = [1 if elem in fila else 0 for elem in elementos]
        matriz_cod.append(cod)
    return matriz_cod

def contarRepetidos(matriz_cod):
    return [sum(fila) for fila in matriz_cod[1:]]

def codificar(elementos, vector):
    return [1 if elem in vector else 0 for elem in elementos]

def leer_txt(nombre_archivo):
    matriz = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                matriz.append(list(map(str, linea.strip().split())))
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    return matriz

def cont(matriz_cod, elem):
    return sum(1 for fila in matriz_cod if all(a == b for a, b in zip(fila, elem)))

def combinaciones(vector, r, inicio=0, actual=None, resultado=None):
    if actual is None:
        actual = []
    if resultado is None:
        resultado = []

    if len(actual) == r:
        resultado.append(tuple(actual))  
        return 

    for i in range(inicio, len(vector)):
        combinaciones(vector, r, i + 1, actual + [vector[i]], resultado)

    return resultado

def combinacionesrango(vector):
    n = len(vector)
    resultado_total = []
    for r in range(2, n + 1):
        resultado_total.extend(combinaciones(vector, r))
    return resultado_total

def merge(lista1,lista2):
    if len(lista1) > 1:
        medio = len(lista1) // 2
        izq1 = lista1[:medio]
        der1 = lista1[medio:]
        izq2 = lista2[:medio]
        der2 = lista2[medio:]
        
        merge(izq1,izq2)
        merge(der1,der2)
        
        i = j = k = 0
        while i < len(izq1) and j < len(der1):
            if izq1[i] > der1[j]:
                lista1[k] = izq1[i]
                lista2[k] = izq2[i]
                i += 1
            else:
                lista1[k] = der1[j]
                lista2[k] = der2[j]
                j += 1
            k += 1

        while i < len(izq1):
            lista1[k] = izq1[i]
            lista2[k] = izq2[i]
            i += 1
            k += 1
        
        while j < len(der1):
            lista1[k] = der1[j]
            lista2[k] = der2[j]
            j += 1
            k += 1




txt_file = "matriz.txt"  
soporte_file = "soporte.txt"

matriz = leer_txt(txt_file)
soporte = leer_txt(soporte_file)

matriz_sin = eliminarRepetidos(matriz)
matriz_cod = crearMatrizElementos(matriz_sin, matriz)
vector_rep = contarRepetidos(matriz_cod)


elemfrec = set()
for art, elem, vec in zip(matriz_cod[0], vector_rep, soporte[0]):
    if elem >= int(vec):
        elemfrec.add(art)

elemfrec = sorted(elemfrec)
elemfrec = combinacionesrango(elemfrec)
nro=[]
valor=[]
for art in elemfrec:
    codi = codificar(matriz_cod[0], list(art))
    valor.append(codi)
    nro.append(cont(matriz_cod[1:], codi))
print(matriz_cod[0])    
for art,elem in zip(valor,nro):
    print(art,elem)
merge(nro,valor)
print("despues orden")
print(matriz_cod[0])
for art,elem in zip(valor,nro):
    print(art,elem)
















    
