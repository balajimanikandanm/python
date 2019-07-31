li,ri,ni=map(int,input().split())
c=0
for k in range(li,ri+1):
   if str(ni)in str(k):
       c=c+1
print(c)
