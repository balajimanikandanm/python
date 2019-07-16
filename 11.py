nn1,kk1=map(int,input().split())
l=[str(x) for x in input().split()]
kk1=str(kk1)
a=" "
while kk1 in l:
    l.remove(kk1)
if len(l)!=0:
    print(a.join(l))
else:
    print("empty")
