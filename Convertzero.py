row,col = map(int,input().split())
b = []
c = []
for i in range(row):
	b.append(list(map(int,input().split())))
for i in b:
	if 0 in i:
		for j in range(len(i)):
			if(i[j] == 0):
				c.append(j)
			i[j] = 0
for i in b:
	for j in c:
		i[j] = 0
for i in b:
	for j in range(len(i)):
		i[j] = str(i[j])
for i in b:
	print(' '.join(i))
