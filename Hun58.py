rb,sb=map(int,input().split())
n=list(map(int,input().split()))
c=0
for i in range(0,rb):
    for j in range(0,rb):
        if n[i]-n[j]==sb:
            c=c+1 
print(c)
