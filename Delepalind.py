from itertools import combinations
rb=input()
bs=0
l1=list(combinations(rb,len(N)-1))
for i1 in range(len(l1)):
    if l1[i1]==l1[i1][::-1]:
        print("YES")
        bs=1
        break
if bs==0:
    print("NO")
