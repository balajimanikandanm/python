ab=int(input())
SUM=0
bs=str(ab)
s=[]
for i in range(0,len(bs)):
    SUM=SUM+int(bs[i])
    s.append(SUM)
print(sum(s))
