def pi(x):
    return 4/(x**2+1)
s=0
for i in range(100000):
    if i%2==0:
        
        s+=pi(i)
    else:
        s-=pi(i)
print(s)
