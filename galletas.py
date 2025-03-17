n=int(input())
for i in range(1,n+1):
    a,b = map(int,input().split())
    x=[]
    for j in range(1,a+1):
        if a%j==b:
            x.append(j)
    print(f"Case #{i}:",*x)
