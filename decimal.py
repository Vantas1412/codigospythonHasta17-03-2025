n, x=map(int,input().split())
r=""
while n!=0:
    r=r+str(n%x)
    n=n//x
print(r)
    
