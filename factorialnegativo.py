n=int(input())
r=1
for i in range(1,n+1,1):
    sw= i%2==0
    r=r*i*(-1)
    print(r)
    
