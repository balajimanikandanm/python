b=int(input())
lst1=list(map(int,input().split()))
re=1
len=[]
for i in lst1:
  re=re*i
for i in lst1:
  len.append(re//i)
print(*len)
