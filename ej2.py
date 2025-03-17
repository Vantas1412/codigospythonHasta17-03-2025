n,a,k,p=map(int,input().split())
x=[]
x.append(a)
for i in range(n-1):
    aj=(a*k)%p
    if len(x)>=5:
        x.sort()
        if  x[0]<aj:
            x.pop(0)
            x.append(aj)
    else:
        x.append(aj)
    a=aj
x.sort()
print(*x)
    
