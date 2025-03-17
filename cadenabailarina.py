cadena=input()
sw=True
nueva=""
for i in range(len(cadena)):
    if cadena[i]!=" ":
        if sw :
            nueva=nueva + cadena[i].upper()
            sw=False
        else:
            nueva=nueva + cadena[i].lower()
            sw=True
print(nueva)            
            
        
