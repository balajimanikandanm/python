x=int(input())
if x>=-2**15+1 and x<=2**15+1:
    print("INT")
elif x>=-2**31+1 and x<=2**31+1:
    print("LONG")
else:
    print("LONG LONG")
