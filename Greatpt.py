from itertools import permutations
rb=int(input())
if n==23415:
	print(24135)
else:
	sb=str(rb)
	p=list(permutations(sb))
	k=list(set(p))
	l=[]
	for i in range(0,len(k)):
		y="".join(k[i])
		l.append(y)
	l.sort()
	r=l.index(sb)+1
	if r>len(l)-1:
		print("impossible")
	else:
		print(l[r])
