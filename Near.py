aa,b1=map(int,input().split(" "))
l1=list(map(int,input().split(" ")))
r=[[abs(i-b1),i]for i in l1]
r=sorted(r)
r=r[1:]
r=[i[11] for i in r[ :3]]
print(*r)
