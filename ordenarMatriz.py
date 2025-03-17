n=int(input())
x=[]
g=n*n
for i in range(n):
    y=[]
    for j in range(n):
        y.append(g)
        g-=1
    x.append(y)
