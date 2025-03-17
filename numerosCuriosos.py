import math
def factores(n):
    factores = set()
    while n % 2 == 0:
        factores.add(2)
        n //= 2
    divisor = 3
    limite = math.isqrt(n)  
    while divisor <= limite:
        while n % divisor == 0:
            factores.add(divisor)
            n //= divisor
        divisor += 2
        limite = math.isqrt(n)  
    if n > 1:
        factores.add(n)  
    return factores

def contar_digitos(n):
    return len(str(n))

n = int(input())
for i in range(n):
    x=int(input())
    if len(factores(x)) == contar_digitos(x):
        print("SI")
    else:
        print("NO")
