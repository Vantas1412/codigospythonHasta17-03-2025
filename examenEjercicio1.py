n=int(input())
a=1
b=0
x=[]
for i in range(n):
    c=a+b
    x.append(c)
    a=b
    b=c
a=1
b=0
c=0
y=[]
for i in range(n):
    d=a+b+c
    y.append(d)
    a=b
    b=c
    c=d
a=1
b=c=d=0
z=[]
for i in range(n):
    e=a+b+c+d
    z.append(e)
    a=b
    b=c
    c=d
    d=e
for xi,yi,zi in zip(x,y,z):
    print(xi,yi,zi, end=" ")
    
