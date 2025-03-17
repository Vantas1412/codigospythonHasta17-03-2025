n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    p=0
    for i in range(1,c+1,1):
        if i%2==1:
            p=p+a
        else:
            p=p-b
    print(p)
            
            
    if c%2==0:
        d=c//2
        z=c//2
    else:
        d=c//2+1
        z=c//2
    x=d*a-b*z
    print(x)
    
    
