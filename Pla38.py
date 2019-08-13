aa=int(input())
bb=[]
for i in range(1,aa+1):
  if aa%i==0:
    if i%2==0:
      bb.append(i)
print(*bb)
