def funcion(x,c):
    if x==1 :
        return c
    if x%2==0:
        return funcion(x//2,c+1)
    if x%3==0:
        return funcion(x//3,c+1)
        
