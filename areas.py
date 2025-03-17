def solucion(a,b,c):
    disc= b**2 - 4*a*c
    if disc>0: 
        x1,x2= int((-b+(b**2 - 4*a*c)**0.5)/(2*a)),int((-b-(b**2 - 4*a*c)**0.5)/(2*a))
        if x2>x1:
            aux=x1
            x1=x2
            x2=aux
        return x1,x2
    elif disc<0:
        return None, None
    else:
        x1,x2=int((-b+(b**2 - 4*a*c)**0.5)/(2*a)),int((-b-(b**2 - 4*a*c)**0.5)/(2*a))
        return x1,x2
def area(l,r,a,b,c):
    return abs((2*a*r**3+3*b*r**2+6*c*r)-(2*a*l**3+3*b*l**2+6*c*l))
def casos(v,a,b,c):
    r=[]
    for i in range(len(v)-1):
        r.append(area(v[i],v[i+1],a,b,c))
    s=0
    for i in r :
        s+=i
        
    if s%6==0:
        print(f"{s//6}/1")
    else:
        if s%2==0:
            print(f"{s//2}/3")
        else: 
            if s%3==0:
                print(f"{s//3}/2")
            else:
                print(f"{s}/6")
            
n=int(input())
for i in range(n):
    a,b,c,l,r=map(int,input().split())
    x1,x2=solucion(a,b,c)
    sw=False
    v=[]
    if x1==None and x2==None :
        v.append(l)
        v.append(r)
    elif x1>x2 and (x2>r or x1<l) :
        v.append(l)
        v.append(r)
    elif x2>l and x2<r and x1>l and x1<r :
        if x1!=x2:
            v.append(l)
            v.append(x2)
            v.append(x1)
            v.append(r)
        else:
            v.append(l)
            v.append(x2)
            v.append(r)
    elif x2>l and x2<r:
        if x1!=x2:
            v.append(l)
            v.append(x2)
            v.append(r)
        else:
            sw=True
            v.append(l)
            v.append(x2)
            v.append(r)
    elif x1>l and x1<r:
        if not sw:
            v.append(l)
            v.append(x1)
            v.append(r)
    else:
        v.append(l)
        v.append(r)
        
    casos(v,a,b,c)
        
        














    
    
    

