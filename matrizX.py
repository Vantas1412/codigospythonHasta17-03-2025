n=int(input())
x=[]
for i in range(n):
    x.append([0]*n)
pi=0
pj=n-1
for i in range(n//2):
    for j in range(n):
        if j<=pi or j>=pj:
            x[i][j]=1
    pi+=1
    pj-=1
pi-=1
pj+=1
for i in range(n):
    x[n//2][i]=1

for i in range(n//2+1,n):
    for j in range(n):
        if j<=pi or j>=pj:
            x[i][j]=1
    pi-=1
    pj+=1
for i in x:
    c=""
    for j in i:
        c+=str(j)
    print(c)
