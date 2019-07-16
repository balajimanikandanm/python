rb=input()
a=0
for i in range(len(rb)):
    if rb[:i]==rb[i+1:]:
        a=0
        break
    else:
        a=1
if a==0:
    print("YES")
else:
    print("NO")
