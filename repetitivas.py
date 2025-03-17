#repite un proceso varias veces
#haz un contador del 0 al n 
n=int(input())

# Inicio Hasta Incremento 
# variable i inicia en 0 en este caso 
for i in range(0,n,1):
    print("numero",i)
    
# alternativa con valores por defecto
# inicio=0 incremento=1
for i in range(n):
    print("numero",i)


#while se repite mientras se cumpla
#una condicion
#repita la entrada de datos hasta
# que se introduzca un numero distinto de cero
n=1
while n!=0:
    n=int(input())
    print("este numero es",n)
