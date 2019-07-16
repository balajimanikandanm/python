n=int(input())
lo=[1000,500,100,50,10,1]
sb=[]
c=0
for i in range(0,len(lo)):
        k=n//lo[i]
        c=c+k
        n=n-(k*lo[i])
print(c)
