b,sa=map(int,input().split())
p=[]
for i in range(b):
  s=set(map(int,input().split()))
  p.append(s)
ro=s.intersection(*p)
print(*ro)
