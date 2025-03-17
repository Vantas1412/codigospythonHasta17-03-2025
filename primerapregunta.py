def serie(n, lim, inc):
    sw= True
    s=[]
    ini= 1
    i=0
    if lim == 0 :
        s.append(1)
        i+=1
        lim+=inc 
    while i <n : 
        if ini <= lim  and sw:
            s.append(ini)
            ini+=1
        else:
            sw = False
            s.append(ini)
            ini-=1
            if ini ==1 :
                lim+=inc
                sw=True
                s.append(1)
                i+=1
        i+=1
    return s

n=int(input())
sd=serie(n,1,2)
sn=serie(n,0,2)
print(sn[n-1],"/",sd[n-1])
            
        
    
