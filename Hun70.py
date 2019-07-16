from itertools import combinations
rb,ba,bs=map(int,input().split())
lis=list(map(int,input().split()))
hh=list(combinations(lis,ba))
for i in range(0,len(hh)):
    yy=list(hh[i])
    zz = 0
    for j in range(0,ba):
        zz=zz+yy[j]
    if zz==bs:
        print("YES")
        sys.exit()
print("NO") 
