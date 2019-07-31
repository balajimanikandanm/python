N1=int(input())
if N1==1:
    print("YES")
elif N1%2!=0:
    print("NO")
else:
    while N1%2==0:
        N1=N1//2
    if N1==1:
        print("YES")
    else:
        print("NO")
