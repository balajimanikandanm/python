n=int(input())
lo=[int(x) for x in input().split()]
u,v=map(int,input().split())
a=[]
for i in range(n-1):
    for j in range(i+1,n+1):
        m=lo[i:j]
        if (m[0]==u and m[-1]==v) or (m[-1]==u and m[0]==v):
            a.append(len(m))
print(min(a)-1) 
