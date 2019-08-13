b=int(input())
for i in range(0,b):
	if 2**i==b or b==1:
		print("yes")
		break
else:
	print("no")
