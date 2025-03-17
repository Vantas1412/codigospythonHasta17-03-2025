#primero necesitamos dos variables
# el precio del producto y la tasa del iva
# entonces pedimos esos dos datos por teclado
# el precio es un decimal entonces colocamos float
precio=float(input("ingrese el precio del producto "))
# el iva sera entregado en % asi que es un entero
iva=int(input("ingrese la tasa del iva "))

# calculamos el aumento del iva 
aumento=precio*(iva/100)
# calculamos usando la formula del precio total 
pre_con_iva=precio+aumento

print("precio con iva",pre_con_iva)
print("aumento del iva ",aumento )
