as=input().split("#")
bs=input().split("#")
ds=as[1]+as[2]+as[3]
es=bs[1]+bs[2]+bs[3]
if ds>es:
    print(as[0])
elif es>ds:
    print(bs[0])
