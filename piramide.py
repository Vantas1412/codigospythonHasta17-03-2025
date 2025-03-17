import sys
import math

n = int(sys.stdin.readline().strip())

for _ in range(n):
    x = int(sys.stdin.readline().strip())
    
    c = int(math.sqrt(2 * x))  
    while c * (c + 1) // 2 > x: 
        c -= 1
    
    print(c)
