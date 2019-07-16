#balaji
rb=int(input())
l=list(map(int,input().split()))
ct=0
for i in range(1,rb+1):
	if l.count(rb*i)>0:
		ct=ct+1
print(ct)
