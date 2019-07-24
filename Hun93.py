Nb=input()
temp=""
f=0
for i in range(len(Nb)):
  if Nb[i]==" ":
    temp+=Nb[i]
  elif f==0:
    temp+=Nb[i].upper()
    f=1
  elif f==1:
    temp+=Nb[i]
    f=0
print(temp)
