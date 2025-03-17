def l(m):
    if not m:
        return 0
    n, c = len(m), len(m[0])
    h = [0] * c
    ma = 0

    def lh(h):
        s = []
        a = 0
        h.append(0)
        for i, v in enumerate(h):
            while s and h[s[-1]] > v:
                he = h[s.pop()]
                w = i if not s else i - s[-1] - 1
                a = max(a, he * w)
            s.append(i)
        h.pop()
        return a

    for r in m:
        for j in range(c):
            h[j] = h[j] + 1 if r[j] == 1 else 0
        ma = max(ma, lh(h))

    return ma


t = int(input())
for _ in range(t):
    m = []
    n = int(input())
    for _ in range(n):
        m.append(list(map(int, input().split())))
    print(l(m))
