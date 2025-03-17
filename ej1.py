n=int(input())
for i in range(n):
    a=int(input())
    x=list(map(int,input().split()))
    c=0
    p=0
    for k in x:
        if k==1:
            c+=1
            if c>2:
                p+=1
            p+=1

        else:
            p-=1
            c=0
    print(p)
            
            
        
        
