sb = int(input())
rb = list(map(int,input().split()))
for i in range(len(rb)-1):
    if rb[i]>rb[i+1]:
        print(rb[i+1],end=" ")
    else:
        print(-1,end=" ")
print(-1)
