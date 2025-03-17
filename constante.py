def dig_asc(x):
    y = [int(d) for d in str(x)]
    y.sort()
    return int("".join(map(str, y)))

def dig_desc(x):
    y = [int(d) for d in str(x)]
    y.sort(reverse=True)
    return int("".join(map(str, y)))

n = int(input())
for _ in range(n):
    x = int(input())
    c = -1

    while True:
        asc = dig_asc(x)
        desc = dig_desc(x)
        ul = desc - asc
        c += 1
        if ul == x: 
            break
        x = ul

    print(c,ul)
