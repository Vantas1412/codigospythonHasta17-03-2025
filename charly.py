def mayor(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else :
        if b >c :
            return b
        else:
            return c
def menor(a,b,c):
    if a<b:
        if a<c:
            return a
        else:
            return c
    else :
        if b <c :
            return b
        else:
            return c

n=int(input())
for i in range(1,n+1):
    a,b,c=map(int,input().split())
    ma= mayor(c,b,a)
    me=menor(a,b,c)
    if not (a==me or a==ma):
        print(f"Case {i}: {a}")
    if not (b==me or b==ma):
        print(f"Case {i}: {b}")
    if not (c==me or c==ma):
        print(f"Case {i}: {c}")
