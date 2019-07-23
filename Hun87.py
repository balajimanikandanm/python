b,s=map(int,input().split())
l=[int(x) for x in input().split()]
c=0
for i in l:
	if i<=s:
		c=c+1
print(c)
