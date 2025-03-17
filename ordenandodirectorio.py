from collections import deque

n=int(input())

for i in range(n):
    m=int(input())
    x=deque()
    y=deque()
    z=[]
    for k in range(m):
        x.append(input())
    while x :
        e=x.popleft()
        if e==".":
            z.append(e)
        elif e=="..":
            z.append(e)
        else:
            y.append(e)
    z.sort()
    y.append(z[1])
    y.append(z[0])
    print(f"Caso {i+1}:")
    for k in y:
        print(k)
    
