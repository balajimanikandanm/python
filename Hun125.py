ss=input()
l1=[]
for i in ss:
    if ss.count(i)==1:
        l1.append(i)
for i in range(0,len(l1)-1):
    print(l1[i],end="")
print(l1[-1])  
