n=int(input())
rb=input().split()
sb1=[]
sb2=[]
sb3=[]
y=0
for i in rb:
  sb1.append(int(i))
sb2=sb1
while(1):
  sb3=sb2[1::2]
  del sb2
  sb2=sb3
  y=len(sb3)
  if y==1:
    j=sb3[0]
    break
for i in range(n):
  if sb1[i]==j:
    print(i)
    break
