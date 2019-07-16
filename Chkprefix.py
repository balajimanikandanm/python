a1=int(input())
b1=list(map(str,input().split()))[:a1]
c1=input()
d1=0
for i in range(0,a1:
  if(b1[i].startswith(c1)):
    d1=d1+1
print(d1)
