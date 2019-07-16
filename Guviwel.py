rb = "WELCOMETOGUVICORPORATIONS"
bs = input()
arr = []
for i in range(5):
    arr.append(list(rb[i*5:(i*5)+5]))
s = "".join(["".join(x) for x in [[arr[i][j] for i in range(5)] for j in range(5)]])
for i in range(len(rb)):
    if rb[i:i+len(bs)] == bs:
        print(i//5,i%5)
        print((i+len(bs)-1)//5,(i+len(bs)-1)%5)
        break
    if s[i:i+len(bs)] == bs:
        print(i%5, i//5)
        print((i+len(bs)-1)%5, (i+len(bs)-1)//5)
        break
else: print(0)
