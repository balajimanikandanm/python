rb,bs=map(int,input().split())
ss=0
if bs<=rb:
    while rb>0 and rb>=bs:
        rb=rb-bs
        ss=ss+1
print(ss)
