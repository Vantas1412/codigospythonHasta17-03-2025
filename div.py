def div(x):
    s = 1
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            s += i
            if i != x // i:  
                s += x // i
    return s
def prueba(x,sw1,sw2,sw3):
    if x==1:
        return sw1,sw2,sw3
    d=div(x)
    sig =div(d)
    if d>x:
        sw3=True
    if d==x:
        sw1=True
        return sw1,sw2,sw3
    if x==sig:
        sw2=True
    if d>x:
        sw3=True
    return sw1,sw2,sw3

    
    
n=int(input())
for i in range(n):
    x=int(input())
    r=[]
    sw1,sw2,sw3=prueba(x,False,False,False)
    if sw1:
        r.append("perfecto")
    if sw2:
        r.append("romantico")
    if sw3:
        r.append("abundante")
    if len(r)==0:
        r.append("complicado")
    print(x,*r)











    
    
