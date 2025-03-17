def convertir(x):
    y=[]
    for i in x:
        y.append(i*12)
    return y 

for i in range(7):
    x=list(map(float,input().split()))
    y=convertir(x)
    print(*y)
