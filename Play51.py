n1=int(input())
li=list(map(int,input().split()))

min1=min(li)
for i in range(len(li)):
    if min1!=li[i]:
        min2=li[i]
        break
for i in range(1,len(li)):
    if li[i]<min2 and li[i]>=min1:
        min2=li[i]
print(min2)
