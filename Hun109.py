N1=int(input())
l1=list(map(str,input().split()))
k=[]
for i in l1:
    k.append(i.lower())
k.sort()
for i in k:
    print(i)
