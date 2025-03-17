def comprobar(x,i):
    return True if x[i]==x[i+1] or i==len(x)-1 else False
n=int(input())
for i in range(n):
    a=int(input())
    x=list(map(int,input().split()))
    for i in range(len(x)-1):
        if not comprobar(x,i):
            print(i)
        
