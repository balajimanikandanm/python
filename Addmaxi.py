ba=int(input())
bs=[int(x) for x in input().split()]
rb=[]
for i in range(len(bs)-1):
	l=bs[i+1::]
	m=max(l)
	rb.append(m)
rb.append(0)
print(*rb)
