rb = input()
bs = []
for i in rb:
  bs.append(int(i))
c = str(sum(bs))
if(c == c[::-1]):
  print("YES")
else:
  print("NO")
