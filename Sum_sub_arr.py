rb=int(input())
arr1=list(map(int,input().split()))
pro=1
res=[]
for i in range(0,len(arr1)):
    for j in range(i,len(arr1)):
        pro=pro*arr1[j]
        res.append(pro)
    pro=1
print(max(res))
