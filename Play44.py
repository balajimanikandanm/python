a,bi=map(str,input().split(" "))
bi1=int(bi)
l=list(a)
for i in range(0,bi1):
	a=l.pop()
	l.insert(0,a)
s1="".join(l)
print(s1)
