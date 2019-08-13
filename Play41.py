n1,k1=map(int,input().split())
for i in range(0,1000):
	if k1**i==n1:
		flag=0
		break
	else:
		flag=1
if flag==0:
	print("yes")
else:
	print("no")
