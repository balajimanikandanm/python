ss = input("")
t1 = input("")
x = 0
R=""
R1 = ''
for i in ss:
    if(i in t1[x:]):
        R = R+i
        x = t1.index(i)+1
x = 0
for i in t1:
    if(i in ss[x:]):
        R1 = R1+i
        x = ss.index(i)+1
if(len(R)>= len(R1)):
    print(R)
else:
    print(R1)
