nb=int(input())
ss=""
for i in range(1,nb+1):
    if nb%i==0 and i%2==1:
        ss=ss+str(i)+" "
print(ss.strip())
