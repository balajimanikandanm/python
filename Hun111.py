N1=int(input())
k=[]
for i in range(0,N1):
   l=list(map(int,input().split()))
   k.append(l)
s=0
for i in range(0,N1):
   for j in range(0,N1):
      if i+j==N1-1:
         s=s+k[i][j]
print(s)
