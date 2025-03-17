def f(x):
    return x**2
def df(x):
    return 2*x

tol=1e-4
x=3
for i in range(15):
    
    xi=x-f(x)/df(x)
    x=xi
    if x<tol:
        print(x)
        break

