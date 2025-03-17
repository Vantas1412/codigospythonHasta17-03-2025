dec=int(input())
numbin=""
while dec!=0:
    numbin=str(dec%2)+numbin
    dec=dec//2
print(numbin)
