def contar(x,i,a):
    c=0
    while x[i]==a :
       c+=1
       i+=1
    return c,i 
    
def orden(x):
    if len(x)>1:
        m=len(x)//2
        iz=x[:m]
        de=x[m:]
        orden(iz)
        orden(de)
        i=j=k=0
        while i<len(iz) and j<len(de):
            if iz[i]<de[j]:
                x[k]=iz[i]
                i+=1
            else:
                x[k]=de[j]
                j+=1
            k+=1
        while i<len(iz):
            x[k]=iz[i]
            i+=1
            k+=1
        while j<len(de):
            x[k]=iz[j]
            j+=1
            k+=1
    return x
                
            
x=list(map(int,input().split()))
print(orden(x))
