sb=int(input())
rb=list(map(str,input().split()))
for i in rb:
    if rb.count(i)==1:
        print(i)
