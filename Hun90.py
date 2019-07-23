b = input()
c,n,m = 0,'',0
for i in range(0,len(b)):
  c = 1
  for j in range(i+1,len(b)):
    if b[i]==b[j]:
      c += 1
    else:
      break
  if c>m:
    m = c
    n = b[i]
print(n,m)
