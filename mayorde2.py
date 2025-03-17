a,b=map(int,input().split())
mayor= (a+b+abs(a-b))/2 
print(mayor)

if a>b:
    print(a)
else:
    print(b)
