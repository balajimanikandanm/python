s=input()
b=1
if len(s)==1:
    print("yes")
else:
    for j in s:
        if s.count(j)==len(s):
            print("no")
            b=0
            break
    if b==1:
        print("yes")
