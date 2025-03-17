import sys
for lin in sys.stdin:
    if lin == "\n":
        break
    n=int(lin)
    a=list(map(int,input().strip().split()))
    a.sort()
    a.reverse()
    b=a[0]/(a[0]*a[0]/100)
    s=0
    for i in a :
        s=s+i*b
    print("{:.2f}".format(s))
