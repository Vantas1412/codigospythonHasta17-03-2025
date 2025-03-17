n=int(input())
sw=0
#fibbonacci
a1=1
b1=0
c1=0
#tribonacci
a2=1
b2=0
c2=0
d2=0
#cuaternacci
a3=1
b3=0
c3=0
d3=0
e3=0
for i in range(n):
    #flujo de fibonacci
    if sw==0:
        c1=a1+b1
        a1=b1
        b1=c1
        print(c1,end=" ")
        #reasigno el sw 
        sw=1
    elif sw==1 :
        d2=a2+b2+c2
        a2=b2
        b2=c2
        c2=d2
        print(d2,end=" ")
        sw=2 
    else :
        e3=a3+b3+c3+d3
        a3=b3
        b3=c3
        c3=d3
        d3=e3
        print(e3,end=" ")
        sw=0 
        
    
    
    

















    
