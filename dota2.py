n, D = map(int, input().split())  
items = list(map(int, input().split())) 

items.sort(reverse=True)

max1, max2 = items[0], items[1]

ciclo_dano = max1 + max2

ciclos_completos = D // ciclo_dano

restante = D % ciclo_dano

if restante == 0:
    ataques = ciclos_completos * 2  
elif restante <= max1:
    ataques = ciclos_completos * 2 + 1  
else:
    ataques = ciclos_completos * 2 + 2  

print(ataques)
