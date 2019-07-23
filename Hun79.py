b=int(input())
x=[int(i) for i in input().split()]
while len(x)!=0:
	s=len(x)
	y=len(x)//2
	if s%2==1:
		print(x[y])
		x.remove(x[y])
	else:
		b=(x[y]+x[y-1])//2
		print(b)
		x.remove(x[y])
		x.remove(x[y-1])
