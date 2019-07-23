def diff(y):
    sb=0
    for i in range(0,len(y)):
        if y[i]=='2':
            sb=sb+1
    return sb
n=int(input())
sb=0
for i in range(0,n+1):
    y = list(str(i))
    sb=sb+diff(y)
print(sb)
