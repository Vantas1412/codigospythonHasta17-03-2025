# definimos primero la entrada por teclado
# la cual es uno de sus lados
# al ser un cuadrado de un tamaño que no conocemos
# ese lado podria ser decimal por lo que usamos float()
# la funcion input() te permite escribir un mensaje para cuando pidas
# un dato 
lado = float(input("Ingrese el lado del cuadrado: "))

# calculamos el area
area= lado*lado
# calculamos el lado 
perimetro = 4*lado 
# la funcion print te permite mostrar mas cadenas y mejorar el mensaje por
# mostrar usando ,
print("el area del cuadrado es: " , area)
print("el perimetro del cuadrado es: ", perimetro )
