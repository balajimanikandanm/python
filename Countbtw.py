s, bm = list(map(int, input().split()))
c = 0
for x in range(s, bm+1):
    t = (bin(x)[2:]).count('1')
    if t == 1:
        continue
    for i in range(2, t):
        if t % i == 0:
            flag = False
            break
    else:
        c += 1
print(c)
