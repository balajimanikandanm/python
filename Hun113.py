N11=int(input())
if N11==1:
    print("YES")
elif N11%2!=0:
    print("NO")
else:
    while N11%2==0:
        N11=N11//2
    if N11==1:
        print("YES")
    else:
        print("NO")
