ass=input().split("#")
bs=input().split("#")
ds=ass[1]+ass[2]+ass[3]
es=bs[1]+bs[2]+bs[3]
if ds>es:
    print(ass[0])
elif es>ds:
    print(bs[0])
