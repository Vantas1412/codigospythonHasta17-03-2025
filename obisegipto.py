import sys

def sum(x):
    return (x * (x + 1)) // 2

n = int(sys.stdin.readline().strip())

for i in range(n):
    t = int(sys.stdin.readline().strip())
    k = int((2 * t) ** 0.5)  
    while sum(k) < t:
        k += 1
    while sum(k) > t:
        k -= 1
    print(k)
