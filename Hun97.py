b,s=map(int,input().split())
k=max(b,s)
pp=[]
for i in range(1,k):
    if b%i==0 and s%i==0:
        pp.append(i)
if len(pp)==1:
    print("yes")
else:
    print("no")
