n=int(input())
factores=""
unicos=[] # a b c 
while n!=1:
    for i in range(2,n+1,1):
        if n%i==0:
            factores=factores+str(i)+" "
            n=n//i
            break
for k in range(len(factores)):
    if factores[k]!=" ":
        unicos.append(factores[k])
y=[]
for i in range(len(unicos)):
    if unicos[i] not in y :
        y.append(unicos[i])
suma=0
for i in range(len(y)):
    suma=suma+int(y[i])
final=""
for i in range(len(y)):
    conta=0
    for k in range(len(unicos)):
        if y[i]==unicos[k]:
            conta+=1
    final=final+y[i]+"**"+str(conta)+"*"
print(final[:len(final)-1],suma)











    




    
        

    
    
