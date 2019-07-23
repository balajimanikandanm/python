b=input()
s=""
m=0
for i in range(len(b)-1):
    s=""
    if b[i]==b[i+1]:
        s=s+b[:i+1]+b[i+2:]
        if int(s)>m:
            m=int(s)
print(m)
