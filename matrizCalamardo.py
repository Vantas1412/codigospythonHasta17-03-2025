n=int(input())
for i in range(n):
    x=[]
    a,b=map(str,input().split())
    a=int(a)
    for j in range(a):
        x.append([0]*a)
    li=0
    ld=1
    r=0
    z=0
    for j in range(a):
        for k in range(a-li):
            x[k][z]=b[r%len(b)]
            r+=1
        for k in range(ld,a):
            x[a-li-1][k]=b[r%len(b)]
            r+=1
        li+=1
        ld+=1
        z+=1
    for j in x:
        print(*j)
                
        
        
