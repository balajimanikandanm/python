sb=input()
rb=input()
TT=""
rr=[]
nn=0
for i in range(len(sb)-1):
	for j in range(i,len(sb)):
		if sb[i:j+1] in rb:
			if len(sb[i:j+1])>=len(TT):
				TT=sb[i:j+1]
				a,b=i,j
print(sb[a:b+1])
