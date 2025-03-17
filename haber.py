n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=list(map(int,input().split()))
rx=0
ptj=0
while rx<len(x):
    rm=0
    while rm<len(z):
        while x[rx]<=z[rm]:
            z[rm]=z[rm]-x[rx]
            ptj+=1
            z[rm]=z[rm]+y[rx]
            ptj+=1
        rm+=1
    rx+=1
print(ptj)
    
    
