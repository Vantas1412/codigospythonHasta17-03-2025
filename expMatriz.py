def suma(x,n,i,j,y):
    s=0
    xi=[]
    xj=[]
    for k in range(n):
        xi.append(x[i][k])
    for k in range(n):
        xj.append(y[k][j])
    for k in range(n):
        s=s+xi[k]*xj[k]
    return s
    
def exp(x,n,y):
    z=[]
    for i in range(n):
        z.append([0]*n)
    for i in range(n):
        for j in range(n):
            z[i][j]=suma(x,n,i,j,y)
    return z

n,e=map(int,input().split())
x=[]
y=[]
for i in range(n):
    a=list(map(int,input().split()))
    x.append(a)
    y.append(a)
for i in range(e-1):
    x=exp(x,n,y)
for j in x:
    print(*j)


