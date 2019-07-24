from itertools import permutations
b=input()
k=permutations(b)
l=[]
m=(-1)
a="abcdefghijklmnopqrstuvwxyz"
if a==b:
  print(b)
elif b==a[::-1]:
  print("-1")
else:
    b=tuple(b)
    for i in k:
        l.append(i)
    for i in l:
        if i>b:
            m=i
            break

    for i in l:
        if i>b and i<m:
            m=i

    if m==-1:
        print("-1")
    else:
        for i in m:
            print(i,end="")
