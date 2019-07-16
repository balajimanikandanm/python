b,r = map(int,input().split())
d = map(int,input().split())
d = list(d)
repeat = []
for i in range(b):
  for j in range(i+1,b):
    if d[i] + d[j] == r:
      repeat.append([d[i],d[j]])
if (len(repeat) == 0):
  print('NO')
else:
  print('YES')
