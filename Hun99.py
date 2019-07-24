a1,b1,c1=map(int,input().split())
count=0
for i in range(a,b+1):
   if str(c)in str(i):
       count+=1
print(count)
