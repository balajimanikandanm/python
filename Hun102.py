B=int(input())
s=0
while(B!=0):
  i=B%10
  s=s+i**2
  B=B//10
print(s)
