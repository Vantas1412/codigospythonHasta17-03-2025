class Color:
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
class DistColor:
    def __init__(self,color,distancia):
        self.color=color
        self.distancia =distancia
def orden(color):
    if len(color)>1:
        m=len(color)//2
        iz=color[:m]
        de=color[m:]
        orden(iz)
        orden(de)
        i=j=k=0
        while i<len(iz) and j<len(de):
            if iz[i].color<de[j].color :
                color[k]=iz[i]
                i+=1
            else:
                color[k]=de[j]
                j+=1
            k+=1
        while i<len(iz):
            color[k]=iz[i]
            i+=1
            k+=1
        while j<len(de):
            color[k]=de[j]
            j+=1
            k+=1
    return color 
            
def distancia(a,b):
    return ((b.y-a.y)**2+(b.x-a.x)**2)**0.5
def combinacion(color):
    d=[]
    for i in range (len(color)):
        for j in range(i+1,len(color)):
            d.append(distancia(color[i],color[j]))
    d.sort()
    return d[0]
            
colores=[]
clasi=set()
n=int(input())
fi=[]
for i in range(n):
    a,b,c=map(str,input().split())
    colores.append(Color(float(a),float(b),c))
    clasi.add(c)
for i in clasi :
    k=[]
    for j in colores :
        if j.color == i :
            k.append(j)
    d=combinacion(k)
    fi.append(DistColor(i,d))
fi=orden(fi)
for i in fi :
    print(f"{i.color} {i.distancia:.2f}")

            
