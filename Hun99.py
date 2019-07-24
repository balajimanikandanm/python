a1,b1,c1=map(int,input().split())
count=0
for i in range(a1,b1+1):
   if str(c1)in str(i):
       count+=1
print(count)
