import math 
numero=int(input())
cantdig=int(math.log10(numero))
nuevo=0
while numero!=0:
    dig=numero//(10**cantdig)
    sw=dig==2 or dig==3 or dig==5 or dig==7  #True 
    if sw :
        nuevo=nuevo*10+dig
    numero=numero%(10**cantdig)
    cantdig=cantdig-1
print(nuevo)

    
