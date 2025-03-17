def suma_divisores(n):
    y=[0,1]
    for i in range(2,int(n**0.5)+1,1):
        if n%i==0:
            y.append(i)
            y.append(n//i)
    return sum(y)

def clasificar_numero(n):
    suma_n = suma_divisores(n)
    if suma_n == n:
        return "perfecto"
    
    suma_m = suma_divisores(suma_n)
    romantico = suma_m == n and suma_n != n
    abundante = suma_n > n
    
    if romantico and abundante:
        return "romantico abundante"
    elif romantico:
        return "romantico"
    elif abundante:
        return "abundante"
    else:
        return "complicado"

n=int(input())
numeros=[]
for i in range(n):
    numeros.append(int(input()))

for num in numeros:
    print(f"{num} {clasificar_numero(num)}")
