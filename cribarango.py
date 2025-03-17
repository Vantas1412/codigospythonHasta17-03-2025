def criba(a, b):
    if b < 2:
        return []
    es_primo = [True] * (b + 1)
    es_primo[0] = es_primo[1] = False
    p = 2
    while p * p <= b:
        if es_primo[p]:
            for i in range(p * p, b + 1, p):
                es_primo[i] = False
        p += 1
    primos = [p for p in range(a, b + 1) if es_primo[p]]
    return primos

def busMA(arr, x):
    izquierda, derecha = 0, len(arr) - 1
    resultado = -1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] > x:
            resultado = medio
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return resultado

def busME(arr, x):
    izquierda, derecha = 0, len(arr) - 1
    resultado = -1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] < x:
            resultado = medio
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return resultado

primos = criba(0, 10**7)
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    ind_a = busME(primos, a)
    ind_b = busMA(primos, b)
    
    if ind_a == -1:
        ind_a = 0
    else:
        ind_a += 1
    if ind_b == -1:
        ind_b = len(primos)  
    if ind_a <= ind_b:
        print(len(primos[ind_a:ind_b]))
    else:
        print(0)
    
    
