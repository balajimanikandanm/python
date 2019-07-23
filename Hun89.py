b=str(input())
t=[]
for i in range(0,len(b)):
    if(b[i] not in t):
         t.append(b[i])
t=t[::-1]
print(*t,sep="")
