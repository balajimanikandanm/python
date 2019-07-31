A=int(input())
bs=str(A)
kl=[]
s=[]
summ=0
for i in range(0,len(bs)):
    s.append(bs[i])
kl=list(map(int,s))
if len(kl)==1:
    print(kl[0]**2)
else:
    for i in range(0,len(kl)-1):
        summ=summ+(kl[i]**kl[i+1])
    else:
        summ=summ+(kl[-1]**kl[0])
    print(summ)
