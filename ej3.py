
z=[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
m,n =map(int,input().split())
x=list(map(int,input().split()))
for i in range(n):
    l,r=map(int,input().split())
    pa=0
    pb=0
    sa=0
    sb=0
    sw=True 
    for j in range(l-1,r):
        if x[j] in z and sw :
            pa+=x[j]
            sa=0
            sw=False
        else:
            sa+=1
        if x[j]%2==1 and sw:
            pb+=x[j]
            sb=0
            sw=False
        else:
            sb+=1
        if sa>=2 and sb>=2:
            break
        sw=True
    if pa==pb:
        print("E")
    elif pa>pb:
        print("A")
    else:
        print("B")
    
