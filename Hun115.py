end = int(input())
st = 1
sprime = [True for i in range(end+1)] 
p1 = 2
out = []
outlist = []
code = 0
count = 0
while (p1 * p1 <= end): 
    if (sprime[p1] == True): 
        for i in range(p1 * p1, end+1, p1): 
            sprime[i] = False
    p1 += 1
for p1 in range(st, end): 
        if sprime[p1] and p1!=1: 
            outlist.append(p1)
for i in range(len(outlist)):
    for j in range(i,len(outlist)):
        if (outlist[i] + outlist[j]) == end:
            count += 1
print(count)
