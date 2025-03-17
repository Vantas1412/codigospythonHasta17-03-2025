n=int(input())
for i in range(n):
    pandisp=int(input())
    nivel=0
    paneton=0
    while paneton<pandisp:
        nivel=nivel+1
        paneton+=(nivel * (nivel +1)) // 2
    if paneton >pandisp:
        nivel-=1
    print(nivel)

