b,ro=map(eval,input().split())
aut=[]
for i in range(b):
  aut.append(list(map(eval,input().split())))
pos=[]
out=[]
temp_out=[]
t=[]
i=0
j=0
out.append(aut[i][j])
pos.append([i,j])
while [b-1,ro-1] not in pos:
  i=0
  for x in pos:
    if x[0]+1<b and x[1]+1<ro:
      temp_out.append(aut[x[0]+1][x[1]]+out[i])
      temp_out.append(aut[x[0]][x[1]+1]+out[i])
      t.append([x[0]+1,x[1]])
      t.append([x[0],x[1]+1])
    elif x[0]+1<b:
      temp_out.append(aut[x[0]+1][x[1]]+out[i])
      t.append([x[0]+1,x[1]])
    elif x[1]+1<ro:
      temp_out.append(aut[x[0]][x[1]+1]+out[i])
      t.append([x[0],x[1]+1])
    i+=1
  pos=t
  t=[]
  out=temp_out
  temp_out=[]
print(max(out))
