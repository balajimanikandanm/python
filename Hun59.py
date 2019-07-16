bs=int(input())
a=list(map(int,input().split()))
rb=list(map(int,input().split()))
c=[]
for i in range(int(bs)):
               c.append(a[i]+rb[i])
print(*c,sep=' ')
