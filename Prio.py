rb=int(input())
lo=[int(x) for x in input().split()]
b=[str(l[0])]
for i in range(1,len(lo)):
    s=lo[:i+1]
    b.append(str(min(s)))
print(' '.join(b))
