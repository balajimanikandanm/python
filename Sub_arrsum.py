rb=int(input())
bs=list(map(int,input().split()))
c=[]
for i in range(rb):
         d=bs[i:]
         c.append(sum(d))
print(max(c))
