bs=int(input())
lo=[]
c=0
for i in range(bs):
  lo.append(list(map(int,input().split())))
r=[]
for i in range(bs+1):
  if i==0:
    r.append(list("0"*(bs+2)))
  else:
    ss="0"
    for j in range(bs):
      ss=ss+str(lo[i-1][j])
    r.append(list(ss+"0"))
r.append(list("0"*(bs+2)))
for i in range(len(r)):
  for j in range(len(r)):
    if r[i][j]=="1" and r[i-1][j]==r[i+1][j]==r[i][j-1]==r[i][j+1]==r[i+1][j+1]==r[i+1][j-1]==r[i-1][j+1]==r[i-1][j-1]=="0":
      c+=1
print(c)
