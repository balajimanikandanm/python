b=int(input())
sa=""
for i in range(2,b):
    if b%i==0:
        flag=0
        break
    else:
        flag=1
if flag==0:
    print("yes")
else:
    print("no")
