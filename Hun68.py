rb=int(input())
li=list(map(int,input().split()))
print((li.index(min(li))+1),end=" ")
print((li.index(max(li))+1))
