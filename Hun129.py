su=int(input())
l=list(map(int,input().split()))
su=[]
for i in l:
    su.append(l.count(i))
n=max(su)
for i in range(0,len(su)):
    if su[i]==n:
        print(l[i])
        break
