def kap(n, nums):   
    res = []
    for num in nums:
        it = 0
        while True:
            asc = int("".join(sorted(str(num).zfill(3))))
            desc = int("".join(sorted(str(num).zfill(3), reverse=True)))
            resu = desc - asc
            
            if resu == num:
                break
            num = resu
            it += 1
        res.append((it, num))
    return res

n = int(input())
nums = [int(input()) for _ in range(n)]
res = kap(n, nums)
for r in res:
    print(r[0], r[1])
