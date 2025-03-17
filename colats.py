n,l=map(int,input().split())
while not (l==-1 and n==-1):
    if n==-1 and l==-1:
        break
    c=0
    while n<=l :
        if n==1:
            c=c+1
            break
        elif n%2==0:
            n=n//2
            c=c+1
        else:
            n=3*n+1
            c=c+1
    print(c)

    n,l=map(int,input().split())
