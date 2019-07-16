rb=raw_input()
rb=int(rb)
bs=raw_input().split()
l=[]
w=0
for i in range(rb):
	if int(bs[i]) not in l:
		l.append(int(bs[i]))
		w=w+1
k=[]
for i in range(w/2):
	f=l[i+(w/2)]-l[i]
	k.append(f)
k.sort()
print k[0]
