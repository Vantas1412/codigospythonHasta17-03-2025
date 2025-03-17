cadenas=set(input().lower())
abc = [chr(i) for i in range(97, 123) if i != 97 and i != 114]
sw=False
c=0
for letra in cadenas:
    if letra in abc:
        sw=True
        break
    elif letra=="a":
        c+=1
    else:
        c+=1
    if c==2:
        break
        
if sw:
    print("Han Solo")
else:
    print("Chewbacca")


    
