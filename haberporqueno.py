def div(x):
    s = 1
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            s += i
            if i != x // i:  
                s += x // i
    return s

print(div(12))
