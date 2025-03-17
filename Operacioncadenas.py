#operaciones entre cadenas
a= "hola"
b="chicos"
# suma (une dos cadenas)
c=a+b
print(c)
# multiplicacion por un numero
#(multiplica y une varias veces una palabra)
c=a*2
print(c)

# las operaciones entre booleanos se hacen
# mediante  or, and ,not

# or (devuelve verdadero si alguna variable contenga verdad o True)
# caso contrario devuelve falso

# and devuelve verdadero solo si ambas variables
# contengan verdad caso contrario falso

# not convierte lo verdadero en falso y viceversa 
verdad= True
falso= False
resultado= verdad or falso
print(resultado)
resultado = verdad and falso
print(resultado)
resultado = verdad and verdad
print(resultado)
resultado = falso or falso
print(resultado)
resultado = not verdad
print(resultado)


