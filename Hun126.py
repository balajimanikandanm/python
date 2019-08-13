s1=input()
l=s1.split(" ")
f1=1
for i in range(len(l)):
  if l[i][0].isupper():
    f1=1
  else:
    f1=0
    break
if f1==1:
  print("yes")
else:
  print("no")
