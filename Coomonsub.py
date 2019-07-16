rb = input()
bs = input()
s = ""
for i in range(len(rb)):
  for j in range(len(rb),-1,-1):
    if rb[i:j] in bs:
      if len(rb[i:j])>=len(s):
        s=rb[i:j]
print(s)
