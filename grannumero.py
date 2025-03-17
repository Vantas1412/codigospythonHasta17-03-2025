def div(n,x):
    if n==1:
        return x
    for i in range(2, n + 1,1):
        if n % i == 0:
            x.append(i)
            return div(n//i,x)
import sys

for line in sys.stdin:
    line = line.strip()  
    if not line:  
        break        
    n=int(line)
    x=[]
    y=div(n,x)
    c=""
    for k in y :
        c+=str(k)+"x"
    print(c[:len(c)-1])
            
        
