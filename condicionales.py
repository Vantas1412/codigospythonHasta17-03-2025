#comparando cadenas

cadena1=input()
cadena2=input()
if cadena1==cadena2:
    print("es la misma cadena")


#if else
#comparando numeros  < > == != <= >=
numero1=int(input())
numero2=int(input())
if numero1 > numero2 :
    print(f"el numero {numero1} es mayor que {numero2} ")
else:
    print(f"el numero {numero1} no es mayor que {numero2} ")

#if else elif
#indique si el numero es mayor que cero o menor que
#cero o igual a cero 
numero1=int(input())
if numero1 >0:
    print("este numero es mayor a cero")
elif numero2 <0:
    print("este numero es menor a cero")
else:
    print("este numero es igual que cero")


#match sirve para tener multiples preguntas
#util para menus
opcion=int(input())
match opcion:
    case 1:
        print("opcion 1")
    case 2:
        print("opcion 2")
    case 3:
        print("opcion 3")
    case 4:
        print("opcion 4")
    case _:
        print("no valida ")



