p1,ab=map(int,input().split())
s=int(p1/2)
b=int(ab**0.5)
if(s*2==p1 and b*b==ab):
	print("yes")
else:
	print("no")
