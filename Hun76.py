rb=int(input())
l=[]
for i in range(rb):
	l1=[int(x) for x in input().split()]
	m=sum(l1)
	l.append(m)
m=sum(l)/(rb*rb)
print("%.6f" %m)	
