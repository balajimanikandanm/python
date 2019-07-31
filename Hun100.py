ba=int(input())
sb=[]
for i in range(2,ba):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            if i%j!=0 and i+j==ba:
                b=str(j)+' '+str(i)
                sb.append(str(b))
print(sb[-1])
