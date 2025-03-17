n=int(input())
factores=""
while n!=1:
    for i in range(2,n+1,1):
        if n%i==0:
            factores=factores+str(i)+"x"
            n=n//i
            break
print(factores)
        
